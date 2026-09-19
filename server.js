// LavaJá — bootstrap do servidor (Express 4 / Node 22).
// Só cuida de middlewares, arquivos estáticos, listen e encerramento.
// Regras de negócio ficam em src/. Sem dependências além de express e pg.

"use strict";

const express = require("express");
const path = require("path");

const config = require("./src/config");
const db = require("./src/db");
const seguranca = require("./src/seguranca");
const rotas = require("./src/rotas");

const DIRETORIO_PUBLICO = path.join(__dirname, "public");
const UM_ANO_MS = 365 * 24 * 60 * 60 * 1000;

function criarApp() {
  const app = express();

  // Roda atrás do proxy do Railway: confia em 1 salto para ler o IP real.
  app.set("trust proxy", 1);
  app.disable("x-powered-by");
  app.set("etag", "strong");

  app.use(seguranca.cabecalhos);
  app.use(express.json({ limit: "32kb" }));

  // Painel: servido antes do estático para injetar o nonce do CSP.
  app.get(["/admin", "/admin.html"], rotas.rotaPainel(DIRETORIO_PUBLICO));

  // /assets é versionável: cache longo e imutável.
  app.use(
    "/assets",
    express.static(path.join(DIRETORIO_PUBLICO, "assets"), {
      maxAge: UM_ANO_MS,
      immutable: true,
      etag: true,
      index: false,
      fallthrough: true,
    })
  );

  // Demais estáticos: HTML sempre revalidado (no-cache), o resto com 1 hora.
  app.use(
    express.static(DIRETORIO_PUBLICO, {
      etag: true,
      maxAge: 3600 * 1000,
      // Permite /privacidade e /franquia sem o .html no fim do endereço.
      extensions: ["html"],
      setHeaders(res, caminho) {
        if (caminho.endsWith(".html")) {
          res.setHeader("Cache-Control", "no-cache");
        }
      },
    })
  );

  // O router já declara os caminhos completos (/api/... e /health).
  app.use(rotas.criarRotas());

  // 404 de API em JSON (nunca HTML).
  app.use("/api", rotas.naoEncontradoApi);

  app.use(rotas.tratadorDeErro);
  return app;
}

/** Sobe o servidor. porta 0 = efêmera (usado nos testes). */
async function iniciar(porta = config.porta) {
  await db.iniciar().catch((e) => {
    console.error("[LavaJá] falha ao iniciar o banco, seguindo em memória:", e.message);
  });

  const app = criarApp();
  const servidor = await new Promise((resolver, rejeitar) => {
    const s = app.listen(porta, () => resolver(s));
    s.on("error", rejeitar);
  });

  const endereco = servidor.address();
  console.log(`[LavaJá] no ar na porta ${endereco.port} (banco: ${db.tipo()})`);

  let encerrando = false;
  async function encerrar(sinal) {
    if (encerrando) return;
    encerrando = true;
    console.log(`[LavaJá] recebido ${sinal}, encerrando com calma...`);
    seguranca.pararLimpeza();
    await new Promise((resolver) => servidor.close(resolver));
    await db.encerrar();
    console.log("[LavaJá] encerrado.");
  }

  return { app, servidor, porta: endereco.port, encerrar };
}

// Nenhuma falha isolada pode derrubar o processo em produção.
process.on("unhandledRejection", (motivo) => {
  console.error("[LavaJá] promessa rejeitada sem tratamento:", motivo);
});
process.on("uncaughtException", (erro) => {
  console.error("[LavaJá] exceção não capturada:", erro && erro.stack ? erro.stack : erro);
});

if (require.main === module) {
  iniciar()
    .then(({ encerrar }) => {
      // Railway envia SIGTERM em todo deploy.
      for (const sinal of ["SIGTERM", "SIGINT"]) {
        process.on(sinal, () => {
          encerrar(sinal)
            .then(() => process.exit(0))
            .catch(() => process.exit(1));
        });
      }
    })
    .catch((e) => {
      console.error("[LavaJá] não foi possível subir o servidor:", e);
      process.exit(1);
    });
}

module.exports = { criarApp, iniciar };
