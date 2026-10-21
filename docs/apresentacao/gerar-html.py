"""
Monta docs/apresentacao/apresentacao.html: um arquivo unico, offline, com os 23
slides empilhados — abre em qualquer navegador e imprime em PDF (Ctrl+P).

Os slides sao secoes de 1920x1080 com estilo inline, escritas para o visualizador
de Slides. Aqui elas sao empilhadas e os elementos proprios do visualizador
(x-shape, x-icon, x-connector) ganham um CSS minimo para aparecerem.

Uso:  python3 gerar-html.py
"""
import json, pathlib, re, html

AQUI = pathlib.Path(__file__).resolve().parent
deck = json.loads((AQUI / "deck.json").read_text(encoding="utf-8"))

CSS = """
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#061024;font-family:'Archivo',Arial,sans-serif}
#capa-doc{max-width:1100px;margin:0 auto;padding:56px 32px 8px;color:#F2F8FF}
#capa-doc h1{font-size:34px;font-weight:800;letter-spacing:-.5px;margin:0 0 8px}
#capa-doc p{font-size:16px;line-height:1.5;color:#AFC9F5;margin:0 0 6px}
#capa-doc ol{font-size:15px;line-height:1.7;color:#AFC9F5;margin:16px 0 0;padding-left:22px}
#palco{display:flex;flex-direction:column;align-items:center;gap:28px;padding:28px 16px 64px}
/* .moldura recorta no tamanho reduzido; .folha mantem 1920x1080 e e escalada dentro dela */
.moldura{position:relative;flex:none;overflow:hidden;border-radius:4px;
  box-shadow:0 10px 36px rgba(0,0,0,.45);background:#FFF}
.folha{width:1920px;height:1080px;transform-origin:top left}
.folha > section{width:1920px;height:1080px;position:relative;overflow:hidden;margin:0;
  display:flex}
.folha aside{display:none}
.numero{position:absolute;right:12px;top:9px;font-size:13px;color:#38E1FF;z-index:9;
  font-family:'Archivo',Arial,sans-serif}
/* elementos do visualizador de Slides */
x-shape{display:block}
x-shape[kind="arrow-right"]{clip-path:polygon(0 30%,62% 30%,62% 0,100% 50%,62% 100%,62% 70%,0 70%)}
x-shape[kind="arrow-left"]{clip-path:polygon(100% 30%,38% 30%,38% 0,0 50%,38% 100%,38% 70%,100% 70%)}
x-shape[kind="arrow-down"]{clip-path:polygon(30% 0,70% 0,70% 62%,100% 62%,50% 100%,0 62%,30% 62%)}
x-shape[kind="arrow-up"]{clip-path:polygon(30% 100%,70% 100%,70% 38%,100% 38%,50% 0,0 38%,30% 38%)}
x-shape[kind="ellipse"]{border-radius:50%}
x-shape[kind="rounded"]{border-radius:12px}
x-shape[kind="diamond"]{clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%)}
x-shape[kind="line"]{min-height:2px}
x-icon,x-connector{display:none}
table{border-collapse:collapse;width:100%}
td,th{padding:14px 18px;text-align:left;vertical-align:top}
@media print{
  html,body{background:#FFF}
  #capa-doc{display:none}
  #palco{gap:0;padding:0;display:block}
  .moldura{box-shadow:none;border-radius:0;width:1920px!important;height:1080px!important;
    page-break-after:always;break-after:page}
  .folha{transform:none!important}
  .numero{display:none}
  @page{size:1920px 1080px;margin:0}
}
"""

AJUSTE = """
// Duas escalas, aplicadas em cadeia:
//
//  1. ENCAIXE NO SLIDE. Alguns slides tem mais conteudo do que 1080px comportam.
//     Em vez de cortar texto, a secao e reduzida ate caber e centralizada; a
//     moldura herda a cor de fundo da secao para a sobra nao aparecer.
//  2. ENCAIXE NA JANELA. Depois disso a folha de 1920x1080 e reduzida para a
//     largura disponivel.
function encaixarNoSlide(){
  document.querySelectorAll('.folha').forEach(function(f){
    var s = f.firstElementChild;
    if (!s) return;
    s.style.transform = 'none';
    s.style.height = 'auto';
    var alt = s.scrollHeight;
    if (alt > 1080){
      // A secao FICA com a altura natural — senao o layout continua de 1080px e
      // o conteudo e cortado antes de encolher — e e a escala que a traz de volta.
      var k = 1080 / alt;
      s.style.height = alt + 'px';
      s.style.transformOrigin = 'top left';
      s.style.transform = 'translateX(' + Math.round(1920 * (1 - k) / 2) + 'px) scale(' + k + ')';
      var m = f.parentElement;
      m.style.background = getComputedStyle(s).backgroundColor;
      m.dataset.encaixe = Math.round(k * 100);
    } else {
      s.style.height = '1080px';
    }
  });
}
function encaixarNaJanela(){
  var w = Math.min(document.documentElement.clientWidth - 32, 1920);
  var k = w / 1920;
  document.querySelectorAll('.moldura').forEach(function(m){
    m.style.width  = Math.round(1920 * k) + 'px';
    m.style.height = Math.round(1080 * k) + 'px';
    var f = m.querySelector('.folha');
    if (f) f.style.transform = 'scale(' + k + ')';
  });
}
function encaixar(){ encaixarNoSlide(); encaixarNaJanela(); }
window.addEventListener('resize', encaixarNaJanela);
if (document.fonts && document.fonts.ready) document.fonts.ready.then(encaixar);
encaixar();
"""


def main():
    partes = []
    for i, sid in enumerate(deck["order"], start=1):
        arq = AQUI / "slides" / f"{sid}.html"
        if not arq.exists():
            print(f"  aviso: {sid}.html nao existe, pulando")
            continue
        corpo = arq.read_text(encoding="utf-8").strip()
        partes.append(
            f'<div class="moldura" id="s-{sid}">'
            f'<span class="numero">{i} / {len(deck["order"])}</span>'
            f'<div class="folha">{corpo}</div></div>'
        )

    titulo = deck.get("title", "Apresentação")
    fontes = "\n".join(
        f'<link rel="stylesheet" href="{f["href"]}">'
        for f in deck.get("faces", {}).values() if f.get("href")
    )
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
{fontes}
<style>{CSS}</style>
</head>
<body>
<div id="capa-doc">
<h1>{html.escape(titulo)}</h1>
<p>{len(partes)} slides. Arquivo único e offline: pode ser aberto por duplo clique, sem
internet (as fontes vêm da web; sem elas o texto aparece em fonte padrão).</p>
<p><b>Para gerar PDF:</b> Ctrl+P (ou Cmd+P), escolha "Salvar como PDF", marque
<i>Gráficos de fundo</i> e deixe margens em zero. Cada slide sai numa página.</p>
<p>As notas do apresentador estão nos arquivos <code>slides/&lt;id&gt;.html</code>, dentro da
tag <code>&lt;aside&gt;</code> no fim de cada um — ficam ocultas aqui.</p>
<ol>
{chr(10).join(f'<li>{html.escape(s)}</li>' for s in deck["order"])}
</ol>
</div>
<div id="palco">
{chr(10).join(partes)}
</div>
<script>{AJUSTE}</script>
</body>
</html>
"""
    destino = AQUI / "apresentacao.html"
    destino.write_text(doc, encoding="utf-8")
    print(f"gravado: {destino}  ({len(partes)} slides, {len(doc)//1024} KB)")


if __name__ == "__main__":
    main()
