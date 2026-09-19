"use strict";

// Limites bem baixos para o estouro acontecer sem centenas de requisições.
process.env.ADMIN_TOKEN = "token-de-teste-123";
process.env.RATE_LIMIT_POST = "3";
process.env.RATE_LIMIT_GLOBAL = "8";
process.env.RATE_LIMIT_JANELA_MS = "60000";
process.env.CACHE_STATS_MS = "1";
delete process.env.DATABASE_URL;

const { test, before, after, beforeEach } = require("node:test");
const assert = require("node:assert/strict");

const { subirServidor, postar, leadValido } = require("./ajuda");
const db = require("../src/db");
const leads = require("../src/leads");
const seguranca = require("../src/seguranca");
const config = require("../src/config");

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

test("POST acima de 3 por minuto no mesmo IP responde 429", async () => {
  const ip = { "x-forwarded-for": "198.51.100.7" };
  for (let i = 0; i < 3; i++) {
    const r = await postar(base, "/api/leads", leadValido({ whatsapp: `3798887000${i}` }), ip);
    assert.equal(r.status, 201, `requisição ${i + 1}`);
  }
  const estourou = await postar(base, "/api/leads", leadValido({ whatsapp: "37988870009" }), ip);
  assert.equal(estourou.status, 429);
  assert.match(estourou.corpo.erro, /muitas tentativas/i);

  // Outro IP continua passando: o limite é por IP.
  const outro = await postar(base, "/api/leads", leadValido({ whatsapp: "37988871111" }), { "x-forwarded-for": "198.51.100.8" });
  assert.equal(outro.status, 201);
});

test("teto global protege contra enxurrada de IPs diferentes", async () => {
  let bloqueios = 0;
  for (let i = 0; i < 12; i++) {
    const r = await postar(
      base,
      "/api/leads",
      leadValido({ whatsapp: `379888620${String(i).padStart(2, "0")}` }),
      { "x-forwarded-for": `203.0.113.${i}` }
    );
    if (r.status === 429) bloqueios += 1;
  }
  assert.ok(bloqueios > 0, "o teto global precisa bloquear alguém");
});

test("o Map do rate limit não cresce para sempre (limpeza dos vencidos)", () => {
  const tetoOriginal = config.rateLimite.maxGlobal;
  config.rateLimite.maxGlobal = 100_000; // o teto global não pode atrapalhar este teste
  try {
    seguranca.zerarRateLimit();
    const t0 = Date.now();
    for (let i = 0; i < 50; i++) seguranca.registrarAcesso("10.0.0." + i, t0);
    assert.equal(seguranca.tamanhoRateLimit(), 50);

    // Depois da janela, a limpeza periódica remove todas as entradas vencidas.
    seguranca.limparExpirados(t0 + config.rateLimite.janelaMs + 1);
    assert.equal(seguranca.tamanhoRateLimit(), 0);
  } finally {
    config.rateLimite.maxGlobal = tetoOriginal;
  }
});

test("a janela reabre depois que expira", () => {
  seguranca.zerarRateLimit();
  const t0 = Date.now();
  for (let i = 0; i < config.rateLimite.maxPorIp; i++) {
    assert.equal(seguranca.registrarAcesso("10.1.1.1", t0).bloqueado, false);
  }
  assert.equal(seguranca.registrarAcesso("10.1.1.1", t0).bloqueado, true);
  const depois = t0 + config.rateLimite.janelaMs + 1;
  assert.equal(seguranca.registrarAcesso("10.1.1.1", depois).bloqueado, false);
});
