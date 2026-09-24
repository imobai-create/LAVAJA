// JatoJá — sanidade dos HTML de public/. Sem dependência externa: roda com o Node puro.
// Uso: node .github/scripts/checar-html.mjs
//
// Erro (quebra o CI): tag essencial faltando, <title>/meta description ausentes,
// href="#" órfão, tag de bloco desbalanceada, arquivo de SEO ausente.
// Aviso (não quebra): título/description fora do tamanho ideal, link interno sem arquivo.

import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join } from "node:path";

const DIR = "public";
const erros = [];
const avisos = [];

const arquivos = existsSync(DIR) ? readdirSync(DIR).filter((f) => f.endsWith(".html")) : [];

if (arquivos.length === 0) {
  console.error("ERRO   nenhum arquivo .html encontrado em public/ — nada a verificar.");
  process.exit(1);
}

// Rotas sem extensão que o servidor resolve para um arquivo .html (/franquia -> franquia.html)
function rotaParaArquivo(href) {
  const limpo = href.split("?")[0].split("#")[0];
  if (limpo === "/" || limpo === "") return "index.html";
  const semBarra = limpo.replace(/^\//, "").replace(/\/$/, "");
  return semBarra.endsWith(".html") ? semBarra : semBarra + ".html";
}

for (const nome of arquivos) {
  const caminho = join(DIR, nome);
  const html = readFileSync(caminho, "utf8");
  const falha = (m) => erros.push(`${caminho}: ${m}`);
  const aviso = (m) => avisos.push(`${caminho}: ${m}`);

  // 1) estrutura essencial
  if (!/<!doctype html>/i.test(html)) falha("falta <!DOCTYPE html>");
  if (!/<html[^>]*\slang\s*=\s*["']pt-BR["']/i.test(html)) falha('falta <html lang="pt-BR">');
  if (!/<meta[^>]+charset\s*=\s*["']?utf-8/i.test(html)) falha('falta <meta charset="UTF-8">');
  if (!/<meta[^>]+name\s*=\s*["']viewport["']/i.test(html)) falha('falta <meta name="viewport">');
  if (!/<\/html>\s*$/i.test(html.trim())) falha("o arquivo não termina com </html>");

  // 2) título
  const titulo = html.match(/<title>([\s\S]*?)<\/title>/i);
  if (!titulo) falha("falta <title>");
  else {
    const t = titulo[1].trim();
    if (t.length < 10) falha(`<title> curto demais ("${t}")`);
    else if (t.length > 70) aviso(`<title> com ${t.length} caracteres (o Google corta perto de 60)`);
  }

  // 3) meta description — exigida só em página indexável (o painel admin é noindex)
  const noindex = /<meta[^>]+name\s*=\s*["']robots["'][^>]*content\s*=\s*["'][^"']*noindex/i.test(html);
  const desc = html.match(/<meta[^>]+name\s*=\s*["']description["'][^>]*>/i);
  if (noindex && !desc) {
    // página privada: sem exigência de SEO
  } else if (!desc) falha('falta <meta name="description">');
  else {
    const conteudo = desc[0].match(/content\s*=\s*["']([\s\S]*?)["']/i);
    const c = conteudo ? conteudo[1].trim() : "";
    if (c.length < 50) falha(`meta description vazia ou curta demais (${c.length} caracteres)`);
    else if (c.length > 165) aviso(`meta description com ${c.length} caracteres (o Google corta perto de 160)`);
  }

  // 4) href="#" órfão — botão que não leva a lugar nenhum.
  // href="#" só é aceito quando a tag tem id= ou data-*: aí o destino é preenchido por JS
  // (ex.: link de WhatsApp montado em tempo de execução, download de CSV com token).
  const tagsComHash = html.match(/<a\b[^>]*href\s*=\s*["']#["'][^>]*>/gi) || [];
  const orfaos = tagsComHash.filter((tag) => !/\s(id|data-[a-z-]+)\s*=/i.test(tag));
  if (orfaos.length) {
    falha(`${orfaos.length} link(s) com href="#" sem id nem data-* — link órfão, aponte para uma âncora ou rota real`);
  }

  // 5) balanceamento das tags de bloco mais comuns
  for (const tag of ["html", "head", "body", "main", "section", "div", "form", "footer", "header", "nav", "ul", "ol", "table"]) {
    const abre = (html.match(new RegExp(`<${tag}(\\s|>)`, "gi")) || []).length;
    const fecha = (html.match(new RegExp(`</${tag}>`, "gi")) || []).length;
    if (abre !== fecha) falha(`<${tag}> desbalanceada: ${abre} aberta(s) e ${fecha} fechada(s)`);
  }

  // 6) âncoras internas (#algo) que não existem na página
  const ancoras = [...html.matchAll(/href\s*=\s*["']#([^"']+)["']/gi)].map((m) => m[1]);
  for (const id of new Set(ancoras)) {
    if (!new RegExp(`id\\s*=\\s*["']${id.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}["']`, "i").test(html)) {
      falha(`âncora "#${id}" não tem elemento com esse id na página`);
    }
  }

  // 7) links internos sem arquivo correspondente (aviso: o arquivo pode nascer noutro PR)
  const hrefs = [...html.matchAll(/href\s*=\s*["'](\/[^"']*)["']/gi)].map((m) => m[1]);
  for (const href of new Set(hrefs)) {
    if (href.startsWith("//") || href.startsWith("/api/")) continue;
    const alvo = join(DIR, rotaParaArquivo(href));
    const direto = join(DIR, href.replace(/^\//, ""));
    if (!existsSync(alvo) && !existsSync(direto)) aviso(`link interno "${href}" ainda não tem arquivo em ${DIR}/`);
  }
}

// 8) arquivos de SEO obrigatórios
for (const obrigatorio of ["robots.txt", "sitemap.xml", "manifest.webmanifest"]) {
  if (!existsSync(join(DIR, obrigatorio))) erros.push(`public/${obrigatorio}: arquivo ausente`);
}

for (const a of avisos) console.log(`AVISO  ${a}`);
for (const e of erros) console.error(`ERRO   ${e}`);
console.log(`\n${arquivos.length} arquivo(s) HTML verificado(s) — ${erros.length} erro(s), ${avisos.length} aviso(s).`);

process.exit(erros.length > 0 ? 1 : 0);
