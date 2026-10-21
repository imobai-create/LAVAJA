// Gera os PDFs de entrega: a apresentacao em 16:9 e cada documento do plano em A4.
// Uso:  node docs/gerar-pdf.mjs
import { chromium } from '../node_modules/playwright-core/index.mjs';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const SAIDA = path.join(AQUI, 'pdf');
const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const DOCS = [
  ['LEIAME-PACOTE.md',      'Comece por aqui'],
  ['BUSINESS-PLAN.md',      '00 - Indice do plano'],
  ['RESUMO-INVESTIDOR.md',  '01 - Resumo para investidor'],
  ['BP-PIUMHI.md',          '02 - Plano da loja de Piumhi'],
  ['BP-REDE.md',            '03 - Plano da rede de franquias'],
  ['CENARIOS.md',           '04 - Todos os cenarios'],
  ['PLANO-IMPLANTACAO.md',  '05 - Plano de implantacao'],
  ['CHECKLIST-PRE-VENDA.md','06 - Checklist de pre-venda'],
  ['EQUIPAMENTO.md',        '07 - Analise das maquinas'],
  ['CONCORRENTES.md',       '08 - Concorrencia e marca'],
  ['ROADMAP-12-MESES.md',   '09 - Roadmap de 12 meses'],
  ['DECISOES.md',           '10 - Registro de decisoes'],
  ['DEPLOY.md',             '11 - Guia de publicacao do site'],
];

const CSS = `
@page { size: A4; margin: 19mm 16mm 20mm; }
*{box-sizing:border-box}
body{font-family:"Archivo","Helvetica Neue",Arial,sans-serif;font-size:10.5pt;line-height:1.55;
  color:#14233D;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1{font-size:25pt;font-weight:800;letter-spacing:-.6pt;line-height:1.12;color:#04122E;
  margin:0 0 6pt;padding-bottom:9pt;border-bottom:4pt solid #0B5CFF}
/* o titulo do arquivo vira sobrelinha, para nao competir com o titulo do documento */
h1.title{font-size:9pt;font-weight:700;letter-spacing:2.4pt;text-transform:uppercase;
  color:#0B5CFF;border:none;padding:0;margin:0 0 3pt}
h1.title+h1{margin-top:0}
h2{font-size:15.5pt;font-weight:800;letter-spacing:-.2pt;color:#0B5CFF;
  margin:20pt 0 7pt;padding-top:8pt;border-top:1pt solid #D4E6FF;break-after:avoid}
h3{font-size:12pt;font-weight:700;color:#04122E;margin:14pt 0 5pt;break-after:avoid}
h4{font-size:10.5pt;font-weight:700;color:#0A3FC4;margin:11pt 0 4pt;break-after:avoid}
p{margin:0 0 7pt}
strong{color:#04122E;font-weight:700}
a{color:#0B5CFF;text-decoration:none}
ul,ol{margin:0 0 8pt;padding-left:16pt}
li{margin:0 0 3.5pt}
code{font-family:"DejaVu Sans Mono",monospace;font-size:9pt;background:#EEF4FF;color:#0A3FC4;
  padding:1pt 3pt;border-radius:3px}
pre{background:#04122E;color:#D4E6FF;padding:10pt 12pt;border-radius:6px;font-size:8.5pt;
  line-height:1.45;overflow:hidden;break-inside:avoid}
pre code{background:none;color:inherit;padding:0}
table{border-collapse:collapse;width:100%;margin:8pt 0 12pt;font-size:9pt;break-inside:avoid}
thead th{background:#0B5CFF;color:#FFFFFF;font-weight:700;text-align:left;
  padding:6pt 8pt;border:none;font-size:8.5pt;letter-spacing:.2pt}
tbody td{padding:5.5pt 8pt;border-bottom:.75pt solid #DCE8FF;vertical-align:top}
tbody tr:nth-child(even) td{background:#F4F8FF}
tbody tr td:first-child{font-weight:600;color:#04122E}
blockquote{margin:10pt 0;padding:9pt 14pt;background:#FFF7E8;border-left:5pt solid #FFB224;
  break-inside:avoid}
blockquote p{margin:0 0 5pt}
blockquote p:last-child{margin:0}
hr{border:none;border-top:1pt solid #D4E6FF;margin:16pt 0}
h1+p em,h1+p{color:#3A5578}
img{max-width:100%}
`;

const RODAPE = (titulo) => `
<div style="width:100%;font-family:Archivo,Arial,sans-serif;font-size:7pt;color:#6E88AD;
     padding:0 16mm;display:flex;justify-content:space-between;align-items:center">
  <span>FastCarWash · Piumhi/MG · ${titulo}</span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>`;

const CABECALHO = '<div></div>';

fs.mkdirSync(SAIDA, { recursive: true });
const b = await chromium.launch({ executablePath: CHROME });

// ---------------------------------------------------------------- apresentacao
{
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(AQUI, 'apresentacao', 'apresentacao.html'),
               { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  const destino = path.join(SAIDA, 'Apresentacao - FastCarWash.pdf');
  await p.pdf({ path: destino, preferCSSPageSize: true, printBackground: true });
  console.log('slides  ->', path.basename(destino));
  await p.close();
}

// ------------------------------------------------------------------ documentos
const p = await b.newPage({ viewport: { width: 1240, height: 1754 } });
for (const [arquivo, nome] of DOCS) {
  const origem = path.join(AQUI, arquivo);
  if (!fs.existsSync(origem)) { console.log('ausente:', arquivo); continue; }
  const corpo = execFileSync('pandoc', [
    origem, '-f', 'gfm', '-t', 'html5', '--standalone',
    '--metadata', 'title=' + nome, '--css', 'estilo.css',
  ], { encoding: 'utf-8', maxBuffer: 64 * 1024 * 1024 });

  const html = corpo.replace('</head>', `<style>${CSS}</style></head>`);
  const tmp = path.join(SAIDA, '.tmp.html');
  fs.writeFileSync(tmp, html, 'utf-8');
  await p.goto('file://' + tmp, { waitUntil: 'load' });
  await p.waitForTimeout(250);
  const destino = path.join(SAIDA, nome + '.pdf');
  await p.pdf({
    path: destino, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: CABECALHO, footerTemplate: RODAPE(nome),
  });
  const kb = Math.round(fs.statSync(destino).size / 1024);
  console.log(`${arquivo.padEnd(26)} -> ${nome}.pdf  (${kb} KB)`);
  fs.rmSync(tmp);
}
await b.close();
