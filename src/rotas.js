// LavaJá — definição das rotas da API e do painel.

"use strict";

const express = require("express");
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const config = require("./config");
const db = require("./db");
const leads = require("./leads");
const seguranca = require("./seguranca");
const { paraCsv } = require("./csv");

/** Embrulha handlers async para que nenhuma rejeição derrube o processo. */
function assincrono(handler) {
  return (req, res, proximo) => Promise.resolve(handler(req, res, proximo)).catch(proximo);
}

function contextoDaRequisicao(req) {
  return {
    ip: seguranca.ipDoCliente(req),
    userAgent: req.headers["user-agent"] || "",
  };
}

function responderErro(res, e) {
  if (e instanceof leads.ErroNegocio) {
    const corpo = { erro: e.message };
    if (e.campo) corpo.campo = e.campo;
    return res.status(e.status).json(corpo);
  }
  return null;
}

const COLUNAS_LEADS_CSV = [
  { chave: "id", titulo: "id" },
  { chave: "nome", titulo: "nome" },
  { chave: "whatsapp", titulo: "whatsapp" },
  { chave: "plano", titulo: "plano" },
  { chave: "consentimento", titulo: "consentimento" },
  { chave: "origem", titulo: "origem" },
  { chave: "cidade", titulo: "cidade" },
  { chave: "utm_source", titulo: "utm_source" },
  { chave: "utm_medium", titulo: "utm_medium" },
  { chave: "utm_campaign", titulo: "utm_campaign" },
  { chave: "referrer", titulo: "referrer" },
  { chave: "status", titulo: "status" },
  { chave: "criado_em", titulo: "criado_em" },
];

const COLUNAS_FRANQUIA_CSV = [
  { chave: "id", titulo: "id" },
  { chave: "nome", titulo: "nome" },
  { chave: "whatsapp", titulo: "whatsapp" },
  { chave: "email", titulo: "email" },
  { chave: "cidade_interesse", titulo: "cidade_interesse" },
  { chave: "capital_disponivel", titulo: "capital_disponivel" },
  { chave: "mensagem", titulo: "mensagem" },
  { chave: "consentimento", titulo: "consentimento" },
  { chave: "utm_source", titulo: "utm_source" },
  { chave: "utm_medium", titulo: "utm_medium" },
  { chave: "utm_campaign", titulo: "utm_campaign" },
  { chave: "status", titulo: "status" },
  { chave: "criado_em", titulo: "criado_em" },
];

function enviarCsv(res, nomeArquivo, linhas, colunas) {
  res.setHeader("Content-Type", "text/csv; charset=utf-8");
  res.setHeader("Content-Disposition", `attachment; filename="${nomeArquivo}"`);
  res.setHeader("Cache-Control", "no-store");
  return res.send(paraCsv(linhas, colunas));
}

function criarRotas() {
  const rotas = express.Router();

  // ---------- público ----------
  rotas.get(
    "/api/stats",
    assincrono(async (_req, res) => {
      res.setHeader("Cache-Control", "no-store");
      res.json(await leads.obterStats());
    })
  );

  rotas.post(
    "/api/leads",
    seguranca.limitarEscrita,
    assincrono(async (req, res) => {
      try {
        const resultado = await leads.registrarReserva(req.body, contextoDaRequisicao(req));
        res.status(201).json(resultado);
      } catch (e) {
        if (!responderErro(res, e)) throw e;
      }
    })
  );

  rotas.post(
    "/api/franquia",
    seguranca.limitarEscrita,
    assincrono(async (req, res) => {
      try {
        const resultado = await leads.registrarInteresseFranquia(req.body, contextoDaRequisicao(req));
        res.status(201).json(resultado);
      } catch (e) {
        if (!responderErro(res, e)) throw e;
      }
    })
  );

  // ---------- admin ----------
  rotas.get(
    "/api/leads",
    seguranca.exigirAdmin,
    assincrono(async (req, res) => {
      const linhas = await db.listarLeads();
      if (String(req.query.formato || "").toLowerCase() === "csv") {
        return enviarCsv(res, "leads-lavaja.csv", linhas, COLUNAS_LEADS_CSV);
      }
      res.setHeader("Cache-Control", "no-store");
      res.json({ total: linhas.length, leads: linhas });
    })
  );

  rotas.get(
    "/api/franquia-leads",
    seguranca.exigirAdmin,
    assincrono(async (req, res) => {
      const linhas = await db.listarFranquiaLeads();
      if (String(req.query.formato || "").toLowerCase() === "csv") {
        return enviarCsv(res, "franquia-lavaja.csv", linhas, COLUNAS_FRANQUIA_CSV);
      }
      res.setHeader("Cache-Control", "no-store");
      res.json({ total: linhas.length, leads: linhas });
    })
  );

  rotas.get(
    "/api/admin/resumo",
    seguranca.exigirAdmin,
    assincrono(async (_req, res) => {
      const [resumo, stats] = await Promise.all([db.resumo(14), leads.obterStats()]);
      res.setHeader("Cache-Control", "no-store");
      res.json({ ...resumo, limite: stats.limite, restantes: stats.restantes, esgotado: stats.esgotado });
    })
  );

  // ---------- saúde ----------
  rotas.get("/health", (_req, res) => {
    res.setHeader("Cache-Control", "no-store");
    res.json({ ok: true, banco: db.tipo(), versao: config.versao });
  });

  return rotas;
}

/**
 * Painel admin servido com nonce por requisição, para manter o CSP sem
 * 'unsafe-inline' em script. O arquivo traz o marcador __NONCE__ nas tags.
 */
function rotaPainel(diretorioPublico) {
  const arquivo = path.join(diretorioPublico, "admin.html");
  return (_req, res, proximo) => {
    fs.readFile(arquivo, "utf8", (erro, html) => {
      if (erro) return proximo(); // deixa o 404 padrão responder
      const nonce = crypto.randomBytes(16).toString("base64");
      res.setHeader("Content-Type", "text/html; charset=utf-8");
      res.setHeader("Cache-Control", "no-store");
      res.setHeader("X-Robots-Tag", "noindex, nofollow");
      res.setHeader("Content-Security-Policy", seguranca.montarCsp(nonce));
      res.send(html.replace(/__NONCE__/g, nonce));
    });
  };
}

/** 404 de /api sempre em JSON — o front nunca deve receber HTML. */
function naoEncontradoApi(req, res) {
  res.status(404).json({ erro: `Rota não encontrada: ${req.method} ${req.originalUrl}` });
}

/** Erro não tratado: log completo no servidor, mensagem genérica pro cliente. */
function tratadorDeErro(erro, req, res, _proximo) {
  // Erros do express.json(): corpo malformado ou grande demais.
  if (erro && (erro.type === "entity.parse.failed" || erro instanceof SyntaxError) && erro.status === 400) {
    return res.status(400).json({ erro: "Não entendemos os dados enviados. Recarregue a página e tente de novo." });
  }
  if (erro && erro.type === "entity.too.large") {
    return res.status(413).json({ erro: "Dados enviados grandes demais." });
  }
  console.error("[LavaJá] erro não tratado em", req.method, req.originalUrl, "-", erro && erro.stack ? erro.stack : erro);
  if (res.headersSent) return;
  const ehApi = req.path.startsWith("/api") || req.path === "/health";
  if (ehApi) {
    return res.status(500).json({ erro: "Não foi possível concluir agora. Tente de novo em instantes." });
  }
  res.status(500).type("text/plain; charset=utf-8").send("Erro interno. Tente de novo em instantes.");
}

module.exports = { criarRotas, rotaPainel, naoEncontradoApi, tratadorDeErro, assincrono };
