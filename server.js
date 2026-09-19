// LavaJá — servidor da landing de pré-venda (Fundadores)
// Node 18+ / Express. Postgres via DATABASE_URL (Railway); sem DATABASE_URL cai em memória (só para teste local).

const express = require("express");
const path = require("path");

const PORT = process.env.PORT || 3000;
const FOUNDERS_LIMIT = parseInt(process.env.FOUNDERS_LIMIT || "80", 10);
const ADMIN_TOKEN = process.env.ADMIN_TOKEN || "";

const app = express();
app.use(express.json({ limit: "50kb" }));
app.use(express.static(path.join(__dirname, "public")));

// ---------- armazenamento ----------
let pool = null;
const memoryLeads = []; // fallback local

async function initDb() {
  if (!process.env.DATABASE_URL) {
    console.warn("[LavaJá] DATABASE_URL ausente — usando memória (os leads somem ao reiniciar). Configure o Postgres no Railway.");
    return;
  }
  const { Pool } = require("pg");
  pool = new Pool({
    connectionString: process.env.DATABASE_URL,
    ssl: process.env.PGSSL === "disable" ? false : { rejectUnauthorized: false },
  });
  await pool.query(`
    CREATE TABLE IF NOT EXISTS leads (
      id SERIAL PRIMARY KEY,
      nome TEXT NOT NULL,
      whatsapp TEXT NOT NULL UNIQUE,
      plano TEXT NOT NULL,
      consentimento BOOLEAN NOT NULL DEFAULT FALSE,
      origem TEXT DEFAULT 'landing-piumhi',
      criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );
  `);
  console.log("[LavaJá] Postgres conectado e tabela leads pronta.");
}

async function countLeads() {
  if (pool) {
    const r = await pool.query("SELECT COUNT(*)::int AS n FROM leads");
    return r.rows[0].n;
  }
  return memoryLeads.length;
}

async function insertLead({ nome, whatsapp, plano, consentimento }) {
  if (pool) {
    await pool.query(
      "INSERT INTO leads (nome, whatsapp, plano, consentimento) VALUES ($1,$2,$3,$4)",
      [nome, whatsapp, plano, consentimento]
    );
  } else {
    if (memoryLeads.some((l) => l.whatsapp === whatsapp)) {
      const err = new Error("duplicado");
      err.code = "23505";
      throw err;
    }
    memoryLeads.push({ id: memoryLeads.length + 1, nome, whatsapp, plano, consentimento, criado_em: new Date().toISOString() });
  }
}

// ---------- rate limit simples (por IP, em memória) ----------
const hits = new Map();
function rateLimited(ip) {
  const now = Date.now();
  const windowMs = 60_000;
  const arr = (hits.get(ip) || []).filter((t) => now - t < windowMs);
  arr.push(now);
  hits.set(ip, arr);
  return arr.length > 10;
}

// ---------- validação ----------
function normalizeWhats(v) {
  const digits = String(v || "").replace(/\D/g, "");
  if (digits.length < 10 || digits.length > 13) return null;
  return digits.startsWith("55") ? digits : "55" + digits;
}
const PLANOS = ["ilimitada-fundador", "essencial", "premium"];

// ---------- rotas ----------
app.get("/api/stats", async (_req, res) => {
  try {
    const n = await countLeads();
    res.json({ limite: FOUNDERS_LIMIT, reservadas: n, restantes: Math.max(FOUNDERS_LIMIT - n, 0) });
  } catch (e) {
    console.error(e);
    res.status(500).json({ erro: "Falha ao consultar vagas." });
  }
});

app.post("/api/leads", async (req, res) => {
  const ip = req.headers["x-forwarded-for"]?.split(",")[0]?.trim() || req.socket.remoteAddress || "?";
  if (rateLimited(ip)) return res.status(429).json({ erro: "Muitas tentativas. Aguarde um minuto." });

  const nome = String(req.body?.nome || "").trim().slice(0, 120);
  const whatsapp = normalizeWhats(req.body?.whatsapp);
  const plano = String(req.body?.plano || "").trim();
  const consentimento = req.body?.consentimento === true;

  if (nome.length < 3) return res.status(400).json({ erro: "Informe seu nome completo." });
  if (!whatsapp) return res.status(400).json({ erro: "Informe um WhatsApp válido com DDD." });
  if (!PLANOS.includes(plano)) return res.status(400).json({ erro: "Escolha um plano." });
  if (!consentimento) return res.status(400).json({ erro: "É preciso autorizar o contato para reservar." });

  try {
    const n = await countLeads();
    const fundador = n < FOUNDERS_LIMIT;
    await insertLead({ nome, whatsapp, plano, consentimento });
    res.status(201).json({
      ok: true,
      fundador,
      mensagem: fundador
        ? "Vaga de fundador reservada. Vamos te chamar no WhatsApp para confirmar — você só paga na inauguração."
        : "As 80 vagas de fundador acabaram, mas você entrou na lista de espera. Te avisamos no WhatsApp.",
    });
  } catch (e) {
    if (e.code === "23505") {
      return res.status(409).json({ erro: "Esse WhatsApp já tem uma reserva. Qualquer dúvida, fale com a gente." });
    }
    console.error(e);
    res.status(500).json({ erro: "Não foi possível salvar agora. Tente de novo em instantes." });
  }
});

// admin: lista de leads em JSON ou CSV. Header: x-admin-token
app.get("/api/leads", async (req, res) => {
  if (!ADMIN_TOKEN || req.headers["x-admin-token"] !== ADMIN_TOKEN) {
    return res.status(401).json({ erro: "Não autorizado." });
  }
  try {
    let rows;
    if (pool) {
      const r = await pool.query("SELECT id, nome, whatsapp, plano, consentimento, criado_em FROM leads ORDER BY id");
      rows = r.rows;
    } else {
      rows = memoryLeads;
    }
    if (req.query.formato === "csv") {
      const header = "id;nome;whatsapp;plano;consentimento;criado_em";
      const body = rows
        .map((l) => [l.id, `"${String(l.nome).replace(/"/g, '""')}"`, l.whatsapp, l.plano, l.consentimento, l.criado_em].join(";"))
        .join("\n");
      res.setHeader("Content-Type", "text/csv; charset=utf-8");
      res.setHeader("Content-Disposition", "attachment; filename=leads-lavaja.csv");
      return res.send(header + "\n" + body);
    }
    res.json({ total: rows.length, leads: rows });
  } catch (e) {
    console.error(e);
    res.status(500).json({ erro: "Falha ao listar." });
  }
});

app.get("/health", (_req, res) => res.json({ ok: true }));

initDb()
  .catch((e) => console.error("[LavaJá] Erro ao iniciar o banco:", e.message))
  .finally(() => {
    app.listen(PORT, () => console.log(`[LavaJá] no ar na porta ${PORT}`));
  });
