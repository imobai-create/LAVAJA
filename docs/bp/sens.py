# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"bp")
from modelo import FORMATOS, unidade, TMA_ANUAL
import copy

print("SENSIBILIDADE — EXPRESS (receita madura)")
print(f"{'cenário':>14} {'receita/mês':>13} {'EBITDA/mês':>12} {'payback':>9} {'TIR a.a.':>10} {'VPL @18%':>13}")
base = FORMATOS["EXPRESS"]["receita"]
for rot, mult in [("-30%",0.70),("-20%",0.80),("-10%",0.90),("base",1.00),("+10%",1.10),("+20%",1.20)]:
    f = copy.deepcopy(FORMATOS["EXPRESS"])
    f["receita"] = base*mult
    # custo fixo NÃO escala com a receita: é o que torna o modelo sensível
    from modelo import fixos_calibrados, IMPOSTO_RECEITA, VARIAVEL, ROYALTY, FUNDO, TECNOLOGIA
    fixo_base = fixos_calibrados(FORMATOS["EXPRESS"])
    f["ebitda_plano"] = f["receita"]*(1-IMPOSTO_RECEITA-VARIAVEL-ROYALTY-FUNDO) - TECNOLOGIA - fixo_base
    u = unidade("EXPRESS", f)
    pb = f"{u['payback']}" if u['payback'] else ">60"
    tir = f"{u['tir_ano']*100:.1f}%" if u['tir_ano'] and u['tir_ano']>-0.99 else "neg."
    print(f"{rot:>14} {f['receita']:>13,.0f} {u['ebitda_maduro']:>12,.0f} {pb:>9} {tir:>10} {u['vpl']:>13,.0f}")

# ponto de equilíbrio: receita que zera o EBITDA
from modelo import IMPOSTO_RECEITA, VARIAVEL, ROYALTY, FUNDO, TECNOLOGIA, fixos_calibrados
fx = fixos_calibrados(FORMATOS["EXPRESS"])
be = (fx + TECNOLOGIA)/(1-IMPOSTO_RECEITA-VARIAVEL-ROYALTY-FUNDO)
print(f"\nPonto de equilíbrio (EBITDA zero): R$ {be:,.0f}/mês  =  {be/FORMATOS['EXPRESS']['receita']*100:.0f}% da receita madura")
print(f"Em lavagens a R$ 35: {be/35:,.0f}/mês  ≈ {be/35/30:,.0f}/dia")
print(f"Receita madura equivale a {FORMATOS['EXPRESS']['receita']/35:,.0f} lavagens/mês ≈ {FORMATOS['EXPRESS']['receita']/35/30:,.0f}/dia")
print(f"Ou, em assinantes a R$ 79: {FORMATOS['EXPRESS']['receita']/79:,.0f} assinantes")
