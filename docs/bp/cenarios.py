"""
Tabela mestra de todos os cenarios simulados neste projeto.

Roda tudo de uma vez e imprime as tabelas que entram em docs/CENARIOS.md.
Sem dependencias externas.  Uso:  PYTHONPATH=. python3 cenarios.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import comum, piumhi, capital as C, rede as R, mcdonalds as M
from comum import brl, tir_anual, vpl, mensal

PL = C.PRO_LABORE          # 3.500/mes
TMA = 0.18
L = 100


def linha(*cols):
    print("  " + "".join(str(c) for c in cols))


# ---------------------------------------------------------------- 1. a loja
def loja():
    print("=" * L)
    print("1. LOJA PROPRIA DE PIUMHI - arranjos de capital (ja com pro-labore de R$ 3.500)")
    print("=" * L)
    print(f"  {'arranjo':<44} {'1a tranche':>11} {'a reservar':>11} {'TIR':>7} {'VPL@18%':>11}")
    casos = [
        ("A. Capex cheio, 100% equity", C.CAPEX_CHEIO, C.GIRO_CHEIO, None, False),
        ("B. Capex enxuto, 100% equity", C.CAPEX_ENXUTO, C.GIRO_ENXUTO, None, False),
        ("C. Enxuto + pre-venda, 100% equity", C.CAPEX_ENXUTO, C.GIRO_ENXUTO, None, True),
        ("D. Enxuto + pre-venda + divida 120k", C.CAPEX_ENXUTO, C.GIRO_ENXUTO,
         "Cooperativa de credito", True),
        ("E. Enxuto + pre-venda + divida 150k", C.CAPEX_ENXUTO, C.GIRO_ENXUTO,
         "Cooperativa 150k", True),
        ("F. Enxuto + pre-venda + divida 180k", C.CAPEX_ENXUTO, C.GIRO_ENXUTO,
         "Cooperativa 180k", True),
    ]
    C.DIVIDAS.setdefault("Cooperativa 150k",
                         dict(valor=150_000, juros=0.21, prazo=60, carencia=6))
    C.DIVIDAS.setdefault("Cooperativa 180k",
                         dict(valor=180_000, juros=0.21, prazo=60, carencia=6))
    out = {}
    for rot, cx, gi, dv, pv in casos:
        a = C.arranjo(rot, cx, gi, divida=dv, pre_venda=pv)
        out[rot[0]] = a
        linha(f"{rot:<44} {brl(a['equity']):>11} {brl(-a['pico']):>11} "
              f"{a['tir']*100:>6.1f}% {brl(a['vpl']):>11}")
    return out


# ---------------------------------------------------------- 2. divisao do equity
DIVISOES = [
    ("50 / 50, um investidor", [("Antonio", 0.50), ("Investidor", 0.50)]),
    ("33,33 x 3, dois investidores", [("Antonio", 1/3), ("Investidor A", 1/3),
                                      ("Investidor B", 1/3)]),
    ("25 / 25 / 50, dois investidores", [("Antonio", 0.50), ("Investidor A", 0.25),
                                         ("Investidor B", 0.25)]),
    ("50,5 / 24,75 / 24,75 (desempate)", [("Antonio", 0.505), ("Investidor A", 0.2475),
                                          ("Investidor B", 0.2475)]),
]


def divisoes(a, rotulo):
    res = -a["pico"]
    print("\n" + "=" * L)
    print(f"2. DIVISAO DO EQUITY - {rotulo}")
    print(f"   capital a reservar R$ {brl(res)} | capital chamado em tranches, proporcional")
    print("=" * L)
    print(f"  {'estrutura':<36} {'socio':<14} {'aporte':>11} {'1a tranche':>11} "
          f"{'TIR':>7} {'caixa 60m':>11}")
    for nome, partes in DIVISOES:
        for i, (quem, fat) in enumerate(partes):
            f = [v * fat for v in a["fluxos"]]
            acc = pk = 0.0
            for v in f:
                acc += v
                pk = min(pk, acc)
            linha(f"{(nome if i == 0 else ''):<36} {quem:<14} {brl(-pk):>11} "
                  f"{brl(-f[0]):>11} {tir_anual(f)*100:>6.1f}% {brl(sum(f[1:])):>11}")
        print()
    print("  Com aporte proporcional a TIR e a MESMA para todos, em qualquer divisao:")
    print("  ela e a TIR do projeto. A divisao muda quanto cada um poe e quem decide.")


def sem_tranche(a):
    """E se o investidor depositar tudo no mes 0 em vez de atender chamadas?"""
    res = -a["pico"]
    print("\n" + "=" * L)
    print("2b. O CUSTO DE NAO USAR CHAMADA DE CAPITAL (dinheiro parado em conta)")
    print("=" * L)
    print(f"  {'fatia':>8} {'aporte':>11} {'TIR com tranches':>18} {'TIR tudo no mes 0':>19}"
          f" {'perda':>8}")
    for fat in (1/3, 0.25, 0.50):
        com = [v * fat for v in a["fluxos"]]
        t_com = tir_anual(com)
        sem = [-res * fat] + [v * fat for v in a["fluxos"][1:]]
        t_sem = tir_anual(sem)
        linha(f"{fat*100:>7.2f}% {brl(res*fat):>11} {t_com*100:>17.1f}% "
              f"{t_sem*100:>18.1f}% {(t_com-t_sem)*100:>7.1f} pp")


# ------------------------------------------------------------------ 3. a rede
def redes():
    print("\n" + "=" * L)
    print("3. REDE / FRANQUEADORA - 65 unidades, 120 meses, TMA 18%")
    print("=" * L)
    print(f"  {'estrutura do ponto comercial':<40} {'capital no':>13} {'pico de':>13} "
          f"{'TIR':>9} {'VPL@18%':>13}")
    print(f"  {'':<40} {'imovel':>13} {'caixa':>13}")
    casos = [
        ("A. Asset-light (franqueado aluga)", dict(estrutura="A")),
        ("B1. Compramos terreno + obra", dict(estrutura="B1")),
        ("B1. Idem, 50% financiado a 14%", dict(estrutura="B1", com_divida=True)),
        ("B2. Locacao longa + obra + sublocacao", dict(estrutura="B2")),
    ]
    for rot, kw in casos:
        r = R.rede(**kw)
        t = f"{r['tir']*100:.1f}%" if r["tir"] else "negativa"
        linha(f"{rot:<40} {brl(r['capital_imovel']):>13} {brl(r['pico']):>13} "
              f"{t:>9} {brl(r['vpl']):>13}")

    print("\n  B3. Over no aluguel (modelo McDonald's): locacao principal + obra com 70% de")
    print("      divida + sublocacao pelo MAIOR entre uma base e um % das vendas")
    print(f"  {'base + % das vendas':<24} {'aluguel':>9} {'franqueado':>12} "
          f"{'franqueadora':>14} {'VPL franqueadora':>18}")
    for base, pct in ((3_800, 0.08), (3_800, 0.10), (4_200, 0.12), (4_500, 0.13)):
        f = M.franqueado_b3(base, pct)
        d = M.franqueadora_b3(base, pct)
        tf = f"{f['tir']*100:.1f}%" if f["tir"] else "n/d"
        td = f"{d['tir']*100:.1f}%" if d["tir"] else "negativa"
        linha(f"{('R$ ' + brl(base) + ' + ' + str(int(pct*100)) + '%'):<24} "
              f"{brl(f['aluguel']):>9} {tf:>12} {td:>14} {brl(d['vpl']):>18}")

    print("\n  O limiar do B3: a partir de que receita madura por unidade ele fecha")
    print(f"  {'receita madura':>16} {'franqueado':>12} {'franqueadora':>14} {'VPL':>14}")
    orig = R.REC_MADURA
    for rec in (48_000, 54_000, 60_000, 64_000, 70_000):
        R.REC_MADURA = float(rec)
        f = M.franqueado_b3(3_800, 0.10)
        d = M.franqueadora_b3(3_800, 0.10)
        marca = "  <-- os dois >= 18%" if (f["tir"] and f["tir"] >= .18
                                           and d["tir"] and d["tir"] >= .18) else ""
        linha(f"{brl(rec):>16} {f['tir']*100:>11.1f}% {d['tir']*100:>13.1f}% "
              f"{brl(d['vpl']):>14}{marca}")
    R.REC_MADURA = orig


def franqueados():
    print("\n" + "=" * L)
    print("4. O FRANQUEADO em cada estrutura (unidade madura a R$ 48.000/mes, 60 meses)")
    print("=" * L)
    print(f"  {'estrutura':<40} {'investimento':>13} {'aluguel':>9} {'EBITDA':>10} "
          f"{'TIR':>7} {'VPL@18%':>11}")
    for est, rot in (("A", "A. Ele constroi o ponto inteiro"),
                     ("B1", "B1. Nos compramos e alugamos a ele"),
                     ("B2", "B2. Nos sublocamos a ele")):
        f = R.franqueado(est)
        linha(f"{rot:<40} {brl(f['invest']):>13} {brl(f['aluguel']):>9} "
              f"{brl(f['ebitda']):>10} {f['tir']*100:>6.1f}% {brl(f['vpl']):>11}")
    print("\n  Com pro-labore de R$ 3.500 para quem administra a unidade franqueada:")
    base_a, base_b = R.ALUGUEL_MERCADO, R.ALUGUEL_B1
    for est, rot in (("A", "A. Ele constroi o ponto inteiro"),
                     ("B1", "B1. Nos compramos e alugamos a ele")):
        if est == "A":
            R.ALUGUEL_MERCADO = base_a + PL
        else:
            R.ALUGUEL_B1 = base_b + PL
        f = R.franqueado(est)
        linha(f"{rot:<40} {brl(f['invest']):>13} {'':>9} {brl(f['ebitda']):>10} "
              f"{f['tir']*100:>6.1f}% {brl(f['vpl']):>11}")
        R.ALUGUEL_MERCADO, R.ALUGUEL_B1 = base_a, base_b


def consolidado():
    print("\n" + "=" * L)
    print("5. CONSOLIDADO - loja propria + franqueadora no mesmo caixa, 120 meses")
    print("=" * L)
    print(f"  {'estrutura do ponto':<40} {'pico de caixa':>15} {'zera':>7} {'TIR':>9} "
          f"{'VPL@18%':>13}")
    for est, rot in (("A", "A. Asset-light"), ("B2", "B2. Locacao longa + sublocacao"),
                     ("B1", "B1. Compra o imovel")):
        c = R.consolidado(est)
        t = f"{c['tir']*100:.1f}%" if c["tir"] else "negativa"
        linha(f"{rot:<40} {brl(c['pico']):>15} {str(c['zera']):>7} {t:>9} "
              f"{brl(c['vpl']):>13}")


if __name__ == "__main__":
    arr = loja()
    divisoes(arr["C"], "100% EQUITY (arranjo C: enxuto + pre-venda, sem divida)")
    divisoes(arr["D"], "COM DIVIDA DE R$ 120 MIL (arranjo D)")
    sem_tranche(arr["C"])
    redes()
    franqueados()
    consolidado()
