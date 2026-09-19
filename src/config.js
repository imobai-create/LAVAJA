// LavaJá — configuração central lida do ambiente.
// Tudo que vem de env passa por aqui, para não espalhar process.env pelo código.

"use strict";

const crypto = require("crypto");

function inteiro(valor, padrao) {
  const n = parseInt(valor, 10);
  return Number.isFinite(n) && n > 0 ? n : padrao;
}

const ADMIN_TOKEN = String(process.env.ADMIN_TOKEN || "").trim();

const config = {
  // Porta: o Railway injeta PORT. 0 = porta efêmera (usado nos testes).
  porta: process.env.PORT !== undefined ? parseInt(process.env.PORT, 10) : 3000,

  // Versão exposta em /health — ajuda a saber qual deploy está no ar.
  versao: require("../package.json").version,

  // Limite de vagas de fundador da pré-venda.
  limiteFundadores: inteiro(process.env.FOUNDERS_LIMIT, 80),

  // Token do painel admin. Vazio => rotas admin respondem 503 (nunca liberam).
  adminToken: ADMIN_TOKEN,

  // Número de WhatsApp da operação (só o número, com DDI). Nunca inventar um real no código.
  whatsappNumero: String(process.env.WHATSAPP_NUMERO || "5531987474828").replace(/\D/g, ""),

  // Sal do hash de IP. Usamos o ADMIN_TOKEN como sal (exigência do projeto);
  // sem ele, geramos um sal aleatório por processo — o IP continua irrecuperável.
  salIp: ADMIN_TOKEN || crypto.randomBytes(16).toString("hex"),

  // Rate limit por IP (configurável para os testes conseguirem forçar o estouro).
  rateLimite: {
    janelaMs: inteiro(process.env.RATE_LIMIT_JANELA_MS, 60_000),
    maxPorIp: inteiro(process.env.RATE_LIMIT_POST, 10),
    maxGlobal: inteiro(process.env.RATE_LIMIT_GLOBAL, 600), // teto global por janela
    limpezaMs: inteiro(process.env.RATE_LIMIT_LIMPEZA_MS, 120_000),
  },

  // Cache do /api/stats, em milissegundos.
  cacheStatsMs: inteiro(process.env.CACHE_STATS_MS, 15_000),

  // Banco
  databaseUrl: process.env.DATABASE_URL || "",
  pgSslDesativado: process.env.PGSSL === "disable",

  // Migração temporária: permite scripts inline enquanto o front não move o JS para /assets.
  cspScriptInline: process.env.CSP_SCRIPT_INLINE === "1",
};

module.exports = config;
