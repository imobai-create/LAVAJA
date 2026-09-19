"use strict";

const { test } = require("node:test");
const assert = require("node:assert/strict");

const v = require("../src/validacao");

test("normaliza WhatsApp brasileiro com e sem DDI", () => {
  assert.equal(v.normalizarWhatsapp("(37) 99999-8888"), "5537999998888");
  assert.equal(v.normalizarWhatsapp("37 3371-2020"), "553733712020");
  assert.equal(v.normalizarWhatsapp("+55 (11) 98888-7777"), "5511988887777");
  assert.equal(v.normalizarWhatsapp("5511988887777"), "5511988887777");
  // DDD 55 (Santa Maria/RS) não pode ser confundido com o DDI.
  assert.equal(v.normalizarWhatsapp("55988887777"), "5555988887777");
});

test("rejeita WhatsApp inválido", () => {
  assert.equal(v.normalizarWhatsapp(""), null);
  assert.equal(v.normalizarWhatsapp("123456"), null, "curto demais");
  assert.equal(v.normalizarWhatsapp("55119888877771234"), null, "longo demais");
  assert.equal(v.normalizarWhatsapp("0399999999"), null, "DDD menor que 11");
  assert.equal(v.normalizarWhatsapp("1099999999"), null, "DDD menor que 11");
  assert.equal(v.normalizarWhatsapp("11111111111"), null, "todos os dígitos iguais");
  assert.equal(v.normalizarWhatsapp("99999999999"), null, "todos os dígitos iguais");
  assert.equal(v.normalizarWhatsapp("371234567890"), null, "12 dígitos sem DDI 55");
});

test("nome exige duas palavras e tamanho", () => {
  assert.equal(v.validarNome("Ana").ok, false);
  assert.equal(v.validarNome("Jo").ok, false);
  assert.equal(v.validarNome("Ana Lima").ok, true);
  assert.equal(v.validarNome("Ana Lima").valor, "Ana Lima");
  assert.equal(v.validarNome("  Ana   Lima  ").valor, "Ana Lima", "normaliza espaços");
  assert.equal(v.validarNome("A".repeat(121) + " Silva").ok, false);
  assert.equal(v.validarNome("12345 67890").ok, false, "precisa ter letras");
  assert.equal(v.validarNome("Ana").campo, "nome");
});

test("plano precisa estar na lista", () => {
  assert.equal(v.validarPlano("essencial").ok, true);
  assert.equal(v.validarPlano("PREMIUM").valor, "premium");
  assert.equal(v.validarPlano("ouro").ok, false);
  assert.equal(v.validarPlano("ouro").campo, "plano");
  assert.deepEqual(v.PLANOS, ["ilimitada-fundador", "essencial", "premium"]);
});

test("consentimento é obrigatório (LGPD)", () => {
  assert.equal(v.validarConsentimento(true).ok, true);
  assert.equal(v.validarConsentimento("true").ok, true);
  assert.equal(v.validarConsentimento(false).ok, false);
  assert.equal(v.validarConsentimento(undefined).campo, "consentimento");
});

test("utm e mensagem são truncados/sanitizados", () => {
  const utm = v.normalizarUtm({ source: "x".repeat(300), medium: null });
  assert.equal(utm.source.length, 120);
  assert.equal(utm.medium, null);
  assert.equal(v.validarMensagem("a".repeat(1001)).ok, false);
  assert.equal(v.validarMensagem("a".repeat(1000)).ok, true);
});

test("validarLead devolve dados prontos com padrões", () => {
  const r = v.validarLead({
    nome: "Maria Silva", whatsapp: "37988887777", plano: "essencial", consentimento: true,
  });
  assert.equal(r.ok, true);
  assert.equal(r.dados.origem, "piumhi");
  assert.equal(r.dados.cidade, "Piumhi");
  assert.equal(r.dados.whatsapp, "5537988887777");
});

test("validarFranquia exige e-mail, cidade e capital", () => {
  const base = {
    nome: "João Souza", whatsapp: "31977776666", email: "joao@exemplo.com",
    cidade: "Divinópolis", capital: "150k-300k", consentimento: true,
  };
  assert.equal(v.validarFranquia(base).ok, true);
  assert.equal(v.validarFranquia({ ...base, email: "semarroba" }).campo, "email");
  assert.equal(v.validarFranquia({ ...base, cidade: "" }).campo, "cidade");
  assert.equal(v.validarFranquia({ ...base, capital: "" }).campo, "capital");
});
