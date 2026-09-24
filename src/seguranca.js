// JatoJá — segurança: cabeçalhos, rate limit em memória e autenticação admin.
// Tudo na mão: o projeto não aceita dependências além de express e pg.

"use strict";

const crypto = require("crypto");
const config = require("./config");

// ---------- IP do cliente ----------
// Atrás do proxy do Railway usamos o primeiro IP do X-Forwarded-For.
function ipDoCliente(req) {
  const encaminhado = req.headers["x-forwarded-for"];
  if (typeof encaminhado === "string" && encaminhado.length) {
    const primeiro = encaminhado.split(",")[0].trim();
    if (primeiro) return primeiro;
  }
  return req.ip || (req.socket && req.socket.remoteAddress) || "desconhecido";
}

// ---------- rate limit por IP (janela fixa) ----------
// Guardamos só { contagem, reiniciaEm } por IP — nada de array crescendo — e
// uma limpeza periódica remove as entradas vencidas (o código antigo vazava).
const contadores = new Map();
let globalContagem = 0;
let globalReiniciaEm = 0;
let temporizadorLimpeza = null;

function limparExpirados(agora = Date.now()) {
  for (const [chave, registro] of contadores) {
    if (registro.reiniciaEm <= agora) contadores.delete(chave);
  }
}

function iniciarLimpeza() {
  if (temporizadorLimpeza) return;
  temporizadorLimpeza = setInterval(() => limparExpirados(), config.rateLimite.limpezaMs);
  // unref: o timer não segura o processo (importante nos testes e no SIGTERM).
  if (typeof temporizadorLimpeza.unref === "function") temporizadorLimpeza.unref();
}

function pararLimpeza() {
  if (temporizadorLimpeza) {
    clearInterval(temporizadorLimpeza);
    temporizadorLimpeza = null;
  }
}

/** Quantidade de IPs sendo rastreados (usado nos testes de vazamento). */
function tamanhoRateLimit() {
  return contadores.size;
}

function zerarRateLimit() {
  contadores.clear();
  globalContagem = 0;
  globalReiniciaEm = 0;
}

/**
 * @returns {{bloqueado:boolean, motivo?:string, esperaSegundos:number}}
 */
function registrarAcesso(ip, agora = Date.now()) {
  const { janelaMs, maxPorIp, maxGlobal } = config.rateLimite;

  // teto global (proteção contra enxurrada distribuída)
  if (globalReiniciaEm <= agora) {
    globalContagem = 0;
    globalReiniciaEm = agora + janelaMs;
  }
  globalContagem += 1;
  if (globalContagem > maxGlobal) {
    return {
      bloqueado: true,
      motivo: "Estamos recebendo muitos acessos agora. Tente de novo em alguns instantes.",
      esperaSegundos: Math.ceil((globalReiniciaEm - agora) / 1000),
    };
  }

  // Limite grande de entradas: se o Map explodir (ataque com muitos IPs),
  // limpamos os vencidos e, se ainda assim estiver cheio, descartamos o mais antigo.
  if (contadores.size > 20_000) {
    limparExpirados(agora);
    if (contadores.size > 20_000) {
      const primeiro = contadores.keys().next().value;
      contadores.delete(primeiro);
    }
  }

  let registro = contadores.get(ip);
  if (!registro || registro.reiniciaEm <= agora) {
    registro = { contagem: 0, reiniciaEm: agora + janelaMs };
    contadores.set(ip, registro);
  }
  registro.contagem += 1;

  if (registro.contagem > maxPorIp) {
    return {
      bloqueado: true,
      motivo: "Muitas tentativas seguidas. Aguarde um minuto e tente de novo.",
      esperaSegundos: Math.ceil((registro.reiniciaEm - agora) / 1000),
    };
  }
  return { bloqueado: false, esperaSegundos: 0 };
}

/** Middleware de rate limit para rotas de escrita. */
function limitarEscrita(req, res, proximo) {
  iniciarLimpeza();
  const resultado = registrarAcesso(ipDoCliente(req));
  if (resultado.bloqueado) {
    res.setHeader("Retry-After", String(Math.max(resultado.esperaSegundos, 1)));
    return res.status(429).json({ erro: resultado.motivo });
  }
  proximo();
}

// ---------- cabeçalhos de segurança ----------
function montarCsp(nonce) {
  const script = ["'self'"];
  if (nonce) script.push(`'nonce-${nonce}'`);
  // Válvula de migração: enquanto o JS da landing ainda for inline, CSP_SCRIPT_INLINE=1
  // permite scripts inline. O alvo é todo JS sair para /assets e desligar isso.
  if (config.cspScriptInline) script.push("'unsafe-inline'");

  return [
    "default-src 'self'",
    "base-uri 'self'",
    "object-src 'none'",
    "frame-ancestors 'none'",
    "form-action 'self'",
    `script-src ${script.join(" ")}`,
    // 'unsafe-inline' em style: as páginas usam <style> inline e atributos style
    // (barras do gráfico do painel, por exemplo). Não há risco de execução de
    // código, e nonce não funciona em atributo style. Sem 'unsafe-eval' em lugar nenhum.
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com data:",
    "img-src 'self' data:",
    "connect-src 'self'",
    "manifest-src 'self'",
  ].join("; ");
}

function cabecalhos(req, res, proximo) {
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("Referrer-Policy", "strict-origin-when-cross-origin");
  res.setHeader("X-Frame-Options", "DENY");
  res.setHeader(
    "Permissions-Policy",
    "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=(), interest-cohort=()"
  );
  res.setHeader("Cross-Origin-Opener-Policy", "same-origin");
  res.setHeader("Cross-Origin-Resource-Policy", "same-origin");
  res.setHeader("X-DNS-Prefetch-Control", "off");
  // O painel injeta o próprio CSP com nonce; as demais respostas usam o padrão.
  res.setHeader("Content-Security-Policy", montarCsp(null));
  proximo();
}

// ---------- autenticação do painel ----------
function comparaSegura(a, b) {
  // Comparamos digests de tamanho fixo: timingSafeEqual exige buffers do mesmo
  // tamanho e assim não vazamos o comprimento do token.
  const da = crypto.createHash("sha256").update(String(a)).digest();
  const dbg = crypto.createHash("sha256").update(String(b)).digest();
  return crypto.timingSafeEqual(da, dbg);
}

/** Middleware das rotas admin: 503 sem token configurado, 401 sem token válido. */
function exigirAdmin(req, res, proximo) {
  if (!config.adminToken) {
    return res.status(503).json({
      erro: "Painel indisponível: a variável ADMIN_TOKEN não está configurada no servidor.",
    });
  }
  const enviado = req.headers["x-admin-token"];
  if (typeof enviado !== "string" || !enviado || !comparaSegura(enviado, config.adminToken)) {
    return res.status(401).json({ erro: "Token inválido ou ausente." });
  }
  proximo();
}

module.exports = {
  ipDoCliente,
  limitarEscrita,
  registrarAcesso,
  zerarRateLimit,
  tamanhoRateLimit,
  iniciarLimpeza,
  pararLimpeza,
  limparExpirados,
  cabecalhos,
  montarCsp,
  exigirAdmin,
  comparaSegura,
};
