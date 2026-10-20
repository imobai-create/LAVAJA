"""Qual aluguel fecha a conta dos dois lados? E compensa comprar o terreno de Piumhi?"""
import comum, rede
from comum import brl, vpl, tir_anual, mensal
from rede import rede as modelo_rede, franqueado, cronograma, receita_unidade
import rede as R

L = 92
print("=" * L)
print("1. QUAL ALUGUEL O FRANQUEADO AINDA SUPORTA?  (investimento de R$ 310 mil)")
print("=" * L)
print(f"  {'aluguel':>10} {'EBITDA/mes':>13} {'margem':>9} {'payback':>10} {'TIR':>8} {'VPL@18%':>13}")
orig_b1 = R.ALUGUEL_B1
for al in (3_000, 3_500, 4_000, 4_500, 5_000, 5_500, 6_000, 6_500):
    R.ALUGUEL_B1 = float(al)
    f = franqueado("B1")
    marca = "  <-- limite para TIR >= 18%" if 0.175 <= f["tir"] < 0.195 else ""
    print(f"  {brl(al):>10} {brl(f['ebitda']):>13} {f['margem']*100:>8.1f}% "
          f"{str(f['payback'])+'m':>10} {f['tir']*100:>7.1f}% {brl(f['vpl']):>13}{marca}")
R.ALUGUEL_B1 = orig_b1

print("\n" + "=" * L)
print("2. QUAL ALUGUEL A FRANQUEADORA PRECISARIA PARA O IMOVEL PAGAR 18% a.a.?")
print("=" * L)
print(f"  {'aluguel':>10} {'TIR B1':>10} {'VPL B1 @18%':>15}   (65 unidades, sem divida)")
for al in (4_000, 5_000, 6_000, 7_000, 8_000, 9_000, 10_000):
    R.ALUGUEL_B1 = float(al)
    r = modelo_rede(estrutura="B1")
    t = f"{r['tir']*100:.1f}%" if r["tir"] else "negativa"
    print(f"  {brl(al):>10} {t:>10} {brl(r['vpl']):>15}")
R.ALUGUEL_B1 = orig_b1

print("\n  Yield do imovel isolado (R$ 500 mil por ponto):")
for al in (4_000, 5_000, 6_000, 7_000):
    liq = (al * (1 - R.TRIB_ALUGUEL) - R.CUSTO_IMOVEL_B1) * 12
    print(f"    aluguel {brl(al)}/mes  ->  {liq/500_000*100:.1f}% a.a. de caixa "
          f"+ ~4,5% de valorizacao do terreno = {liq/500_000*100+4.5*280/500:.1f}% total")

print("\n" + "=" * L)
print("3. PIUMHI: COMPRAR O TERRENO OU ALUGAR A R$ 3.000?")
print("=" * L)
TERRENO_PIUMHI = 280_000.0
ALUG = 3_000.0
VALOR_IPCA = 0.045
for horizonte in (60, 120):
    # alugar: paga aluguel todo mes, nada no fim
    f_alug = [0.0] + [-ALUG] * horizonte
    # comprar: desembolsa o terreno, nao paga aluguel, vende no fim
    f_comp = [-TERRENO_PIUMHI] + [0.0] * horizonte
    f_comp[horizonte] += TERRENO_PIUMHI * (1 + VALOR_IPCA) ** (horizonte / 12)
    # diferenca (comprar - alugar): investe o terreno e "recebe" o aluguel economizado
    dif = [c - a for c, a in zip(f_comp, f_alug)]
    t = tir_anual(dif)
    for tma in (0.14, 0.18):
        v = vpl(mensal(tma), dif)
        print(f"  {horizonte} meses | TIR de comprar em vez de alugar: "
          f"{t*100:>5.1f}% a.a. | VPL @ {tma*100:.0f}%: {brl(v):>12}")
print(f"\n  Leitura: com a Selic a 14% a.a., comprar o terreno rende menos que o")
print(f"  dinheiro parado em renda fixa. Alugar e manter OPCAO DE COMPRA a preco")
print(f"  travado hoje custa zero e preserva o upside se o juro cair.")

print("\n" + "=" * L)
print("4. QUANTO DO CAPEX DE PIUMHI FICA NO IMOVEL DE TERCEIRO")
print("=" * L)
import piumhi
cap = piumhi.capex_total()[2]
print(f"  Capex total                        R$ {brl(cap)}")
print(f"  Benfeitoria (obra, separadora, energia) R$ {brl(piumhi.BENFEITORIA)} "
      f"= {piumhi.BENFEITORIA/cap*100:.0f}%")
print(f"  Equipamento que sai no caminhao    R$ {brl(cap - piumhi.BENFEITORIA)} "
      f"= {(cap-piumhi.BENFEITORIA)/cap*100:.0f}%")
print(f"\n  Em 5 anos de aluguel a R$ 3.000 pagamos R$ {brl(ALUG*60)} ao proprietario")
print(f"  e deixamos R$ {brl(piumhi.BENFEITORIA)} de benfeitoria no terreno dele.")
