"""
Estrutura "McDonald's" (B3): a franqueadora NAO compra o terreno.
Ela assina a locacao principal, constroi a baia com divida, e subloca ao
franqueado por ALUGUEL PERCENTUAL - o maior entre uma base e um % das vendas.

Comparar com:
  A  asset-light puro        (franqueado aluga de terceiro e constroi tudo)
  B1 franqueadora compra terreno + obra
  B2 franqueadora aluga longo + constroi, subloca por valor fixo
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum, rede
from comum import brl, vpl, tir_anual, payback, mensal

MESES = 120
TMA = 0.18
REC = rede.REC_MADURA          # 48.000/mes madura
OBRA = rede.CONSTRUCAO         # 220.000 por ponto
HEAD = rede.ALUGUEL_MERCADO    # 3.000/mes pago ao proprietario
MANUT = 350.0
TRIB_AL = rede.TRIB_ALUGUEL
LTV, JUROS, PRAZO = 0.70, 0.14, 120


def parcela(p, j, n):
    i = mensal(j)
    return p * i / (1 - (1 + i) ** -n)


def aluguel_percentual(receita, base, pct):
    return max(base, receita * pct)


def franqueado_b3(base, pct, invest=310_100.0, capex=224_100.0):
    """60 meses. Ticket reduzido porque a franqueadora construiu a baia."""
    FIXO_SEM_ALUGUEL, CV = 8_550.0, 0.293
    fluxos = [-invest]
    for m in range(1, 61):
        rec = rede.receita_unidade(m)
        al = aluguel_percentual(rec, base, pct)
        aliq = comum.aliquota_simples(rec * 12)
        ebitda = (rec * (1 - aliq - CV - rede.ROYALTY - rede.FUNDO)
                  - rede.TEC - FIXO_SEM_ALUGUEL - al)
        fcl = ebitda - rec * 0.015
        if m == 60:
            fcl += capex * 0.30
        fluxos.append(fcl)
    al_mad = aluguel_percentual(REC, base, pct)
    aliq = comum.aliquota_simples(REC * 12)
    eb = (REC * (1 - aliq - CV - rede.ROYALTY - rede.FUNDO)
          - rede.TEC - FIXO_SEM_ALUGUEL - al_mad)
    return dict(aluguel=al_mad, ebitda=eb, margem=eb / REC,
                tir=tir_anual(fluxos), vpl=vpl(mensal(TMA), fluxos),
                payback=payback(fluxos))


def franqueadora_b3(base, pct, com_divida=True):
    aberturas = rede.cronograma()
    fluxos = [0.0] * (MESES + 1)
    parcelas = []
    equity = 0.0
    for ma in aberturas:
        m_pag = max(1, ma - rede.MESES_ANTES)
        proprio = OBRA * (1 - LTV) if com_divida else OBRA
        fluxos[m_pag] -= proprio
        equity += proprio
        if com_divida:
            parcelas.append((m_pag, parcela(OBRA * LTV, JUROS, PRAZO)))
        fluxos[max(1, ma - 3)] += rede.TAXA_FRANQUIA * (1 - rede.TRIB_SERVICOS)

    anos = {a: dict(u=0, ebitda=0.0) for a in range(1, 11)}
    for m in range(1, MESES + 1):
        ano = min(10, (m - 1) // 12 + 1)
        ativas = [ma for ma in aberturas if ma <= m]
        serv = alug = 0.0
        for ma in ativas:
            r = rede.receita_unidade(m - ma + 1)
            serv += r * rede.ROYALTY
            alug += aluguel_percentual(r, base, pct)
        serv += rede.TEC * len(ativas)
        trib = serv * rede.TRIB_SERVICOS + alug * TRIB_AL
        ebitda = (serv + alug - trib - rede.ESTRUTURA[ano]
                  - MANUT * len(ativas) - HEAD * len(ativas))
        div = sum(v for ini, v in parcelas if ini <= m < ini + PRAZO)
        fluxos[m] += ebitda - div
        anos[ano]["u"] = len(ativas)
        anos[ano]["ebitda"] += ebitda

    # residual: a benfeitoria vale pouco; o negocio de franquia, 5x o EBITDA do ano 10
    resid = OBRA * 0.25 * len(aberturas) + max(0.0, anos[10]["ebitda"]) * 5
    if com_divida:
        saldo = 0.0
        for ini, v in parcelas:
            rest = PRAZO - max(0, min(PRAZO, MESES - ini + 1))
            if rest > 0:
                i = mensal(JUROS)
                saldo += v * (1 - (1 + i) ** -rest) / i
        resid -= saldo
    fluxos[MESES] += resid

    acum, pico, zera = 0.0, 0.0, None
    for m, f in enumerate(fluxos):
        acum += f
        pico = min(pico, acum)
        if zera is None and m > 0 and acum >= 0:
            zera = m
    return dict(equity=equity, pico=pico, zera=zera, tir=tir_anual(fluxos),
                vpl=vpl(mensal(TMA), fluxos), ebitda10=anos[10]["ebitda"],
                obrigacao_mes=HEAD * len(aberturas))


if __name__ == "__main__":
    L = 104
    print("=" * L)
    print("ESTRUTURA McDONALD'S (B3): locacao principal + obra com divida + aluguel percentual")
    print("=" * L)
    print(f"  Obra por ponto                R$ {brl(OBRA)}  financiada a {LTV*100:.0f}% "
          f"({JUROS*100:.0f}% a.a., {PRAZO} meses)")
    print(f"  Equity da franqueadora/ponto  R$ {brl(OBRA*(1-LTV))}")
    print(f"  Locacao principal paga        R$ {brl(HEAD)}/mes por ponto")
    print(f"  Aluguel cobrado               o MAIOR entre a base e um % das vendas\n")

    print(f"  {'base':>8} {'%vendas':>8} {'aluguel':>9} | {'FRANQUEADO':>24} | {'FRANQUEADORA':>34}")
    print(f"  {'':>8} {'':>8} {'maduro':>9} | {'EBITDA':>9} {'TIR':>7} {'VPL@18%':>9}"
          f" | {'equity':>10} {'TIR':>8} {'VPL@18%':>12}")
    for base, pct in ((3_800, 0.08), (3_800, 0.09), (3_800, 0.10),
                      (4_200, 0.11), (4_200, 0.12), (4_500, 0.13)):
        f = franqueado_b3(base, pct)
        d = franqueadora_b3(base, pct)
        tf = f"{f['tir']*100:.1f}%" if f['tir'] else "n/d"
        td = f"{d['tir']*100:.1f}%" if d['tir'] else "negativa"
        ok = "  <-- os dois >= 18%" if (f['tir'] and f['tir'] >= 0.18
                                        and d['tir'] and d['tir'] >= 0.18) else ""
        print(f"  {brl(base):>8} {pct*100:>7.0f}% {brl(f['aluguel']):>9} |"
              f" {brl(f['ebitda']):>9} {tf:>7} {brl(f['vpl']):>9} |"
              f" {brl(d['equity']):>10} {td:>8} {brl(d['vpl']):>12}{ok}")

    print("\n" + "=" * L)
    print("A OBRIGACAO FIXA QUE A LOCACAO PRINCIPAL CRIA")
    print("=" * L)
    d = franqueadora_b3(3_800, 0.10)
    print(f"  65 pontos x R$ {brl(HEAD)} de locacao principal = "
          f"R$ {brl(d['obrigacao_mes'])}/mes de obrigacao fixa")
    print(f"  Se 10% dos pontos ficarem vagos: R$ {brl(d['obrigacao_mes']*0.10)}/mes de sangria")
    print(f"  EBITDA da franqueadora no ano 10: R$ {brl(d['ebitda10'])} "
          f"(R$ {brl(d['ebitda10']/12)}/mes)")
    print(f"  Equity total na obra: R$ {brl(d['equity'])} | pico de caixa R$ {brl(d['pico'])}")

    print("\n" + "=" * L)
    print("SEM DIVIDA (a franqueadora paga a obra a vista)")
    print("=" * L)
    for base, pct in ((3_800, 0.10), (4_200, 0.12)):
        d = franqueadora_b3(base, pct, com_divida=False)
        td = f"{d['tir']*100:.1f}%" if d['tir'] else "negativa"
        print(f"  base {brl(base)} + {pct*100:.0f}% das vendas -> equity "
              f"R$ {brl(d['equity'])}, pico R$ {brl(d['pico'])}, TIR {td}, "
              f"VPL R$ {brl(d['vpl'])}")

    print("\n" + "=" * L)
    print("COMPARACAO COM AS ESTRUTURAS JA MODELADAS")
    print("=" * L)
    for rot, kw in (("A  asset-light", dict(estrutura="A")),
                    ("B1 compra terreno + obra", dict(estrutura="B1")),
                    ("B2 aluga longo + obra, aluguel fixo", dict(estrutura="B2"))):
        r = rede.rede(**kw)
        td = f"{r['tir']*100:.1f}%" if r['tir'] else "negativa"
        print(f"  {rot:<38} capital no ponto R$ {brl(r['capital_imovel']):>12}  "
              f"TIR {td:>9}  VPL R$ {brl(r['vpl']):>12}")


def varredura_receita():
    """A partir de que receita madura a estrutura McDonald's passa a fechar?"""
    import rede as R
    orig = R.REC_MADURA
    print("\n" + "=" * 104)
    print("A PARTIR DE QUE RECEITA A ESTRUTURA McDONALD'S FECHA?  (base 3.800 + 10% das vendas)")
    print("=" * 104)
    print(f"  {'receita madura':>15} {'aluguel':>9} | {'franqueado TIR':>15} "
          f"{'franqueadora TIR':>18} {'franqueadora VPL':>18}")
    for rec in (48_000, 54_000, 60_000, 64_000, 70_000, 80_000, 90_000):
        R.REC_MADURA = float(rec)
        f = franqueado_b3(3_800, 0.10)
        d = franqueadora_b3(3_800, 0.10)
        tf = f"{f['tir']*100:.1f}%" if f['tir'] else "n/d"
        td = f"{d['tir']*100:.1f}%" if d['tir'] else "negativa"
        ok = "  <-- os dois >= 18%" if (f['tir'] and f['tir'] >= 0.18
                                        and d['tir'] and d['tir'] >= 0.18) else ""
        print(f"  {brl(rec):>15} {brl(max(3800, rec*0.10)):>9} | {tf:>15} "
              f"{td:>18} {brl(d['vpl']):>18}{ok}")
    R.REC_MADURA = orig


def razao_aluguel_ativo():
    print("\n" + "=" * 104)
    print("A RAZAO QUE EXPLICA TUDO: aluguel anual recebido / valor do imovel")
    print("=" * 104)
    # McDonald's FY2024 10-K: alugueis 10.017 mi; imobilizado ao custo 44.177 mi,
    # liquido de depreciacao 25.295 mi
    for rot, den in (("imobilizado ao custo (44.177)", 44_177), ("liquido (25.295)", 25_295)):
        print(f"  McDonald's, {rot:<32} {10_017/den*100:>6.1f}% a.a. de aluguel bruto")
    for al in (4_000, 5_000, 6_000):
        print(f"  Ponto de lava jato de R$ 500 mil a R$ {brl(al)}/mes    "
              f"{al*12/500_000*100:>6.1f}% a.a. de aluguel bruto")


if __name__ == "__main__":
    varredura_receita()
    razao_aluguel_ativo()
