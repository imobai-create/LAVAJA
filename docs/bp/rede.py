"""
Plano macro da rede - 120 meses.
Tres estruturas para o ponto comercial:
  A  - asset-light: o franqueado aluga de terceiro. Franqueadora so licencia.
  B1 - imobiliario proprio: a franqueadora COMPRA o terreno e constroi. Franqueado aluga.
  B2 - locacao longa + benfeitoria + sublocacao: a franqueadora aluga de terceiro por
       10-15 anos, constroi a baia e subloca pronta ao franqueado.
"""
import comum
from comum import brl, vpl, tir_anual, payback, mensal

TMA = 0.18
MESES = 120
IPCA = 0.047          # usado so na valorizacao do terreno

# ---- unidade franqueada generica (cidade de 30-80 mil hab)
REC_MADURA = 48_000.0
RAMPA_U = [0.35]*3 + [0.55]*3 + [0.75]*3 + [0.88]*3 + [1.00]*(MESES)

ROYALTY, FUNDO, TEC = 0.06, 0.02, 700.0
TAXA_FRANQUIA = 40_000.0      # menor que os R$ 50 mil: a franqueadora fica com o imovel

# ---- aluguel
ALUGUEL_MERCADO = 3_000.0     # o que o franqueado pagaria a um terceiro (praca tipica)
ALUGUEL_B1 = 4_000.0          # ponto pronto, licenciado, com separadora e entrada de energia
ALUGUEL_B2 = 6_500.0          # idem, mas a franqueadora paga 3.000 ao proprietario

# ---- capex do ponto, por unidade
TERRENO = 280_000.0
CONSTRUCAO = 220_000.0        # baia, portico, piso, patio, separadora, entrada de energia
MESES_ANTES = 6               # o ponto fica pronto 6 meses antes da inauguracao

CUSTO_IMOVEL_B1 = 650.0       # IPTU, seguro predial, manutencao estrutural
CUSTO_IMOVEL_B2 = 350.0       # idem, sem IPTU do proprietario

# ---- tributos da franqueadora (Lucro Presumido - ESTIMATIVA, validar com contador)
TRIB_SERVICOS = 0.160         # royalty + taxa de tecnologia (presumido 32% + PIS/COFINS + ISS)
TRIB_ALUGUEL = 0.115         # locacao de imovel proprio (presumido 32%, sem ISS)

# ---- estrutura da franqueadora, por ano
ESTRUTURA = {1: 11_250, 2: 28_000, 3: 42_000, 4: 52_000, 5: 60_000,
             6: 68_000, 7: 76_000, 8: 86_000, 9: 94_000, 10: 102_000}

# ---- cronograma de inauguracoes (unidades novas por ano; ano 1 = so a loja propria)
NOVAS = {1: 0, 2: 2, 3: 5, 4: 5, 5: 7, 6: 8, 7: 8, 8: 10, 9: 10, 10: 10}

# ---- divida opcional sobre o imovel
DIVIDA_LTV = 0.50
DIVIDA_JUROS = 0.14
DIVIDA_PRAZO = 120


def cronograma():
    """Mes de inauguracao de cada unidade franqueada."""
    meses = []
    for ano, n in NOVAS.items():
        for i in range(n):
            m = (ano - 1) * 12 + 1 + int(i * 12 / max(1, n))
            meses.append(m)
    return sorted(meses)


def receita_unidade(idade):
    """Receita da unidade no mes `idade` apos a inauguracao (1-based)."""
    if idade < 1:
        return 0.0
    return REC_MADURA * RAMPA_U[min(idade - 1, len(RAMPA_U) - 1)]


def parcela(principal, juros_anual, prazo):
    i = mensal(juros_anual)
    return principal * i / (1 - (1 + i) ** -prazo)


def rede(estrutura="A", com_divida=False, com_residual=True, novas=None):
    aberturas = cronograma() if novas is None else novas
    fluxos = [0.0] * (MESES + 1)
    anos = {a: dict(unidades=0, receita=0.0, ebitda=0.0, imovel=0.0) for a in range(1, 11)}
    capital_imovel = 0.0
    parcelas = []   # (mes_inicio, valor)

    for m_abertura in aberturas:
        # capex do ponto
        if estrutura == "B1":
            invest = TERRENO + CONSTRUCAO
        elif estrutura == "B2":
            invest = CONSTRUCAO
        else:
            invest = 0.0
        if invest:
            m_pag = max(1, m_abertura - MESES_ANTES)
            proprio = invest * (1 - DIVIDA_LTV) if com_divida else invest
            fluxos[m_pag] -= proprio
            capital_imovel += invest
            if com_divida:
                parcelas.append((m_pag, parcela(invest * DIVIDA_LTV,
                                                DIVIDA_JUROS, DIVIDA_PRAZO)))
            ano = min(10, (m_pag - 1) // 12 + 1)
            anos[ano]["imovel"] += invest
        # taxa de franquia, na assinatura (3 meses antes de abrir)
        fluxos[max(1, m_abertura - 3)] += TAXA_FRANQUIA * (1 - TRIB_SERVICOS)

    for m in range(1, MESES + 1):
        ano = min(10, (m - 1) // 12 + 1)
        ativas = [ma for ma in aberturas if ma <= m]
        rec_rede = sum(receita_unidade(m - ma + 1) for ma in ativas)

        # receita da franqueadora
        serv = rec_rede * ROYALTY + TEC * len(ativas)
        if estrutura == "B1":
            alug = ALUGUEL_B1 * len(ativas)
            custo_imovel = CUSTO_IMOVEL_B1 * len(ativas)
            alug_pago = 0.0
        elif estrutura == "B2":
            alug = ALUGUEL_B2 * len(ativas)
            custo_imovel = CUSTO_IMOVEL_B2 * len(ativas)
            alug_pago = ALUGUEL_MERCADO * len(ativas)
        else:
            alug = custo_imovel = alug_pago = 0.0

        bruto = serv + alug
        trib = serv * TRIB_SERVICOS + alug * TRIB_ALUGUEL
        est = ESTRUTURA[ano]
        ebitda = bruto - trib - est - custo_imovel - alug_pago

        servico_divida = sum(v for ini, v in parcelas
                             if ini <= m < ini + DIVIDA_PRAZO)
        fluxos[m] += ebitda - servico_divida

        anos[ano]["unidades"] = len(ativas)
        anos[ano]["receita"] += bruto
        anos[ano]["ebitda"] += ebitda

    # valor residual
    residual = 0.0
    if com_residual:
        if estrutura == "B1":
            for ma in aberturas:
                anos_posse = max(0, (MESES - max(1, ma - MESES_ANTES)) / 12)
                residual += TERRENO * (1 + 0.045) ** anos_posse + CONSTRUCAO * 0.75
            if com_divida:
                saldo = 0.0
                for ini, v in parcelas:
                    pagas = max(0, min(DIVIDA_PRAZO, MESES - ini + 1))
                    rest = DIVIDA_PRAZO - pagas
                    if rest > 0:
                        i = mensal(DIVIDA_JUROS)
                        saldo += v * (1 - (1 + i) ** -rest) / i
                residual -= saldo
        elif estrutura == "B2":
            residual += CONSTRUCAO * 0.25 * len(aberturas)
        # valor do negocio de franquia: 5x o EBITDA do ano 10 (conservador)
        residual += max(0.0, anos[10]["ebitda"]) * 5
    fluxos[MESES] += residual

    acum, pico, zera = 0.0, 0.0, None
    for m, f in enumerate(fluxos):
        acum += f
        pico = min(pico, acum)
        if zera is None and m > 0 and acum >= 0:
            zera = m

    return dict(anos=anos, fluxos=fluxos, pico=pico, zera=zera,
                tir=tir_anual(fluxos), vpl=vpl(mensal(TMA), fluxos),
                capital_imovel=capital_imovel, residual=residual,
                unidades=len(aberturas))


def franqueado(estrutura="A"):
    """Economia do franqueado em cada estrutura. Horizonte 60 meses."""
    # capex = o que deprecia e tem valor residual. Taxa de franquia e giro ficam fora.
    if estrutura == "A":
        capex, taxa, giro = 399_060.0, 50_000.0, 55_000.0   # ele constroi o ponto inteiro
        aluguel = ALUGUEL_MERCADO
    else:
        # ponto pronto: maquina, interface, totem, boxes, fachada, software, contingencia
        capex = 132_500 + 26_000 + 18_000 + 19_000 + 12_000 + 16_600
        taxa, giro = TAXA_FRANQUIA, 46_000.0
        aluguel = ALUGUEL_B1 if estrutura == "B1" else ALUGUEL_B2
    invest = capex + taxa + giro

    FIXO_SEM_ALUGUEL = 8_550.0    # custo fixo da loja modelo menos o aluguel
    CV_REL = 0.293                # custo variavel + meios de pagamento, % da receita

    fluxos = [-invest]
    for m in range(1, 61):
        rec = receita_unidade(m)
        aliq = comum.aliquota_simples(rec * 12)
        ebitda = (rec * (1 - aliq - CV_REL - ROYALTY - FUNDO)
                  - TEC - FIXO_SEM_ALUGUEL - aluguel)
        fcl = ebitda - rec * 0.015
        if m == 60:
            fcl += capex * 0.30      # residual so sobre o capex
        fluxos.append(fcl)
    rec_mad = receita_unidade(60)
    aliq = comum.aliquota_simples(rec_mad * 12)
    ebitda_mad = (rec_mad * (1 - aliq - CV_REL - ROYALTY - FUNDO)
                  - TEC - FIXO_SEM_ALUGUEL - aluguel)
    return dict(invest=invest, aluguel=aluguel, ebitda=ebitda_mad,
                margem=ebitda_mad / rec_mad, tir=tir_anual(fluxos),
                vpl=vpl(mensal(TMA), fluxos), payback=payback(fluxos))


if __name__ == "__main__":
    L = 96
    print("=" * L)
    print("O FRANQUEADO EM CADA ESTRUTURA DE PONTO  (unidade madura a R$ 48.000/mes)")
    print("=" * L)
    print(f"  {'':<42} {'A: aluga':>15} {'B1: compramos':>15} {'B2: sublocamos':>15}")
    fa, fb1, fb2 = franqueado("A"), franqueado("B1"), franqueado("B2")
    rows = [
        ("Investimento do franqueado", "invest", 0),
        ("Aluguel que ele paga", "aluguel", 0),
        ("EBITDA maduro/mes", "ebitda", 0),
    ]
    for rot, k, c in rows:
        print(f"  {rot:<42} {brl(fa[k],c):>15} {brl(fb1[k],c):>15} {brl(fb2[k],c):>15}")
    print(f"  {'Margem EBITDA':<42} {fa['margem']*100:>14.1f}% "
          f"{fb1['margem']*100:>14.1f}% {fb2['margem']*100:>14.1f}%")
    print(f"  {'Payback':<42} {str(fa['payback'])+' meses':>15} "
          f"{str(fb1['payback'])+' meses':>15} {str(fb2['payback'])+' meses':>15}")
    print(f"  {'TIR':<42} {fa['tir']*100:>14.1f}% "
          f"{fb1['tir']*100:>14.1f}% {fb2['tir']*100:>14.1f}%")
    print(f"  {'VPL @ 18%':<42} {brl(fa['vpl']):>15} {brl(fb1['vpl']):>15} "
          f"{brl(fb2['vpl']):>15}")

    print("\n" + "=" * L)
    print("A FRANQUEADORA EM CADA ESTRUTURA  (120 meses, 65 unidades no ano 10)")
    print("=" * L)
    casos = [
        ("A  - asset-light",                       dict(estrutura="A")),
        ("B1 - compra o imovel, sem divida",       dict(estrutura="B1")),
        ("B1 - compra o imovel, 50% financiado",   dict(estrutura="B1", com_divida=True)),
        ("B2 - locacao longa + sublocacao",        dict(estrutura="B2")),
    ]
    print(f"  {'':<40} {'capital no':>13} {'pico de':>13} {'caixa':>8} "
          f"{'TIR':>8} {'VPL @18%':>13}")
    print(f"  {'':<40} {'imovel':>13} {'caixa':>13} {'zera':>8} {'':>8} {'':>13}")
    res = {}
    for rot, kw in casos:
        r = rede(**kw)
        res[rot] = r
        print(f"  {rot:<40} {brl(r['capital_imovel']):>13} {brl(r['pico']):>13} "
              f"{str(r['zera'] or '-'):>8} "
              f"{(f'{r[chr(116)+chr(105)+chr(114)]*100:.1f}%' if r['tir'] else 'n/d'):>8} "
              f"{brl(r['vpl']):>13}")

    print("\n  Ano 10 - EBITDA anual da franqueadora:")
    for rot, r in res.items():
        print(f"    {rot:<40} {brl(r['anos'][10]['ebitda']):>13}")
    print("\n  Valor residual embutido no mes 120:")
    for rot, r in res.items():
        print(f"    {rot:<40} {brl(r['residual']):>13}")

    print("\n" + "=" * L)
    print("SEM VALOR RESIDUAL (so o caixa operacional dos 120 meses)")
    print("=" * L)
    for rot, kw in casos:
        r = rede(com_residual=False, **kw)
        t = f"{r['tir']*100:.1f}%" if r["tir"] else "negativa"
        print(f"  {rot:<40} TIR {t:>9}   VPL {brl(r['vpl']):>13}")

    print("\n" + "=" * L)
    print("ESCALA: e se a rede parar em 20 unidades em vez de 65?")
    print("=" * L)
    cron = cronograma()
    for n in (12, 20, 35, 65):
        sub = cron[:n]
        for rot, kw in [("B1", dict(estrutura="B1")), ("B2", dict(estrutura="B2"))]:
            r = rede(novas=sub, **kw)
            t = f"{r['tir']*100:.1f}%" if r["tir"] else "negativa"
            print(f"  {n:>3} unidades  {rot}   capital no imovel {brl(r['capital_imovel']):>12}   "
                  f"pico {brl(r['pico']):>12}   TIR {t:>9}   VPL {brl(r['vpl']):>13}")
        print()


def consolidado(estrutura="A", com_divida=False):
    """Fase 1 (Piumhi, 120 meses) + Fase 2 (franqueadora) no mesmo caixa.

    A unidade propria passa a pagar royalty, fundo e tecnologia a partir do mes 13,
    quando a franqueadora existe - e a franqueadora recebe.
    """
    import piumhi
    u = piumhi.unidade(piumhi.CENARIOS["Base"], meses=MESES)
    f = rede(estrutura=estrutura, com_divida=com_divida)

    fluxos = [0.0] * (MESES + 1)
    fluxos[0] += u["fluxos"][0]
    for m in range(1, MESES + 1):
        fcl = u["fluxos"][m]
        if m >= 13:
            rec = u["linhas"][m - 1]["receita"]
            fcl -= rec * (ROYALTY + FUNDO) + TEC   # sai da unidade
        fluxos[m] += fcl
    for m in range(0, MESES + 1):
        fluxos[m] += f["fluxos"][m]
    # a franqueadora recebe o royalty da unidade propria
    for m in range(13, MESES + 1):
        rec = u["linhas"][m - 1]["receita"]
        fluxos[m] += (rec * ROYALTY + TEC) * (1 - TRIB_SERVICOS)

    acum, pico, zera, mpico = 0.0, 0.0, None, 0
    for m, x in enumerate(fluxos):
        acum += x
        if acum < pico:
            pico, mpico = acum, m
        if zera is None and m > 0 and acum >= 0:
            zera = m
    return dict(pico=pico, mes_pico=mpico, zera=zera, tir=tir_anual(fluxos),
                vpl=vpl(mensal(TMA), fluxos), fluxos=fluxos)
