# -*- coding: utf-8 -*-
"""Gera o modelo econômico em Excel, com fórmulas vivas."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

TINTA="FF0E2231"; AZUL="FF0E63A8"; PAPEL="FFEFF3F6"; OCRE="FFB8801F"; AREIA="FFF6EDDC"; BRANCO="FFFFFFFF"
b_tit=Font(name="Calibri",size=14,bold=True,color=BRANCO)
b_sub=Font(name="Calibri",size=11,bold=True,color="FF4A5F70")
b_neg=Font(name="Calibri",size=11,bold=True)
f_tit=PatternFill("solid",fgColor=TINTA); f_azul=PatternFill("solid",fgColor=AZUL)
f_papel=PatternFill("solid",fgColor=PAPEL); f_areia=PatternFill("solid",fgColor=AREIA)
fino=Side(style="thin",color="FFD5DFE6"); borda=Border(bottom=fino)
MOEDA='#,##0;[Red]-#,##0'; PCT='0.0%'; PCT2='0.00%'

wb=Workbook(); 

# ---------------- PREMISSAS ----------------
ws=wb.active; ws.title="Premissas"
ws.column_dimensions["A"].width=46
for c in "BCD": ws.column_dimensions[c].width=16
def titulo(ws,row,texto,span=4):
    ws.cell(row,1,texto).font=b_tit
    for i in range(1,span+1): ws.cell(row,i).fill=f_tit
ws["A1"]="MODELO ECONÔMICO — REDE DE LAVAGEM AUTOMATIZADA POR ASSINATURA"; ws["A1"].font=Font(size=16,bold=True,color=TINTA)
ws["A2"]="Reconstrução a partir dos números-resumo do Plano de Franquia (set/2026). O Excel original não foi fornecido."
ws["A2"].font=Font(size=10,italic=True,color="FF7C8E9C")
ws["A3"]="Células azuis são premissas editáveis. Tudo o mais é fórmula."; ws["A3"].font=Font(size=10,italic=True,color=AZUL)

titulo(ws,5,"PREMISSAS COMUNS")
linhas=[("Taxa mínima de atratividade (a.a.)",0.18,PCT),
        ("Imposto sobre receita da unidade (Simples, efetivo)",0.11,PCT),
        ("Custos variáveis (água, energia, química, gateway)",0.22,PCT),
        ("Royalty sobre receita bruta",0.06,PCT),
        ("Fundo de marketing sobre receita bruta",0.02,PCT),
        ("Taxa de tecnologia (R$/mês por unidade)",700,MOEDA),
        ("Capex de manutenção (% da receita)",0.015,PCT),
        ("Valor residual no mês 60 (% do capex)",0.35,PCT),
        ("Imposto sobre receita da franqueadora",0.16,PCT),
        ("Rebate do fabricante por unidade instalada",25000,MOEDA)]
r=6
for nome,val,fmt in linhas:
    ws.cell(r,1,nome); c=ws.cell(r,2,val); c.number_format=fmt; c.fill=f_papel; c.font=b_neg
    ws.cell(r,1).border=borda; ws.cell(r,2).border=borda; r+=1
TMA="Premissas!$B$6"; IMP="Premissas!$B$7"; VAR="Premissas!$B$8"; ROY="Premissas!$B$9"
FUN="Premissas!$B$10"; TEC="Premissas!$B$11"; MAN="Premissas!$B$12"; RES="Premissas!$B$13"

r+=1; titulo(ws,r,"PREMISSAS POR FORMATO")
r+=1
ws.cell(r,1,"").font=b_sub
for j,f in enumerate(["BOX","EXPRESS","PRIME"]):
    c=ws.cell(r,2+j,f); c.font=Font(bold=True,color=BRANCO); c.fill=f_azul; c.alignment=Alignment(horizontal="center")
base=r
dados=[("Taxa de franquia",35000,50000,60000,MOEDA),
       ("Capex de instalação",155000,326000,600000,MOEDA),
       ("Capital de giro",25000,40000,60000,MOEDA),
       ("Receita madura (R$/mês)",19000,48000,75000,MOEDA),
       ("EBITDA maduro informado no plano",5000,15600,24800,MOEDA)]
r+=1
for nome,a,bv,cv,fmt in dados:
    ws.cell(r,1,nome)
    for j,v in enumerate([a,bv,cv]):
        c=ws.cell(r,2+j,v); c.number_format=fmt; c.fill=f_papel; c.font=b_neg
    r+=1
inv=r
ws.cell(r,1,"Investimento total (taxa + capex + giro)").font=b_neg
for j in range(3):
    col=get_column_letter(2+j)
    c=ws.cell(r,2+j,f"={col}{base+1}+{col}{base+2}+{col}{base+3}"); c.number_format=MOEDA; c.font=b_neg; c.fill=f_areia
r+=1
fx=r
ws.cell(r,1,"Custo fixo mensal (calibrado para reproduzir o EBITDA)")
for j in range(3):
    col=get_column_letter(2+j)
    c=ws.cell(r,2+j,f"={col}{base+4}*(1-{IMP}-{VAR}-{ROY}-{FUN})-{TEC}-{col}{base+5}")
    c.number_format=MOEDA
r+=2
titulo(ws,r,"CURVA DE MATURAÇÃO (% da receita madura)")
r+=1
for j,(rot,v) in enumerate([("Meses 1–3",0.35),("Meses 4–6",0.55),("Meses 7–9",0.75),("Meses 10–12",0.88),("Mês 13 em diante",1.00)]):
    ws.cell(r+j,1,rot); c=ws.cell(r+j,2,v); c.number_format=PCT; c.fill=f_papel; c.font=b_neg
RAMPA_R=r

# ---------------- UNIDADES ----------------
def aba_unidade(nome, col_idx):
    w=wb.create_sheet(nome)
    w.column_dimensions["A"].width=10
    for c in "BCDEFGHIJK": w.column_dimensions[c].width=15
    w["A1"]=f"UNIDADE {nome.upper()} — FLUXO MENSAL (60 MESES)"; w["A1"].font=Font(size=14,bold=True,color=TINTA)
    cab=["Mês","% rampa","Receita","Impostos","Variáveis","Royalty","Fundo","Tecnologia","Fixos","EBITDA","Fluxo livre","Acumulado"]
    for j,t in enumerate(cab):
        c=w.cell(3,1+j,t); c.font=Font(bold=True,color=BRANCO); c.fill=f_tit; c.alignment=Alignment(horizontal="center",wrap_text=True)
    L=get_column_letter(1+col_idx)
    w.cell(4,1,0); w.cell(4,12,f"=-Premissas!{L}{inv}").number_format=MOEDA
    w.cell(4,11,f"=-Premissas!{L}{inv}").number_format=MOEDA
    for i in range(1,61):
        r2=4+i
        w.cell(r2,1,i)
        w.cell(r2,2,f'=IF(A{r2}<=3,Premissas!$B${RAMPA_R},IF(A{r2}<=6,Premissas!$B${RAMPA_R+1},IF(A{r2}<=9,Premissas!$B${RAMPA_R+2},IF(A{r2}<=12,Premissas!$B${RAMPA_R+3},Premissas!$B${RAMPA_R+4}))))').number_format=PCT
        w.cell(r2,3,f"=Premissas!{L}{base+4}*B{r2}").number_format=MOEDA
        w.cell(r2,4,f"=-C{r2}*{IMP}").number_format=MOEDA
        w.cell(r2,5,f"=-C{r2}*{VAR}").number_format=MOEDA
        w.cell(r2,6,f"=-C{r2}*{ROY}").number_format=MOEDA
        w.cell(r2,7,f"=-C{r2}*{FUN}").number_format=MOEDA
        w.cell(r2,8,f"=-{TEC}").number_format=MOEDA
        w.cell(r2,9,f"=-Premissas!{L}{fx}").number_format=MOEDA
        w.cell(r2,10,f"=SUM(C{r2}:I{r2})").number_format=MOEDA
        resid=f"+Premissas!{L}{base+2}*{RES}" if i==60 else ""
        w.cell(r2,11,f"=J{r2}-C{r2}*{MAN}{resid}").number_format=MOEDA
        w.cell(r2,12,f"=L{r2-1}+K{r2}").number_format=MOEDA
    rr=70
    w.cell(rr,1,"RESULTADO").font=Font(bold=True,size=12,color=TINTA)
    res=[("Investimento total",f"=Premissas!{L}{inv}",MOEDA),
         ("EBITDA maduro (mês 60)","=J64",MOEDA),
         ("Margem EBITDA madura","=J64/C64",PCT),
         ("Payback (meses)","=MATCH(TRUE,INDEX(L5:L64>=0,0),0)","0"),
         ("TIR mensal","=IRR(K4:K64)",PCT2),
         ("TIR anual","=(1+B74)^12-1",PCT),
         ("VPL @ TMA","=NPV((1+"+TMA+")^(1/12)-1,K5:K64)+K4",MOEDA),
         ("ROI 5 anos (caixa/investimento)","=SUM(K5:K64)/B71",PCT)]
    for i,(nm,fo,fmt) in enumerate(res):
        w.cell(rr+1+i,1,nm); c=w.cell(rr+1+i,2,fo); c.number_format=fmt; c.font=b_neg
        c.fill=f_areia if "TIR anual" in nm or "VPL" in nm else f_papel
    return w

aba_unidade("Box",1); aba_unidade("Express",2); aba_unidade("Prime",3)

# ---------------- RESUMO ----------------
w=wb.create_sheet("Resumo",1)
w.column_dimensions["A"].width=42
for c in "BCD": w.column_dimensions[c].width=18
w["A1"]="RESUMO EXECUTIVO"; w["A1"].font=Font(size=16,bold=True,color=TINTA)
w["A2"]="Todos os valores vêm das abas de cálculo. Mude as premissas e tudo se move."
w["A2"].font=Font(size=10,italic=True,color="FF7C8E9C")
w.cell(4,1,"FRANQUEADO").font=b_tit; 
for i in range(1,5): w.cell(4,i).fill=f_tit
for j,f in enumerate(["BOX","EXPRESS","PRIME"]):
    c=w.cell(5,2+j,f); c.font=Font(bold=True,color=BRANCO); c.fill=f_azul; c.alignment=Alignment(horizontal="center")
mapa=[("Investimento total","B71",MOEDA),("EBITDA maduro (R$/mês)","B72",MOEDA),
      ("Margem EBITDA","B73",PCT),("Payback (meses)","B74","0"),
      ("TIR (a.a.)","B76",PCT),("VPL @ TMA","B77",MOEDA),("ROI 5 anos","B78",PCT)]
# ajuste: payback está em B74? recalcula índices reais
idx={"Investimento total":71,"EBITDA maduro (R$/mês)":72,"Margem EBITDA":73,"Payback (meses)":74,"TIR mensal":75,"TIR (a.a.)":76,"VPL @ TMA":77,"ROI 5 anos":78}
r=6
for nome,_,fmt in mapa:
    w.cell(r,1,nome)
    for j,ab in enumerate(["Box","Express","Prime"]):
        c=w.cell(r,2+j,f"={ab}!B{idx[nome]}"); c.number_format=fmt
        if nome in ("TIR (a.a.)","VPL @ TMA"): c.font=b_neg; c.fill=f_areia
    r+=1
r+=1
w.cell(r,1,"LEITURA").font=b_neg
w.cell(r+1,1,"O formato BOX rende abaixo da TMA: VPL negativo. A recomendação do BP é retirá-lo da oferta.")
w.cell(r+1,1).font=Font(italic=True,color="FF8A5F16")
w.cell(r+2,1,"EXPRESS é o produto principal; PRIME só depois de validado em praça turística.")
w.cell(r+2,1).font=Font(italic=True,color="FF4A5F70")

cam="/tmp/claude-0/-home-user-LAVAJA/aec1d33d-07ef-53b1-9514-d47c73fb217a/scratchpad/bp/Modelo-Economico-Rede-Lavagem.xlsx"
wb.save(cam); print("gravado:",cam)
