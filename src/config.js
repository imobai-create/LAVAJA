// FastCarWash — configuração central lida do ambiente.
// Tudo que vem de env passa por aqui, para não espalhar process.env pelo código.

"use strict";

const crypto = require("crypto");

function inteiro(valor, padrao) {
  const n = parseInt(valor, 10);
  return Number.isFinite(n) && n > 0 ? n : padrao;
}

const ADMIN_TOKEN = String(process.env.ADMIN_TOKEN || "").trim();

// Em plataforma serverless (Vercel) cada invocação pode ser um processo novo:
// nada que dependa de memória entre requisições pode ser considerado confiável.
const SERVERLESS = Boolean(process.env.VERCEL || process.env.AWS_LAMBDA_FUNCTION_NAME);

const config = {
  // true quando rodando em função serverless (Vercel). Ver docs/DEPLOY.md.
  serverless: SERVERLESS,

  // Ambiente: a Vercel injeta VERCEL_ENV (production | preview | development).
  ambiente: process.env.VERCEL_ENV || process.env.NODE_ENV || "development",

  // Porta: o host injeta PORT. 0 = porta efêmera (usado nos testes).
  porta: process.env.PORT !== undefined ? parseInt(process.env.PORT, 10) : 3000,

  // Versão exposta em /health — ajuda a saber qual deploy está no ar.
  versao: require("../package.json").version,

  // Limite de vagas de fundador da pré-venda.
  limiteFundadores: inteiro(process.env.FOUNDERS_LIMIT, 80),

  // Token do painel admin. Vazio => rotas admin respondem 503 (nunca liberam).
  adminToken: ADMIN_TOKEN,

  // Número de WhatsApp da operação (só o número, com DDI). Nunca inventar um real no código.
  whatsappNumero: String(process.env.WHATSAPP_NUMERO || "5531992941888").replace(/\D/g, ""),

  // Sal do hash de IP. Preferimos um sal dedicado; na falta dele usamos o
  // ADMIN_TOKEN; e só então um sal aleatório por processo.
  //
  // ATENÇÃO em serverless: o sal aleatório muda a cada processo novo, então o
  // mesmo IP gera hashes diferentes e a deduplicação por IP deixa de funcionar.
  // Em produção, IP_SALT (ou ADMIN_TOKEN) é obrigatório — ver avisoDeAmbiente().
  salIp: String(process.env.IP_SALT || "").trim() || ADMIN_TOKEN || crypto.randomBytes(16).toString("hex"),
  salIpEfemero: !String(process.env.IP_SALT || "").trim() && !ADMIN_TOKEN,

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

  // Rodar as migrações no boot. Em serverless isso custa dezenas de DDLs a cada
  // processo novo: lá o padrão é não rodar, e `npm run migrar` faz o trabalho.
  migrarNoBoot: process.env.MIGRAR_NO_BOOT === "1" || !SERVERLESS,
};

/**
 * Problemas de configuração que valem um aviso alto no log do deploy.
 * Devolve uma lista de strings — vazia significa que está tudo configurado.
 */
function avisoDeAmbiente() {
  const avisos = [];
  const producao = config.ambiente === "production";
  if (!config.databaseUrl) {
    avisos.push(
      producao
        ? "DATABASE_URL ausente em produção: os cadastros NÃO serão gravados em lugar nenhum."
        : "DATABASE_URL ausente: rodando em memória (os dados somem ao reiniciar)."
    );
  }
  if (!config.adminToken) {
    avisos.push("ADMIN_TOKEN ausente: o painel e as exportações responderão 503.");
  }
  if (config.salIpEfemero && config.serverless) {
    avisos.push(
      "IP_SALT e ADMIN_TOKEN ausentes em serverless: o sal do hash de IP muda a cada processo."
    );
  }
  if (config.cspScriptInline) {
    avisos.push("CSP_SCRIPT_INLINE=1: o CSP está aceitando script inline. Desligue quando puder.");
  }
  return avisos;
}

config.avisoDeAmbiente = avisoDeAmbiente;

module.exports = config;
