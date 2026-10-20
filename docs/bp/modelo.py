# -*- coding: utf-8 -*-
"""Modelo econômico — rede de lava jato automatizado por assinatura.
Reconstrução a partir dos números-resumo do Plano de Franquia (set/2026).
O plano cita um Excel que NÃO foi fornecido: esta é uma reconstrução transparente."""

MESES = 60                      # contrato de franquia: 5 anos
TMA_ANUAL = 0.18                # premissa — ajustar à Selic/CDI do fechamento
TMA_MES = (1 + TMA_ANUAL) ** (1/12) - 1

# ---- premissas comuns ao franqueado -------------------------------------
IMPOSTO_RECEITA = 0.11          # Simples Nacional, alíquota efetiva estimada
VARIAVEL = 0.22                 # água, energia, química, gateway, insumos
ROYALTY = 0.06
FUNDO = 0.02
TECNOLOGIA = 700.0              # R$/mês por unidade
CAPEX_MANUT = 0.015             # manutenção sobre receita
RESIDUAL = 0.35                 # valor residual do capex no mês 60

RAMPA = [0.35]*3 + [0.55]*3 + [0.75]*3 + [0.88]*3 + [1.00]*48

FORMATOS = {
    "BOX":     dict(taxa=35_000,  capex=155_000, giro=25_000, receita=19_000, ebitda_plano=5_000,  payback_plano=42),
    "EXPRESS": dict(taxa=50_000,  capex=326_000, giro=40_000, receita=48_000, ebitda_plano=15_600, payback_plano=29),
    "PRIME":   dict(taxa=60_000,  capex=600_000, giro=60_000, receita=75_000, ebitda_plano=24_800, payback_plano=31),
}

def fixos_calibrados(f):
    """Custo fixo mensal que reproduz o EBITDA maduro informado no plano."""
    r = f["receita"]
    return r*(1-IMPOSTO_RECEITA-VARIAVEL-ROYALTY-FUNDO) - TECNOLOGIA - f["ebitda_plano"]

def tir(fluxos, chute=0.01):
    """TIR por bissecção. fluxos[0] é negativo."""
    def vpl(t):
        return sum(f/((1+t)**i) for i, f in enumerate(fluxos))
    lo, hi = -0.99, 10.0
    if vpl(lo)*vpl(hi) > 0: return None
    for _ in range(300):
        m = (lo+hi)/2
        if vpl(lo)*vpl(m) <= 0: hi = m
        else: lo = m
    return (lo+hi)/2

def vpl(fluxos, taxa):
    return sum(f/((1+taxa)**i) for i, f in enumerate(fluxos))

def unidade(nome, f, meses=MESES):
    fixos = fixos_calibrados(f)
    inv = f["taxa"] + f["capex"] + f["giro"]
    fluxos = [-inv]
    linhas = []
    acum = -inv
    payback = None
    for m in range(1, meses+1):
        rec = f["receita"] * RAMPA[min(m-1, len(RAMPA)-1)]
        imp = rec*IMPOSTO_RECEITA
        var = rec*VARIAVEL
        roy = rec*ROYALTY
        fun = rec*FUNDO
        ebitda = rec - imp - var - roy - fun - TECNOLOGIA - fixos
        fcl = ebitda - rec*CAPEX_MANUT
        if m == meses:
            fcl += f["capex"]*RESIDUAL
        fluxos.append(fcl)
        acum += fcl
        if payback is None and acum >= 0:
            payback = m
        linhas.append(dict(mes=m, receita=rec, imposto=imp, variavel=var, royalty=roy,
                           fundo=fun, tecnologia=TECNOLOGIA, fixos=fixos, ebitda=ebitda,
                           fcl=fcl, acumulado=acum))
    t_mes = tir(fluxos)
    t_ano = (1+t_mes)**12 - 1 if t_mes else None
    ebitda_maduro = linhas[-1]["ebitda"]
    ebitda_ano_maduro = ebitda_maduro*12
    return dict(nome=nome, investimento=inv, fixos=fixos, fluxos=fluxos, linhas=linhas,
                payback=payback, tir_mes=t_mes, tir_ano=t_ano,
                vpl=vpl(fluxos, TMA_MES),
                ebitda_maduro=ebitda_maduro, ebitda_ano=ebitda_ano_maduro,
                margem=ebitda_maduro/f["receita"],
                roi_5a=sum(fluxos[1:])/inv,
                payback_capex=None)

print("="*78)
print("FRANQUEADO — por formato (horizonte 60 meses, TMA %.0f%% a.a.)" % (TMA_ANUAL*100))
print("="*78)
res = {}
for nome, f in FORMATOS.items():
    u = unidade(nome, f)
    res[nome] = u
    print(f"\n{nome}")
    print(f"  Investimento total          R$ {u['investimento']:>12,.0f}   (taxa {f['taxa']:,.0f} + capex {f['capex']:,.0f} + giro {f['giro']:,.0f})")
    print(f"  Custo fixo mensal calibrado R$ {u['fixos']:>12,.0f}")
    print(f"  EBITDA maduro               R$ {u['ebitda_maduro']:>12,.0f} /mês   (plano: {f['ebitda_plano']:,.0f})  margem {u['margem']*100:.1f}%")
    print(f"  EBITDA maduro anual         R$ {u['ebitda_ano']:>12,.0f}")
    print(f"  Payback (invest. total)     {u['payback']:>12} meses        (plano, s/ taxa e giro: {f['payback_plano']})")
    print(f"  TIR                         {u['tir_ano']*100:>12.1f}% a.a.")
    print(f"  VPL @ {TMA_ANUAL*100:.0f}%                 R$ {u['vpl']:>12,.0f}")
    print(f"  ROI 5 anos (caixa/invest.)  {u['roi_5a']*100:>12.0f}%")
