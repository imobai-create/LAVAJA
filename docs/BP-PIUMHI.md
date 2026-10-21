# Fase 1 — Loja modelo de Piumhi/MG

Business plan da primeira unidade. **Área alugada a R$ 3.000/mês**, capex apenas de
implantação do lava jato, sem terreno. Unidade própria: não paga taxa de franquia,
royalty, fundo de marketing nem taxa de tecnologia.

Planilha com fórmulas vivas:
`docs/bp/Modelo-Economico-Piumhi.xlsx`. Data da versão: 2026-10-20.

---

## 0. Antes de tudo: o que era aquele R$ 815 mil

Não era capex. Era o **pico de caixa consolidado** de dois projetos rodando ao mesmo
tempo por dez anos: a unidade própria **mais** a franqueadora, incluindo o vale de
caixa dos anos 2 e 3 da formatação da rede. Dinheiro que entraria aos poucos, ao longo
de três a quatro anos — não um cheque na largada.

Com a decisão de **fazer Piumhi primeiro e a franquia depois**, aquele número sai de
cena. O que a Fase 1 precisa é:

| | Arranjo cru | **Sem dívida** | **Com dívida** |
|---|---|---|---|
| Capex de implantação | R$ 399.060 | **R$ 323.925** (no teto) | **R$ 323.925** (no teto) |
| Capital de giro | R$ 55.000 | **R$ 45.000** | **R$ 45.000** |
| Dívida | — | — | **R$ 120.000** a ~21% a.a. |
| Pré-venda de 80 fundadores | — | **R$ 69.520** | **R$ 69.520** |
| **Capital a reservar** | **R$ 481.006** | **R$ 372.353** | **R$ 274.178** |
| TIR do equity | 24,0% | **32,9%** | **37,1%** |
| VPL @ 18% | R$ 73.260 | **R$ 147.622** | R$ 140.020 |

**Capital a reservar no arranjo cru: R$ 481 mil** (R$ 496 mil no conservador). Isso é capex
cheio e 100% capital próprio, sem nenhuma alavanca. A [seção 11](#11-estrutura-de-capital)
mostra como esse número cai para **R$ 372 mil sem dívida nenhuma** ou **R$ 274 mil com dívida
de R$ 120 mil** — e os dois arranjos seguem em aberto, porque a escolha entre eles não é
financeira (o VPL é quase empate) e sim de caixa. A franqueadora só volta à mesa depois
de doze meses de número real em Piumhi — e com um plano próprio, decidido com dados que
hoje não existem ([BP-REDE.md](BP-REDE.md)).

---

## 1. Piumhi — o mercado, com os números que existem

| Indicador | Valor | Ano | Fonte |
|---|---|---|---|
| População (censo) | 36.062 | 2022 | IBGE |
| População (estimativa) | 38.257 | 2024/26 | IBGE |
| **Frota total de veículos** | **27.599** | **2024** | Senatran/IBGE via imprensa regional |
| **Automóveis** | **13.652** | **2024** | idem |
| Crescimento da frota | +3,47% a/a | 2024 | idem |
| Posição na frota de MG | 84º | 2024 | idem |
| PIB per capita | R$ 43.496,60 | 2023 | IBGE |
| Empregos formais | ~7,4 mil | — | base de empregos formais |

> **Ressalva sobre a frota.** Os 27.599 veículos e 13.652 automóveis vêm de **uma única
> fonte secundária** (reportagem regional citando Senatran/IBGE). O número não foi
> confirmado na tabela original. **Antes de assinar o contrato da máquina**, baixe a
> planilha "Frota por Município e Tipo" no portal do Ministério dos Transportes e
> confirme a linha de Piumhi. É a premissa de demanda mais importante do plano inteiro
> e a confirmação custa quinze minutos.

### Praça ampliada

Piumhi é a **sede da região imediata de Piumhi** (região intermediária de Varginha) e
fica na **MG-050**, a principal via da região. **Capitólio está a cerca de 20 km** e é
destino turístico de peso (cânions e Lago de Furnas), com fluxo de veículos de fora,
muitos vindos de estrada de terra. Isso não entra na base de assinantes — assinatura é
produto de morador — mas sustenta a **receita avulsa**, que no cenário base responde por
R$ 8.400/mês, cerca de 16% do faturamento.

### A pergunta que o número responde

| Cenário | Assinantes | % dos 13.652 automóveis |
|---|---|---|
| Conservador | 380 | 2,8% |
| **Base** | **500** | **3,7%** |
| Otimista | 650 | 4,8% |
| **Equilíbrio operacional** | **~134** | **1,0%** |
| **Mínimo para TIR ≥ 18%** | **~400** | **2,9%** |

É assim que a premissa de demanda deve ser julgada: **precisamos de 2,9% dos carros de
Piumhi para o projeto pagar 18% ao ano.** Não de 46 lavagens por dia abstratas.

(Os dois números de referência já pagam o pró-labore de R$ 3.500/mês — ver a correção na
seção 4. Sem ele seriam 1,3% e 2,5%, que é o que versões anteriores deste documento traziam.)

---

## 2. Capex de implantação — linha por linha

**O teto é R$ 325.000**, definido pelo empreendedor em outubro de 2026. A lista abaixo é a
que cabe nesse teto. Câmbio de planejamento **R$ 5,30/USD** (Focus para o fim de 2026:
R$ 5,20; entre o pedido e o pagamento final passam 60 a 120 dias).

| Item | R$ |
|---|---|
| Máquina JM-70 posta em Piumhi (USD 23.000) | 121.900 |
| Interface Modbus/API + kit de peças de desgaste 2 anos (USD 2.000) | 10.600 |
| Obra civil: pórtico, baia coberta, piso com caimento, pátio 150 m² | 62.000 |
| Caixa separadora água/óleo + hidráulica + reservatório | 26.000 |
| Entrada de energia, quadro, cabeamento, projeto e ART | 24.000 |
| Laudo NR-12 com ART | 6.000 |
| Totem de pagamento PIX/cartão + **câmera de placa** + CFTV | 26.000 |
| Fachada e comunicação visual, versão simples | 10.000 |
| Software da unidade e implantação | 8.000 |
| Projeto, licenças, alvarás, bombeiros, taxas | 14.000 |
| **Subtotal** | **308.500** |
| Contingência 5% | 15.425 |
| **CAPEX TOTAL** | **323.925** |

**Cabe no teto por R$ 1.075.** É pouca folga, e a seção 2.2 diz exatamente onde ela pode
sumir.

### 2.1 O que saiu, e o que não saiu

Em relação à lista completa de R$ 399.060, foram quatro cortes e um adiamento:

| Linha | Completa | No teto | O que muda de verdade |
|---|---|---|---|
| Obra civil | 92.000 | **62.000** | Pátio de 150 m² em vez de 300 m². Cabem 6 carros em espera em vez de 12. Vira problema só se a fila passar disso — e aí o pátio se amplia com caixa da operação |
| Box de alta pressão + 2 aspiradores | 18.000 | **adiado** | Entram no mês 6, pagos pelo caixa. Custam os R$ 2.200/mês de receita complementar até lá |
| Fachada e comunicação visual | 19.000 | **10.000** | Lançamento menos impressionante. Em negócio de assinatura isso pesa mais do que parece — é o corte que eu menos gosto |
| Software e implantação | 12.000 | **8.000** | Sem integrações extras no dia 1. O essencial (assinatura, cobrança, liberação) fica |
| Contingência | 8% | **5%** | Menos colchão para surpresa de obra |

**O que não saiu, e por quê:**

- **A câmera de placa fica.** Ela é o que faz valer "uma placa, um plano" — a trava que
  protege o preço de R$ 79 (seção 12). Cortá-la para economizar R$ 6 mil e depois perder
  R$ 85/mês por assinante que compartilha é troca ruim.
- **A caixa separadora, a entrada de energia e o laudo NR-12 ficam inteiros.** Não são
  escolha: são licenciamento. Cortar aqui é não abrir.
- **O kit de peças de 2 anos fica.** Máquina importada parada por falta de peça custa mais
  do que o kit inteiro.

### 2.2 A folga é de R$ 1.075. O câmbio come ela sozinho.

A máquina e a interface somam **USD 25.000**. A R$ 5,30 isso é R$ 132.500. Cada centavo de
alta no dólar custa R$ 250 no capex — mais a contingência:

| Câmbio | Capex | Teto de R$ 325 mil |
|---|---|---|
| **R$ 5,30** (planejamento) | **R$ 323.925** | cabe por R$ 1.075 |
| R$ 5,60 | R$ 331.800 | **estoura por R$ 6.800** |
| R$ 6,00 | R$ 342.300 | **estoura por R$ 17.300** |

**É a maior ameaça ao teto, e tem solução operacional:** fechar o câmbio junto com o
pedido, em vez de deixá-lo correr até o embarque. A condição usual do fornecedor é 30% na
assinatura e 70% contra cópia do BL — então são 60 a 120 dias de exposição em 70% do
valor. Peça ao banco uma trava de câmbio para essa parcela no dia do pedido. Custa um
spread pequeno e transforma uma variável aberta em número fixo.

A segunda ameaça é a obra: 5% de contingência sobre R$ 308 mil são R$ 15.425, e reforma
pequena estoura isso com facilidade. **Mitigação: três orçamentos fechados com escopo
escrito antes de assinar**, não orçamento por estimativa.

### 2.3 Se o capital permitir, a versão completa

A lista original soma **R$ 399.060** (contingência de 8%) e entrega pátio de 300 m², box e
aspiradores no dia 1, fachada completa e software com integrações. Ela **rende menos**:
TIR de 24,0% contra 32,4%, porque R$ 75 mil a mais de capital não trazem receita
proporcional. **Não é a versão recomendada nem com dinheiro sobrando** — se sobrar capital,
ele vale mais como reserva para a segunda unidade do que como pátio maior na primeira.

### Capital de giro

| Item | R$ |
|---|---|
| Caução de 3 aluguéis | 9.000 |
| Campanha de pré-venda e inauguração | 18.000 |
| Estoque inicial de químicos | 5.000 |
| Colchão de 3 meses de custo fixo | 13.000 |
| **TOTAL** | **45.000** |

O colchão não é conservadorismo decorativo: **os meses 1 a 4 fecham com EBITDA
negativo** (−R$ 3.084 no mês 1), porque a base de assinantes ainda está em formação e o
custo fixo já é integral.

**Investimento total: R$ 323.925 + R$ 45.000 = R$ 368.925.**

---

## 3. Receita — construída de baixo para cima

Preços do site: Essencial R$ 59 (4 lavagens/mês), Ilimitada R$ 99 (R$ 79 fundador),
Premium R$ 139, avulsa R$ 35.

Mix no estado maduro: 45% Essencial, 40% Ilimitada, 15% Premium → **ticket médio de
R$ 87/assinante**.

| Cenário Base | |
|---|---|
| 500 assinantes × R$ 87 | R$ 43.500 |
| Avulsas: 8/dia × 30 × R$ 35 | R$ 8.400 |
| Box de alta pressão, aspirador, complementos | R$ 2.200 |
| **Receita madura** | **R$ 54.100/mês** |

Cruza com os R$ 48.000/mês do Plano de Franquia dentro de 13% — construída por caminho
independente. O plano não estava longe.

---

## 4. Custos

### Variável por lavagem

| Item | R$ |
|---|---|
| Água: 85 L a R$ 14,00/m³ (água + esgoto comercial) — *estimativa* | 1,19 |
| Energia: 1,6 kWh a R$ 1,11/kWh — **tarifa confirmada** | 1,78 |
| Químicos (detergente touchless, espuma, cera) | 2,50 |
| **Total por lavagem** | **5,47** |

Mais 1,5% da receita em meios de pagamento (PIX + cartão).

O 1,6 kWh é **cálculo próprio pelos componentes** da JM-70 (bomba de 15 kW, 4
ventiladores de 22 kW, auxiliares), não o 0,6–1,2 kWh declarado pelo fornecedor.

> **Atualização — out/2026: a tarifa da CEMIG foi confirmada em R$ 1,11/kWh** na baixa
> tensão, contra os R$ 0,98 que o modelo estimava. São 13% a mais, e a energia passa a ser
> **33% do custo variável** da lavagem. O efeito no projeto não é desprezível: o custo
> variável sobe de R$ 5,26 para R$ 5,47 por lavagem, o EBITDA maduro cai de R$ 17.341 para
> **R$ 16.745/mês** e a TIR do arranjo recomendado cai de 39,0% para **37,1%**. Toda a
> seção 5 em diante já está recalculada com R$ 1,11.

### 4.1 A conta de água: o mínimo de 30 m³ não é o que importa

O empreendedor confirmou a tarifa do SAAE: **mínimo de 30 m³ por R$ 93,59**. É informação
boa de ter, e é **irrelevante para esta loja** — vale entender por quê antes de usar os
R$ 3,12/m³ que essa divisão sugere.

| Cenário | Lavagens/mês | Água | Por dia |
|---|---|---|---|
| Conservador | 2.175 | 185 m³ | 6,2 m³ |
| **Base** | **2.865** | **244 m³** | **8,1 m³** |
| Otimista | 3.772 | 321 m³ | 10,7 m³ |

**A loja consome oito vezes o mínimo.** Os 30 m³ cobrem 12% do consumo; os outros 214 m³
são cobrados pela tarifa do **excedente**, que é progressiva e que ninguém informou ainda.
Dividir R$ 93,59 por 30 dá a tarifa da *primeira faixa*, não a da faixa em que a loja cai.

E falta a segunda metade da conta: **o esgoto**. No Brasil costuma ser cobrado como
percentual da água — frequentemente 80% a 100%. Uma loja que lança na rede pública depois
da caixa separadora paga esgoto sobre tudo que consome.

Com as duas incógnitas, a conta mensal no cenário base fica assim:

| Tarifa do excedente | Só água | Com esgoto a 50% | Com esgoto a 100% | R$/m³ efetivo |
|---|---|---|---|---|
| R$ 3,12 | R$ 760 | R$ 1.140 | R$ 1.520 | 6,24 |
| R$ 5,00 | R$ 1.161 | R$ 1.742 | R$ 2.322 | 9,54 |
| R$ 7,00 | R$ 1.588 | R$ 2.382 | R$ 3.177 | 13,04 |
| R$ 9,00 | R$ 2.015 | R$ 3.023 | R$ 4.031 | 16,55 |
| R$ 12,00 | R$ 2.656 | R$ 3.984 | R$ 5.312 | 21,81 |

**É por isso que os R$ 14,00/m³ do modelo continuam.** Não eram um chute pessimista: caem
no meio da faixa plausível — excedente de R$ 7,00 com esgoto a 100% dá R$ 13,04. Baixar a
premissa para R$ 3,12 porque o mínimo divide nesse valor seria o tipo de otimismo que
estoura no primeiro boleto.

**O que a tarifa faz com o projeto** (base, capex enxuto, com pró-labore):

| R$/m³ efetivo | Água/mês | CV/lavagem | EBITDA | TIR | VPL @ 18% |
|---|---|---|---|---|---|
| R$ 3,12 | R$ 760 | R$ 4,54 | R$ 19.394 | **40,3%** | R$ 234.675 |
| R$ 6,50 | R$ 1.583 | R$ 4,83 | R$ 18.571 | 37,7% | R$ 206.817 |
| R$ 10,00 | R$ 2.435 | R$ 5,13 | R$ 17.719 | 35,1% | R$ 177.970 |
| **R$ 14,00 (premissa)** | **R$ 3.409** | **R$ 5,47** | **R$ 16.745** | **32,4%** | **R$ 148.543** |

**A boa notícia é a forma da tabela:** entre o melhor e o pior caso de água há 8 pontos de
TIR, e **o projeto fecha em todos eles**. A água não é variável de vida ou morte, ao
contrário do uso do plano Ilimitada ou do número de assinantes. Se a tarifa vier baixa, é
upside de até R$ 90 mil de VPL — não é o que sustenta a tese.

**As duas perguntas para o SAAE — (37) 3371-1332, dez minutos:**

1. Na categoria comercial, **quanto custa o m³ acima dos 30 m³**? Peça a tabela de faixas
   inteira, porque 244 m³/mês provavelmente cai na última.
2. **Como o esgoto é cobrado** — percentual da água ou tabela própria? E um lava jato com
   caixa separadora licenciada paga a mesma coisa?

Pergunte também se existe **categoria industrial** e em qual delas um lava jato automático
é enquadrado: a diferença entre comercial e industrial costuma ser grande.

**Duas coisas que podem mudar a conta inteira, e que valem a pergunta agora:**

- **Reúso.** A cotação fala em 60–100 L por carro e o equipamento tem sistema de
  reaproveitamento. **Não está claro se os 85 L do modelo são água nova ou consumo bruto.**
  Se o reúso recupera metade, a conta cai pela metade. É pergunta para o fornecedor, junto
  das outras da Fase 0, e muda mais a conta do que a tarifa.
- **Poço artesiano.** 8 m³/dia é volume pequeno. Em Minas a captação subterrânea precisa de
  outorga do IGAM, e abaixo de certo volume há dispensa por uso insignificante — **não sei
  de cabeça qual é o limite e não vou chutar**. Se couber na dispensa, a água vira custo de
  energia de bomba. Vale uma ligação a um hidrogeólogo local antes de assinar o contrato do
  terreno, porque isso também influencia *qual* terreno.

### 4.2 Baixa tensão ou média tensão? Baixa tensão.

A CEMIG cobra R$ 1,11/kWh na baixa tensão e R$ 0,70/kWh na média, esta com **demanda
contratada de ~R$ 1.900/mês**. A demanda é fixa: paga-se cheia, com ou sem movimento.

| | lavagens/mês | kWh/mês | Baixa tensão | Média tensão | Diferença |
|---|---|---|---|---|---|
| Conservador | 2.175 | 4.021 | R$ 4.463 | R$ 4.714 | BT é R$ 252 melhor |
| **Base** | **2.865** | **5.125** | **R$ 5.688** | **R$ 5.487** | MT é R$ 201 melhor |
| Otimista | 3.772 | 6.577 | R$ 7.300 | R$ 6.504 | MT é R$ 796 melhor |

**O ponto de empate é 4.634 kWh/mês — 2.559 lavagens, 85 por dia.** A loja só passa disso
no mês 18 da rampa:

| | mês 1 | mês 6 | mês 12 | mês 18 |
|---|---|---|---|---|
| Assinantes | 80 | 170 | 395 | 482 |
| Baixa tensão | R$ 1.772 | R$ 2.615 | R$ 4.705 | R$ 5.522 |
| Média tensão | R$ 3.018 | R$ 3.549 | R$ 4.867 | R$ 5.383 |
| | MT custa R$ 1.245 mais | R$ 934 mais | R$ 162 mais | MT ganha por R$ 140 |

**Veredicto: fica na baixa tensão.** A média tensão só começa a compensar no mês 18, e
quando compensa é por R$ 140 a R$ 200 por mês. Em 60 meses isso soma pouco mais de R$ 10
mil — contra uma entrada em média tensão (cabine de medição, transformador, proteção,
projeto e ART) que no mercado fica entre R$ 80 mil e R$ 150 mil. Não paga. E na rampa,
quando o caixa é mais apertado, a demanda contratada cobraria R$ 1.900/mês por uma loja
que ainda não tem volume. Os 40 kW da máquina cabem na baixa tensão: a CEMIG atende até
75 kW em baixa, sem subestação.

**Onde a tarifa de R$ 1,11 abre uma oportunidade real:** a conta de energia madura é de
~R$ 5.700/mês, R$ 68 mil por ano. Geração solar própria de ~40 kWp cobriria quase toda
ela, e a lavagem acontece de dia, com alta simultaneidade entre geração e consumo — que é
exatamente o caso em que a Lei 14.300/2022 menos pesa, porque a cobrança do Fio B incide
sobre a energia *injetada*, não sobre a autoconsumida na hora. **Não está no capex deste
BP** e não deve estar: entra como decisão da Fase 1.5, depois que a loja provar o volume,
com três orçamentos locais. Mas é a alavanca de custo mais clara que apareceu até agora.

### Fixo mensal

| Item | R$ |
|---|---|
| Aluguel da área | 3.000 |
| 1 atendente meio período + encargos | 2.600 |
| Manutenção preventiva e peças de desgaste | 1.400 |
| Marketing recorrente | 1.800 |
| Energia de base (iluminação, standby, aspirador) | 600 |
| Contador | 700 |
| Internet, telefonia, gateway, software | 450 |
| Seguro do equipamento + RC | 400 |
| Limpeza, uniformes, materiais | 350 |
| IPTU, taxas, alvará (rateio) | 250 |
| **TOTAL** | **11.550** |

O atendente de meio período não contradiz o "24h automático": ele existe para converter
assinante, orientar o primeiro uso, manter o pátio e cuidar do aspirador. Na loja modelo
ele também é quem aprende a operação que a rede vai replicar.

> **Correção: falta o pró-labore do operador.** A tabela acima — e os resultados da seção 5 —
> não remuneram quem administra a loja. Um negócio que só fecha com o dono trabalhando de
> graça não fechou. Com **pró-labore de R$ 3.500/mês**, o custo fixo vai para **R$ 15.050** e o
> resultado do cenário base muda assim:
>
> | | Sem pró-labore | **Com pró-labore de R$ 3.500** |
> |---|---|---|
> | EBITDA maduro/mês | R$ 20.245 (37,4%) | **R$ 16.745 (31,0%)** |
> | TIR, capex cheio e 100% equity | 35,9% | **24,0%** |
> | VPL @ 18% | R$ 235.282 | **R$ 73.260** |
> | Capital a reservar | R$ 472.671 | **R$ 481.006** |
>
> **O número de referência para conversa com investidor é o da coluna da direita.** Um
> investidor compra retorno de capital; se o operador não é pago, o retorno dele está sendo
> subsidiado pelo trabalho não remunerado do sócio — e isso não dura.
>
> Em Simples Nacional Anexo III a CPP patronal está dentro do DAS, então os R$ 3.500 custam
> R$ 3.500 à empresa, mais o INSS de 11% retido do sócio. **Confirmar com o contador junto da
> questão Anexo III / Anexo V.**
>
> A seção 11 mostra que, com o arranjo de capital recomendado, a TIR volta para **37,1%**
> mesmo pagando o pró-labore — o ganho vem de capex enxuto e alavancagem, não de deixar de
> pagar quem trabalha.

### Tributação

**Simples Nacional, Anexo III.** A R$ 650 mil de receita anual, a alíquota efetiva é
de **10,8%**.

> **Risco fiscal a resolver com contador, antes de abrir.** Se a atividade for
> enquadrada no **Anexo V** (o que depende da classificação do CNAE 4520-0/05 e de
> incidir ou não o Fator R, com folha de apenas 5% da receita), a alíquota vai para
> **12,4%**. O EBITDA cai de R$ 16.745 para R$ 12.854/mês e a **TIR cai de 32,4% para
> 18,8%** — ainda acima da TMA, e só porque o capex está no teto: com a lista completa
> cairia para 12,4%, abaixo dela. Não é detalhe contábil: são R$ 47 mil por ano.

---

## 5. Resultado

Capex de R$ 323.925 (o teto), giro de R$ 45.000, 100% capital próprio, **com pró-labore de
R$ 3.500/mês**. É o arranjo cru: a seção 11 mostra o que a estrutura de capital faz com
estes números.

| | Piso | **Base** | Otimista |
|---|---|---|---|
| Assinantes | 380 | **500** | 650 |
| Receita madura/mês | R$ 40.760 | **R$ 54.100** | R$ 72.350 |
| Lavagens/dia | 72 | **95** | 126 |
| Custo variável | R$ 12.500 (30,7%) | **R$ 16.472 (30,4%)** | R$ 21.706 (30,0%) |
| EBITDA maduro/mês | R$ 9.177 | **R$ 16.745** | R$ 26.988 |
| Margem EBITDA | 22,5% | **31,0%** | 37,3% |
| Capital a reservar | R$ 412.203 | **R$ 395.871** | R$ 381.073 |
| **Payback** | **60 meses** | **35 meses** | **24 meses** |
| **TIR (60 meses)** | **7,1%** | **32,4%** | **65,9%** |
| **VPL @ 18% a.a.** | **−R$ 107.747** | **+R$ 148.543** | **+R$ 501.949** |
| VPL @ 22% a.a. | −R$ 136.595 | +R$ 99.485 | +R$ 425.386 |
| ROI 5 anos | 128% | 236% | 383% |

**No arranjo de capital recomendado** (teto de capex, dívida de R$ 120 mil, pré-venda dos
fundadores — seção 11), o cenário base vira: capital a reservar de **R$ 274 mil**, TIR do
equity de **37,1%** e VPL de **R$ 140.020**.

### 5.1 A primeira coluna não é um cenário. É o gatilho de não fazer.

A coluna da esquerda estava rotulada "Conservador", e o rótulo estava errado — foi erro de
nomenclatura deste documento, não de conta. **380 assinantes é menos do que os 399 de que
o projeto precisa para pagar a TMA de 18%.** Chamar de "conservador" um número que está
*abaixo do mínimo* sugere que é um plano aceitável. Não é: é o cenário em que o projeto
não deveria ter sido feito.

A leitura certa da coluna é esta:

> **Abaixo de ~400 assinantes no mês 12, este projeto não remunera o capital.** Não é
> questão de apertar custo: com o capex já no teto e o pró-labore no mínimo, a conta não
> fecha. É por isso que a campanha de 80 fundadores acontece **antes** da obra, e é por
> isso que existe o gate da seção 13.

Nesse cenário a TIR é 7,1% — acima de zero, abaixo da Selic. O projeto não quebra: devolve
o capital em cinco anos e paga mal. **A decisão certa, se a pré-venda indicar esse
patamar, é não construir** — e o custo de descobrir isso é a campanha de fundadores, não a
loja inteira.

Com o capex de R$ 399 mil da versão completa, essa mesma coluna dava **2,4%**. Os R$ 75
mil a menos de capital valem 4,7 pontos de TIR no pior caso — é a melhor demonstração de
por que o teto de R$ 325 mil é decisão acertada.

**Ponto de equilíbrio:** R$ 25.608/mês — 47,3% da receita madura, já com o pró-labore. Em
assinantes a resposta depende do que se conta junto: **134 assinantes** se as avulsas e as
receitas complementares do cenário base estiverem lá, **302** se o equilíbrio tiver de sair
só da assinatura. O primeiro número é o realista; o segundo é o piso de segurança. Repare
na distância entre **134 para pagar as contas** e **399 para pagar o capital**: a loja fica
de pé muito antes de valer a pena. Essa distância é o risco real do negócio.

### Sobre a TMA de 18%

Com a **Selic a 14% a.a.** (agosto/2026) e IPCA em torno de 4,7%, uma TMA de 18% embute
apenas 4 pontos de prêmio de risco sobre o CDI — para um negócio novo, de um produto que
ninguém na cidade ainda comprou, com máquina importada. **É pouco.** A coluna de 22%
está na tabela por isso. O cenário base sobrevive aos dois; o piso não sobrevive a nenhum.

---

## 6. Sensibilidade

Já com o pró-labore de R$ 3.500/mês, capex no teto de R$ 323.925 e 100% capital próprio,
para isolar o efeito de cada variável da estrutura de capital (seção 11).

| Cenário | EBITDA/mês | TIR | VPL @ 18% |
|---|---|---|---|
| **BASE** | R$ 16.745 | **32,4%** | R$ 148.543 |
| Receita −15% | R$ 9.847 | 9,3% | −R$ 85.819 |
| Aluguel a R$ 5.000 | R$ 14.745 | 24,5% | R$ 67.484 |
| Simples no Anexo V | R$ 12.854 | 18,8% | R$ 8.349 |
| Capex +20% (câmbio/obra estourando) | R$ 16.745 | 25,8% | R$ 92.253 |
| Já pagando royalty 6% + fundo 2% + tecnologia | R$ 11.817 | 15,6% | −R$ 24.285 |

**Tolerância de receita: −10%.** Com o capex da versão completa seria −6%. Pagar o operador
estreitou a margem de erro e **baixar o capex devolveu parte dela** — é a segunda razão
para o teto de R$ 325 mil, além do caixa.

Repare na linha do Anexo V: com capex no teto ela ainda dá **18,8%**, acima da TMA. Com o
capex completo dava 12,4%, abaixo. O mesmo risco tributário deixa de ser fatal só por
investir R$ 75 mil a menos.

A última linha merece leitura: pagando royalty, fundo e taxa de tecnologia, a mesma unidade
rende 15,6%. É a prova aritmética de que a franqueadora não pode nascer antes de a praça
estar provada — e a base da correção registrada em [BP-REDE seção 1](BP-REDE.md).

### O risco número 1 não é a demanda. É o uso do plano Ilimitada.

| Lavagens/mês por assinante Ilimitada | Lavagens/dia | Custo variável/mês | EBITDA/mês | TIR |
|---|---|---|---|---|
| 4 | 82 | R$ 14.285 | R$ 18.931 | 39,3% |
| 5 | 89 | R$ 15.378 | R$ 17.838 | 35,9% |
| **6 (premissa)** | **95** | **R$ 16.472** | **R$ 16.745** | **32,4%** |
| 8 | 109 | R$ 18.658 | R$ 14.559 | 25,4% |
| 10 | 122 | R$ 20.844 | R$ 12.372 | 18,2% |
| 12 | 135 | R$ 23.031 | R$ 10.186 | **10,7%** |

A receita não muda em nenhuma dessas linhas — só o custo. **O plano Ilimitada é a única
variável que pode matar o projeto sem que a demanda caia um real.** O assinante de
R$ 79 que lava doze vezes por mês consome R$ 66 de água, energia e química: sobram
R$ 4 antes de imposto e custo fixo. A oito lavagens por mês o projeto cai para 25,4%;
a doze, para 10,7% — abaixo da Selic.

**Três travas, a implantar antes da inauguração, não depois:**

1. **Uso justo no contrato:** 1 lavagem por veículo por dia, e teto de 12 por mês para o
   Ilimitada. Não é pegadinha — é o que torna o preço sustentável, e deve ser dito assim.
2. **Uma placa, um plano.** O vazamento clássico é o assinante lavando o carro do
   vizinho. A liberação por código do plano é frágil; a câmera de placa resolve. É o
   principal argumento para **não** cortar a câmera na versão enxuta.
3. **O preço de fundador de R$ 79 "travado enquanto a assinatura estiver ativa" é um
   passivo perpétuo.** Oitenta assinantes a R$ 79 para sempre, num plano cujo custo sobe
   com o uso. Limite a trava a 24 ou 36 meses, ou limite os fundadores a 80 de verdade e
   nunca reabra. Mudar isso depois de vender é quebra de promessa.

---

## 7. Capacidade: a máquina satura antes do mercado

| | |
|---|---|
| Ciclo + manobra | 6,5 min |
| Capacidade bruta | 9,2 carros/hora |
| Com 90% de disponibilidade | 8,3 carros/hora |
| **Teto prático** | **~144 lavagens/dia** |
| **Teto de receita com uma máquina** | **~R$ 81.500/mês** |

| Cenário | Lavagens/dia | % do teto |
|---|---|---|
| Conservador | 72 | 50% |
| Base | 95 | 66% |
| Otimista | 126 | **87% — fila no pico** |

Boa notícia disfarçada de problema: **se Piumhi for para o cenário otimista, o limite
passa a ser a máquina, não a cidade.** Aí a decisão é segunda baia — e aí já se sabe que
a demanda existe. O que não dá é descobrir isso com a obra pronta sem espaço para a
segunda baia: **reserve o terreno e a entrada de energia para duas máquinas desde o
projeto.** Custa pouco agora.

---

## 8. Área alugada: o que precisa estar no contrato

**36% do capex — R$ 142 mil — é benfeitoria que fica no terreno de terceiro:** obra
civil, caixa separadora e entrada de energia. Em cinco anos pagamos R$ 180 mil de
aluguel e deixamos R$ 142 mil construídos na propriedade de outra pessoa.

Comprar o terreno em vez de alugar rende **17,3% a.a.** em 60 meses — abaixo da TMA de
18% e pouco acima da Selic de 14%. **Financeiramente, alugar é a decisão certa.** Mas o
contrato tem de proteger a benfeitoria:

1. **Prazo de 10 anos**, com renovação por mais 5 a critério do locatário.
2. **Opção de compra com preço travado hoje** e corrigido por IPCA. Custa zero assinar e
   vale muito se o juro cair — a conta de comprar vira positiva com a Selic abaixo de
   12%.
3. **Cláusula de indenização de benfeitoria** ou abatimento no aluguel em caso de
   rescisão por parte do locador.
4. **Direito de preferência** na venda do imóvel.
5. **Anuência expressa para a obra**, com o projeto anexado ao contrato.
6. Registro do contrato em cartório, para valer contra futuro comprador do imóvel.

Item 2 é o mais importante e o mais barato. Não feche o aluguel sem ele.

---

## 9. Riscos da Fase 1

| Risco | Impacto | Mitigação |
|---|---|---|
| Uso abusivo do plano Ilimitada | **Alto** | Uso justo em contrato + câmera de placa + teto de 12/mês |
| Demanda abaixo de ~400 assinantes | Alto | Pré-venda de 80 fundadores **antes** da obra; equilíbrio operacional a 134 |
| Simples no Anexo V em vez do III | Alto | Parecer de contador antes de abrir (R$ 47 mil/ano) |
| Frota de Piumhi diferente do que a fonte diz | Alto | Baixar a planilha do Senatran — 15 minutos |
| Benfeitoria perdida no fim do aluguel | Alto | Contrato de 10 anos + opção de compra + indenização |
| Máquina 50 Hz / 380 V incompatível | **Crítico** | 60 Hz e tensão CEMIG por escrito no pedido |
| Câmbio entre pedido e pagamento | Médio | Travar câmbio ou orçar a R$ 5,60 |
| Tarifa de água acima do estimado | Baixo | Entre o melhor e o pior caso há 8 pontos de TIR e o projeto fecha nos dois (seção 4.1). Energia já confirmada |
| Licença ambiental e caixa separadora | Médio | Consulta à Prefeitura antes de comprar o equipamento |
| Máquina parada por falta de peça | Alto | Kit de peças de 2 anos no pedido + distribuidor no Brasil |

---

## 10. O que ainda não está provado

1. **A frota de Piumhi vem de fonte secundária única.** Confirmar no Senatran.
2. **A receita madura nunca foi medida.** 500 assinantes = 3,7% dos automóveis da cidade.
   Nenhuma unidade da rede operou.
3. **A tarifa de água ainda não fecha.** O mínimo do SAAE está confirmado — 30 m³ por
   R$ 93,59 — mas a loja consome 244 m³/mês, oito vezes isso. **Faltam a tarifa do
   excedente e a regra do esgoto** (seção 4.1). A premissa de R$ 14,00/m³ fica porque cai
   no meio da faixa plausível; entre o melhor e o pior caso há 8 pontos de TIR e o projeto
   fecha nos dois. **A tarifa de energia já está confirmada** em R$ 1,11/kWh (CEMIG, baixa
   tensão) e o modelo foi recalculado.
4. **O enquadramento tributário é estimativa.** Anexo III ou V muda a TIR em 11 pontos.
5. **O consumo de 1,6 kWh é cálculo próprio**, não medição. O fornecedor declara 0,6–1,2.
6. **O uso médio do plano Ilimitada é a premissa mais frágil do modelo.** 6 lavagens/mês
   por assinante é estimativa sem base local.
7. **O capex de R$ 324 mil não tem orçamento local.** Cada linha precisa de três
   cotações em Piumhi.
8. **A dívida de R$ 120 mil a 21% é premissa, não proposta.** Nenhuma cooperativa foi
   consultada. PJ nova, sem histórico, pode receber taxa pior ou carência menor — e isso muda
   a seção 11. O BDMG Pronampe, que teria a melhor condição, exige receita do ano anterior e
   **só está disponível no ano 2**.
9. **A pré-venda de R$ 69,5 mil supõe 80 fundadores pagando 12 meses à vista** — e, pela
   [ADR-014](DECISOES.md), essa cobrança só é oferecida **depois da máquina instalada**,
   não no mês 0. Na prática o caixa entra no fim da obra, não no começo: a alavanca
   enfraquece e o capital a reservar sobe. É o preço de não receber por uma loja que ainda
   não existe. Se saírem menos de 80, o capital sobe mais — mas isso é o teste de demanda
   falando, e é informação, não só problema.
10. **O pró-labore de R$ 3.500 é escolha, não cálculo.** Acima de R$ 6.000 a TIR do arranjo
    recomendado cai para 22,6% e o projeto encosta na TMA.

Nenhum desses pontos invalida a tese. Os itens 1, 3, 4 e 7 se resolvem em trinta dias e
custam quase nada — e é isso que a Fase 0 abaixo existe para fazer.

---

## 11. Estrutura de capital

Objetivo: **o menor capital possível em risco**, sem estrangular a rampa, com um ou dois
investidores entrando e o controle e a marca preservados.

Todos os números desta seção **já pagam o pró-labore de R$ 3.500/mês**.

### 11.1 Primeiro reduzir a necessidade, depois dividi-la

| Arranjo | 1ª tranche | **Capital a reservar** | TIR do equity | VPL @ 18% |
|---|---|---|---|---|
| 1. Lista de capex completa (R$ 399 mil), 100% equity | R$ 454.060 | **R$ 481.006** | 24,0% | R$ 73.260 |
| 2. **Capex no teto de R$ 325 mil**, 100% equity | R$ 368.925 | **R$ 395.871** | 32,4% | R$ 148.543 |
| 3. + pré-venda anual dos fundadores | R$ 299.405 | **R$ 372.353** | 32,9% | R$ 147.622 |
| **4. + dívida de R$ 120 mil a 21% a.a.** | **R$ 179.405** | **R$ 274.178** | **37,1%** | **R$ 140.020** |
| 5. + dívida de R$ 150 mil | R$ 149.405 | R$ 250.187 | 38,6% | R$ 138.119 |
| 6. + dívida de R$ 180 mil | R$ 119.405 | R$ 226.680 | 40,6% | R$ 136.218 |

**Do arranjo 1 para o 4: o capital cai 42%** — de R$ 481 mil para R$ 274 mil — e a TIR do
equity sobe de 24,0% para 37,1%.

"Capital a reservar" é o **pico de caixa**, não o desembolso inicial. A 1ª tranche entra na
assinatura; o resto é chamado durante a rampa, quando os meses 1 a 4 fecham com EBITDA
negativo. Prometer só a 1ª tranche é como o projeto morre no mês 6.

### 11.2 As quatro alavancas, em ordem de valor

**1. Capex enxuto: −R$ 81 mil de capital, +8,3 pontos de TIR.** A maior alavanca, e a única
que não custa nada: adiar o box de alta pressão e os aspiradores para o mês 6 pagos pelo
caixa, pátio de 150 m² em vez de 300 m², fachada mais simples, contingência de 5%.
**Não corte a câmera de placa** — ela é a trava do plano Ilimitada (seção 6).

**2. Dívida de R$ 120 mil: −R$ 99 mil de capital, +4,7 pontos de TIR.** Alavancagem funciona
aqui porque o projeto rende 34% desalavancado contra 21% de juro. **Mas é uma troca, não
mágica:** o VPL cai de R$ 165 mil para R$ 140 mil, porque 21% é acima da TMA de 18%. Você
troca R$ 8 mil de valor por R$ 99 mil de capital liberado. Com capital escasso, vale.

Onde buscar, em ordem de probabilidade real:

| Fonte | Condição | Observação |
|---|---|---|
| **Cooperativa de crédito local** (Sicoob, Sicredi) | ~21% a.a., 60 meses, 6 de carência | A mais provável para PJ nova em cidade do interior, com aval e relacionamento. **Comece por aqui.** |
| Banco comercial com aval | ~26% a.a. | Caro: derruba o VPL para R$ 148 mil. Último recurso. |
| **BDMG Pronampe investimento** | Selic + 5,50% a.a. (≈19,5%), 72 meses, 12 de carência | Melhor condição do mercado, **mas o teto é 30% da receita bruta do ano anterior, limitado a R$ 250 mil.** PJ nova não tem receita anterior — **só entra no ano 2.** |
| BNDES Finame | Selic + 0,75% + spread do agente | Exige **máquina credenciada no BNDES**, ou seja nacional. A chinesa não entra. Ver 12.4. |

A carência importa mais que a taxa: os meses 1 a 4 têm EBITDA negativo. Exija **pelo menos 6
meses de carência**, e prefira 12.

**3. Pré-venda anual dos 80 fundadores: −R$ 24 mil de capital, e vale mais pelo que não é
dinheiro.** Oferta: 12 meses pelo preço de 11, a R$ 79 — R$ 869 à vista, contra R$ 1.044 de
quem paga mês a mês. Oitenta fundadores são **R$ 69.520 no mês 0**.

O ganho de capital é modesto porque antecipa receita que depois não entra. O valor real é
duplo: **prova a demanda antes de a máquina ser comprada**, e **trava a rotatividade por 12
meses** justamente no período de maior risco.

> **Cuidado jurídico.** Receber antes de entregar cria obrigação de devolução se a loja não
> abrir (CDC). Mantenha o dinheiro em conta separada, com devolução integral prometida por
> escrito e prazo de inauguração declarado. Se a campanha não atingir 80, **o plano é revisto
> antes da compra** — é exatamente para isso que ela existe.

**4. Prazo do fornecedor: ~R$ 85 mil de float por ~100 dias, de graça.** A condição usual é
30% na assinatura e 70% contra cópia do BL. Não reduz o capital total, mas desloca o pico.
Peça por escrito junto das outras exigências da seção 13 (Fase 0).

### 11.3 O pró-labore adiado: a alavanca que só você pode decidir

Se você passar os **12 primeiros meses sem retirada**:

| | Com pró-labore do mês 1 | Sem retirada nos 12 primeiros meses |
|---|---|---|
| Capital a reservar | R$ 274.178 | **R$ 225.867** |
| TIR do equity | 37,1% | **42,6%** |
| VPL @ 18% | R$ 140.020 | **R$ 140.030** |

**−R$ 31 mil de capital e +7,5 pontos de TIR.** É a alavanca mais barata que existe e a única
que depende só de você ter outra renda durante um ano. Se não tiver, **não faça** — sócio
operador apertado é risco maior do que R$ 31 mil de capital.

Se usar, deixe explícito no contrato social: pró-labore de R$ 3.500 a partir do mês 13, com o
valor dos 12 meses não retirados **não** acumulando como crédito contra a empresa.

### 11.4 A origem da máquina não é a alavanca que parecia

A hipótese era: comprar máquina nacional credenciada destrava o **BNDES Finame** (Selic +
0,75% + spread, até 100% do equipamento, até 10 anos), o que converteria R$ 122 mil de equity
em dívida longa e barata. Testamos.

| Máquina nacional a | Capex | Capital a reservar | TIR | VPL @ 18% |
|---|---|---|---|---|
| R$ 130.000 | R$ 325.400 | R$ 259.692 | 41,9% | R$ 160.703 |
| R$ 150.000 | R$ 345.400 | R$ 262.416 | 39,3% | R$ 142.433 |
| R$ 175.000 | R$ 370.400 | R$ 265.858 | 36,0% | R$ 119.594 |
| *rota chinesa, sem Finame* | *R$ 323.925* | *R$ 274.178* | *37,1%* | *R$ 140.020* |

**Ponto de indiferença: máquina nacional a R$ 134.400.** Acima disso, a rota chinesa com
crédito de cooperativa vale mais — a vantagem do Finame é anulada pelo preço mais alto do
equipamento. A chinesa posta em Piumhi custa R$ 132.600 com interface e kit de peças.

**Conclusão honesta: não é a grande alavanca que eu supus.** A rota nacional reserva de
R$ 10 a R$ 16 mil menos de capital em todos os preços, então se o objetivo for puramente
minimizar capital ela ganha por pouco — mas custa VPL.

Ainda assim, **faça as duas ligações** (Grupo MF e Covre, fabricantes brasileiros de
lavadoras automáticas): pergunte se têm modelo **sem escova**, se é **credenciado no BNDES**,
e o preço. Se vier abaixo de R$ 134 mil, troca a decisão. E há um ganho que não está na
tabela: assistência técnica e peças no Brasil valem muito para a unidade que vai virar padrão
da rede.

### 11.5 Os dois arranjos em aberto

Os dois ficam na mesa. Não são "o recomendado e uma variante": são duas decisões de caixa
igualmente defensáveis, e a escolha entre elas não é financeira.

| | **Sem dívida — 100% equity** | **Com dívida de R$ 120 mil** |
|---|---|---|
| Capex | R$ 323.925 (enxuto) | R$ 323.925 (enxuto) |
| Capital de giro | R$ 45.000 | R$ 45.000 |
| Dívida — cooperativa local | — | R$ 120.000 a ~21% a.a., 60 meses, 6 de carência |
| Pré-venda de 80 fundadores | R$ 69.520 | R$ 69.520 |
| **Capital a reservar (equity)** | **R$ 372.353** | **R$ 274.178** |
| 1ª tranche, na assinatura | R$ 299.405 | R$ 179.405 |
| A chamar durante a rampa | R$ 71.473 | R$ 92.531 |
| **TIR do equity** | **32,9%** | **37,1%** |
| **VPL @ 18% a.a.** | **R$ 147.622** | R$ 140.020 |
| Payback | 33 meses | 33 meses |
| EBITDA maduro | R$ 16.745/mês (31,0%) | R$ 16.745/mês (31,0%) |

**R$ 99 mil mais de capital e 4,7 pontos menos de TIR — mas R$ 7,6 mil MAIS de valor.** A
dívida a 21% a.a. custa mais que a TMA de 18%: ela compra eficiência de capital e vende valor.
Em VPL é quase empate, e é por isso que a decisão não sai da planilha.

#### O que decide, já que o VPL não decide

**Escolha 100% equity se:**

- o dinheiro está disponível e não tem uso melhor nos próximos 5 anos;
- você prefere não dar **aval pessoal** — em PJ nova, a cooperativa quase sempre exige;
- a rampa pode atrasar dois meses sem que nada quebre. Com dívida, há parcela no mês 7 (depois
  da carência de 6) venha ou não venha assinante;
- você quer fechar o negócio em semanas, não meses. Negociar R$ 120 mil com cooperativa leva
  de 3 a 6 semanas e pode voltar com taxa pior, prazo menor ou carência de 3 meses em vez de 6.

**Escolha equity + dívida se:**

- o capital é escasso, ou tem uso melhor em outro lugar (inclusive segurar caixa para a Fase 2);
- você quer entrar com menos e preservar reserva pessoal durante a rampa;
- a cooperativa oferecer **pelo menos 6 meses de carência** e taxa até 24% a.a. Acima disso, a
  conta piora rápido: a 26% o VPL cai para R$ 143.985.

**O que não muda entre os dois:** o payback de 33 meses, o EBITDA maduro, o ponto de
equilíbrio de 134 assinantes e o mínimo de ~400 para pagar a TMA. A estrutura de capital não
muda a operação — muda só quem financia a espera.

#### O cap table em cada um

Na divisão escolhida (25 / 25 / 50 — ver 11.5b), com aporte proporcional e capital chamado em
tranches:

| | Sem dívida | Com dívida |
|---|---|---|
| Investidor A (25%) | R$ 93.088 | R$ 68.544 |
| Investidor B (25%) | R$ 93.088 | R$ 68.544 |
| **Antonio (50%)** | **R$ 186.177** | **R$ 137.089** |
| **Total** | **R$ 372.353** | **R$ 274.178** |
| TIR de todos | **32,9%** | **37,1%** |

Todas as outras divisões (50/50, 33,33 × 3 e a de desempate), nos dois arranjos, estão em
[CENARIOS.md](CENARIOS.md) §2.

#### Uma recomendação, já que você vai ter de escolher

**Leve os dois para a conversa com o investidor e deixe que o apetite dele desempate.** É
informação que ele vai pedir de qualquer forma, e mostrar as duas contas prontas vale mais do
que defender uma. Na prática:

- Investidor que quer **colocar menos e entrar rápido** prefere o arranjo com dívida — e aceita
  que o negócio tenha uma parcela mensal.
- Investidor mais conservador, ou que estranha dívida em negócio novo, prefere 100% equity — e
  aceita pôr R$ 24,7 mil a mais por 25%.

Enquanto a proposta da cooperativa não chegar, **os dois seguem abertos**: o item de 15 dias da
Fase 0 existe para transformar "≈21% a.a." em número real. Se a proposta vier pior que 24% a.a.
ou com menos de 6 meses de carência, o 100% equity passa a ser a escolha por eliminação.

### 11.6 A divisão do equity — decidida em out/2026

O empreendedor optou por **50% para os dois investidores (25% cada) e 50% para ele**, com
aporte proporcional. A tabela abaixo é do arranjo **com dívida**; a mesma divisão sem dívida
está em 11.5, e as divisões 50/50 e 33,33 × 3 nos dois arranjos estão em
[CENARIOS.md](CENARIOS.md) §2.

| | Por investidor (25%) | Os dois (50%) | Antonio (50%) |
|---|---|---|---|
| Compromisso | R$ 68.544 | R$ 137.089 | R$ 137.089 |
| 1ª tranche, na assinatura | R$ 44.851 | R$ 89.702 | R$ 89.702 |
| **TIR** | **37,1%** | **37,1%** | **37,1%** |
| Payback | 33 meses | 33 meses | 33 meses |
| Distribuição madura | R$ 3.350/mês | R$ 6.701/mês | R$ 6.701/mês |
| Caixa em 60 meses | R$ 148.556 | R$ 297.112 | R$ 297.112 |
| Sobre o capital | 2,14x | 2,14x | 2,14x |
| VPL @ 18% | R$ 39.162 | R$ 78.324 | R$ 78.324 |

**Dinheiro igual, quota igual, retorno igual: 37,1% para os dois lados.** É a estrutura mais
simples de explicar e de vender — e é mais generosa com os investidores que a recomendação
anterior (que dava a eles 48% por R$ 150 mil, ou seja, menos quota por mais dinheiro).

O retorno de 37,1% dos dois lados **depende do capital ser chamado em tranches**, proporcional
à necessidade real. Se o investidor depositar os R$ 69 mil inteiros no dia da assinatura e o
dinheiro ficar parado até a obra pedir, a TIR dele cai para **24,8%** — ainda boa, mas 14
pontos jogados fora por desenho ruim de contrato. A cláusula de chamada de capital não é
burocracia: vale 14 pontos de TIR.

> **Ressalva de governança: 50/50 trava a sociedade, e isso tem de ser resolvido no papel.**
>
> Na Limitada as deliberações se contam por capital. A **50% exatos ninguém tem maioria** — e
> qualquer matéria que exija mais da metade fica parada se os dois lados discordarem. Não é
> hipótese remota: é a forma mais comum de uma sociedade de dois sócios morrer.
>
> Duas saídas, e as duas custam quase nada agora:
>
> 1. **Economia 50/50, voto 50,5%/49,5%** — o Antonio fica com meio ponto a mais apenas para
>    desempate. A diferença no retorno é irrelevante (R$ 1,4 mil de capital); o efeito na
>    governança é total. **É a recomendação.**
> 2. **50/50 exato, com cláusula de desempate escrita**: voto de qualidade do administrador
>    sobre uma lista fechada de matérias operacionais, e cláusula *buy-sell* (quem propõe um
>    preço aceita vender ou comprar por ele) para impasse em matéria estrutural. Funciona, mas
>    exige advogado e disciplina de redação.
>
> O que **não** se faz é assinar 50/50 sem nenhuma das duas e descobrir o problema na primeira
> discordância séria. Isso também está no [resumo para investidor](RESUMO-INVESTIDOR.md), item
> 5 das proteções — dizer isso na entrada é o que faz o investidor confiar na estrutura.

### 11.7 As seis cláusulas que valem mais que a taxa

**1. A marca fica na PJ 1, 100% sua, e o pedido no INPI é feito no nome dela — antes de os
investidores assinarem.** Esta é a cláusula mais valiosa deste documento. Se a marca estiver
na PJ 2, você vendeu 48% da futura franqueadora por R$ 150 mil. A franqueadora vale, sozinha,
**R$ 1,26 milhão de VPL** ([BP-REDE.md](BP-REDE.md) seção 2). Os investidores estão
comprando uma loja em Piumhi, não a rede.

**2. Contrato de licença da PJ 1 para a PJ 2, assinado antes da entrada deles, com o royalty
declarado e com carência.** Sugestão: 0% nos primeiros 24 meses — não há serviço de
franqueadora a pagar ainda — e 6% a partir do mês 25, igual a qualquer franqueado. Declarado
na entrada é estrutura legítima; combinado depois é transferência entre partes relacionadas
que eles podem contestar, e com razão.

**3. Direito de preferência deles na primeira rodada da PJ 1.** Eles financiaram o campo de
provas; é justo e custa zero agora. Se quiser ser generoso e alinhar de verdade, 5% a 10% da
PJ 1 para o grupo que entrou na Fase 1 resolve o assunto para sempre.

**4. Capital chamado em tranches.** R$ 179.405 na assinatura e o restante em chamadas de
capital durante a rampa, com prazo de 15 dias e consequência clara para quem não atender.
Aumenta a TIR deles e evita dinheiro parado em conta.

**5. Retorno preferencial e opção de compra.** Distribuições preferenciais aos investidores
até recuperarem 1,0× o capital, depois pro-rata. E uma **opção de compra sua** sobre as quotas
deles a partir do mês 36, pelo maior entre 2,0× o capital aportado e 4× o EBITDA dos últimos
12 meses. Protege a entrada deles e te deixa consolidar depois.

**6. Governança enxuta.** Você como administrador único. Matérias reservadas com quórum
qualificado: venda de ativo relevante, novo endividamento acima de R$ 50 mil, mudança de
objeto social, distribuição abaixo do mínimo, entrada de novo sócio. Relatório mensal com
assinantes, lavagens/dia, churn e EBITDA — o mesmo painel que a rede vai usar depois.

### 11.8 Veículo e pendências para o contador e o advogado

**Sociedade Limitada** para a PJ 2, com acordo de quotistas separado do contrato social. É o
que um investidor do interior entende e o que o banco aceita como garantia.

Se algum investidor não quiser aparecer no CNPJ nem ter exposição operacional, existe a
**SCP (Sociedade em Conta de Participação)**, em que ele é sócio oculto. **Não feche sem
parecer do contador:** o enquadramento tributário da SCP e a compatibilidade com o Simples
Nacional têm regra própria e podem anular a vantagem.

Pendências que precisam de profissional habilitado antes da assinatura:

1. **Anexo III ou Anexo V do Simples** — vale R$ 47 mil por ano (seção 4).
2. **Tratamento do pró-labore** e da CPP dentro do DAS.
3. **Enquadramento da SCP**, se algum investidor pedir.
4. **Acordo de quotistas**: preferência, opção de compra, matérias reservadas, saída.
5. **Registro da marca no INPI em nome da PJ 1**, antes de qualquer assinatura.

---

## 12. O preço de fundador

**Recomendação: R$ 79/mês no plano Ilimitada, travado por 24 meses, 80 vagas, com três
limites de uso escritos.** O preço está certo; o que falta no site são os limites.

### 12.1 Por que R$ 79

O custo variável é de R$ 5,47 por lavagem. Somando o Simples (10,8% efetivo no cenário
base) e o meio de pagamento (1,5%), a margem de contribuição por assinante depende do
preço **e do uso**:

| Preço | 4 lav/mês | 6 lav/mês | 8 lav/mês | 10 lav/mês | 12 lav/mês | 15 lav/mês |
|---|---|---|---|---|---|---|
| R$ 69 | 38,65 | 27,72 | 16,79 | 5,85 | **−5,08** | **−21,48** |
| R$ 74 | 43,03 | 32,10 | 21,17 | 10,24 | **−0,69** | **−17,09** |
| **R$ 79** | **47,42** | **36,49** | **25,55** | **14,62** | **3,69** | **−12,71** |
| R$ 84 | 51,80 | 40,87 | 29,94 | 19,01 | 8,08 | **−8,32** |
| R$ 89 | 56,19 | 45,26 | 34,32 | 23,39 | 12,46 | **−3,94** |
| R$ 99 (tabela) | 64,96 | 54,03 | 43,09 | 32,16 | 21,23 | 4,83 |

A escolha é entre duas coisas que se puxam: desconto que faz a pessoa decidir, e margem
que sobrevive ao uso real.

- **R$ 79 é 20% abaixo da tabela.** É o desconto que lê como oferta de verdade — "de 99 por
  79" — e ainda deixa R$ 36,49 de margem na premissa de 6 lavagens/mês.
- **R$ 69 custa R$ 28.800 em 12 meses** contra R$ 19.200 do R$ 79, e a margem zera em 11,1
  lavagens/mês em vez de 12,7. São R$ 9.600 a mais de desconto para comprar uma decisão
  que, de quem já estava interessado, os R$ 79 já compravam.
- **R$ 89 é só 10% de desconto.** Não se sustenta como condição de fundador para quem está
  pagando por uma loja que ainda não existe.

O que o desconto custa, e o caixa que a pré-venda anual traz:

| | R$ 69 | R$ 74 | **R$ 79** | R$ 84 | R$ 89 |
|---|---|---|---|---|---|
| Desconto, 12 meses | R$ 28.800 | R$ 24.000 | **R$ 19.200** | R$ 14.400 | R$ 9.600 |
| Uso em que a margem zera | 11,1 | 11,9 | **12,7** | 13,5 | 14,3 |
| Anual (12 pelo preço de 11) | R$ 759 | R$ 814 | **R$ 869** | R$ 924 | R$ 979 |
| Caixa dos 80 fundadores | R$ 60.720 | R$ 65.120 | **R$ 69.520** | R$ 73.920 | R$ 78.320 |

### 12.2 Os três limites que faltam no site — e são o que protege o preço

Hoje o site vende "Ilimitada por R$ 79, travado enquanto a assinatura estiver ativa", sem
nenhum limite escrito. **Isso é uma exposição aberta, não um detalhe de redação.** A R$ 79
a margem zera em 12,7 lavagens/mês. Três cláusulas resolvem:

1. **Uma placa, cadastrada no ato.** Sem isso a assinatura vira plano de família: dois ou
   três carros no preço de um. É o modo de abuso mais provável e o mais fácil de evitar.
2. **Uso pessoal, não comercial.** É o limite que mais importa em Piumhi. Um motorista de
   aplicativo lavando todo dia são 30 lavagens/mês: **R$ 164 de custo variável sobre R$ 79
   de receita — prejuízo de R$ 85/mês naquele assinante.** Frota, táxi e aplicativo pagam
   plano próprio.
3. **Uma lavagem por dia.** É o padrão do setor, é fácil de explicar e não incomoda
   ninguém de uso normal.

Com os três, "ilimitada" continua verdade para o cliente comum e o pior caso realista fica
em ~8 lavagens/mês, onde a margem ainda é de R$ 25,55.

### 12.3 "Travado para sempre" é o erro que não dá para desfazer

O site diz que o preço vale *enquanto a assinatura estiver ativa* — na prática, para
sempre. A R$ 79 de hoje, com 5% de inflação ao ano, vale R$ 48 em dez anos. E os dois
maiores custos variáveis — água e energia — sobem historicamente acima do IPCA; a própria
correção da tarifa da CEMIG nesta revisão (de R$ 0,98 para R$ 1,11, 13% de uma vez) é a
demonstração.

**Recomendação: travado por 24 meses, depois reajuste anual pelo IPCA, com a condição de
fundador mantida como desconto permanente sobre a tabela.** O fundador continua sendo
fundador — paga sempre ~20% menos que a tabela da época — mas a loja não fica com uma
coorte de 80 assinantes congelados em um preço que o custo já deixou para trás.

Vinte e quatro meses é tempo suficiente para a promessa parecer séria e curto o bastante
para a loja sobreviver a ela. É também, não por coincidência, o prazo em que a Fase 2
começa.

### 12.4 Quando cobrar

A pré-venda anual de R$ 869 traz R$ 69.520 ao mês 0 e é a alavanca de caixa da seção 11.3
— mas ela significa **receber de 80 pessoas por uma loja que ainda não está construída**.
Em uma cidade de 36 mil habitantes, se a obra atrasar isso não é um problema de fluxo de
caixa, é um problema de reputação que fecha o negócio antes de abrir.

**Recomendação: a reserva é grátis e sem cobrança, como o site já diz.** A cobrança do
plano anual só é oferecida **depois que a máquina estiver fisicamente instalada e houver
data de inauguração firmada** — na prática, umas três semanas antes de abrir. Isso adia o
caixa da pré-venda do mês 0 para o fim da obra e reduz o efeito da alavanca; é o preço de
não vender o que ainda não existe, e vale a pena pagá-lo.

Quem quiser antecipar o caixa de verdade tem a opção honesta do sinal simbólico (R$ 50 a
R$ 100, abatido na primeira mensalidade, devolução por escrito a qualquer momento): derruba
o número de reservas e sobe muito a conversão, porque a lista fica menor e real. Mas é
dinheiro com obrigação de devolver — **não é equity e não entra como redução de capital no
modelo.**

---

## 13. Fase 0 — os 90 dias antes de comprar a máquina

| Prazo | Ação | Por que decide |
|---|---|---|
| 7 dias | Baixar a planilha do Senatran e confirmar a frota de Piumhi | É a premissa de demanda do plano inteiro |
| 7 dias | Busca de anterioridade no INPI e definição do nome | Trava o gasto com fachada e adesivagem |
| 7 dias | Parecer do contador: Anexo III ou V, CNAE e tratamento do pró-labore | Vale R$ 47 mil por ano |
| 15 dias | CEMIG: tensão no ponto e prazo de aumento de carga | Define 220 V ou 380 V no pedido da máquina |
| 15 dias | SAAE: **tarifa do m³ acima dos 30** e **como o esgoto é cobrado** (o mínimo de 30 m³ por R$ 93,59 já está confirmado e não manda na conta — seção 4.1) | Linha de custo variável, para sempre |
| 15 dias | Prefeitura: licença ambiental e exigência de caixa separadora | Pode mudar a obra civil inteira |
| 30 dias | Três orçamentos locais de obra civil, elétrica e separadora, com escopo escrito | Valida ou derruba os R$ 324 mil, e a contingência de 5% é fina |
| 30 dias | Negociar o aluguel **com opção de compra** e prazo de 10 anos | Protege R$ 142 mil de benfeitoria |
| 30 dias | Ligar para o distribuidor brasileiro do fabricante | Números reais de operação no Brasil |
| 30 dias | **Site no ar e campanha dos 80 fundadores** | Transforma premissa de demanda em evidência |
| 60 dias | Fechar o fornecedor: 60 Hz, tensão, Modbus, kit de peças, garantia | Destrava a obra e o cronograma |
| 90 dias | Constituir a PJ da operação | Para contratar, faturar e emitir nota |
| **7 dias** | **Registrar a marca no INPI em nome da PJ 1, antes de qualquer conversa com investidor** | Sem isso você vende 48% da futura franqueadora por R$ 150 mil |
| 15 dias | Cooperativa de crédito local: proposta de R$ 120 mil com 6 a 12 meses de carência | Libera R$ 99 mil de capital próprio |
| 15 dias | Ligar para Grupo MF e Covre: têm modelo sem escova? é credenciado no BNDES? preço? | Abaixo de R$ 134 mil muda a decisão da máquina |
| 30 dias | Acordo de quotistas com advogado e contrato de licença PJ 1 → PJ 2 | Declarado na entrada é legítimo; combinado depois é contestável |

**A campanha de fundadores é o teste mais barato deste plano, e agora é também fonte de
capital.** Custa cerca de R$ 22 mil
e responde à pergunta de R$ 274 mil. Se as 80 reservas não saírem em Piumhi — cidade
onde você nasceu e tem rede — o problema não é a campanha.

A franqueadora não entra em nenhuma linha desta tabela. Ela é a Fase 2, e só começa a
ser formatada quando esta unidade tiver doze meses de número auditável.
