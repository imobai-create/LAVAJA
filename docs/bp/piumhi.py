"""
Loja modelo de Piumhi/MG - lava jato automatico sem contato, por assinatura.
Area ALUGADA (R$ 3.000/mes). Capex so de implantacao, sem terreno.
Unidade propria: NAO paga taxa de franquia, royalty, fundo nem taxa de tecnologia.

Horizonte 60 meses. Sem dependencias externas.
"""
import comum
from comum import brl

# ------------------------------------------------------------------ premissas

CAMBIO = 5.30          # R$/USD de planejamento (Focus fim-2026: 5,20; fecha em 60-120 dias)
TMA = 0.18             # cenario base
TMA_ALT = 0.22         # hurdle mais honesto com Selic a 14% a.a.

CAPEX = [
    ("Maquina JM-70 posta em Piumhi (USD 23.000)",        23_000 * CAMBIO),
    ("Interface Modbus/API + kit de pecas 2 anos (USD 2.000)", 2_000 * CAMBIO),
    ("Obra civil: portico, baia coberta, piso, patio 300 m2",   92_000),
    ("Caixa separadora agua/oleo + hidraulica + reservatorio",  26_000),
    ("Entrada de energia, quadro, cabeamento, projeto e ART",   24_000),
    ("Laudo NR-12 com ART",                                      6_000),
    ("Totem de pagamento PIX/cartao + camera + CFTV + rede",    26_000),
    ("1 box de alta pressao + 2 aspiradores",                   18_000),
    ("Fachada, comunicacao visual, iluminacao",                 19_000),
    ("Software da unidade, integracao e implantacao",            12_000),
    ("Projeto, licencas, alvaras, bombeiros, taxas",             14_000),
]
CONTINGENCIA = 0.08

GIRO = [
    ("Caucao de 3 alugueis",                      9_000),
    ("Campanha de pre-venda e inauguracao",      22_000),
    ("Estoque inicial de quimicos",               6_000),
    ("Colchao de 3 meses de custo fixo",         18_000),
]

# Benfeitoria que fica no imovel de terceiro se o contrato nao for renovado
BENFEITORIA = 92_000 + 26_000 + 24_000

# ---- precos (site)
P_ESSENCIAL, P_ILIMITADA, P_PREMIUM, P_AVULSA = 59.0, 99.0, 139.0, 35.0

# ---- mix e uso
MIX = {
    "Essencial": dict(share=0.45, preco=P_ESSENCIAL, lav_mes=4.0),
    "Ilimitada": dict(share=0.40, preco=P_ILIMITADA, lav_mes=6.0),
    "Premium":   dict(share=0.15, preco=P_PREMIUM,   lav_mes=7.0),
}

# ---- custo variavel por lavagem
AGUA_L = 85.0           # 60-100 L/carro (cotacao Yugong)
TARIFA_AGUA = 14.00     # R$/m3, agua + esgoto comercial (ESTIMATIVA - confirmar SAAE Piumhi)
ENERGIA_KWH = 1.6       # calculo proprio pelos componentes, nao os 0,6-1,2 do fornecedor
TARIFA_KWH = 0.98       # R$/kWh comercial com tributos (ESTIMATIVA - confirmar CEMIG)
QUIMICOS = 2.50         # R$/lavagem (detergente touchless, espuma, cera)
TAXA_MEIO_PAGTO = 0.015 # PIX + cartao, media sobre a receita

CV_LAVAGEM = AGUA_L / 1000 * TARIFA_AGUA + ENERGIA_KWH * TARIFA_KWH + QUIMICOS

FIXOS = [
    ("Aluguel da area",                              3_000),
    ("1 atendente meio periodo + encargos",          2_600),
    ("Manutencao preventiva e pecas de desgaste",    1_400),
    ("Internet, telefonia, gateway, software",         450),
    ("Contador",                                       700),
    ("Seguro do equipamento + RC",                     400),
    ("Energia de base (iluminacao, standby, aspirador)", 600),
    ("Limpeza, uniformes, materiais",                  350),
    ("Marketing recorrente",                         1_800),
    ("IPTU, taxas, alvara (rateio mensal)",            250),
]

CAPEX_MANUT = 0.015    # % da receita, reposicao de bicos/bombas/pintura
RESIDUAL = 0.30        # valor residual no mes 60: so o equipamento, nao a benfeitoria

# ---- rampa de assinantes: logistica ate o teto, em 18 meses
def rampa(teto, meses=60, m_meio=8.0, k=0.33, inicial=80):
    """80 fundadores na abertura; curva em S convergindo para o teto."""
    import math
    out = []
    for m in range(1, meses + 1):
        v = teto / (1 + math.exp(-k * (m - m_meio)))
        out.append(min(teto, max(inicial, v)))
    return out


# ------------------------------------------------------------------- cenarios

CENARIOS = {
    "Conservador": dict(assinantes=380, avulsas_dia=6,  compl=1_400),
    "Base":        dict(assinantes=500, avulsas_dia=8,  compl=2_200),
    "Otimista":    dict(assinantes=650, avulsas_dia=12, compl=3_200),
}

FROTA_AUTOMOVEIS_PIUMHI = 13_652   # 2024, Senatran via IBGE (fonte secundaria)


def capex_total():
    base = sum(v for _, v in CAPEX)
    return base, base * CONTINGENCIA, base * (1 + CONTINGENCIA)


def receita_e_lavagens(n_assinantes, avulsas_dia, compl):
    """Receita mensal e numero de lavagens no mes, para um dado numero de assinantes."""
    rec_assin = 0.0
    lav_assin = 0.0
    for p in MIX.values():
        n = n_assinantes * p["share"]
        rec_assin += n * p["preco"]
        lav_assin += n * p["lav_mes"]
    lav_avulsas = avulsas_dia * 30
    rec_avulsas = lav_avulsas * P_AVULSA
    return rec_assin + rec_avulsas + compl, lav_assin + lav_avulsas


def unidade(cen, tma=TMA, tabela_simples=comum.ANEXO_III, meses=60,
            escala_receita=1.0, aluguel_extra=0.0, royalty=0.0, fundo=0.0,
            tecnologia=0.0, capex_override=None, giro_override=None,
            taxa_franquia=0.0):
    teto = cen["assinantes"]
    curva = rampa(teto, meses)

    _, _, capex = capex_total()
    if capex_override is not None:
        capex = capex_override
    giro = sum(v for _, v in GIRO) if giro_override is None else giro_override
    investimento = capex + giro + taxa_franquia

    fixo_mes = sum(v for _, v in FIXOS) + aluguel_extra

    fluxos = [-investimento]
    linhas = []
    hist_receita = []

    for m in range(1, meses + 1):
        n = curva[m - 1]
        rec, lav = receita_e_lavagens(n, cen["avulsas_dia"], cen["compl"])
        # rampa tambem nas avulsas e complementares durante os 12 primeiros meses
        f_ramp = min(1.0, 0.45 + 0.55 * (m / 12))
        rec_av = (cen["avulsas_dia"] * 30 * P_AVULSA + cen["compl"]) * (f_ramp - 1)
        lav_av = cen["avulsas_dia"] * 30 * (f_ramp - 1)
        rec = (rec + rec_av) * escala_receita
        lav = lav + lav_av

        hist_receita.append(rec)
        rbt12 = sum(hist_receita[-12:]) * (12 / min(12, len(hist_receita)))
        aliq = comum.aliquota_simples(rbt12, tabela_simples)

        imposto = rec * aliq
        var = lav * CV_LAVAGEM + rec * TAXA_MEIO_PAGTO
        taxas_rede = rec * (royalty + fundo) + tecnologia
        ebitda = rec - imposto - var - fixo_mes - taxas_rede
        fcl = ebitda - rec * CAPEX_MANUT
        if m == meses:
            fcl += capex * RESIDUAL
        fluxos.append(fcl)
        linhas.append(dict(mes=m, assin=n, receita=rec, lavagens=lav, aliq=aliq,
                           imposto=imposto, var=var, fixo=fixo_mes,
                           taxas=taxas_rede, ebitda=ebitda, fcl=fcl))

    rm = comum.mensal(tma)
    return dict(
        investimento=investimento, capex=capex, giro=giro,
        fluxos=fluxos, linhas=linhas,
        tir=comum.tir_anual(fluxos),
        vpl=comum.vpl(rm, fluxos),
        payback=comum.payback(fluxos),
        maduro=linhas[-1],
        roi=sum(fluxos[1:]) / investimento,
    )


def equilibrio(cen):
    """Receita mensal de equilibrio no estado maduro (EBITDA = 0)."""
    fixo = sum(v for _, v in FIXOS)
    rec_m, lav_m = receita_e_lavagens(cen["assinantes"], cen["avulsas_dia"], cen["compl"])
    cv_rel = (lav_m * CV_LAVAGEM) / rec_m + TAXA_MEIO_PAGTO
    aliq = comum.aliquota_simples(rec_m * 12)
    # rec*(1 - aliq - cv_rel) = fixo
    return fixo / (1 - aliq - cv_rel), cv_rel, aliq


if __name__ == "__main__":
    L = 84
    base, cont, cap = capex_total()
    print("=" * L)
    print("LOJA MODELO PIUMHI/MG - area alugada, capex so de implantacao")
    print("=" * L)
    print(f"\nCAPEX  (cambio de planejamento R$ {CAMBIO:.2f}/USD)")
    for nome, v in CAPEX:
        print(f"  {nome:<58} {brl(v):>12}")
    print(f"  {'Subtotal':<58} {brl(base):>12}")
    print(f"  {'Contingencia 8%':<58} {brl(cont):>12}")
    print(f"  {'CAPEX TOTAL':<58} {brl(cap):>12}")
    print(f"\n  do qual benfeitoria em imovel de terceiro: {brl(BENFEITORIA)} "
          f"({BENFEITORIA/cap*100:.0f}% do capex)")

    giro = sum(v for _, v in GIRO)
    print(f"\nCAPITAL DE GIRO")
    for nome, v in GIRO:
        print(f"  {nome:<58} {brl(v):>12}")
    print(f"  {'TOTAL GIRO':<58} {brl(giro):>12}")
    print(f"\n  INVESTIMENTO TOTAL                                         {brl(cap+giro):>12}")

    print(f"\nCUSTO VARIAVEL POR LAVAGEM")
    print(f"  Agua {AGUA_L:.0f} L a R$ {TARIFA_AGUA:.2f}/m3                "
          f"{brl(AGUA_L/1000*TARIFA_AGUA,2):>12}")
    print(f"  Energia {ENERGIA_KWH:.1f} kWh a R$ {TARIFA_KWH:.2f}/kWh          "
          f"{brl(ENERGIA_KWH*TARIFA_KWH,2):>12}")
    print(f"  Quimicos                                              {brl(QUIMICOS,2):>12}")
    print(f"  TOTAL por lavagem                                     {brl(CV_LAVAGEM,2):>12}")

    fixo = sum(v for _, v in FIXOS)
    print(f"\nCUSTO FIXO MENSAL")
    for nome, v in FIXOS:
        print(f"  {nome:<58} {brl(v):>12}")
    print(f"  {'TOTAL FIXO':<58} {brl(fixo):>12}")

    for nome, cen in CENARIOS.items():
        r = unidade(cen)
        m = r["maduro"]
        pen = cen["assinantes"] / FROTA_AUTOMOVEIS_PIUMHI
        print("\n" + "-" * L)
        print(f"{nome.upper()}  -  {cen['assinantes']} assinantes "
              f"({pen*100:.1f}% dos {brl(FROTA_AUTOMOVEIS_PIUMHI)} automoveis de Piumhi)")
        print("-" * L)
        print(f"  Receita madura/mes       R$ {brl(m['receita']):>10}")
        print(f"  Lavagens/mes             {m['lavagens']:>13.0f}   "
              f"({m['lavagens']/30:.0f}/dia)")
        print(f"  Aliquota Simples efetiva {m['aliq']*100:>12.1f}%")
        print(f"  Custo variavel/mes       R$ {brl(m['var']):>10}   "
              f"({m['var']/m['receita']*100:.1f}% da receita)")
        print(f"  Custo fixo/mes           R$ {brl(m['fixo']):>10}")
        print(f"  EBITDA maduro/mes        R$ {brl(m['ebitda']):>10}   "
              f"(margem {m['ebitda']/m['receita']*100:.1f}%)")
        print(f"  Investimento             R$ {brl(r['investimento']):>10}")
        print(f"  Payback                  {r['payback']:>13} meses")
        print(f"  TIR                      {r['tir']*100:>12.1f}% a.a.")
        print(f"  VPL @ {TMA*100:.0f}%              R$ {brl(r['vpl']):>10}")
        r22 = unidade(cen, tma=TMA_ALT)
        print(f"  VPL @ {TMA_ALT*100:.0f}%              R$ {brl(r22['vpl']):>10}")
        print(f"  ROI 5 anos               {r['roi']*100:>12.0f}%")

    print("\n" + "=" * L)
    print("PONTO DE EQUILIBRIO (estado maduro, cenario Base)")
    print("=" * L)
    eq, cv_rel, aliq = equilibrio(CENARIOS["Base"])
    rec_m, lav_m = receita_e_lavagens(500, 8, 2_200)
    print(f"  Receita de equilibrio       R$ {brl(eq)}/mes "
          f"({eq/rec_m*100:.0f}% da receita madura)")
    print(f"  Equivale a                  {eq/rec_m*lav_m/30:.0f} lavagens/dia "
          f"ou ~{eq/rec_m*500:.0f} assinantes")
