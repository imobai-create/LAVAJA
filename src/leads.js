// JatoJá — regras de negócio da pré-venda e do interesse em franquia.

"use strict";

const config = require("./config");
const db = require("./db");
const { validarLead, validarFranquia, truncar, LIMITE_USER_AGENT } = require("./validacao");

// Erro de negócio com status HTTP e campo do formulário.
class ErroNegocio extends Error {
  constructor(status, mensagem, campo) {
    super(mensagem);
    this.status = status;
    this.campo = campo || null;
  }
}

// ---------- cache do /api/stats (15s) ----------
let cacheStats = { valor: null, expiraEm: 0 };

function invalidarCacheStats() {
  cacheStats = { valor: null, expiraEm: 0 };
}

async function obterStats() {
  const agora = Date.now();
  if (cacheStats.valor && agora < cacheStats.expiraEm) return cacheStats.valor;

  const reservadas = await db.contarLeads();
  const limite = config.limiteFundadores;
  const valor = {
    limite,
    reservadas,
    restantes: Math.max(limite - reservadas, 0),
    esgotado: reservadas >= limite,
    whatsapp: config.whatsappNumero,
  };
  cacheStats = { valor, expiraEm: agora + config.cacheStatsMs };
  return valor;
}

function mensagemReserva(fundador, posicao) {
  if (fundador) {
    return (
      `Vaga de fundador reservada (posição ${posicao} de ${config.limiteFundadores}). ` +
      "Vamos te chamar no WhatsApp para confirmar — nada é cobrado agora, você só paga na inauguração."
    );
  }
  return (
    "As vagas de fundador acabaram, mas você entrou na lista de espera. " +
    "Assim que abrir vaga ou lançarmos novos planos, te avisamos no WhatsApp."
  );
}

/**
 * Registra uma reserva da pré-venda.
 * @param {object} corpo corpo da requisição
 * @param {{ip:string, userAgent:string}} contexto
 */
async function registrarReserva(corpo, contexto = {}) {
  const validado = validarLead(corpo);
  if (!validado.ok) throw new ErroNegocio(400, validado.erro, validado.campo);

  const dados = {
    ...validado.dados,
    user_agent: truncar(contexto.userAgent, LIMITE_USER_AGENT) || null,
    ip_hash: db.hashIp(contexto.ip), // LGPD: só o hash, nunca o IP
  };

  try {
    await db.inserirLead(dados);
  } catch (e) {
    if (e && e.code === "23505") {
      throw new ErroNegocio(
        409,
        "Esse WhatsApp já tem uma reserva. Se precisar mudar algo, fale com a gente.",
        "whatsapp"
      );
    }
    throw e;
  }

  invalidarCacheStats();
  const total = await db.contarLeads();
  const posicao = total;
  const fundador = posicao <= config.limiteFundadores;

  return { ok: true, fundador, posicao, mensagem: mensagemReserva(fundador, posicao) };
}

// A rede ainda NÃO vende franquia: a Lei 13.966/2019 exige operação própria
// auditável e COF entregue antes de qualquer oferta. A mensagem abaixo só
// confirma registro de interesse — sem promessa, sem oferta, sem pagamento.
const MENSAGEM_FRANQUIA =
  "Interesse registrado. A JatoJá ainda não oferta franquia: estamos concluindo a " +
  "formatação e o período de operação própria exigido pela Lei 13.966/2019. " +
  "Quando a formatação estiver concluída, entramos em contato com as informações e a " +
  "Circular de Oferta de Franquia. Nenhum compromisso e nenhum pagamento é solicitado agora.";

async function registrarInteresseFranquia(corpo, contexto = {}) {
  const validado = validarFranquia(corpo);
  if (!validado.ok) throw new ErroNegocio(400, validado.erro, validado.campo);

  const dados = {
    ...validado.dados,
    user_agent: truncar(contexto.userAgent, LIMITE_USER_AGENT) || null,
    ip_hash: db.hashIp(contexto.ip),
  };

  try {
    await db.inserirFranquiaLead(dados);
  } catch (e) {
    if (e && e.code === "23505") {
      throw new ErroNegocio(
        409,
        "Já recebemos um interesse com esse WhatsApp. Pode ficar tranquilo, vamos retornar.",
        "whatsapp"
      );
    }
    throw e;
  }

  return { ok: true, mensagem: MENSAGEM_FRANQUIA };
}

module.exports = {
  ErroNegocio,
  obterStats,
  invalidarCacheStats,
  registrarReserva,
  registrarInteresseFranquia,
  MENSAGEM_FRANQUIA,
};
