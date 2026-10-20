"""
Reduz a densidade dos slides para caber nos 1080px do formato 16:9.

Os slides foram escritos com mais conteudo do que a altura util comporta
(824px entre as margens). Em vez de cortar texto, este script reduz margens,
espacamentos e a escala tipografica, mantendo a hierarquia visual e o piso de
legibilidade de 20px.

Uso:  python3 ajustar-densidade.py [--conferir]
"""
import pathlib, re, sys

AQUI = pathlib.Path(__file__).resolve().parent
SLIDES = AQUI / "slides"

PISO = 20          # nenhum texto abaixo disso
FATOR = 0.78       # escala tipografica

# padding da secao: ganha altura util e alarga a area de conteudo
PADDING_SECAO = ("padding:128px 128px 160px", "padding:76px 88px 104px")


def escala_fonte(v):
    n = round(v * FATOR)
    return max(PISO, n)


def ajustar(texto):
    t = texto.replace(*PADDING_SECAO)

    # fontes
    t = re.sub(r"font-size:(\d+)px",
               lambda m: f"font-size:{escala_fonte(int(m.group(1)))}px", t)

    # espacamentos entre blocos
    t = re.sub(r"\bgap:(\d+)px",
               lambda m: f"gap:{max(8, round(int(m.group(1)) * 0.62))}px", t)

    # padding interno de cartoes e tabelas
    def pad(m):
        vals = [int(x) for x in m.group(1).split("px ") if x.strip().isdigit()]
        crus = re.findall(r"(\d+)px", m.group(0))
        novos = " ".join(f"{max(6, round(int(v) * 0.66))}px" for v in crus)
        return f"padding:{novos}"
    t = re.sub(r"padding:((?:\d+px\s*){1,4})(?=[;\"])", pad, t)
    t = t.replace(*PADDING_SECAO)   # repoe o da secao, que o passo acima mexeu

    # rodape fixo sobe junto com a margem
    t = re.sub(r"bottom:64px", "bottom:40px", t)
    t = re.sub(r"left:128px", "left:88px", t)

    # larguras fixas de titulo acompanham a area util maior (1920-176=1744)
    t = re.sub(r"width:1(5|6)\d\dpx", "width:1700px", t)

    # alturas de setas e formas
    t = re.sub(r"(<x-shape[^>]*?)height:(\d+)px",
               lambda m: f"{m.group(1)}height:{round(int(m.group(2))*0.7)}px", t)
    return t


def main():
    conferir = "--conferir" in sys.argv
    for arq in sorted(SLIDES.glob("*.html")):
        antes = arq.read_text(encoding="utf-8")
        depois = ajustar(antes)
        if conferir:
            fontes = sorted({int(x) for x in re.findall(r"font-size:(\d+)px", depois)})
            print(f"  {arq.stem:<16} fontes: {fontes[:3]} ... {fontes[-3:]}")
        else:
            arq.write_text(depois, encoding="utf-8")
    if not conferir:
        print(f"ajustados {len(list(SLIDES.glob('*.html')))} slides "
              f"(fator {FATOR}, piso {PISO}px)")


if __name__ == "__main__":
    main()
