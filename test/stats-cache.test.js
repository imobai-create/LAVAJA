"use strict";

// Cache padrão (15s) do /api/stats: o banco não pode ser consultado a cada visita.
delete process.env.CACHE_STATS_MS;
delete process.env.DATABASE_URL;
process.env.FOUNDERS_LIMIT = "80";

const { test, beforeEach } = require("node:test");
const assert = require("node:assert/strict");

const db = require("../src/db");
const leads = require("../src/leads");
const config = require("../src/config");

beforeEach(() => {
  db.limparMemoria();
  leads.invalidarCacheStats();
});

test("o cache padrão é de 15 segundos", () => {
  assert.equal(config.cacheStatsMs, 15_000);
});

test("stats vem do cache até expirar e é invalidado por uma nova reserva", async () => {
  const primeiro = await leads.obterStats();
  assert.equal(primeiro.reservadas, 0);

  // Gravação direta no banco não passa pela regra de negócio: o cache segura.
  await db.inserirLead({
    nome: "Teste Cache", whatsapp: "5537911112222", plano: "essencial", consentimento: true,
    origem: "piumhi", cidade: "Piumhi", utm_source: null, utm_medium: null, utm_campaign: null,
    referrer: null, user_agent: null, ip_hash: null,
  });
  const segundo = await leads.obterStats();
  assert.equal(segundo.reservadas, 0, "ainda dentro da janela de cache");

  // Uma reserva pela API invalida o cache e o número atualiza na hora.
  await leads.registrarReserva(
    { nome: "Maria Silva", whatsapp: "37988887777", plano: "essencial", consentimento: true },
    { ip: "198.51.100.1", userAgent: "teste" }
  );
  const terceiro = await leads.obterStats();
  assert.equal(terceiro.reservadas, 2);
});
