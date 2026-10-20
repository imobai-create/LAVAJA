// FastCarWash — aplica as migrações do banco e sai.
//
// Em serverless as migrações não rodam no boot (seriam dezenas de DDLs a cada
// processo novo). Rode este script uma vez por deploy que mexa no esquema:
//
//   DATABASE_URL='postgres://...' npm run migrar
//
// É idempotente: CREATE TABLE IF NOT EXISTS / ADD COLUMN IF NOT EXISTS.
//
// Sem banco à mão, `npm run migrar -- --imprimir` escreve o SQL na tela para
// colar no SQL Editor do Neon (é o que docs/migracoes.sql guarda).

"use strict";

const config = require("../src/config");
const db = require("../src/db");

function imprimir() {
  const linhas = [
    "-- FastCarWash — migrações do banco.",
    "-- Gerado por `npm run migrar -- --imprimir`. Não edite à mão:",
    "-- a fonte é MIGRACOES em src/db.js.",
    "-- Idempotente: pode rodar quantas vezes quiser.",
    "",
  ];
  for (const sql of db.MIGRACOES) linhas.push(sql.trim() + ";", "");
  process.stdout.write(linhas.join("\n"));
}

async function principal() {
  if (process.argv.includes("--imprimir")) return imprimir();

  if (!config.databaseUrl) {
    console.error("[migrar] DATABASE_URL não está definida. Nada a fazer.");
    process.exit(1);
  }
  console.log(`[migrar] aplicando ${db.MIGRACOES.length} migrações...`);
  const modo = await db.iniciar({ migrar: true });
  if (modo !== "postgres") {
    console.error("[migrar] não foi possível conectar ao Postgres. Veja o log acima.");
    await db.encerrar();
    process.exit(1);
  }
  await db.encerrar();
  console.log("[migrar] pronto.");
}

principal().catch((e) => {
  console.error("[migrar] falhou:", e && e.stack ? e.stack : e);
  process.exit(1);
});
