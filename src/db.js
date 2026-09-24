// JatoJá — acesso a dados.
// Usa Postgres quando DATABASE_URL existe; senão, cai num armazenamento em
// memória com o mesmo contrato (inclusive erro 23505 de duplicidade), para
// desenvolvimento local e para os testes automatizados.

"use strict";

const crypto = require("crypto");
const config = require("./config");

let pool = null;
let modo = "memoria";

// ---------- armazenamento em memória (fallback) ----------
const memoria = {
  leads: [],
  franquia: [],
  seqLeads: 0,
  seqFranquia: 0,
};

function erroDuplicado() {
  const erro = new Error("registro duplicado");
  erro.code = "23505";
  return erro;
}

/** Zera o armazenamento em memória. Usado só pelos testes. */
function limparMemoria() {
  memoria.leads.length = 0;
  memoria.franquia.length = 0;
  memoria.seqLeads = 0;
  memoria.seqFranquia = 0;
}

// ---------- migrações (idempotentes) ----------
// CREATE TABLE IF NOT EXISTS + ALTER TABLE ADD COLUMN IF NOT EXISTS: roda em
// base nova e em base já existente sem quebrar nem perder dado.
const MIGRACOES = [
  `CREATE TABLE IF NOT EXISTS leads (
     id SERIAL PRIMARY KEY,
     nome TEXT NOT NULL,
     whatsapp TEXT NOT NULL UNIQUE,
     plano TEXT NOT NULL,
     consentimento BOOLEAN NOT NULL DEFAULT FALSE,
     criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
   )`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS origem TEXT DEFAULT 'piumhi'`,
  `ALTER TABLE leads ALTER COLUMN origem SET DEFAULT 'piumhi'`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS cidade TEXT DEFAULT 'Piumhi'`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS utm_source TEXT`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS utm_medium TEXT`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS utm_campaign TEXT`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS referrer TEXT`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS user_agent TEXT`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS ip_hash TEXT`,
  `ALTER TABLE leads ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'novo'`,
  `UPDATE leads SET status = 'novo' WHERE status IS NULL`,
  `CREATE UNIQUE INDEX IF NOT EXISTS leads_whatsapp_uidx ON leads (whatsapp)`,
  `CREATE INDEX IF NOT EXISTS leads_criado_em_idx ON leads (criado_em)`,

  `CREATE TABLE IF NOT EXISTS franquia_leads (
     id SERIAL PRIMARY KEY,
     nome TEXT NOT NULL,
     whatsapp TEXT NOT NULL UNIQUE,
     email TEXT,
     cidade_interesse TEXT,
     capital_disponivel TEXT,
     mensagem TEXT,
     consentimento BOOLEAN NOT NULL DEFAULT FALSE,
     criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
   )`,
  `ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS utm_source TEXT`,
  `ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS utm_medium TEXT`,
  `ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS utm_campaign TEXT`,
  `ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS user_agent TEXT`,
  `ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS ip_hash TEXT`,
  `ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'novo'`,
  `CREATE UNIQUE INDEX IF NOT EXISTS franquia_leads_whatsapp_uidx ON franquia_leads (whatsapp)`,
];

async function iniciar() {
  if (!config.databaseUrl) {
    modo = "memoria";
    console.warn(
      "[JatoJá] DATABASE_URL ausente — rodando em memória (os dados somem ao reiniciar). Configure o Postgres no Railway."
    );
    return modo;
  }
  const { Pool } = require("pg");
  pool = new Pool({
    connectionString: config.databaseUrl,
    ssl: config.pgSslDesativado ? false : { rejectUnauthorized: false },
    max: 5,
    idleTimeoutMillis: 30_000,
    connectionTimeoutMillis: 10_000,
  });
  // O pool emite 'error' em conexões ociosas derrubadas pelo provedor;
  // sem esse listener o processo cairia.
  pool.on("error", (e) => console.error("[JatoJá] erro no pool do Postgres:", e.message));

  // Se nem conectar dá, voltamos para a memória em vez de derrubar o site.
  try {
    await pool.query("SELECT 1");
  } catch (e) {
    console.error("[JatoJá] não foi possível conectar ao Postgres:", e.message, "— seguindo em memória.");
    await pool.end().catch(() => {});
    pool = null;
    modo = "memoria";
    return modo;
  }
  modo = "postgres";

  // Cada migração é independente: uma falha é registrada, mas não impede o boot.
  let falhas = 0;
  for (const sql of MIGRACOES) {
    try {
      await pool.query(sql);
    } catch (e) {
      falhas += 1;
      console.error("[JatoJá] migração falhou:", sql.split("\n")[0].trim(), "->", e.message);
    }
  }
  console.log(`[JatoJá] Postgres conectado, migrações aplicadas${falhas ? ` (${falhas} com erro, veja o log)` : ""}.`);
  return modo;
}

function tipo() {
  return modo;
}

/** Hash irreversível do IP (LGPD: nunca gravamos o IP cru). */
function hashIp(ip) {
  if (!ip) return null;
  return crypto.createHash("sha256").update(String(ip) + "|" + config.salIp).digest("hex");
}

// ---------- leads ----------
async function contarLeads() {
  if (pool) {
    const r = await pool.query("SELECT COUNT(*)::int AS n FROM leads");
    return r.rows[0].n;
  }
  return memoria.leads.length;
}

async function inserirLead(dados) {
  if (pool) {
    const r = await pool.query(
      `INSERT INTO leads
         (nome, whatsapp, plano, consentimento, origem, cidade,
          utm_source, utm_medium, utm_campaign, referrer, user_agent, ip_hash, status)
       VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,'novo')
       RETURNING id, criado_em`,
      [
        dados.nome, dados.whatsapp, dados.plano, dados.consentimento, dados.origem, dados.cidade,
        dados.utm_source, dados.utm_medium, dados.utm_campaign, dados.referrer,
        dados.user_agent, dados.ip_hash,
      ]
    );
    return r.rows[0];
  }
  if (memoria.leads.some((l) => l.whatsapp === dados.whatsapp)) throw erroDuplicado();
  const registro = {
    id: ++memoria.seqLeads,
    ...dados,
    status: "novo",
    criado_em: new Date().toISOString(),
  };
  memoria.leads.push(registro);
  return { id: registro.id, criado_em: registro.criado_em };
}

const COLUNAS_LEADS =
  "id, nome, whatsapp, plano, consentimento, origem, cidade, utm_source, utm_medium, utm_campaign, referrer, status, criado_em";

async function listarLeads() {
  if (pool) {
    const r = await pool.query(`SELECT ${COLUNAS_LEADS} FROM leads ORDER BY id`);
    return r.rows;
  }
  // Não devolvemos ip_hash nem user_agent na listagem: não interessam ao painel.
  return memoria.leads.map((l) => ({
    id: l.id, nome: l.nome, whatsapp: l.whatsapp, plano: l.plano,
    consentimento: l.consentimento, origem: l.origem, cidade: l.cidade,
    utm_source: l.utm_source, utm_medium: l.utm_medium, utm_campaign: l.utm_campaign,
    referrer: l.referrer, status: l.status, criado_em: l.criado_em,
  }));
}

// ---------- franquia ----------
async function inserirFranquiaLead(dados) {
  if (pool) {
    const r = await pool.query(
      `INSERT INTO franquia_leads
         (nome, whatsapp, email, cidade_interesse, capital_disponivel, mensagem,
          consentimento, utm_source, utm_medium, utm_campaign, user_agent, ip_hash, status)
       VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,'novo')
       RETURNING id, criado_em`,
      [
        dados.nome, dados.whatsapp, dados.email, dados.cidade_interesse, dados.capital_disponivel,
        dados.mensagem, dados.consentimento, dados.utm_source, dados.utm_medium, dados.utm_campaign,
        dados.user_agent, dados.ip_hash,
      ]
    );
    return r.rows[0];
  }
  if (memoria.franquia.some((l) => l.whatsapp === dados.whatsapp)) throw erroDuplicado();
  const registro = {
    id: ++memoria.seqFranquia,
    ...dados,
    status: "novo",
    criado_em: new Date().toISOString(),
  };
  memoria.franquia.push(registro);
  return { id: registro.id, criado_em: registro.criado_em };
}

const COLUNAS_FRANQUIA =
  "id, nome, whatsapp, email, cidade_interesse, capital_disponivel, mensagem, consentimento, utm_source, utm_medium, utm_campaign, status, criado_em";

async function listarFranquiaLeads() {
  if (pool) {
    const r = await pool.query(`SELECT ${COLUNAS_FRANQUIA} FROM franquia_leads ORDER BY id`);
    return r.rows;
  }
  return memoria.franquia.map((l) => ({
    id: l.id, nome: l.nome, whatsapp: l.whatsapp, email: l.email,
    cidade_interesse: l.cidade_interesse, capital_disponivel: l.capital_disponivel,
    mensagem: l.mensagem, consentimento: l.consentimento,
    utm_source: l.utm_source, utm_medium: l.utm_medium, utm_campaign: l.utm_campaign,
    status: l.status, criado_em: l.criado_em,
  }));
}

// ---------- agregados do painel ----------
function diaISO(valor) {
  const d = valor instanceof Date ? valor : new Date(valor);
  return Number.isNaN(d.getTime()) ? null : d.toISOString().slice(0, 10);
}

function agrupar(linhas, chave, padrao) {
  const mapa = new Map();
  for (const linha of linhas) {
    const k = linha[chave] || padrao;
    mapa.set(k, (mapa.get(k) || 0) + 1);
  }
  return [...mapa.entries()]
    .map(([valor, total]) => ({ valor, total }))
    .sort((a, b) => b.total - a.total);
}

/** Totais do painel admin: por plano, por dia (14 dias) e por utm_source. */
async function resumo(dias = 14) {
  const leads = await listarLeads();
  const franquia = await listarFranquiaLeads();

  const hoje = new Date();
  const serie = [];
  const contagemDia = new Map();
  for (const l of leads) {
    const d = diaISO(l.criado_em);
    if (d) contagemDia.set(d, (contagemDia.get(d) || 0) + 1);
  }
  for (let i = dias - 1; i >= 0; i--) {
    const d = new Date(hoje.getTime() - i * 86_400_000).toISOString().slice(0, 10);
    serie.push({ dia: d, total: contagemDia.get(d) || 0 });
  }

  const hojeISO = diaISO(hoje);
  return {
    total_leads: leads.length,
    total_franquia: franquia.length,
    hoje: leads.filter((l) => diaISO(l.criado_em) === hojeISO).length,
    por_plano: agrupar(leads, "plano", "(sem plano)"),
    por_dia: serie,
    por_utm_source: agrupar(leads, "utm_source", "direto"),
  };
}

async function encerrar() {
  if (pool) {
    const p = pool;
    pool = null;
    await p.end().catch((e) => console.error("[JatoJá] erro ao fechar o pool:", e.message));
  }
}

module.exports = {
  iniciar,
  encerrar,
  tipo,
  hashIp,
  contarLeads,
  inserirLead,
  listarLeads,
  inserirFranquiaLead,
  listarFranquiaLeads,
  resumo,
  limparMemoria,
  MIGRACOES,
};
