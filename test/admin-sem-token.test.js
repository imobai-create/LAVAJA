"use strict";

// Sem ADMIN_TOKEN configurado, o painel precisa responder 503 — nunca liberar acesso.
delete process.env.ADMIN_TOKEN;
delete process.env.DATABASE_URL;
process.env.CACHE_STATS_MS = "1";

const { test, before, after } = require("node:test");
const assert = require("node:assert/strict");

const { subirServidor, pegarJson, postar, leadValido } = require("./ajuda");

let base;
let encerrar;

before(async () => {
  const servidor = await subirServidor();
  base = servidor.base;
  encerrar = servidor.encerrar;
});

after(async () => {
  await encerrar("fim dos testes");
});

test("rotas admin respondem 503 quando ADMIN_TOKEN não está definido", async () => {
  for (const caminho of ["/api/leads", "/api/franquia-leads", "/api/admin/resumo"]) {
    const sem = await pegarJson(base + caminho);
    assert.equal(sem.status, 503, caminho);
    assert.match(sem.corpo.erro, /ADMIN_TOKEN/);

    // Nem com um palpite de token: sem configuração, ninguém entra.
    const comPalpite = await pegarJson(base + caminho, { headers: { "x-admin-token": "" } });
    assert.equal(comPalpite.status, 503, caminho);
    const comOutro = await pegarJson(base + caminho, { headers: { "x-admin-token": "qualquer" } });
    assert.equal(comOutro.status, 503, caminho);
    assert.ok(!JSON.stringify(comOutro.corpo).includes("nome"), "não pode vazar dado nenhum");
  }
});

test("as rotas públicas continuam funcionando sem ADMIN_TOKEN", async () => {
  const stats = await pegarJson(base + "/api/stats");
  assert.equal(stats.status, 200);
  const lead = await postar(base, "/api/leads", leadValido({ whatsapp: "37988885555" }));
  assert.equal(lead.status, 201);
});
