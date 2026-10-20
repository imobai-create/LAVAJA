# -*- coding: utf-8 -*-
"""Modelo da franqueadora — 60 meses."""
import sys; sys.path.insert(0, "bp")
from modelo import (FORMATOS, RAMPA, ROYALTY, TECNOLOGIA, tir, vpl, TMA_MES, TMA_ANUAL, unidade)

MESES = 60
IMPOSTO_FRANQ = 0.16        # premissa sobre receita (royalties, taxas, rebate)
REBATE = 25_000             # por unidade instalada, pago pelo fabricante
IMPLANTACAO = 8_000         # custo de obra assistida/treinamento por unidade
DEFASAGEM = 4               # meses entre venda (taxa) e instalação (royalty começa)

CENARIOS = {
    # ano: lista de formatos vendidos naquele ano
    "A — plano original (com BOX)": {
        2: ["EXPRESS"]*3,
        3: ["EXPRESS"]*4 + ["BOX"]*2,
        4: ["EXPRESS"]*4 + ["BOX"]*2 + ["PRIME"],
        5: ["EXPRESS"]*5 + ["BOX"]*2 + ["PRIME"],
    },
    "B — recomendado (sem BOX)": {
        2: ["EXPRESS"]*3,
        3: ["EXPRESS"]*5,
        4: ["EXPRESS"]*5 + ["PRIME"],
        5: ["EXPRESS"]*6 + ["PRIME"],
    },
}

def custos_mes(m, unidades_instaladas_no_mes):
    c = 0.0
    c += 2_000                                     # white-label de assinatura
    if 10 <= m <= 15: c += 180_000/6               # formatação: COF, contrato, manuais
    if m == 10: c += 6_000                         # INPI, classes 35 e 37
    if m >= 10: c += 5_000                         # overhead: contabilidade, jurídico, software
    if m >= 15: c += 11_000 + 8_000                # consultor de campo + marketing de expansão
    if m >= 18: c += 6_000                         # suporte/administrativo
    if 18 <= m <= 29: c += 350_000/12              # app próprio
    if m >= 36: c += 11_000                        # segundo consultor de campo
    c += unidades_instaladas_no_mes * IMPLANTACAO
    return c

def rodar(nome, plano):
    vendas = {}                                     # mês -> [formatos]
    for ano, lista in plano.items():
        for i, fmt in enumerate(lista):
            mes = (ano-1)*12 + 1 + int(i * (12/max(len(lista),1)))
            vendas.setdefault(mes, []).append(fmt)

    fluxos, linhas, caixa, pico = [0.0], [], 0.0, 0.0
    instaladas = []                                 # (mes_instalacao, formato)
    for m in range(1, MESES+1):
        novas = vendas.get(m, [])
        taxas = sum(FORMATOS[f]["taxa"] for f in novas)
        inst_agora = [f for (mi, f) in [(mm+DEFASAGEM, ff) for mm, lst in vendas.items() for ff in lst] if mi == m]
        rebates = len(inst_agora) * REBATE
        for f in inst_agora: instaladas.append((m, f))

        royalties = tech = 0.0
        for (mi, f) in instaladas:
            idade = m - mi
            if idade < 0: continue
            rec = FORMATOS[f]["receita"] * RAMPA[min(idade, len(RAMPA)-1)]
            royalties += rec * ROYALTY
            tech += TECNOLOGIA
        receita = taxas + rebates + royalties + tech
        imposto = receita * IMPOSTO_FRANQ
        custo = custos_mes(m, len(inst_agora))
        ebitda = receita - imposto - custo
        fluxos.append(ebitda); caixa += ebitda; pico = min(pico, caixa)
        linhas.append(dict(mes=m, vendas=len(novas), instaladas=len(instaladas),
                           taxas=taxas, rebates=rebates, royalties=royalties, tech=tech,
                           receita=receita, imposto=imposto, custo=custo,
                           ebitda=ebitda, caixa=caixa))
    anos = {}
    for a in range(1, 6):
        bloco = linhas[(a-1)*12:a*12]
        anos[a] = dict(receita=sum(l["receita"] for l in bloco),
                       ebitda=sum(l["ebitda"] for l in bloco),
                       unidades=bloco[-1]["instaladas"])
    t = tir([f for f in fluxos])
    return dict(nome=nome, linhas=linhas, anos=anos, pico=pico, caixa_final=caixa,
                tir_ano=((1+t)**12-1) if t else None, vpl=vpl(fluxos, TMA_MES), fluxos=fluxos)

print("="*78); print("FRANQUEADORA — 60 meses"); print("="*78)
saida = {}
for nome, plano in CENARIOS.items():
    r = rodar(nome, plano); saida[nome] = r
    print(f"\n{nome}")
    print(f"  {'ano':>4} {'unid.':>6} {'receita':>14} {'EBITDA':>14}")
    for a, v in r["anos"].items():
        print(f"  {a:>4} {v['unidades']:>6} {v['receita']:>14,.0f} {v['ebitda']:>14,.0f}")
    print(f"  Pico de consumo de caixa    R$ {-r['pico']:>12,.0f}   (plano: ~720.000)")
    print(f"  Caixa acumulado no mês 60   R$ {r['caixa_final']:>12,.0f}")
    print(f"  TIR da franqueadora         {r['tir_ano']*100 if r['tir_ano'] else 0:>12.1f}% a.a.")
    print(f"  VPL @ {TMA_ANUAL*100:.0f}%                 R$ {r['vpl']:>12,.0f}")

import json, pathlib
pathlib.Path("bp/saida.json").write_text(json.dumps({
    "franqueadora": {k: {"anos": v["anos"], "pico": v["pico"], "caixa_final": v["caixa_final"],
                         "tir": v["tir_ano"], "vpl": v["vpl"]} for k, v in saida.items()}
}, indent=2, default=float), encoding="utf-8")
print("\nsaida.json gravado")
