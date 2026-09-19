// LavaJá — validação e normalização de entrada.
// Toda regra devolve { ok:false, erro, campo } para o front destacar o input certo.

"use strict";

const PLANOS = ["ilimitada-fundador", "essencial", "premium"];

// Faixas sugeridas no formulário de franquia (aceitamos texto livre curto
// para não quebrar o front caso ele use outros rótulos).
const FAIXAS_CAPITAL = ["ate-150k", "150k-300k", "300k-500k", "acima-500k", "a-definir"];

const LIMITE_MENSAGEM = 1000;
const LIMITE_USER_AGENT = 300;
const LIMITE_REFERRER = 500;
const LIMITE_UTM = 120;

/** Remove caracteres de controle e espaços das pontas. */
function limpar(valor) {
  return String(valor === undefined || valor === null ? "" : valor)
    .replace(/[\u0000-\u001F\u007F]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function truncar(valor, max) {
  const texto = limpar(valor);
  return texto.length > max ? texto.slice(0, max) : texto;
}

/**
 * Normaliza um WhatsApp brasileiro para o formato 55DDDNUMERO.
 * Aceita 10 a 13 dígitos. Devolve null quando inválido.
 */
function normalizarWhatsapp(valor) {
  const digitos = String(valor === undefined || valor === null ? "" : valor).replace(/\D/g, "");
  if (digitos.length < 10 || digitos.length > 13) return null;

  let local; // DDD + número, sem DDI
  if (digitos.length >= 12) {
    // 12 ou 13 dígitos só fazem sentido com o DDI 55 na frente.
    if (!digitos.startsWith("55")) return null;
    local = digitos.slice(2);
  } else {
    // 10 ou 11 dígitos: é o número local, mesmo que comece com "55" (DDD de Santa Maria/RS).
    local = digitos;
  }
  if (local.length < 10 || local.length > 11) return null;

  const ddd = parseInt(local.slice(0, 2), 10);
  if (!Number.isFinite(ddd) || ddd < 11 || ddd > 99) return null;

  // Números com todos os dígitos iguais são digitação de teste/lixo.
  if (/^(\d)\1+$/.test(local)) return null;

  // Celular de 9 dígitos no Brasil sempre começa com 9.
  if (local.length === 11 && local[2] !== "9") return null;

  return "55" + local;
}

/** Nome: 3 a 120 caracteres e pelo menos duas palavras de 2+ letras. */
function validarNome(valor) {
  const nome = truncar(valor, 200);
  if (nome.length < 3) {
    return { ok: false, erro: "Informe seu nome completo (mínimo 3 letras).", campo: "nome" };
  }
  if (nome.length > 120) {
    return { ok: false, erro: "O nome pode ter no máximo 120 caracteres.", campo: "nome" };
  }
  if (!/[A-Za-zÀ-ÿ]/.test(nome)) {
    return { ok: false, erro: "Informe seu nome completo.", campo: "nome" };
  }
  const palavras = nome.split(" ").filter((p) => p.length >= 2);
  if (palavras.length < 2) {
    return { ok: false, erro: "Informe nome e sobrenome.", campo: "nome" };
  }
  return { ok: true, valor: nome };
}

function validarWhatsapp(valor) {
  const whatsapp = normalizarWhatsapp(valor);
  if (!whatsapp) {
    return { ok: false, erro: "Informe um WhatsApp válido com DDD. Ex.: (37) 99999-9999.", campo: "whatsapp" };
  }
  return { ok: true, valor: whatsapp };
}

function validarPlano(valor) {
  const plano = limpar(valor).toLowerCase();
  if (!PLANOS.includes(plano)) {
    return { ok: false, erro: "Escolha um dos planos disponíveis.", campo: "plano" };
  }
  return { ok: true, valor: plano };
}

/** LGPD: sem consentimento explícito não gravamos nada. */
function validarConsentimento(valor) {
  const aceito = valor === true || valor === "true" || valor === 1 || valor === "1" || valor === "on";
  if (!aceito) {
    return {
      ok: false,
      erro: "É preciso autorizar o contato pelo WhatsApp para concluir.",
      campo: "consentimento",
    };
  }
  return { ok: true, valor: true };
}

function validarEmail(valor) {
  const email = limpar(valor).toLowerCase();
  if (email.length < 5 || email.length > 160 || !/^[^@\s]+@[^@\s.]+(\.[^@\s.]+)+$/.test(email)) {
    return { ok: false, erro: "Informe um e-mail válido.", campo: "email" };
  }
  return { ok: true, valor: email };
}

function validarCidade(valor) {
  const cidade = truncar(valor, 120);
  if (cidade.length < 2) {
    return { ok: false, erro: "Informe a cidade de interesse.", campo: "cidade" };
  }
  return { ok: true, valor: cidade };
}

function validarCapital(valor) {
  const capital = truncar(valor, 60);
  if (capital.length < 2) {
    return { ok: false, erro: "Selecione a faixa de capital disponível.", campo: "capital" };
  }
  return { ok: true, valor: capital };
}

function validarMensagem(valor) {
  const bruta = limpar(valor);
  if (bruta.length > LIMITE_MENSAGEM) {
    return { ok: false, erro: `A mensagem pode ter no máximo ${LIMITE_MENSAGEM} caracteres.`, campo: "mensagem" };
  }
  return { ok: true, valor: bruta };
}

/** Normaliza os utm_* vindos do front (nunca confiar no tamanho). */
function normalizarUtm(utm) {
  const fonte = utm && typeof utm === "object" ? utm : {};
  return {
    source: truncar(fonte.source, LIMITE_UTM) || null,
    medium: truncar(fonte.medium, LIMITE_UTM) || null,
    campaign: truncar(fonte.campaign, LIMITE_UTM) || null,
  };
}

/**
 * Valida o corpo de POST /api/leads.
 * @returns {{ok:true, dados:object}|{ok:false, erro:string, campo:string}}
 */
function validarLead(corpo) {
  const body = corpo && typeof corpo === "object" ? corpo : {};

  const nome = validarNome(body.nome);
  if (!nome.ok) return nome;
  const whatsapp = validarWhatsapp(body.whatsapp);
  if (!whatsapp.ok) return whatsapp;
  const plano = validarPlano(body.plano);
  if (!plano.ok) return plano;
  const consentimento = validarConsentimento(body.consentimento);
  if (!consentimento.ok) return consentimento;

  const utm = normalizarUtm(body.utm);
  return {
    ok: true,
    dados: {
      nome: nome.valor,
      whatsapp: whatsapp.valor,
      plano: plano.valor,
      consentimento: true,
      origem: truncar(body.origem, 60) || "piumhi",
      cidade: truncar(body.cidade, 80) || "Piumhi",
      utm_source: utm.source,
      utm_medium: utm.medium,
      utm_campaign: utm.campaign,
      referrer: truncar(body.referrer, LIMITE_REFERRER) || null,
    },
  };
}

/** Valida o corpo de POST /api/franquia. */
function validarFranquia(corpo) {
  const body = corpo && typeof corpo === "object" ? corpo : {};

  const nome = validarNome(body.nome);
  if (!nome.ok) return nome;
  const whatsapp = validarWhatsapp(body.whatsapp);
  if (!whatsapp.ok) return whatsapp;
  const email = validarEmail(body.email);
  if (!email.ok) return email;
  const cidade = validarCidade(body.cidade);
  if (!cidade.ok) return cidade;
  const capital = validarCapital(body.capital);
  if (!capital.ok) return capital;
  const mensagem = validarMensagem(body.mensagem);
  if (!mensagem.ok) return mensagem;
  const consentimento = validarConsentimento(body.consentimento);
  if (!consentimento.ok) return consentimento;

  const utm = normalizarUtm(body.utm);
  return {
    ok: true,
    dados: {
      nome: nome.valor,
      whatsapp: whatsapp.valor,
      email: email.valor,
      cidade_interesse: cidade.valor,
      capital_disponivel: capital.valor,
      mensagem: mensagem.valor || null,
      consentimento: true,
      utm_source: utm.source,
      utm_medium: utm.medium,
      utm_campaign: utm.campaign,
    },
  };
}

module.exports = {
  PLANOS,
  FAIXAS_CAPITAL,
  LIMITE_USER_AGENT,
  limpar,
  truncar,
  normalizarWhatsapp,
  normalizarUtm,
  validarNome,
  validarWhatsapp,
  validarPlano,
  validarConsentimento,
  validarEmail,
  validarCidade,
  validarCapital,
  validarMensagem,
  validarLead,
  validarFranquia,
};
