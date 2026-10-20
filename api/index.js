// FastCarWash — ponto de entrada da função serverless (Vercel).
//
// A Vercel serve public/ pela CDN e manda para cá apenas as rotas dinâmicas
// declaradas em vercel.json: /api/*, /health e /admin. O app Express é o mesmo
// de server.js — aqui só cuidamos do ciclo de vida de uma função:
//
//   - o app é construído uma vez por instância (fora do handler);
//   - db.iniciar() roda no máximo uma vez por instância, numa promessa única;
//   - as migrações NÃO rodam aqui (ver config.migrarNoBoot e npm run migrar).

"use strict";

const { criarApp } = require("../server");
const config = require("../src/config");
const db = require("../src/db");

const app = criarApp();

let preparando = null;

function preparar() {
  if (!preparando) {
    for (const aviso of config.avisoDeAmbiente()) {
      console.warn("[FastCarWash] ATENÇÃO:", aviso);
    }
    // Uma falha aqui não derruba a função: db.iniciar() já cai para memória, e
    // o /health informa o modo em que ficou.
    preparando = db.iniciar().catch((e) => {
      console.error("[FastCarWash] falha ao iniciar o banco:", e.message);
      return "memoria";
    });
  }
  return preparando;
}

module.exports = async function handler(req, res) {
  await preparar();
  return app(req, res);
};
