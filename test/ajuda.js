// Utilidades dos testes: sobe o servidor numa porta efêmera e fala com ele via fetch.
// Sempre em modo memória (sem DATABASE_URL).

"use strict";

delete process.env.DATABASE_URL;

async function subirServidor() {
  const { iniciar } = require("../server");
  const { porta, encerrar } = await iniciar(0);
  const base = `http://127.0.0.1:${porta}`;
  return { base, encerrar };
}

async function pegarJson(url, opcoes) {
  const resposta = await fetch(url, opcoes);
  let corpo = null;
  try {
    corpo = await resposta.json();
  } catch (_e) {
    corpo = null;
  }
  return { status: resposta.status, corpo, resposta };
}

function postar(base, caminho, dados, cabecalhos = {}) {
  return pegarJson(base + caminho, {
    method: "POST",
    headers: { "content-type": "application/json", ...cabecalhos },
    body: JSON.stringify(dados),
  });
}

function leadValido(extra = {}) {
  return {
    nome: "Maria Aparecida Silva",
    whatsapp: "(37) 98888-7777",
    plano: "ilimitada-fundador",
    consentimento: true,
    ...extra,
  };
}

function franquiaValida(extra = {}) {
  return {
    nome: "João Pedro Souza",
    whatsapp: "(31) 97777-6666",
    email: "joao@exemplo.com.br",
    cidade: "Divinópolis",
    capital: "150k-300k",
    consentimento: true,
    ...extra,
  };
}

module.exports = { subirServidor, pegarJson, postar, leadValido, franquiaValida };
