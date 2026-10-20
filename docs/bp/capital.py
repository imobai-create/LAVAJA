"""
Estrutura de capital da loja modelo de Piumhi.

Compara formas de montar os R$ 373 mil a R$ 454 mil que a Fase 1 precisa:
capital proprio, investidor, divida e alavancas de caixa (pre-venda anual dos
fundadores, credito do fornecedor, obra parcelada).

Para cada arranjo calcula: pico de caixa, equity necessario, TIR alavancada
do bloco de equity, e a fatia que o investidor precisa para bater a TMA dele.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import comum, piumhi
from comum import brl, vpl, tir_anual, payback, mensal

TMA_ANTONIO = 0.18
PRO_LABORE = 3_500.0      # o modelo base NAO remunerava o operador. Agora remunera.
TMA_INVESTIDOR = 0.22     # investidor local pede mais que o dono: menos controle, menos informacao

# ---- capex cheio e capex enxuto (BP-PIUMHI secao 2)
CAPEX_CHEIO, GIRO_CHEIO = 399_060.0, 55_000.0
CAPEX_ENXUTO, GIRO_ENXUTO = 328_000.0, 45_000.0

# ---- dividas candidatas
#   BDMG Pronampe investimento: Selic + 5,50% a.a., 72 meses, 12 de carencia.
#   TETO = 30% da receita bruta do ano anterior, maximo R$ 250 mil  ->  PJ nova NAO acessa.
#   Finame: so maquina credenciada no BNDES (nacional). Maquina chinesa nao entra.
SELIC = 0.14
DIVIDAS = {
    "Finame em maquina nacional": dict(valor=170_000, juros=SELIC + 0.0575, prazo=84,
                                       carencia=12),
    "BDMG Pronampe investimento": dict(valor=150_000, juros=SELIC + 0.055, prazo=72,
                                       carencia=12),
    "Banco comercial com aval":   dict(valor=120_000, juros=0.26, prazo=60, carencia=6),
    "Cooperativa de credito":     dict(valor=120_000, juros=0.21, prazo=60, carencia=6),
}

# ---- pre-venda dos fundadores
FUNDADORES = 80
MENSALIDADE_FUNDADOR = 79.0
MESES_PAGOS = 11            # 12 meses pelo preco de 11: um mes de brinde
TICKET_MIX = 87.0           # ticket medio do mix no modelo


def servico_divida(valor, juros, prazo, carencia):
    """Lista de 120 posicoes com a parcela de cada mes. Carencia paga so juros."""
    i = mensal(juros)
    parc = valor * i / (1 - (1 + i) ** -prazo)
    fluxo = [0.0] * 121
    for m in range(1, carencia + 1):
        fluxo[m] = valor * i
    for m in range(carencia + 1, min(120, carencia + prazo) + 1):
        fluxo[m] = parc
    return fluxo, parc, valor * i


def arranjo(nome, capex, giro, divida=None, pre_venda=False, meses=60,
            pro_labore=PRO_LABORE):
    """Fluxo do bloco de equity: projeto, menos servico da divida, mais alavancas."""
    cen = piumhi.CENARIOS["Base"]
    u = piumhi.unidade(cen, capex_override=capex, giro_override=giro, meses=meses,
                       aluguel_extra=pro_labore)
    invest = capex + giro

    fluxos = list(u["fluxos"])          # [0] = -investimento

    # divida entra no mes 0 e reduz o desembolso de equity
    sd = [0.0] * (meses + 1)
    parc = juros_car = 0.0
    if divida:
        d = DIVIDAS[divida]
        fluxos[0] += d["valor"]
        sdf, parc, juros_car = servico_divida(**d)
        for m in range(1, meses + 1):
            sd[m] = sdf[m]
            fluxos[m] -= sdf[m]
        # saldo devedor no mes 60 sai do valor residual
        i = mensal(d["juros"])
        pagas = max(0, meses - d["carencia"])
        rest = max(0, d["prazo"] - pagas)
        if rest > 0:
            fluxos[meses] -= parc * (1 - (1 + i) ** -rest) / i

    # pre-venda anual dos fundadores: entra no mes 0, sai da receita dos 12 primeiros
    caixa_pre = 0.0
    if pre_venda:
        caixa_pre = FUNDADORES * MENSALIDADE_FUNDADOR * MESES_PAGOS
        fluxos[0] += caixa_pre
        perda = FUNDADORES * TICKET_MIX
        for m in range(1, 13):
            fluxos[m] -= perda * (1 - comum.aliquota_simples(
                u["linhas"][m - 1]["receita"] * 12))

    acum, pico, mpico = 0.0, 0.0, 0
    for m, f in enumerate(fluxos):
        acum += f
        if acum < pico:
            pico, mpico = acum, m

    return dict(nome=nome, invest=invest, equity=-fluxos[0], fluxos=fluxos,
                pico=pico, mes_pico=mpico, parcela=parc, juros_carencia=juros_car,
                caixa_pre=caixa_pre, divida=divida,
                tir=tir_anual(fluxos), vpl=vpl(mensal(TMA_ANTONIO), fluxos),
                payback=payback(fluxos), ebitda=u["maduro"]["ebitda"])


def fatia_investidor(fluxos, aporte, tma):
    """% das distribuicoes que da ao investidor exatamente a TMA dele."""
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        x = (lo + hi) / 2
        f = [-aporte] + [v * x for v in fluxos[1:]]
        t = tir_anual(f)
        if t is None or t < tma:
            lo = x
        else:
            hi = x
    return (lo + hi) / 2


def mostra(a):
    print(f"\n  {a['nome']}")
    print(f"    Investimento (capex + giro)      R$ {brl(a['invest']):>9}")
    print(f"    Desembolso de equity no mes 0    R$ {brl(a['equity']):>9}")
    if a["divida"]:
        print(f"    Divida                           R$ {brl(DIVIDAS[a['divida']]['valor']):>9}"
              f"   {DIVIDAS[a['divida']]['juros']*100:.2f}% a.a., "
              f"{DIVIDAS[a['divida']]['prazo']}m, "
              f"{DIVIDAS[a['divida']]['carencia']}m de carencia")
        print(f"    Juros na carencia / parcela      R$ {brl(a['juros_carencia']):>9}"
              f" / R$ {brl(a['parcela'])} por mes")
    if a["caixa_pre"]:
        print(f"    Pre-venda anual de fundadores    R$ {brl(a['caixa_pre']):>9}"
              f"   {FUNDADORES} x R$ {brl(MENSALIDADE_FUNDADOR,0)} x {MESES_PAGOS} meses")
    print(f"    CAPITAL A RESERVAR (pico)        R$ {brl(-a['pico']):>9}   atingido no mes "
          f"{a['mes_pico']}")
    print(f"      1a tranche, na assinatura      R$ {brl(a['equity']):>9}")
    print(f"      a chamar durante a rampa       R$ {brl(-a['pico'] - a['equity']):>9}")
    print(f"    Payback do equity                {str(a['payback']) + ' meses':>12}")
    print(f"    TIR do equity                    {a['tir']*100:>11.1f}% a.a.")
    print(f"    VPL @ 18%                        R$ {brl(a['vpl']):>9}")


if __name__ == "__main__":
    L = 92
    print("=" * L)
    print("ESTRUTURA DE CAPITAL - LOJA MODELO DE PIUMHI")
    print("=" * L)
    print(f"  Cenario base: 500 assinantes, receita madura de R$ 54.100/mes")
    print(f"  Selic de referencia: {SELIC*100:.0f}% a.a.")

    arr = [
        arranjo("1. Capex cheio, 100% equity", CAPEX_CHEIO, GIRO_CHEIO),
        arranjo("2. Capex enxuto, 100% equity", CAPEX_ENXUTO, GIRO_ENXUTO),
        arranjo("3. Enxuto + pre-venda anual dos fundadores",
                CAPEX_ENXUTO, GIRO_ENXUTO, pre_venda=True),
        arranjo("4. Enxuto + pre-venda + cooperativa de credito",
                CAPEX_ENXUTO, GIRO_ENXUTO, divida="Cooperativa de credito", pre_venda=True),
        arranjo("5. Enxuto + pre-venda + banco comercial",
                CAPEX_ENXUTO, GIRO_ENXUTO, divida="Banco comercial com aval", pre_venda=True),
        arranjo("6. Enxuto + pre-venda + Finame (maquina NACIONAL)",
                CAPEX_ENXUTO, GIRO_ENXUTO, divida="Finame em maquina nacional",
                pre_venda=True),
    ]
    for a in arr:
        mostra(a)

    print("\n" + "=" * L)
    print("RESUMO: quanto de equity cada arranjo exige, e o que ele rende")
    print("=" * L)
    print(f"  {'arranjo':<46} {'1a tranche':>11} {'a reservar':>11} {'TIR':>8} {'VPL@18%':>11}")
    for a in arr:
        print(f"  {a['nome']:<46} {brl(a['equity']):>11} {brl(-a['pico']):>11} "
              f"{a['tir']*100:>7.1f}% {brl(a['vpl']):>11}")

    print("\n" + "=" * L)
    print("QUANTO O INVESTIDOR PRECISA RECEBER")
    print("=" * L)
    rec = arr[3]   # arranjo recomendado
    print(f"  Arranjo: {rec['nome']}")
    print(f"  Equity total: R$ {brl(rec['equity'])}\n")
    print(f"  {'aporte do investidor':>22} {'fatia p/ TIR 18%':>18} {'fatia p/ TIR 22%':>18}"
          f" {'fatia p/ TIR 25%':>18}")
    for aporte in (100_000, 130_000, 150_000, 180_000):
        linha = f"  {brl(aporte):>22}"
        for tma in (0.18, 0.22, 0.25):
            x = fatia_investidor(rec["fluxos"], aporte, tma)
            linha += f" {x*100:>17.1f}%"
        print(linha)
    print(f"\n  Referencia: o aporte como % do capital a reservar (divisao proporcional)")
    for aporte in (100_000, 130_000, 150_000, 180_000):
        print(f"  {brl(aporte):>22} {aporte/-rec['pico']*100:>17.1f}%")

    print("\n" + "=" * 92)
    print("A DIVISAO PROPOSTA: o que cada lado faz")
    print("=" * 92)
    reservar = -rec["pico"]
    for aporte_inv, fatia in ((130_000, 0.35), (130_000, 0.40), (150_000, 0.40),
                              (150_000, 0.45)):
        aporte_ant = reservar - aporte_inv
        f_inv = [-aporte_inv] + [v * fatia for v in rec["fluxos"][1:]]
        f_ant = [-aporte_ant] + [v * (1 - fatia) for v in rec["fluxos"][1:]]
        ti, ta = tir_anual(f_inv), tir_anual(f_ant)
        print(f"  investidor R$ {brl(aporte_inv)} por {fatia*100:.0f}%  |  "
              f"Antonio R$ {brl(aporte_ant)} por {(1-fatia)*100:.0f}%  ->  "
              f"TIR investidor {ti*100:>5.1f}%  |  TIR Antonio {ta*100:>5.1f}%")

    print("\n" + "=" * 92)
    print("O QUE O PRO-LABORE DE R$ 3.500/MES CUSTA AO PROJETO")
    print("=" * 92)
    for pl, rot in ((0.0, "sem pro-labore (como o BP estava)"),
                    (3_500.0, "com pro-labore de R$ 3.500"),
                    (6_000.0, "com pro-labore de R$ 6.000")):
        a = arranjo(rot, CAPEX_ENXUTO, GIRO_ENXUTO, divida="Cooperativa de credito",
                    pre_venda=True, pro_labore=pl)
        print(f"  {rot:<40} EBITDA R$ {brl(a['ebitda']):>8}   "
              f"a reservar R$ {brl(-a['pico']):>9}   TIR {a['tir']*100:>5.1f}%")
