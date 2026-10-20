"""
Gera as duas planilhas do business plan, com formulas vivas.

  Modelo-Economico-Piumhi.xlsx   Fase 1 - loja modelo
  Modelo-Economico-Rede.xlsx     Fase 2 - franqueado e franqueadora

Toda linha mensal e formula apontando para a aba Premissas. TIR, VPL e payback
sao IRR, NPV e MATCH de verdade: mudar uma premissa recalcula tudo.

Uso:  python3 planilha.py          (precisa de openpyxl)
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

import piumhi as P
import rede as R

AZUL = "0E63A8"
ESCURO = "0E2231"
CLARO = "EFF3F6"
OCRE = "F6EDDC"

h1 = Font(bold=True, size=14, color="FFFFFF")
hcab = Font(bold=True, size=10, color="FFFFFF")
bold = Font(bold=True)
fill_tit = PatternFill("solid", fgColor=ESCURO)
fill_cab = PatternFill("solid", fgColor=AZUL)
fill_in = PatternFill("solid", fgColor=OCRE)      # celula de entrada (editavel)
fill_out = PatternFill("solid", fgColor=CLARO)
borda = Border(bottom=Side(style="thin", color="C8D2DA"))

MOEDA = 'R$ #,##0'
MOEDA2 = 'R$ #,##0.00'
PCT = '0.0%'
PCT2 = '0.00%'
NUM = '#,##0'


def titulo(ws, texto, linha=1, span=8):
    ws.cell(linha, 1, texto).font = h1
    for c in range(1, span + 1):
        ws.cell(linha, c).fill = fill_tit
    ws.row_dimensions[linha].height = 22
    return linha + 2


def cabecalho(ws, linha, rotulos, largura=None):
    for i, r in enumerate(rotulos, start=1):
        c = ws.cell(linha, i, r)
        c.font = hcab
        c.fill = fill_cab
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    ws.row_dimensions[linha].height = 30
    if largura:
        for i, w in enumerate(largura, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    return linha + 1


def entrada(ws, linha, rotulo, valor, fmt=MOEDA, nota=""):
    ws.cell(linha, 1, rotulo)
    c = ws.cell(linha, 2, valor)
    c.fill = fill_in
    c.number_format = fmt
    c.font = bold
    if nota:
        ws.cell(linha, 3, nota).font = Font(italic=True, size=9, color="6B7F93")
    ws.cell(linha, 1).border = borda
    return linha + 1


# aliquota efetiva do Simples, Anexo III, como formula.
# `ref` pode ser uma expressao (ex.: "C4*12"), por isso vai sempre entre parenteses:
# sem isso, (ref*0.135-17640)/ref*12 e lido como ((...)/C4)*12.
def f_simples(ref):
    r = f"({ref})"
    return (f'=IF({r}<=0,0.06,'
            f'IF({r}<=180000,0.06,'
            f'IF({r}<=360000,({r}*0.112-9360)/{r},'
            f'IF({r}<=720000,({r}*0.135-17640)/{r},'
            f'IF({r}<=1800000,({r}*0.16-35640)/{r},0.165)))))')


# ============================================================ PLANILHA 1
def planilha_piumhi(caminho):
    wb = Workbook()

    # -------------------------------------------------- Premissas
    ws = wb.active
    ws.title = "Premissas"
    ln = titulo(ws, "FASE 1 - LOJA MODELO PIUMHI/MG  |  premissas", span=4)
    ws.column_dimensions["A"].width = 52
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 56

    ws.cell(ln, 1, "As celulas em bege sao as unicas para editar. "
                   "Tudo o mais e formula.").font = Font(italic=True, color="8A5F16")
    ln += 2

    ws.cell(ln, 1, "DEMANDA").font = bold; ln += 1
    L = {}
    L["assinantes"] = ln; ln = entrada(ws, ln, "Assinantes no estado maduro", 500, NUM,
                                       "Conservador 380 | Base 500 | Otimista 650")
    L["avulsas"] = ln; ln = entrada(ws, ln, "Lavagens avulsas por dia", 8, NUM)
    L["compl"] = ln; ln = entrada(ws, ln, "Receita complementar/mes (box, aspirador)", 2200)
    L["inicial"] = ln; ln = entrada(ws, ln, "Assinantes na abertura (fundadores)", 80, NUM)
    L["k"] = ln; ln = entrada(ws, ln, "Velocidade da rampa (k)", 0.33, '0.00',
                              "maior = rampa mais rapida")
    L["mmeio"] = ln; ln = entrada(ws, ln, "Mes de meia-rampa", 8, NUM)
    L["frota"] = ln; ln = entrada(ws, ln, "Automoveis em Piumhi (Senatran 2024)", 13652, NUM,
                                  "CONFIRMAR na planilha do Senatran")
    ln += 1

    ws.cell(ln, 1, "PRECOS E MIX").font = bold; ln += 1
    L["p_ess"] = ln; ln = entrada(ws, ln, "Essencial - preco/mes", 59, MOEDA2)
    L["l_ess"] = ln; ln = entrada(ws, ln, "Essencial - lavagens/mes", 4, '0.0')
    L["s_ess"] = ln; ln = entrada(ws, ln, "Essencial - participacao no mix", 0.45, PCT)
    L["p_ili"] = ln; ln = entrada(ws, ln, "Ilimitada - preco/mes", 99, MOEDA2)
    L["l_ili"] = ln; ln = entrada(ws, ln, "Ilimitada - lavagens/mes por assinante", 6, '0.0',
                                  "a premissa mais sensivel do modelo")
    L["s_ili"] = ln; ln = entrada(ws, ln, "Ilimitada - participacao no mix", 0.40, PCT)
    L["p_pre"] = ln; ln = entrada(ws, ln, "Premium - preco/mes", 139, MOEDA2)
    L["l_pre"] = ln; ln = entrada(ws, ln, "Premium - lavagens/mes por assinante", 7, '0.0')
    L["s_pre"] = ln; ln = entrada(ws, ln, "Premium - participacao no mix", 0.15, PCT)
    L["p_avu"] = ln; ln = entrada(ws, ln, "Lavagem avulsa", 35, MOEDA2)
    ln += 1

    ws.cell(ln, 1, "CUSTO VARIAVEL").font = bold; ln += 1
    L["agua_l"] = ln; ln = entrada(ws, ln, "Agua por lavagem (litros)", 85, NUM)
    L["tar_agua"] = ln; ln = entrada(ws, ln, "Tarifa de agua + esgoto (R$/m3)", 14.00, MOEDA2,
                                     "ESTIMATIVA - confirmar com SAAE Piumhi")
    L["kwh"] = ln; ln = entrada(ws, ln, "Energia por lavagem (kWh)", 1.6, '0.00',
                                "calculo proprio; fornecedor declara 0,6-1,2")
    L["tar_kwh"] = ln; ln = entrada(ws, ln, "Tarifa de energia (R$/kWh)", 0.98, MOEDA2,
                                    "ESTIMATIVA - confirmar com CEMIG")
    L["quim"] = ln; ln = entrada(ws, ln, "Quimicos por lavagem", 2.50, MOEDA2)
    L["meios"] = ln; ln = entrada(ws, ln, "Meios de pagamento (% da receita)", 0.015, PCT2)
    L["cv"] = ln
    ws.cell(ln, 1, "CUSTO VARIAVEL POR LAVAGEM").font = bold
    c = ws.cell(ln, 2, f"=B{L['agua_l']}/1000*B{L['tar_agua']}+B{L['kwh']}*B{L['tar_kwh']}"
                       f"+B{L['quim']}")
    c.number_format = MOEDA2; c.font = bold; c.fill = fill_out
    ln += 2

    ws.cell(ln, 1, "CUSTO FIXO MENSAL").font = bold; ln += 1
    prim_fixo = ln
    for nome, v in P.FIXOS:
        ln = entrada(ws, ln, nome.replace("  ", " "), v)
    ult_fixo = ln - 1
    L["fixo"] = ln
    ws.cell(ln, 1, "TOTAL FIXO").font = bold
    c = ws.cell(ln, 2, f"=SUM(B{prim_fixo}:B{ult_fixo})")
    c.number_format = MOEDA; c.font = bold; c.fill = fill_out
    ln += 2

    ws.cell(ln, 1, "CAPEX DE IMPLANTACAO").font = bold; ln += 1
    L["cambio"] = ln; ln = entrada(ws, ln, "Cambio de planejamento (R$/USD)", P.CAMBIO, MOEDA2,
                                   "Focus fim-2026: 5,20")
    prim_cap = ln
    for nome, v in P.CAPEX:
        ln = entrada(ws, ln, nome, round(v, 2))
    ult_cap = ln - 1
    L["sub_cap"] = ln
    ws.cell(ln, 1, "Subtotal")
    c = ws.cell(ln, 2, f"=SUM(B{prim_cap}:B{ult_cap})"); c.number_format = MOEDA; c.font = bold
    ln += 1
    L["cont"] = ln; ln = entrada(ws, ln, "Contingencia (%)", P.CONTINGENCIA, PCT)
    L["capex"] = ln
    ws.cell(ln, 1, "CAPEX TOTAL").font = bold
    c = ws.cell(ln, 2, f"=B{L['sub_cap']}*(1+B{L['cont']})")
    c.number_format = MOEDA; c.font = bold; c.fill = fill_out
    ln += 1
    L["benf"] = ln
    ws.cell(ln, 1, "do qual benfeitoria em imovel de terceiro")
    c = ws.cell(ln, 2, f"=B{prim_cap+2}+B{prim_cap+3}+B{prim_cap+4}")
    c.number_format = MOEDA
    ws.cell(ln, 3, "obra civil + separadora + entrada de energia").font = Font(
        italic=True, size=9, color="6B7F93")
    ln += 2

    ws.cell(ln, 1, "CAPITAL DE GIRO").font = bold; ln += 1
    prim_giro = ln
    for nome, v in P.GIRO:
        ln = entrada(ws, ln, nome, v)
    ult_giro = ln - 1
    L["giro"] = ln
    ws.cell(ln, 1, "TOTAL GIRO").font = bold
    c = ws.cell(ln, 2, f"=SUM(B{prim_giro}:B{ult_giro})")
    c.number_format = MOEDA; c.font = bold; c.fill = fill_out
    ln += 1
    L["invest"] = ln
    ws.cell(ln, 1, "INVESTIMENTO TOTAL").font = Font(bold=True, size=12)
    c = ws.cell(ln, 2, f"=B{L['capex']}+B{L['giro']}")
    c.number_format = MOEDA; c.font = Font(bold=True, size=12); c.fill = fill_in
    ln += 2

    ws.cell(ln, 1, "FINANCEIRO").font = bold; ln += 1
    L["tma"] = ln; ln = entrada(ws, ln, "TMA (a.a.)", P.TMA, PCT,
                                "Selic em ago/2026: 14% a.a.")
    L["cap_man"] = ln; ln = entrada(ws, ln, "Capex de manutencao (% da receita)",
                                    P.CAPEX_MANUT, PCT)
    L["resid"] = ln; ln = entrada(ws, ln, "Valor residual do capex no mes 60", P.RESIDUAL, PCT)
    ln += 1

    ws.cell(ln, 1, "CAPACIDADE").font = bold; ln += 1
    L["ciclo"] = ln; ln = entrada(ws, ln, "Ciclo + manobra (min)", 6.5, '0.0')
    L["disp"] = ln; ln = entrada(ws, ln, "Disponibilidade da maquina", 0.90, PCT)
    L["janela"] = ln; ln = entrada(ws, ln, "Janela diaria de pico (horas)", 13, NUM)
    L["conc"] = ln; ln = entrada(ws, ln, "Lavagens na janela de pico", 0.75, PCT)

    # -------------------------------------------------- Fluxo
    fx = wb.create_sheet("Fluxo")
    ln = titulo(fx, "FASE 1 - fluxo de caixa mensal, 60 meses", span=14)
    cols = ["Mes", "Assinantes", "% da frota", "Receita assin.", "Receita avulsa",
            "Complementar", "Receita total", "Lavagens/mes", "Lavagens/dia",
            "RBT12", "Aliq. Simples", "Imposto", "Custo variavel", "Custo fixo",
            "EBITDA", "Margem", "Capex manut.", "Fluxo livre", "Caixa acumulado"]
    cab = cabecalho(fx, ln, cols,
                    largura=[6, 11, 10, 14, 13, 13, 14, 12, 11, 14, 12, 13, 14, 12,
                             14, 9, 12, 14, 16])
    p = "Premissas!$B$"
    r0 = cab                      # r0 = mes 0 (so o desembolso); meses 1..60 em r0+1..r0+60
    fx.cell(r0, 1, 0)
    fx.cell(r0, 18, f"=-{p}{L['invest']}").number_format = MOEDA
    fx.cell(r0, 19, f"=R{r0}").number_format = MOEDA
    for c in (18, 19):
        fx.cell(r0, c).font = bold
    for m in range(1, 61):
        r = r0 + m
        fx.cell(r, 1, m)
        # assinantes: curva logistica, piso nos fundadores, teto no maduro
        fx.cell(r, 2, f"=MIN({p}{L['assinantes']},MAX({p}{L['inicial']},"
                      f"{p}{L['assinantes']}/(1+EXP(-{p}{L['k']}*(A{r}-{p}{L['mmeio']})))))"
                ).number_format = NUM
        fx.cell(r, 3, f"=B{r}/{p}{L['frota']}").number_format = PCT
        # rampa das avulsas e complementares
        ramp = f"MIN(1,0.45+0.55*A{r}/12)"
        fx.cell(r, 4, f"=B{r}*({p}{L['s_ess']}*{p}{L['p_ess']}+{p}{L['s_ili']}*{p}{L['p_ili']}"
                      f"+{p}{L['s_pre']}*{p}{L['p_pre']})").number_format = MOEDA
        fx.cell(r, 5, f"={p}{L['avulsas']}*30*{p}{L['p_avu']}*{ramp}").number_format = MOEDA
        fx.cell(r, 6, f"={p}{L['compl']}*{ramp}").number_format = MOEDA
        fx.cell(r, 7, f"=D{r}+E{r}+F{r}").number_format = MOEDA
        fx.cell(r, 8, f"=B{r}*({p}{L['s_ess']}*{p}{L['l_ess']}+{p}{L['s_ili']}*{p}{L['l_ili']}"
                      f"+{p}{L['s_pre']}*{p}{L['l_pre']})+{p}{L['avulsas']}*30*{ramp}"
                ).number_format = NUM
        fx.cell(r, 9, f"=H{r}/30").number_format = NUM
        # RBT12: soma dos ultimos 12 meses, anualizada enquanto nao houver 12
        ini = max(r0 + 1, r - 11)
        n = r - ini + 1
        fx.cell(r, 10, f"=SUM(G{ini}:G{r})*12/{n}").number_format = MOEDA
        fx.cell(r, 11, f_simples(f"J{r}")).number_format = PCT
        fx.cell(r, 12, f"=G{r}*K{r}").number_format = MOEDA
        fx.cell(r, 13, f"=H{r}*{p}{L['cv']}+G{r}*{p}{L['meios']}").number_format = MOEDA
        fx.cell(r, 14, f"={p}{L['fixo']}").number_format = MOEDA
        fx.cell(r, 15, f"=G{r}-L{r}-M{r}-N{r}").number_format = MOEDA
        fx.cell(r, 16, f"=IF(G{r}=0,0,O{r}/G{r})").number_format = PCT
        fx.cell(r, 17, f"=G{r}*{p}{L['cap_man']}").number_format = MOEDA
        if m == 60:
            fx.cell(r, 18, f"=O{r}-Q{r}+{p}{L['capex']}*{p}{L['resid']}").number_format = MOEDA
        else:
            fx.cell(r, 18, f"=O{r}-Q{r}").number_format = MOEDA
        fx.cell(r, 19, f"=S{r-1}+R{r}").number_format = MOEDA
    fx.freeze_panes = f"A{cab}"

    # -------------------------------------------------- Resumo
    rs = wb.create_sheet("Resumo", 1)
    ln = titulo(rs, "FASE 1 - resumo", span=4)
    rs.column_dimensions["A"].width = 46
    rs.column_dimensions["B"].width = 18
    rs.column_dimensions["C"].width = 54

    def item(linha, rot, formula, fmt=MOEDA, nota="", destaque=False):
        rs.cell(linha, 1, rot).border = borda
        c = rs.cell(linha, 2, formula)
        c.number_format = fmt
        if destaque:
            c.font = Font(bold=True, size=12)
            c.fill = fill_in
        if nota:
            rs.cell(linha, 3, nota).font = Font(italic=True, size=9, color="6B7F93")
        return linha + 1

    MAD = r0 + 60                 # linha do mes 60 (estado maduro)
    f60 = f"Fluxo!$R${r0}:$R${MAD}"           # inclui o mes 0
    f1_60 = f"Fluxo!$R${r0+1}:$R${MAD}"       # meses 1 a 60
    ln = item(ln, "Investimento total", f"={p}{L['invest']}", destaque=True)
    ln = item(ln, "  capex de implantacao", f"={p}{L['capex']}")
    ln = item(ln, "  capital de giro", f"={p}{L['giro']}")
    ln = item(ln, "  benfeitoria em imovel de terceiro", f"={p}{L['benf']}",
              nota="fica no terreno do locador se o contrato nao for renovado")
    ln += 1
    ln = item(ln, "Receita madura/mes", f"=Fluxo!G{MAD}")
    ln = item(ln, "Lavagens/dia no estado maduro", f"=Fluxo!I{MAD}", NUM)
    ln = item(ln, "EBITDA maduro/mes", f"=Fluxo!O{MAD}", destaque=True)
    ln = item(ln, "Margem EBITDA madura", f"=Fluxo!P{MAD}", PCT)
    ln += 1
    ln = item(ln, "TIR anual", f'=IFERROR((1+IRR({f60},0.02))^12-1,"nao converge")', PCT,
              nota="TIR mensal capitalizada para o ano", destaque=True)
    ln = item(ln, "VPL na TMA",
              f"=NPV((1+{p}{L['tma']})^(1/12)-1,{f1_60})+Fluxo!$R${r0}", MOEDA,
              destaque=True)
    ln = item(ln, "Payback (mes em que o caixa zera)",
              f'=IFERROR(MATCH(TRUE,INDEX(Fluxo!$S${r0+1}:$S${MAD}>=0,0),0),"nao paga")',
              NUM, destaque=True)
    ln = item(ln, "ROI 5 anos (caixa gerado / investimento)",
              f"=SUM({f1_60})/{p}{L['invest']}", PCT)
    ln += 1
    rs.cell(ln, 1, "PONTO DE EQUILIBRIO").font = bold; ln += 1
    ln = item(ln, "Custo variavel relativo (maduro)",
              f"=Fluxo!M{MAD}/Fluxo!G{MAD}", PCT)
    eqrow = ln
    ln = item(ln, "Receita de equilibrio/mes",
              f"={p}{L['fixo']}/(1-Fluxo!K{MAD}-Fluxo!M{MAD}/Fluxo!G{MAD})")
    ln = item(ln, "  como % da receita madura", f"=B{eqrow}/Fluxo!G{MAD}", PCT)
    ln = item(ln, "  assinantes equivalentes",
              f"=B{eqrow}/Fluxo!G{MAD}*{p}{L['assinantes']}", NUM)
    ln += 1
    rs.cell(ln, 1, "CAPACIDADE DA MAQUINA").font = bold; ln += 1
    caprow = ln
    ln = item(ln, "Teto pratico (lavagens/dia)",
              f"=60/{p}{L['ciclo']}*{p}{L['disp']}*{p}{L['janela']}/{p}{L['conc']}", NUM)
    ln = item(ln, "Uso no estado maduro", f"=Fluxo!I{MAD}/B{caprow}", PCT,
              nota="acima de 85% a fila aparece no horario de pico")
    ln += 1
    rs.cell(ln, 1, "A aba Fluxo comeca no mes 0, que carrega o investimento. "
                   "IRR, NPV e payback incluem esse desembolso.").font = Font(
        italic=True, size=9, color="6B7F93")
    wb.save(caminho)
    return caminho


# ============================================================ PLANILHA 2
def planilha_rede(caminho):
    wb = Workbook()
    ws = wb.active
    ws.title = "Premissas"
    ln = titulo(ws, "FASE 2 - REDE  |  premissas", span=4)
    ws.column_dimensions["A"].width = 54
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 56
    ws.cell(ln, 1, "Celulas em bege sao de entrada. Tudo o mais e formula."
            ).font = Font(italic=True, color="8A5F16")
    ln += 2
    M = {}
    ws.cell(ln, 1, "UNIDADE FRANQUEADA (praca tipica de 30 a 80 mil hab)").font = bold
    ln += 1
    M["rec"] = ln; ln = entrada(ws, ln, "Receita madura da unidade/mes", R.REC_MADURA)
    M["cv"] = ln; ln = entrada(ws, ln, "Custo variavel + meios (% da receita)", 0.293, PCT)
    M["fixo"] = ln; ln = entrada(ws, ln, "Custo fixo da unidade sem aluguel", 8550)
    ln += 1
    ws.cell(ln, 1, "TAXAS DA REDE").font = bold; ln += 1
    M["roy"] = ln; ln = entrada(ws, ln, "Royalty (% da receita)", R.ROYALTY, PCT)
    M["fundo"] = ln; ln = entrada(ws, ln, "Fundo de marketing (% da receita)", R.FUNDO, PCT,
                                  "vinculado: nao e margem da franqueadora")
    M["tec"] = ln; ln = entrada(ws, ln, "Taxa de tecnologia/mes por unidade", R.TEC)
    M["taxa"] = ln; ln = entrada(ws, ln, "Taxa de franquia (na assinatura)", R.TAXA_FRANQUIA)
    ln += 1
    ws.cell(ln, 1, "ESTRUTURA DO PONTO COMERCIAL").font = bold; ln += 1
    M["al_merc"] = ln; ln = entrada(ws, ln, "A - aluguel de mercado (franqueado paga a terceiro)",
                                    R.ALUGUEL_MERCADO)
    M["al_b1"] = ln; ln = entrada(ws, ln, "B1 - aluguel que cobramos (compramos o ponto)",
                                  R.ALUGUEL_B1,
                                  nota="janela que fecha dos dois lados: 5.000 a 5.500")
    M["al_b2"] = ln; ln = entrada(ws, ln, "B2 - sublocacao (alugamos longo e sublocamos)",
                                  R.ALUGUEL_B2)
    M["terreno"] = ln; ln = entrada(ws, ln, "Terreno por ponto", R.TERRENO)
    M["obra"] = ln; ln = entrada(ws, ln, "Obra da baia por ponto", R.CONSTRUCAO)
    M["cust_b1"] = ln; ln = entrada(ws, ln, "B1 - IPTU, seguro, manutencao estrutural/mes",
                                    R.CUSTO_IMOVEL_B1)
    M["cust_b2"] = ln; ln = entrada(ws, ln, "B2 - manutencao estrutural/mes", R.CUSTO_IMOVEL_B2)
    ln += 1
    ws.cell(ln, 1, "INVESTIMENTO DO FRANQUEADO").font = bold; ln += 1
    M["inv_a"] = ln; ln = entrada(ws, ln, "A - ele constroi tudo (taxa 50k + capex + giro)",
                                  504060)
    M["inv_b"] = ln; ln = entrada(ws, ln, "B1/B2 - ponto pronto: so maquina e equipamentos",
                                  310100)
    M["cap_a"] = ln; ln = entrada(ws, ln, "A - capex dentro do investimento", 399060,
                                  nota="o resto e taxa de franquia (50 mil) e giro (55 mil)")
    M["cap_b"] = ln; ln = entrada(ws, ln, "B1/B2 - capex dentro do investimento", 224100,
                                  nota="o resto e taxa de franquia (40 mil) e giro (46 mil)")
    M["res_eq"] = ln; ln = entrada(ws, ln, "Valor residual do capex no mes 60", 0.30, PCT,
                                   "nao incide sobre taxa de franquia nem sobre giro")
    ln += 1
    ws.cell(ln, 1, "FRANQUEADORA").font = bold; ln += 1
    M["trib_s"] = ln; ln = entrada(ws, ln, "Tributos sobre servicos (royalty + tecnologia)",
                                   R.TRIB_SERVICOS, PCT, "Lucro Presumido - ESTIMATIVA")
    M["trib_a"] = ln; ln = entrada(ws, ln, "Tributos sobre aluguel", R.TRIB_ALUGUEL, PCT)
    M["tma"] = ln; ln = entrada(ws, ln, "TMA (a.a.)", R.TMA, PCT)
    M["antes"] = ln; ln = entrada(ws, ln, "Meses entre pagar o ponto e inaugurar",
                                  R.MESES_ANTES, NUM)
    prim_est = ln
    for a in range(1, 11):
        ln = entrada(ws, ln, f"Estrutura da franqueadora - ano {a} (R$/mes)", R.ESTRUTURA[a])
    M["est"] = prim_est

    # -------------------------------------------------- Cronograma
    cr = wb.create_sheet("Cronograma")
    ln = titulo(cr, "FASE 2 - mes de inauguracao de cada unidade franqueada", span=3)
    cab = cabecalho(cr, ln, ["Unidade", "Mes de inauguracao", "Ano"],
                    largura=[12, 22, 10])
    for i, m in enumerate(R.cronograma(), start=1):
        r = cab + i - 1
        cr.cell(r, 1, i)
        c = cr.cell(r, 2, m); c.fill = fill_in; c.font = bold
        cr.cell(r, 3, f"=ROUNDUP(B{r}/12,0)")
    n_un = len(R.cronograma())
    ult = cab + n_un - 1
    ABERT = f"Cronograma!$B${cab}:$B${ult}"

    # -------------------------------------------------- Franqueado
    fq = wb.create_sheet("Franqueado", 1)
    ln = titulo(fq, "O FRANQUEADO NAS TRES ESTRUTURAS DE PONTO  |  60 meses", span=13)
    p = "Premissas!$B$"
    cols = ["Mes", "Rampa", "Receita",
            "FCL  A: aluga", "FCL  B1: compramos", "FCL  B2: sublocamos"]
    cab2 = cabecalho(fq, ln, cols, largura=[6, 9, 14, 18, 20, 20])
    r0 = cab2
    for m in range(1, 61):
        r = r0 + m - 1
        fq.cell(r, 1, m)
        fq.cell(r, 2, f'=IF(A{r}<=3,0.35,IF(A{r}<=6,0.55,IF(A{r}<=9,0.75,'
                      f'IF(A{r}<=12,0.88,1))))').number_format = PCT
        fq.cell(r, 3, f"={p}{M['rec']}*B{r}").number_format = MOEDA
        aliq = f_simples(f"C{r}*12")[1:]
        for col, al, inv, capex in (
                ("D", f"{p}{M['al_merc']}", f"{p}{M['inv_a']}", f"{p}{M['cap_a']}"),
                ("E", f"{p}{M['al_b1']}", f"{p}{M['inv_b']}", f"{p}{M['cap_b']}"),
                ("F", f"{p}{M['al_b2']}", f"{p}{M['inv_b']}", f"{p}{M['cap_b']}")):
            ebitda = (f"C{r}*(1-({aliq})-{p}{M['cv']}-{p}{M['roy']}-{p}{M['fundo']})"
                      f"-{p}{M['tec']}-{p}{M['fixo']}-{al}")
            f = f"=({ebitda})-C{r}*0.015"
            if m == 60:
                f += f"+{capex}*{p}{M['res_eq']}"
            fq.cell(r, {"D": 4, "E": 5, "F": 6}[col], f).number_format = MOEDA
    fq.freeze_panes = f"A{cab2}"

    ln = r0 + 62
    fq.cell(ln, 1, "RESULTADO").font = Font(bold=True, size=12); ln += 1
    rot = ["Investimento do franqueado", "Aluguel que ele paga", "EBITDA maduro/mes",
           "Margem EBITDA", "TIR anual", "VPL na TMA", "Payback (meses)"]
    for i, t in enumerate(rot):
        fq.cell(ln + i, 1, t).font = bold
    # investimento, aluguel, EBITDA maduro e margem: direto das premissas e do mes 60.
    # O mes 60 carrega o valor residual do equipamento, por isso ele e retirado aqui.
    for j, (col, al, inv, capex) in enumerate([
            ("D", M['al_merc'], M['inv_a'], M['cap_a']),
            ("E", M['al_b1'], M['inv_b'], M['cap_b']),
            ("F", M['al_b2'], M['inv_b'], M['cap_b'])]):
        cc = 4 + j
        letra = get_column_letter(cc)
        fq.cell(ln, cc, f"={p}{inv}").number_format = MOEDA
        fq.cell(ln + 1, cc, f"={p}{al}").number_format = MOEDA
        fq.cell(ln + 2, cc, f"={col}{r0+59}-{p}{capex}*{p}{M['res_eq']}"
                            f"+C{r0+59}*0.015").number_format = MOEDA
        fq.cell(ln + 3, cc, f"=IF(C{r0+59}=0,0,{letra}{ln+2}/C{r0+59})"
                ).number_format = PCT

    # TIR, VPL e payback precisam do desembolso no mes 0: bloco auxiliar abaixo
    aux = ln + 9
    fq.cell(aux - 1, 1, "Fluxo com o mes 0 (para IRR / NPV / payback)").font = bold
    cab3 = cabecalho(fq, aux, ["Mes", "", "", "A", "B1", "B2"])
    for m in range(0, 61):
        r = cab3 + m
        fq.cell(r, 1, m)
        if m == 0:
            fq.cell(r, 4, f"=-{p}{M['inv_a']}").number_format = MOEDA
            fq.cell(r, 5, f"=-{p}{M['inv_b']}").number_format = MOEDA
            fq.cell(r, 6, f"=-{p}{M['inv_b']}").number_format = MOEDA
        else:
            for cc, col in ((4, "D"), (5, "E"), (6, "F")):
                fq.cell(r, cc, f"={col}{r0+m-1}").number_format = MOEDA
    # caixa acumulado para o payback
    fq.cell(cab3 - 1, 8, "Caixa acumulado A").font = Font(size=9, bold=True)
    fq.cell(cab3 - 1, 9, "B1").font = Font(size=9, bold=True)
    fq.cell(cab3 - 1, 10, "B2").font = Font(size=9, bold=True)
    for m in range(0, 61):
        r = cab3 + m
        for cc, src in ((8, "D"), (9, "E"), (10, "F")):
            if m == 0:
                fq.cell(r, cc, f"={src}{r}").number_format = MOEDA
            else:
                fq.cell(r, cc, f"={get_column_letter(cc)}{r-1}+{src}{r}"
                        ).number_format = MOEDA
    for j, col in enumerate(["D", "E", "F"]):
        cc = 4 + j
        acc = get_column_letter(8 + j)
        rng = f"{col}{cab3}:{col}{cab3+60}"
        fq.cell(ln + 4, cc, f'=IFERROR((1+IRR({rng},0.02))^12-1,"nao converge")').number_format = PCT
        fq.cell(ln + 5, cc, f"=NPV((1+{p}{M['tma']})^(1/12)-1,{col}{cab3+1}:{col}{cab3+60})"
                            f"+{col}{cab3}").number_format = MOEDA
        fq.cell(ln + 6, cc,
                f'=IFERROR(MATCH(TRUE,INDEX({acc}{cab3+1}:{acc}{cab3+60}>=0,0),0),"nao paga")'
                ).number_format = NUM
    for i in range(7):
        for j in range(3):
            fq.cell(ln + i, 4 + j).font = Font(bold=True)

    # -------------------------------------------------- Franqueadora
    fr = wb.create_sheet("Franqueadora", 2)
    ln = titulo(fr, "A FRANQUEADORA  |  120 meses  |  escolha a estrutura em B4", span=16)
    fr.cell(3, 1, "Estrutura do ponto (A, B1 ou B2):").font = bold
    sel = fr.cell(4, 1, "A"); sel.fill = fill_in; sel.font = Font(bold=True, size=14)
    fr.cell(4, 2, 'A = asset-light (capital zero no imovel)   '
                  'B1 = compramos terreno e construimos   '
                  'B2 = alugamos longo e sublocamos').font = Font(italic=True, size=9,
                                                                   color="6B7F93")
    S = "$A$4"
    cols = ["Mes", "Ano", "Unidades ativas", "Receita da rede", "Royalty",
            "Tecnologia", "Aluguel recebido", "Receita bruta", "Tributos",
            "Estrutura", "Custo do imovel", "Aluguel pago", "EBITDA",
            "Capex do ponto", "Taxa de franquia", "Fluxo livre", "Caixa acumulado"]
    cab4 = cabecalho(fr, 6, cols,
                     largura=[6, 6, 14, 15, 13, 12, 15, 14, 13, 12, 14, 13, 14, 15, 14,
                              14, 16])
    r0 = cab4
    for m in range(1, 121):
        r = r0 + m - 1
        fr.cell(r, 1, m)
        fr.cell(r, 2, f"=ROUNDUP(A{r}/12,0)")
        fr.cell(r, 3, f'=COUNTIF({ABERT},"<="&A{r})').number_format = NUM
        # receita da rede por faixa de idade
        fr.cell(r, 4,
                f'={p}{M["rec"]}*('
                f'COUNTIFS({ABERT},">="&A{r}-2,{ABERT},"<="&A{r})*0.35'
                f'+COUNTIFS({ABERT},">="&A{r}-5,{ABERT},"<="&A{r}-3)*0.55'
                f'+COUNTIFS({ABERT},">="&A{r}-8,{ABERT},"<="&A{r}-6)*0.75'
                f'+COUNTIFS({ABERT},">="&A{r}-11,{ABERT},"<="&A{r}-9)*0.88'
                f'+COUNTIF({ABERT},"<="&A{r}-12)*1)').number_format = MOEDA
        fr.cell(r, 5, f"=D{r}*{p}{M['roy']}").number_format = MOEDA
        fr.cell(r, 6, f"=C{r}*{p}{M['tec']}").number_format = MOEDA
        fr.cell(r, 7, f'=IF({S}="B1",C{r}*{p}{M["al_b1"]},'
                      f'IF({S}="B2",C{r}*{p}{M["al_b2"]},0))').number_format = MOEDA
        fr.cell(r, 8, f"=E{r}+F{r}+G{r}").number_format = MOEDA
        fr.cell(r, 9, f"=(E{r}+F{r})*{p}{M['trib_s']}+G{r}*{p}{M['trib_a']}"
                ).number_format = MOEDA
        fr.cell(r, 10, f"=INDEX(Premissas!$B${M['est']}:$B${M['est']+9},MIN(10,B{r}))"
                ).number_format = MOEDA
        fr.cell(r, 11, f'=IF({S}="B1",C{r}*{p}{M["cust_b1"]},'
                       f'IF({S}="B2",C{r}*{p}{M["cust_b2"]},0))').number_format = MOEDA
        fr.cell(r, 12, f'=IF({S}="B2",C{r}*{p}{M["al_merc"]},0)').number_format = MOEDA
        fr.cell(r, 13, f"=H{r}-I{r}-J{r}-K{r}-L{r}").number_format = MOEDA
        fr.cell(r, 14, f'=COUNTIF({ABERT},"="&A{r}+{p}{M["antes"]})'
                       f'*IF({S}="B1",{p}{M["terreno"]}+{p}{M["obra"]},'
                       f'IF({S}="B2",{p}{M["obra"]},0))').number_format = MOEDA
        fr.cell(r, 15, f'=COUNTIF({ABERT},"="&A{r}+3)*{p}{M["taxa"]}'
                       f'*(1-{p}{M["trib_s"]})').number_format = MOEDA
        fr.cell(r, 16, f"=M{r}-N{r}+O{r}").number_format = MOEDA
        if m == 1:
            fr.cell(r, 17, f"=P{r}").number_format = MOEDA
        else:
            fr.cell(r, 17, f"=Q{r-1}+P{r}").number_format = MOEDA
    fr.freeze_panes = f"A{cab4}"

    lr = r0 + 122
    fr.cell(lr, 1, "RESULTADO DA FRANQUEADORA (sem valor residual)").font = Font(
        bold=True, size=12)
    rng = f"P{r0}:P{r0+119}"
    linhas = [
        ("Unidades no ano 10", f"=C{r0+119}", NUM),
        ("Receita bruta no ano 10", f"=SUMIF($B${r0}:$B${r0+119},10,$H${r0}:$H${r0+119})",
         MOEDA),
        ("EBITDA no ano 10", f"=SUMIF($B${r0}:$B${r0+119},10,$M${r0}:$M${r0+119})", MOEDA),
        ("Capital total no imovel", f"=SUM(N{r0}:N{r0+119})", MOEDA),
        ("Pico de caixa", f"=MIN(Q{r0}:Q{r0+119})", MOEDA),
        ("Mes do pico", f"=MATCH(MIN(Q{r0}:Q{r0+119}),Q{r0}:Q{r0+119},0)", NUM),
        ("Mes em que o caixa zera",
         f'=IFERROR(MATCH(TRUE,INDEX(Q{r0}:Q{r0+119}>=0,0),0),"nao zera")', NUM),
        ("TIR anual", f'=IFERROR((1+IRR({rng},0.02))^12-1,"negativa")', PCT),
        ("VPL na TMA", f"=NPV((1+{p}{M['tma']})^(1/12)-1,{rng})", MOEDA),
    ]
    for i, (rot, f, fmt) in enumerate(linhas):
        fr.cell(lr + 1 + i, 1, rot).font = bold
        c = fr.cell(lr + 1 + i, 4, f)
        c.number_format = fmt
        c.font = Font(bold=True)
        c.fill = fill_out
    fr.cell(lr + 12, 1,
            "Nota: estas linhas NAO incluem valor residual (terreno valorizado nem "
            "multiplo do negocio de franquia). Ver BP-REDE.md secao 2."
            ).font = Font(italic=True, size=9, color="6B7F93")

    wb.save(caminho)
    return caminho


if __name__ == "__main__":
    import os
    d = os.path.dirname(os.path.abspath(__file__))
    for f in (planilha_piumhi(os.path.join(d, "Modelo-Economico-Piumhi.xlsx")),
              planilha_rede(os.path.join(d, "Modelo-Economico-Rede.xlsx"))):
        print("gravado:", f)
