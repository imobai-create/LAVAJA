// Guardas da configuração da Vercel.
//
// O risco real desta plataforma é a divergência silenciosa: a CDN serve
// public/ sem passar pelo Express, então os cabeçalhos de segurança existem em
// dois lugares. Estes testes falham se os dois deixarem de dizer a mesma coisa.

"use strict";

const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const seguranca = require("../src/seguranca");

const raiz = path.join(__dirname, "..");
const vercel = JSON.parse(fs.readFileSync(path.join(raiz, "vercel.json"), "utf8"));

function cabecalhosDe(origem) {
  const bloco = vercel.headers.find((h) => h.source === origem);
  assert.ok(bloco, `vercel.json não tem bloco de headers para ${origem}`);
  return Object.fromEntries(bloco.headers.map((h) => [h.key, h.value]));
}

test("o CSP estático da Vercel é igual ao que o Express manda", () => {
  const daCdn = cabecalhosDe("/(.*)")["Content-Security-Policy"];
  assert.equal(
    daCdn,
    seguranca.montarCsp(null),
    "o CSP de vercel.json divergiu de seguranca.montarCsp(null)"
  );
});

test("a CDN manda os mesmos cabeçalhos de segurança do Express", () => {
  const daCdn = cabecalhosDe("/(.*)");
  // Captura o que o middleware do Express define, sem duplicar a lista aqui.
  const doExpress = {};
  const res = {
    setHeader(nome, valor) {
      doExpress[nome] = valor;
    },
  };
  seguranca.cabecalhos({}, res, () => {});

  for (const [nome, valor] of Object.entries(doExpress)) {
    assert.equal(daCdn[nome], valor, `cabeçalho ${nome} divergiu entre Express e vercel.json`);
  }
});

test("as rotas dinâmicas estão todas reescritas para a função", () => {
  const destinos = new Set(vercel.rewrites.map((r) => r.destination));
  assert.deepEqual([...destinos], ["/api/index.js"], "há rewrite apontando para outro destino");

  const origens = vercel.rewrites.map((r) => r.source);
  for (const esperada of ["/api/:caminho*", "/health", "/admin", "/admin.html"]) {
    assert.ok(origens.includes(esperada), `falta rewrite para ${esperada}`);
  }
});

test("admin.html não está em public/: na CDN ele sairia sem o nonce do CSP", () => {
  assert.ok(
    !fs.existsSync(path.join(raiz, "public", "admin.html")),
    "public/admin.html voltou a existir — a CDN serviria o painel sem nonce"
  );
  assert.ok(
    fs.existsSync(path.join(raiz, "views", "admin.html")),
    "views/admin.html não existe"
  );
});

test("a função serverless existe e exporta um handler", () => {
  const handler = require("../api/index.js");
  assert.equal(typeof handler, "function");
});

test("outputDirectory é public/ — a função nunca serve estático", () => {
  assert.equal(vercel.outputDirectory, "public");
  assert.equal(vercel.cleanUrls, true, "cleanUrls=true é o que faz /privacidade funcionar");
});
