"""Sensibilidade e capacidade da loja modelo de Piumhi."""
import comum, piumhi
from comum import brl
from piumhi import CENARIOS, unidade, TMA, TMA_ALT, receita_e_lavagens, MIX, capex_total, GIRO

L = 92
CICLO_MIN = 6.5          # 5 min de lavagem + 1,5 min de manobra
DISPONIBILIDADE = 0.90   # manutencao, limpeza, falhas
JANELA_H = 13            # 7h as 20h, onde cai a maior parte da demanda
CONC_JANELA = 0.75       # fracao das lavagens que acontece nessa janela

cap_hora = 60 / CICLO_MIN * DISPONIBILIDADE
cap_janela_dia = cap_hora * JANELA_H
cap_dia_pratica = cap_janela_dia / CONC_JANELA

print("=" * L)
print("CAPACIDADE DA MAQUINA")
print("=" * L)
print(f"  Ciclo + manobra                     {CICLO_MIN:.1f} min")
print(f"  Capacidade bruta                    {60/CICLO_MIN:.1f} carros/hora")
print(f"  Com {DISPONIBILIDADE*100:.0f}% de disponibilidade          {cap_hora:.1f} carros/hora")
print(f"  Janela 7h-20h ({JANELA_H} h)                {cap_janela_dia:.0f} lavagens")
print(f"  Teto pratico/dia ({CONC_JANELA*100:.0f}% na janela)     {cap_dia_pratica:.0f} lavagens/dia")
print(f"  Teto de receita com 1 maquina       ~R$ {brl(cap_dia_pratica*30*(54_100/2865))}/mes\n")
for nome, cen in CENARIOS.items():
    _, lav = receita_e_lavagens(cen["assinantes"], cen["avulsas_dia"], cen["compl"])
    d = lav / 30
    print(f"  {nome:<13} {d:>5.0f} lavagens/dia   "
          f"{d/cap_dia_pratica*100:>5.0f}% do teto pratico"
          f"{'   <-- fila no horario de pico' if d/cap_dia_pratica > 0.85 else ''}")

print("\n" + "=" * L)
print("QUANTOS ASSINANTES PARA BATER A TMA")
print("=" * L)
for tma in (0.18, 0.22):
    alvo = None
    for n in range(200, 800, 5):
        cen = dict(assinantes=n, avulsas_dia=8, compl=2_200)
        if unidade(cen, tma=tma)["vpl"] > 0:
            alvo = n
            break
    pen = alvo / piumhi.FROTA_AUTOMOVEIS_PIUMHI
    print(f"  TMA {tma*100:.0f}% a.a.  ->  {alvo} assinantes "
          f"({pen*100:.1f}% dos automoveis de Piumhi) para VPL = 0")

print("\n" + "=" * L)
print("SENSIBILIDADE - uso do plano Ilimitada (lavagens/mes por assinante)")
print("=" * L)
print(f"  {'uso':>5} {'receita/mes':>13} {'lav/dia':>9} {'CV/mes':>11} "
      f"{'EBITDA/mes':>12} {'TIR':>8} {'VPL@18%':>12}")
orig = MIX["Ilimitada"]["lav_mes"]
for uso in (4, 5, 6, 8, 10, 12):
    MIX["Ilimitada"]["lav_mes"] = float(uso)
    MIX["Premium"]["lav_mes"] = float(uso) + 1
    r = unidade(CENARIOS["Base"])
    m = r["maduro"]
    print(f"  {uso:>5} {brl(m['receita']):>13} {m['lavagens']/30:>9.0f} "
          f"{brl(m['var']):>11} {brl(m['ebitda']):>12} "
          f"{r['tir']*100:>7.1f}% {brl(r['vpl']):>12}")
MIX["Ilimitada"]["lav_mes"] = orig
MIX["Premium"]["lav_mes"] = 7.0

print("\n" + "=" * L)
print("SENSIBILIDADE - variaveis de uma linha so (cenario Base)")
print("=" * L)
base = unidade(CENARIOS["Base"])
print(f"  {'cenario':<44} {'EBITDA/mes':>12} {'TIR':>8} {'VPL@18%':>12}")
print(f"  {'BASE':<44} {brl(base['maduro']['ebitda']):>12} "
      f"{base['tir']*100:>7.1f}% {brl(base['vpl']):>12}")

def linha(rot, **kw):
    r = unidade(CENARIOS["Base"], **kw)
    print(f"  {rot:<44} {brl(r['maduro']['ebitda']):>12} "
          f"{r['tir']*100:>7.1f}% {brl(r['vpl']):>12}")

linha("Receita -15%", escala_receita=0.85)
linha("Receita -25%", escala_receita=0.75)
linha("Aluguel R$ 5.000 em vez de R$ 3.000", aluguel_extra=2_000)
linha("Simples no Anexo V (Fator R < 28%)", tabela_simples=comum.ANEXO_V)
cap_base = capex_total()[2]
linha("Capex +20% (cambio/obra estourando)", capex_override=cap_base*1.20)
linha("Versao enxuta: capex R$ 328 mil", capex_override=328_000, giro_override=45_000)
linha("Ja pagando royalty 6% + fundo 2% + tec",
      royalty=0.06, fundo=0.02, tecnologia=700)

print("\n" + "=" * L)
print("E SE A UNIDADE FOSSE FRANQUEADA (paga taxa, royalty, fundo e tecnologia)")
print("=" * L)
r = unidade(CENARIOS["Base"], royalty=0.06, fundo=0.02, tecnologia=700,
            taxa_franquia=50_000)
m = r["maduro"]
print(f"  Investimento (com taxa de R$ 50 mil)  R$ {brl(r['investimento'])}")
print(f"  EBITDA maduro/mes                     R$ {brl(m['ebitda'])} "
      f"(margem {m['ebitda']/m['receita']*100:.1f}%)")
print(f"  Payback                               {r['payback']} meses")
print(f"  TIR                                   {r['tir']*100:.1f}% a.a.")
print(f"  VPL @ 18%                             R$ {brl(r['vpl'])}")
print(f"\n  Diferenca de EBITDA que a propria unidade captura por nao ser franqueada:")
print(f"  R$ {brl(base['maduro']['ebitda'] - m['ebitda'])}/mes")
