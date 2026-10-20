# Business Plan — rede de lavagem automatizada por assinatura

Unidade modelo em Piumhi/MG, com formatação de franquia em 12 meses.

Documento de trabalho. Os números vêm do modelo em `docs/bp/` e da planilha
`docs/bp/Modelo-Economico-Rede-Lavagem.xlsx`, que tem as fórmulas vivas — mudar
uma premissa na aba `Premissas` recalcula TIR, VPL e payback de todos os formatos.

Data da versão: 2026-10-20.

---

## 1. Premissas gerais

| Premissa | Valor | Origem |
|---|---|---|
| TMA (taxa mínima de atratividade) | 18% a.a. | premissa; ajustar à Selic e ao custo de capital no fechamento |
| Horizonte da unidade | 60 meses | padrão de contrato de franquia (5 anos) |
| Horizonte da franqueadora | 120 meses | 60 meses não é suficiente — ver seção 4 |
| Imposto sobre receita (unidade) | 11% | Simples Nacional estimado; **validar com contador** |
| Custo variável | 22% da receita | água, energia, químicos, cartão |
| Royalty | 6% da receita | Plano de Franquia |
| Fundo de marketing | 2% da receita | Plano de Franquia |
| Taxa de tecnologia | R$ 700/mês por unidade | Plano de Franquia |
| Capex de manutenção | 1,5% da receita | reposição de bicos, bombas, pintura |
| Valor residual do capex | 35% no mês 60 | equipamento importado com 3 anos de garantia |
| Rampa de maturação | 35% (m1–3), 55% (m4–6), 75% (m7–9), 88% (m10–12), 100% a partir do m13 | premissa de ramp-up de assinatura |

O custo fixo mensal de cada formato é **calibrado**: é o valor que faz o modelo
reproduzir exatamente o EBITDA maduro informado no Plano de Franquia. Isso garante
que o modelo não inventa um resultado melhor que o do plano — ele chega no mesmo
número por um caminho auditável.

---

## 2. Franqueado — os três formatos

| | BOX | EXPRESS | PRIME |
|---|---|---|---|
| Taxa de franquia | R$ 35.000 | R$ 50.000 | R$ 60.000 |
| Capex (obra + equipamento) | R$ 155.000 | R$ 326.000 | R$ 600.000 |
| Capital de giro | R$ 25.000 | R$ 40.000 | R$ 60.000 |
| **Investimento total** | **R$ 215.000** | **R$ 416.000** | **R$ 720.000** |
| Receita madura/mês | R$ 19.000 | R$ 48.000 | R$ 75.000 |
| Custo fixo mensal (calibrado) | R$ 5.510 | R$ 12.020 | R$ 18.750 |
| EBITDA maduro/mês | R$ 5.000 | R$ 15.600 | R$ 24.800 |
| Margem EBITDA | 26,3% | 32,5% | 33,1% |
| **Payback (investimento total)** | **56 meses** | **37 meses** | **39 meses** |
| **TIR (60 meses)** | **9,4% a.a.** | **29,6% a.a.** | **26,4% a.a.** |
| **VPL @ 18% a.a.** | **−R$ 45.400** | **+R$ 122.738** | **+R$ 152.868** |
| ROI 5 anos (caixa acumulado / investimento) | 134% | 213% | 200% |

### 2.1 O BOX destrói valor — recomendação: retirar da oferta

TIR de 9,4% contra TMA de 18%, VPL negativo de R$ 45 mil e payback de 56 meses em
um contrato de 60. Na prática: o franqueado do BOX paga R$ 215 mil, trabalha cinco
anos e termina com menos dinheiro do que se tivesse deixado na renda fixa.

O payback de 42 meses que aparece no Plano de Franquia ignora a taxa de franquia e
o capital de giro — considera só o capex. Com o desembolso real, são 56 meses.

Por que isso importa para a franqueadora, e não só para o franqueado: franqueado que
não ganha dinheiro não renova, não indica, atrasa royalty e reclama em público. O BOX
é a porta de entrada mais barata e, por isso, a que mais vende — e também a que mais
produz franqueado insatisfeito. É um passivo de marca com desconto.

**Opções:**

1. **Retirar o BOX da oferta** e abrir a rede só com Express e Prime. Perde-se volume
   de unidades; ganha-se rede saudável. *Recomendada.*
2. Reprecificar o BOX: taxa de franquia a R$ 15 mil e royalty a 4% elevam a TIR para
   a casa dos 15% — ainda abaixo da TMA. Não resolve.
3. Manter o BOX apenas como **expansão de franqueado já existente** (segundo ponto numa
   cidade onde ele já opera um Express), onde a estrutura fixa é compartilhada e o
   custo fixo incremental é menor. Aqui o número fecha, mas é caso particular.

### 2.2 Express — o formato-âncora

É o formato da unidade modelo de Piumhi e o que deve carregar a rede.

- **Ponto de equilíbrio: R$ 21.559/mês**, ou 45% da receita madura — cerca de
  **21 lavagens por dia**.
- **Maturidade: 46 lavagens por dia**, aproximadamente **600 assinantes**.
- Tolera queda de receita de até ≈ **12%** antes de o VPL virar negativo.

Sensibilidade da receita madura (Express):

| Cenário | Receita/mês | EBITDA/mês | Payback | TIR | VPL @ 18% |
|---|---|---|---|---|---|
| −30% | R$ 33.600 | R$ 7.104 | 60 meses | 0,6% | −R$ 178.581 |
| −20% | R$ 38.400 | R$ 9.936 | 55 meses | 10,5% | −R$ 78.142 |
| −10% | R$ 43.200 | R$ 12.768 | 44 meses | 20,1% | +R$ 22.298 |
| **base** | **R$ 48.000** | **R$ 15.600** | **37 meses** | **29,6%** | **+R$ 122.738** |
| +10% | R$ 52.800 | R$ 18.432 | 32 meses | 39,0% | +R$ 223.178 |

A leitura prática: o projeto aguenta errar 10% na demanda. Errar 20% e ele fica abaixo
da TMA. É por isso que a pré-venda de fundadores vem antes da obra, não depois.

---

## 3. Franqueadora — 5 anos não fecha

Rodando exatamente o plano de expansão do Plano de Franquia num horizonte de 60 meses:

| | Com BOX | Sem BOX |
|---|---|---|
| Unidades no ano 5 | 22 | 19 |
| Receita ano 5 | R$ 1,204 mi | R$ 1,145 mi |
| EBITDA ano 5 | R$ 431.028 | R$ 389.576 |
| Pico de caixa | −R$ 714.655 | −R$ 722.659 |
| Caixa acumulado no mês 60 | −R$ 109.153 | −R$ 223.900 |
| **TIR** | **−6,2%** | **−12,9%** |
| **VPL @ 18%** | **−R$ 245.937** | **−R$ 308.970** |

**A franqueadora é inviável em 5 anos.** No mês 60 o caixa acumulado ainda é negativo:
a estrutura (equipe de campo, app, formatação, marketing) é montada nos anos 1–3, e a
receita recorrente de royalty só supera essa estrutura depois. Avaliar a franqueadora
em cinco anos é medir a rede exatamente no ano em que ela acabou de pagar o investimento.

Observação relevante: o modelo reproduziu de forma independente o **pico de consumo de
caixa de ≈ R$ 720 mil** citado no Plano de Franquia (obtivemos R$ 714 mil). Os dois
cálculos convergem — o plano está internamente consistente nesse ponto.

---

## 4. Franqueadora em 10 anos — aqui fecha

| Ano | Unidades | Receita | EBITDA | Caixa acumulado |
|---|---|---|---|---|
| 1 | 0 | — | −R$ 135.000 | −R$ 135.000 |
| 2 | 2 | R$ 225.104 | −R$ 437.079 | −R$ 572.079 |
| 3 | 7 | R$ 535.014 | −R$ 120.422 | −R$ 692.501 |
| 4 | 12 | R$ 798.987 | +R$ 225.149 | −R$ 467.352 |
| 5 | 19 | R$ 1.170.832 | +R$ 411.499 | −R$ 55.853 |
| 6 | 27 | R$ 1.567.404 | +R$ 537.620 | +R$ 481.766 |
| 7 | 35 | R$ 1.988.236 | +R$ 814.118 | +R$ 1.295.885 |
| 8 | 45 | R$ 2.503.099 | +R$ 1.098.603 | +R$ 2.394.488 |
| 9 | 55 | R$ 2.946.603 | +R$ 1.361.147 | +R$ 3.755.635 |
| 10 | 65 | R$ 3.417.194 | +R$ 1.657.443 | +R$ 5.413.078 |

- Pico de caixa: **−R$ 714.259** (ano 3)
- Caixa acumulado vira positivo no **mês 61**
- **TIR: 49,4% a.a.**
- **VPL @ 18%: R$ 1.264.934**

O vale dos anos 2 e 3 é o risco central do projeto, e ele é de **caixa**, não de modelo:
a franqueadora precisa atravessar R$ 714 mil negativos antes de a recorrência sustentar
a estrutura.

---

## 5. Consolidado — unidade própria + franqueadora

É assim que o investidor deve olhar, porque é assim que o negócio vai existir: a unidade
Express de Piumhi gerando EBITDA enquanto a franqueadora queima caixa.

- **Capital necessário (pico consolidado): R$ 815.404**
- Caixa acumulado vira positivo no **mês 54**
- **TIR: 45,1% a.a.** (120 meses)
- **VPL @ 18%: R$ 1.623.210**

O EBITDA da unidade própria amortece o vale da franqueadora. Separados, os dois projetos
exigiriam cerca de **R$ 1,13 milhão**; juntos, **R$ 815 mil**. A sinergia é de capital,
não de operação.

Três formas de entrar, para o investidor escolher:

| Entrada | Capital | TIR | Risco |
|---|---|---|---|
| Só a unidade Express | R$ 416 mil | 29,6% | menor — negócio local, ativo real |
| Só a franqueadora | ≈ R$ 714 mil | 49,4% | maior — depende de vender franquia, capital paciente |
| **Consolidado** | **R$ 815 mil** | **45,1%** | intermediário |

---

## 6. Estrutura societária — duas PJs, não uma

| | Papel |
|---|---|
| **PJ 1 — Franqueadora** | Dona das marcas e do software. Licencia, cobra royalty e taxa de tecnologia. É o balanço dela que vai para a COF. |
| **PJ 2 — Operação Piumhi** | A unidade que lava carro. Paga royalty como qualquer franqueado. |
| **PJ 3+** | Franqueados, território exclusivo por contrato de 5 anos. |

Por que não pode ser um CNPJ só:

1. **A COF exige o balanço da franqueadora** (Lei nº 13.966/2019). Com tudo junto, cada
   candidato a franqueado recebe o faturamento e as despesas da operação de Piumhi dez
   dias antes de assinar qualquer coisa — inclusive candidatos que vão desistir.
2. **Risco cruzado.** Franqueado que processa a franqueadora alcançaria o caixa e os
   equipamentos da operação, e vice-versa.

A unidade própria pagar royalty para a franqueadora não é formalidade: é o que faz os
indicadores da rede serem comparáveis desde o primeiro dia e dá histórico limpo à COF.

**Validar com advogado societário e contador antes de constituir.**

---

## 7. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| Demanda abaixo do previsto em Piumhi | Alto | Pré-venda de 80 fundadores antes da obra; equilíbrio a 45% da receita madura |
| Marca sem exclusividade no INPI | Alto | Busca de anterioridade e nome distintivo antes de fachada e adesivagem |
| Máquina importada parada por falta de peça | Alto | Fornecedor com distribuidor e estoque no Brasil; garantia de 3 anos em contrato |
| Tensão da rede: 220 V contra 380 V da máquina | Médio | Exigir versão 220 V/60 Hz por escrito, ou orçar transformador elevador |
| Caixa da franqueadora nos anos 2 e 3 | Alto | EBITDA da unidade própria; faseamento do app; sócio ou master regional |
| Franqueado quebrar e manchar a marca | Alto | Capital próprio mínimo de 40%; pré-venda por praça; retirar o formato BOX |
| Licenciamento ambiental e caixa separadora | Médio | Consulta à Prefeitura de Piumhi antes da compra do equipamento |
| Venda de franquia antes da COF | Crítico | Gate absoluto de 12 meses de operação auditável — sem exceção |

---

## 8. O que ainda não está provado

Honestidade metodológica. Nenhum destes pontos invalida a tese; todos mudam o número.

1. **O Excel original não foi fornecido.** O Plano de Franquia cita um modelo econômico
   que não acompanhou o documento. Este BP é uma reconstrução a partir dos números-resumo
   (receita, EBITDA e payback de cada formato).
2. **A decomposição de custos é inferida.** Imposto de 11%, variáveis de 22% e o fixo
   calibrado reproduzem o EBITDA informado, mas são uma composição plausível — não
   necessariamente a do autor do plano.
3. **A receita madura nunca foi medida.** R$ 48 mil/mês equivalem a 46 lavagens por dia
   em Piumhi. Nenhuma unidade operou ainda.
4. **TMA de 18% é premissa, não medida.** A 25%, o VPL do Express cai para perto de zero.
5. **Tributação precisa de contador.** Simples Nacional na unidade e 16% sobre a receita
   da franqueadora são estimativas.
6. **Capex do equipamento em dólar.** Entre pedido e pagamento final passam 60 a 120
   dias — variação cambial é risco real sobre os R$ 326 mil.

---

## 9. Próximos 90 dias

| Prazo | Ação | Por que decide |
|---|---|---|
| 7 dias | Busca de anterioridade no INPI e definição do nome | Trava o gasto com fachada, uniforme e adesivagem |
| 7 dias | Ligar para o distribuidor brasileiro do fabricante | Números reais de operação no Brasil, com a mesma máquina |
| 15 dias | CEMIG: tensão no ponto e prazo de aumento de carga | Define se entra transformador no capex |
| 15 dias | Prefeitura: licença ambiental e caixa separadora | Pode mudar a obra civil inteira |
| 30 dias | Frota de Piumhi no SENATRAN e pesquisa de preço na rua | Valida ou derruba as 46 lavagens/dia |
| 30 dias | Site no ar e campanha dos 80 fundadores | Transforma a premissa de demanda em evidência |
| 60 dias | Fechar o fornecedor com 60 Hz e Modbus em contrato | Destrava obra e cronograma de inauguração |
| 90 dias | Constituir as duas PJs com contador e advogado | Sem isso não há COF, e sem COF não há rede |

A campanha de fundadores é o teste mais barato deste plano inteiro: custa alguns milhares
de reais e responde a pergunta de R$ 815 mil. Se as 80 reservas não saírem, o plano não
morre — ele é revisto antes de a máquina ser comprada.

---

## 10. Como mexer no modelo

```
docs/bp/modelo.py        unidade franqueada, três formatos, 60 meses
docs/bp/franqueadora.py  franqueadora, 60 meses (cenários com e sem BOX)
docs/bp/dez_anos.py      franqueadora 120 meses + consolidado
docs/bp/sens.py          sensibilidade de receita do Express
docs/bp/planilha.py      gera a planilha com fórmulas vivas
```

Rodar: `cd docs/bp && PYTHONPATH=. python3 modelo.py` (idem para os outros).
Sem dependências externas, exceto `planilha.py`, que precisa de `openpyxl`.

Na planilha `Modelo-Economico-Rede-Lavagem.xlsx` as abas `Box`, `Express` e `Prime`
têm 60 linhas mensais com fórmulas que apontam para a aba `Premissas`. TIR, VPL e
payback são `IRR`, `NPV` e `MATCH` de verdade — mudar a TMA ou a receita madura
recalcula tudo.
