"use strict";

// Ambiente do teste: precisa ser definido ANTES de carregar os módulos,
// porque src/config.js lê process.env na carga.
process.env.ADMIN_TOKEN = "token-de-teste-123";
process.env.FOUNDERS_LIMIT = "3";
process.env.CACHE_STATS_MS = "1"; // cache praticamente desligado para conferir os números
process.env.RATE_LIMIT_POST = "500";
process.env.RATE_LIMIT_GLOBAL = "5000";
process.env.WHATSAPP_NUMERO = "5537912345678";
delete process.env.DATABASE_URL;

const { test, before, after, beforeEach } = require("node:test");
const assert = require("node:assert/strict");

const { subirServidor, pegarJson, postar, leadValido, franquiaValida } = require("./ajuda");
const db = require("../src/db");
const leads = require("../src/leads");
const seguranca = require("../src/seguranca");

const TOKEN = process.env.ADMIN_TOKEN;
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

beforeEach(() => {
  db.limparMemoria();
  leads.invalidarCacheStats();
  seguranca.zerarRateLimit();
});

test("GET /health informa banco e versão", async () => {
  const { status, corpo } = await pegarJson(base + "/health");
  assert.equal(status, 200);
  assert.equal(corpo.ok, true);
  assert.equal(corpo.banco, "memoria");
  assert.equal(typeof corpo.versao, "string");
});

test("GET /api/stats devolve o contrato e acompanha as reservas", async () => {
  let r = await pegarJson(base + "/api/stats");
  assert.equal(r.status, 200);
  assert.deepEqual(Object.keys(r.corpo).sort(), ["esgotado", "limite", "reservadas", "restantes", "whatsapp"]);
  assert.equal(r.corpo.limite, 3);
  assert.equal(r.corpo.reservadas, 0);
  assert.equal(r.corpo.restantes, 3);
  assert.equal(r.corpo.esgotado, false);
  assert.equal(r.corpo.whatsapp, "5537912345678");

  await postar(base, "/api/leads", leadValido());
  r = await pegarJson(base + "/api/stats");
  assert.equal(r.corpo.reservadas, 1);
  assert.equal(r.corpo.restantes, 2);
  assert.equal(r.corpo.limite, r.corpo.reservadas + r.corpo.restantes);
});

test("POST /api/leads cria reserva de fundador", async () => {
  const { status, corpo } = await postar(base, "/api/leads", leadValido());
  assert.equal(status, 201);
  assert.equal(corpo.ok, true);
  assert.equal(corpo.fundador, true);
  assert.equal(corpo.posicao, 1);
  assert.match(corpo.mensagem, /fundador/i);
});

test("acima do limite vira lista de espera (fundador:false)", async () => {
  for (let i = 0; i < 3; i++) {
    const r = await postar(base, "/api/leads", leadValido({ whatsapp: `3798888000${i}` }));
    assert.equal(r.status, 201);
    assert.equal(r.corpo.fundador, true);
  }
  const quarto = await postar(base, "/api/leads", leadValido({ whatsapp: "37988880009" }));
  assert.equal(quarto.status, 201);
  assert.equal(quarto.corpo.fundador, false);
  assert.equal(quarto.corpo.posicao, 4);

  const stats = await pegarJson(base + "/api/stats");
  assert.equal(stats.corpo.esgotado, true);
  assert.equal(stats.corpo.restantes, 0);
});

test("WhatsApp duplicado responde 409 com campo whatsapp", async () => {
  await postar(base, "/api/leads", leadValido());
  const r = await postar(base, "/api/leads", leadValido({ nome: "Outra Pessoa", whatsapp: "37 98888-7777" }));
  assert.equal(r.status, 409);
  assert.equal(r.corpo.campo, "whatsapp");
  assert.match(r.corpo.erro, /já tem uma reserva/i);
});

test("erros de validação trazem o campo certo", async () => {
  const casos = [
    [{ nome: "Ana" }, "nome"],
    [{ whatsapp: "123" }, "whatsapp"],
    [{ plano: "ouro" }, "plano"],
    [{ consentimento: false }, "consentimento"],
  ];
  for (const [alteracao, campo] of casos) {
    const r = await postar(base, "/api/leads", leadValido(alteracao));
    assert.equal(r.status, 400, JSON.stringify(alteracao));
    assert.equal(r.corpo.campo, campo);
    assert.equal(typeof r.corpo.erro, "string");
  }
});

test("sem consentimento nada é gravado (LGPD)", async () => {
  const r = await postar(base, "/api/leads", leadValido({ consentimento: false }));
  assert.equal(r.status, 400);
  const stats = await pegarJson(base + "/api/stats");
  assert.equal(stats.corpo.reservadas, 0);
});

test("POST /api/franquia registra interesse sem prometer franquia", async () => {
  const { status, corpo } = await postar(base, "/api/franquia", franquiaValida());
  assert.equal(status, 201);
  assert.equal(corpo.ok, true);
  assert.match(corpo.mensagem, /interesse registrado/i);
  assert.match(corpo.mensagem, /13\.966/);
  assert.match(corpo.mensagem, /nenhum pagamento/i);
  // Não pode soar como oferta.
  assert.doesNotMatch(corpo.mensagem, /garantid|investimento aprovado|compre|taxa de adesão/i);

  const dup = await postar(base, "/api/franquia", franquiaValida());
  assert.equal(dup.status, 409);
});

test("rotas admin exigem token", async () => {
  for (const caminho of ["/api/leads", "/api/franquia-leads", "/api/admin/resumo"]) {
    const sem = await pegarJson(base + caminho);
    assert.equal(sem.status, 401, caminho);
    assert.equal(typeof sem.corpo.erro, "string");

    const errado = await pegarJson(base + caminho, { headers: { "x-admin-token": "outro" } });
    assert.equal(errado.status, 401, caminho);

    const certo = await pegarJson(base + caminho, { headers: { "x-admin-token": TOKEN } });
    assert.equal(certo.status, 200, caminho);
  }
});

test("CSV sai com BOM UTF-8, separador ; e aspas escapadas", async () => {
  await postar(base, "/api/leads", leadValido({ nome: 'Maria "Teste" Silva; Souza' }));
  const resposta = await fetch(base + "/api/leads?formato=csv", { headers: { "x-admin-token": TOKEN } });
  assert.equal(resposta.status, 200);
  assert.match(resposta.headers.get("content-type"), /text\/csv/);
  assert.match(resposta.headers.get("content-disposition"), /leads-jatoja\.csv/);

  // Conferimos os bytes crus: fetch().text() descarta o BOM ao decodificar.
  const bytes = Buffer.from(await resposta.arrayBuffer());
  assert.deepEqual([...bytes.subarray(0, 3)], [0xef, 0xbb, 0xbf], "precisa começar com BOM UTF-8");
  const texto = bytes.toString("utf8");
  assert.equal(texto.charCodeAt(0), 0xfeff);
  const linhas = texto.slice(1).split("\r\n");
  assert.equal(linhas[0].split(";")[0], "id");
  assert.ok(linhas[0].includes("whatsapp"));
  assert.ok(linhas[1].includes('"Maria ""Teste"" Silva; Souza"'), linhas[1]);

  const franquiaCsv = await fetch(base + "/api/franquia-leads?formato=csv", { headers: { "x-admin-token": TOKEN } });
  const bytesFranquia = Buffer.from(await franquiaCsv.arrayBuffer());
  assert.deepEqual([...bytesFranquia.subarray(0, 3)], [0xef, 0xbb, 0xbf]);
  assert.ok(bytesFranquia.toString("utf8").includes("capital_disponivel"));
});

test("GET /api/admin/resumo traz totais, planos, dias e utm", async () => {
  await postar(base, "/api/leads", leadValido({ whatsapp: "37988881111", utm: { source: "instagram", medium: "bio" } }));
  await postar(base, "/api/leads", leadValido({ whatsapp: "37988882222", plano: "essencial" }));
  await postar(base, "/api/franquia", franquiaValida());

  const { status, corpo } = await pegarJson(base + "/api/admin/resumo", { headers: { "x-admin-token": TOKEN } });
  assert.equal(status, 200);
  assert.equal(corpo.total_leads, 2);
  assert.equal(corpo.total_franquia, 1);
  assert.equal(corpo.hoje, 2);
  assert.equal(corpo.por_dia.length, 14);
  assert.equal(corpo.por_dia[13].total, 2, "o último dia da série é hoje");
  assert.equal(corpo.por_plano.reduce((s, p) => s + p.total, 0), 2);
  assert.ok(corpo.por_utm_source.some((u) => u.valor === "instagram"));
  assert.ok(corpo.por_utm_source.some((u) => u.valor === "direto"));
  assert.equal(corpo.limite, 3);
});

test("404 de API responde JSON e não HTML", async () => {
  const resposta = await fetch(base + "/api/rota-que-nao-existe");
  assert.equal(resposta.status, 404);
  assert.match(resposta.headers.get("content-type"), /application\/json/);
  const corpo = await resposta.json();
  assert.match(corpo.erro, /não encontrada/i);
});

test("JSON malformado vira 400 e não derruba o processo", async () => {
  const resposta = await fetch(base + "/api/leads", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: "{isso não é json",
  });
  assert.equal(resposta.status, 400);
  const corpo = await resposta.json();
  assert.equal(typeof corpo.erro, "string");
});

test("cabeçalhos de segurança presentes e CSP sem unsafe-eval", async () => {
  const resposta = await fetch(base + "/health");
  assert.equal(resposta.headers.get("x-content-type-options"), "nosniff");
  assert.equal(resposta.headers.get("referrer-policy"), "strict-origin-when-cross-origin");
  assert.equal(resposta.headers.get("x-frame-options"), "DENY");
  assert.ok(resposta.headers.get("permissions-policy").includes("geolocation=()"));
  assert.equal(resposta.headers.get("x-powered-by"), null);

  const csp = resposta.headers.get("content-security-policy");
  assert.ok(csp.includes("connect-src 'self'"));
  assert.ok(csp.includes("fonts.googleapis.com"));
  assert.ok(csp.includes("fonts.gstatic.com"));
  assert.ok(csp.includes("img-src 'self' data:"));
  assert.ok(!csp.includes("unsafe-eval"));
  assert.ok(!/script-src[^;]*unsafe-inline/.test(csp));
});

test("painel /admin.html é servido com nonce, noindex e sem cache", async () => {
  const resposta = await fetch(base + "/admin.html");
  assert.equal(resposta.status, 200);
  assert.equal(resposta.headers.get("cache-control"), "no-store");
  assert.match(resposta.headers.get("x-robots-tag"), /noindex/);
  const html = await resposta.text();
  assert.ok(!html.includes("__NONCE__"), "o marcador precisa ser substituído");
  assert.match(html, /<meta name="robots" content="noindex/);
  const csp = resposta.headers.get("content-security-policy");
  const nonce = csp.match(/'nonce-([^']+)'/);
  assert.ok(nonce, "CSP do painel precisa ter nonce");
  assert.ok(html.includes(`nonce="${nonce[1]}"`));
});

test("o IP nunca é gravado em texto puro (só hash)", async () => {
  await postar(base, "/api/leads", leadValido(), { "x-forwarded-for": "203.0.113.9" });
  const lista = await pegarJson(base + "/api/leads", { headers: { "x-admin-token": TOKEN } });
  const bruto = JSON.stringify(lista.corpo);
  assert.ok(!bruto.includes("203.0.113.9"));
  assert.notEqual(db.hashIp("203.0.113.9"), "203.0.113.9");
  assert.equal(db.hashIp("203.0.113.9").length, 64);
});
