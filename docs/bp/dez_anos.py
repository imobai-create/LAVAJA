# -*- coding: utf-8 -*-
"""Franqueadora em 10 anos + visão consolidada (unidade própria + franqueadora)."""
import sys, json, pathlib; sys.path.insert(0, "bp")
from modelo import FORMATOS, RAMPA, ROYALTY, TECNOLOGIA, tir, vpl, TMA_MES, TMA_ANUAL, unidade

MESES=120; IMPOSTO=0.16; REBATE=25_000; IMPLANTACAO=8_000; DEFASAGEM=4

# expansão: regional até o ano 5, depois sai da região (Sul de Minas, Triângulo, SP)
VENDAS_ANO = {2:3, 3:5, 4:6, 5:7, 6:8, 7:9, 8:10, 9:10, 10:10}   # total 68
FORMATO_ANO = {2:"EXPRESS",3:"EXPRESS",4:"EXPRESS",5:"EXPRESS",6:"EXPRESS",
               7:"EXPRESS",8:"EXPRESS",9:"EXPRESS",10:"EXPRESS"}
PRIME_A_CADA = 6   # 1 em cada 6 unidades é Prime

def custos(m, novas_inst, unidades):
    c = 2_000
    if 10 <= m <= 15: c += 180_000/6
    if m == 10: c += 6_000
    if m >= 10: c += 5_000
    if m >= 15: c += 11_000 + 8_000
    if m >= 18: c += 6_000
    if 18 <= m <= 29: c += 350_000/12
    # equipe de campo escala com a rede: 1 consultor a cada 12 unidades
    extra = max(0, (unidades // 12)) * 11_000
    c += extra
    if m >= 61: c += 12_000          # estrutura de expansão fora da região
    c += novas_inst * IMPLANTACAO
    return c

vendas={}; k=0
for ano, qtd in VENDAS_ANO.items():
    for i in range(qtd):
        k += 1
        fmt = "PRIME" if k % PRIME_A_CADA == 0 else FORMATO_ANO[ano]
        mes = (ano-1)*12 + 1 + int(i*(12/qtd))
        vendas.setdefault(mes, []).append(fmt)

inst_por_mes={}
for mm, lst in vendas.items():
    for f in lst: inst_por_mes.setdefault(mm+DEFASAGEM, []).append(f)

fluxos=[0.0]; linhas=[]; caixa=0.0; pico=0.0; instaladas=[]
for m in range(1, MESES+1):
    novas = vendas.get(m, [])
    taxas = sum(FORMATOS[f]["taxa"] for f in novas)
    agora = inst_por_mes.get(m, [])
    for f in agora: instaladas.append((m,f))
    rebates = len(agora)*REBATE
    roy = tech = 0.0
    for (mi,f) in instaladas:
        idade = m-mi
        rec = FORMATOS[f]["receita"]*RAMPA[min(idade,len(RAMPA)-1)]
        roy += rec*ROYALTY; tech += TECNOLOGIA
    receita = taxas+rebates+roy+tech
    ebitda = receita - receita*IMPOSTO - custos(m, len(agora), len(instaladas))
    fluxos.append(ebitda); caixa += ebitda; pico = min(pico, caixa)
    linhas.append(dict(mes=m, unidades=len(instaladas), receita=receita, ebitda=ebitda, caixa=caixa))

anos={a: dict(unidades=linhas[a*12-1]["unidades"],
              receita=sum(l["receita"] for l in linhas[(a-1)*12:a*12]),
              ebitda=sum(l["ebitda"] for l in linhas[(a-1)*12:a*12]),
              caixa=linhas[a*12-1]["caixa"]) for a in range(1,11)}

t=tir(fluxos); tir_a=((1+t)**12-1) if t else None
mes_zera = next((l["mes"] for l in linhas if l["caixa"]>=0), None)

print("="*86); print("FRANQUEADORA — 10 ANOS"); print("="*86)
print(f"  {'ano':>4} {'unid.':>6} {'receita':>14} {'EBITDA':>14} {'caixa acum.':>16}")
for a,v in anos.items():
    print(f"  {a:>4} {v['unidades']:>6} {v['receita']:>14,.0f} {v['ebitda']:>14,.0f} {v['caixa']:>16,.0f}")
print(f"\n  Pico de consumo de caixa      R$ {-pico:>14,.0f}")
print(f"  Caixa acumulado vira positivo no mês {mes_zera} (ano {mes_zera/12:.1f})" if mes_zera else "  Caixa não vira positivo em 10 anos")
print(f"  TIR da franqueadora (10 anos) {tir_a*100:>14.1f}% a.a.")
print(f"  VPL @ {TMA_ANUAL*100:.0f}% (10 anos)        R$ {vpl(fluxos,TMA_MES):>14,.0f}")

# ---------- consolidado: investidor financia unidade própria + franqueadora ----------
u = unidade("EXPRESS", FORMATOS["EXPRESS"], meses=MESES)
cons=[0.0]
for m in range(1, MESES+1):
    cons.append(u["fluxos"][m] + fluxos[m])
cons[0] = u["fluxos"][0]
tc=tir(cons); tc_a=((1+tc)**12-1) if tc else None
caixa=0; pico_c=0; zera=None
for i,f in enumerate(cons):
    caixa+=f; pico_c=min(pico_c,caixa)
    if zera is None and i>0 and caixa>=0: zera=i
print("\n"+"="*86); print("CONSOLIDADO — unidade própria (Express) + franqueadora"); print("="*86)
print(f"  Capital necessário (pico)     R$ {-pico_c:>14,.0f}")
print(f"  Caixa vira positivo no mês    {zera} (ano {zera/12:.1f})" if zera else "  não vira positivo")
print(f"  TIR consolidada (10 anos)     {tc_a*100:>14.1f}% a.a.")
print(f"  VPL @ {TMA_ANUAL*100:.0f}%                   R$ {vpl(cons,TMA_MES):>14,.0f}")

pathlib.Path("bp/dez_anos.json").write_text(json.dumps(
    dict(anos=anos, pico=pico, tir=tir_a, vpl=vpl(fluxos,TMA_MES), mes_zera=mes_zera,
         cons=dict(pico=pico_c, tir=tc_a, vpl=vpl(cons,TMA_MES), zera=zera)),
    indent=2, default=float), encoding="utf-8")
