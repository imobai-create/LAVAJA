// JatoJá — geração de CSV para o Excel brasileiro.
// BOM UTF-8 + separador ";" (o Excel pt-BR usa ponto e vírgula) + aspas escapadas.

"use strict";

const BOM = "﻿";

function celula(valor) {
  if (valor === null || valor === undefined) return "";
  let texto = typeof valor === "boolean" ? (valor ? "sim" : "não") : String(valor);

  // Protege contra fórmula injetada no Excel (=, +, -, @ no início).
  if (/^[=+\-@\t\r]/.test(texto)) texto = "'" + texto;

  if (/[";\n\r]/.test(texto)) {
    return '"' + texto.replace(/"/g, '""') + '"';
  }
  return texto;
}

/**
 * @param {object[]} linhas
 * @param {{chave:string, titulo:string}[]} colunas
 */
function paraCsv(linhas, colunas) {
  const cabecalho = colunas.map((c) => celula(c.titulo)).join(";");
  const corpo = linhas.map((linha) => colunas.map((c) => celula(linha[c.chave])).join(";"));
  // \r\n: o Excel do Windows lida melhor com CRLF.
  return BOM + [cabecalho, ...corpo].join("\r\n") + "\r\n";
}

module.exports = { paraCsv, celula, BOM };
