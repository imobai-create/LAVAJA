# Fase 1 — Loja modelo de Piumhi/MG

Business plan da primeira unidade. **Área alugada a R$ 3.000/mês**, capex apenas de
implantação do lava jato, sem terreno. Unidade própria: não paga taxa de franquia,
royalty, fundo de marketing nem taxa de tecnologia.

Modelo em `docs/bp/piumhi.py`. Planilha com fórmulas vivas:
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
| Capex de implantação | R$ 399.060 | **R$ 328.000** (enxuto) | **R$ 328.000** (enxuto) |
| Capital de giro | R$ 55.000 | **R$ 45.000** | **R$ 45.000** |
| Dívida | — | — | **R$ 120.000** a ~21% a.a. |
| Pré-venda de 80 fundadores | — | **R$ 69.520** | **R$ 69.520** |
| **Capital a reservar** | **R$ 480.111** | **R$ 374.953** | **R$ 276.011** |
| TIR do equity | 25,6% | **34,3%** | **39,0%** |
| VPL @ 18% | R$ 93.429 | **R$ 164.250** | R$ 156.648 |

**Capital a reservar no arranjo cru: R$ 480 mil** (R$ 496 mil no conservador). Isso é capex
cheio e 100% capital próprio, sem nenhuma alavanca. A [seção 11](#11-estrutura-de-capital)
mostra como esse número cai para **R$ 375 mil sem dívida nenhuma** ou **R$ 276 mil com dívida
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
| **Equilíbrio operacional** | **~232** | **1,7%** |
| **Mínimo para TIR ≥ 18%** | **~400** | **2,9%** |

É assim que a premissa de demanda deve ser julgada: **precisamos de 2,9% dos carros de
Piumhi para o projeto pagar 18% ao ano.** Não de 46 lavagens por dia abstratas.

(Os dois números de referência já pagam o pró-labore de R$ 3.500/mês — ver a correção na
seção 4. Sem ele seriam 1,3% e 2,5%, que é o que versões anteriores deste documento traziam.)

---

## 2. Capex de implantação — linha por linha

Câmbio de planejamento **R$ 5,30/USD** (Focus para o fim de 2026: R$ 5,20; entre o
pedido e o pagamento final passam 60 a 120 dias).

| Item | R$ |
|---|---|
| Máquina JM-70 posta em Piumhi (USD 23.000) | 121.900 |
| Interface Modbus/API + kit de peças de desgaste 2 anos (USD 2.000) | 10.600 |
| Obra civil: pórtico, baia coberta, piso com caimento, pátio 300 m² | 92.000 |
| Caixa separadora água/óleo + hidráulica + reservatório | 26.000 |
| Entrada de energia, quadro, cabeamento, projeto e ART | 24.000 |
| Laudo NR-12 com ART | 6.000 |
| Totem de pagamento PIX/cartão + câmera + CFTV + rede | 26.000 |
| 1 box de alta pressão + 2 aspiradores | 18.000 |
| Fachada, comunicação visual, iluminação | 19.000 |
| Software da unidade, integração e implantação | 12.000 |
| Projeto, licenças, alvarás, bombeiros, taxas | 14.000 |
| **Subtotal** | **369.500** |
| Contingência 8% | 29.560 |
| **CAPEX TOTAL** | **399.060** |

**Isto é R$ 73 mil acima dos R$ 326 mil que o Plano de Franquia usa para o formato
Express.** A diferença não é inflação de orçamento: é o que aparece quando se monta a
lista item por item, com NR-12, caixa separadora, totem e contingência. Cada linha acima
é discutível e deve ser desafiada com orçamento local — mas o número do plano original
está otimista.

### Capital de giro

| Item | R$ |
|---|---|
| Caução de 3 aluguéis | 9.000 |
| Campanha de pré-venda e inauguração | 22.000 |
| Estoque inicial de químicos | 6.000 |
| Colchão de 3 meses de custo fixo | 18.000 |
| **TOTAL** | **55.000** |

O colchão não é conservadorismo decorativo: **os meses 1 a 4 fecham com EBITDA
negativo** (−R$ 3.084 no mês 1), porque a base de assinantes ainda está em formação e o
custo fixo já é integral.

### Versão enxuta, se o capital apertar

Dá para entrar com **R$ 328 mil de capex + R$ 45 mil de giro = R$ 373 mil**: adiar a
câmera de placa (liberação por código do plano), adiar o box de alta pressão e os
aspiradores para o mês 6 pagos pelo caixa, pátio de 150 m² em vez de 300 m², fachada
mais simples e contingência de 5%. **A TIR sobe de 25,6% para 33,9%** e a tolerância de
receita de −6% para −10,6% — menos capital parado na largada e mais margem de erro. O custo é um lançamento menos impressionante, o que em negócio de
assinatura pesa mais do que parece.

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
| Água: 85 L a R$ 14,00/m³ (água + esgoto comercial) | 1,19 |
| Energia: 1,6 kWh a R$ 0,98/kWh | 1,57 |
| Químicos (detergente touchless, espuma, cera) | 2,50 |
| **Total por lavagem** | **5,26** |

Mais 1,5% da receita em meios de pagamento (PIX + cartão).

O 1,6 kWh é **cálculo próprio pelos componentes** da JM-70 (bomba de 15 kW, 4
ventiladores de 22 kW, auxiliares), não o 0,6–1,2 kWh declarado pelo fornecedor. Tarifas
de água e energia são **estimativas**: confirmar com SAAE Piumhi e CEMIG.

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
> | EBITDA maduro/mês | R$ 20.841 (38,5%) | **R$ 17.341 (32,1%)** |
> | TIR, capex cheio e 100% equity | 37,5% | **25,6%** |
> | VPL @ 18% | R$ 235.282 | **R$ 93.429** |
> | Capital a reservar | R$ 472.671 | **R$ 480.111** |
>
> **O número de referência para conversa com investidor é o da coluna da direita.** Um
> investidor compra retorno de capital; se o operador não é pago, o retorno dele está sendo
> subsidiado pelo trabalho não remunerado do sócio — e isso não dura.
>
> Em Simples Nacional Anexo III a CPP patronal está dentro do DAS, então os R$ 3.500 custam
> R$ 3.500 à empresa, mais o INSS de 11% retido do sócio. **Confirmar com o contador junto da
> questão Anexo III / Anexo V.**
>
> A seção 11 mostra que, com o arranjo de capital recomendado, a TIR volta para **39,0%**
> mesmo pagando o pró-labore — o ganho vem de capex enxuto e alavancagem, não de deixar de
> pagar quem trabalha.

### Tributação

**Simples Nacional, Anexo III.** A R$ 650 mil de receita anual, a alíquota efetiva é
de **10,8%**.

> **Risco fiscal a resolver com contador, antes de abrir.** Se a atividade for
> enquadrada no **Anexo V** (o que depende da classificação do CNAE 4520-0/05 e de
> incidir ou não o Fator R, com folha de apenas 5% da receita), a alíquota vai para
> **17,9%**. O EBITDA cai de R$ 17.341 para R$ 13.450/mês e a **TIR cai de 25,6% para
> 14,1%**, abaixo da TMA. Não é detalhe contábil: são R$ 47 mil por ano.

---

## 5. Resultado

Capex cheio, 100% capital próprio, **com pró-labore de R$ 3.500/mês**. É o arranjo cru: a
seção 11 mostra o que a estrutura de capital faz com estes números.

| | Conservador | **Base** | Otimista |
|---|---|---|---|
| Assinantes | 380 | **500** | 650 |
| Receita madura/mês | R$ 40.760 | **R$ 54.100** | R$ 72.350 |
| Lavagens/dia | 72 | **95** | 126 |
| Custo variável | R$ 12.048 (29,6%) | **R$ 15.876 (29,3%)** | R$ 20.921 (28,9%) |
| EBITDA maduro/mês | R$ 9.630 | **R$ 17.341** | R$ 27.773 |
| Margem EBITDA | 23,6% | **32,1%** | 38,4% |
| Capital a reservar | R$ 496.157 | **R$ 480.111** | R$ 465.601 |
| **Payback** | **60 meses** | **39 meses** | **27 meses** |
| **TIR (60 meses)** | **3,7%** | **25,6%** | **54,2%** |
| **VPL @ 18% a.a.** | **−R$ 167.659** | **+R$ 93.429** | **+R$ 453.211** |
| VPL @ 22% a.a. | −R$ 199.251 | +R$ 41.238 | +R$ 373.001 |
| ROI 5 anos | 114% | 203% | 325% |

**No arranjo de capital recomendado** (capex enxuto, dívida de R$ 120 mil, pré-venda dos
fundadores — seção 11), o cenário base vira: capital a reservar de **R$ 276 mil**, TIR do
equity de **39,0%** e VPL de **R$ 156.648**.

**Ponto de equilíbrio:** R$ 25.137/mês — 46,5% da receita madura, 44 lavagens/dia,
~232 assinantes. (Com pró-labore. Sem ele seria R$ 19.291 e 178 assinantes.)

**O cenário conservador não paga a TMA, e agora nem de longe.** A 380 assinantes a TIR é
3,7% e o VPL é negativo em R$ 168 mil. O projeto precisa de ~400 assinantes para empatar a 18% ao ano. Entre 400 e 500
está a diferença entre um negócio bom e um negócio que não valeu o risco. Com o arranjo
de capital da seção 11, o mesmo projeto empata com os mesmos ~400 assinantes, mas rende
39,0% no cenário base em vez de 25,6%.

### Sobre a TMA de 18%

Com a **Selic a 14% a.a.** (agosto/2026) e IPCA em torno de 4,7%, uma TMA de 18% embute
apenas 4 pontos de prêmio de risco sobre o CDI — para um negócio novo, de um produto que
ninguém na cidade ainda comprou, com máquina importada. **É pouco.** A coluna de 22%
está na tabela por isso. O cenário base sobrevive aos dois; o conservador não sobrevive
a nenhum.

---

## 6. Sensibilidade

Já com o pró-labore de R$ 3.500/mês. Capex cheio e 100% capital próprio, para isolar o efeito
de cada variável da estrutura de capital (seção 11).

| Cenário | EBITDA/mês | TIR | VPL @ 18% |
|---|---|---|---|
| **BASE** | R$ 17.341 | 25,6% | R$ 93.429 |
| Receita −15% | R$ 10.443 | 6,1% | −R$ 140.932 |
| Receita −25% | R$ 5.845 | −8,1% | −R$ 297.548 |
| Aluguel a R$ 5.000 | R$ 15.341 | 19,0% | R$ 12.370 |
| Simples no Anexo V | R$ 13.450 | 14,1% | −R$ 46.764 |
| Capex +20% (câmbio/obra) | R$ 17.341 | 19,7% | R$ 24.083 |
| **Versão enxuta (capex R$ 328 mil)** | R$ 17.341 | **33,9%** | **R$ 165.171** |
| Já pagando royalty 6% + fundo 2% + tecnologia | R$ 12.313 | 11,0% | −R$ 83.452 |

**Tolerância de receita: −6% com capex cheio, −10,6% com capex enxuto.** Pagar o operador
estreitou muito a margem de erro: antes eu reportava −15%, e aquele número não pagava o
pró-labore. **Esta é a razão mais forte para fazer a versão enxuta** — ela não é só mais
barata, é o que devolve margem de erro ao projeto.

A última linha merece leitura: pagando royalty, fundo e taxa de tecnologia, a mesma unidade
rende 11,0%. É a prova aritmética de que a franqueadora não pode nascer antes de a praça
estar provada — e a base da correção registrada em [BP-REDE seção 1](BP-REDE.md).

### O risco número 1 não é a demanda. É o uso do plano Ilimitada.

| Lavagens/mês por assinante Ilimitada | Lavagens/dia | Custo variável/mês | EBITDA/mês | TIR |
|---|---|---|---|---|
| 4 | 77 | R$ 12.984 | R$ 20.233 | 33,3% |
| 5 | 86 | R$ 14.430 | R$ 18.787 | 29,5% |
| **6 (premissa)** | **95** | **R$ 15.876** | **R$ 17.341** | **25,6%** |
| 8 | 114 | R$ 18.768 | R$ 14.449 | 17,7% |
| 10 | 132 | R$ 21.659 | R$ 11.557 | 9,5% |
| 12 | 150 | R$ 24.551 | R$ 8.665 | **0,9%** |

A receita não muda em nenhuma dessas linhas — só o custo. **O plano Ilimitada é a única
variável que pode matar o projeto sem que a demanda caia um real.** O assinante de
R$ 79 que lava doze vezes por mês consome R$ 63 de água, energia e química: sobra
R$ 16 antes de imposto e custo fixo. A oito lavagens por mês o projeto já encosta na TMA;
a dez, está abaixo dela.

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
| Demanda abaixo de ~400 assinantes | Alto | Pré-venda de 80 fundadores **antes** da obra; equilíbrio operacional a 232 |
| Simples no Anexo V em vez do III | Alto | Parecer de contador antes de abrir (R$ 47 mil/ano) |
| Frota de Piumhi diferente do que a fonte diz | Alto | Baixar a planilha do Senatran — 15 minutos |
| Benfeitoria perdida no fim do aluguel | Alto | Contrato de 10 anos + opção de compra + indenização |
| Máquina 50 Hz / 380 V incompatível | **Crítico** | 60 Hz e tensão CEMIG por escrito no pedido |
| Câmbio entre pedido e pagamento | Médio | Travar câmbio ou orçar a R$ 5,60 |
| Tarifa de água/energia acima do estimado | Médio | Confirmar com SAAE e CEMIG antes de fechar o capex |
| Licença ambiental e caixa separadora | Médio | Consulta à Prefeitura antes de comprar o equipamento |
| Máquina parada por falta de peça | Alto | Kit de peças de 2 anos no pedido + distribuidor no Brasil |

---

## 10. O que ainda não está provado

1. **A frota de Piumhi vem de fonte secundária única.** Confirmar no Senatran.
2. **A receita madura nunca foi medida.** 500 assinantes = 3,7% dos automóveis da cidade.
   Nenhuma unidade da rede operou.
3. **Tarifas de água e energia são estimativas.** R$ 14/m³ e R$ 0,98/kWh. Confirmar.
4. **O enquadramento tributário é estimativa.** Anexo III ou V muda a TIR em 11 pontos.
5. **O consumo de 1,6 kWh é cálculo próprio**, não medição. O fornecedor declara 0,6–1,2.
6. **O uso médio do plano Ilimitada é a premissa mais frágil do modelo.** 6 lavagens/mês
   por assinante é estimativa sem base local.
7. **O capex de R$ 399 mil não tem orçamento local.** Cada linha precisa de três
   cotações em Piumhi.
8. **A dívida de R$ 120 mil a 21% é premissa, não proposta.** Nenhuma cooperativa foi
   consultada. PJ nova, sem histórico, pode receber taxa pior ou carência menor — e isso muda
   a seção 11. O BDMG Pronampe, que teria a melhor condição, exige receita do ano anterior e
   **só está disponível no ano 2**.
9. **A pré-venda de R$ 69,5 mil supõe 80 fundadores pagando 12 meses à vista.** Pode sair
   menos, e aí o capital a reservar sobe. É também o teste de demanda, então sair menos é
   informação, não só problema.
10. **O pró-labore de R$ 3.500 é escolha, não cálculo.** Acima de R$ 6.000 a TIR do arranjo
    recomendado cai para 25,2% e o projeto encosta na TMA.

Nenhum desses pontos invalida a tese. Os itens 1, 3, 4 e 7 se resolvem em trinta dias e
custam quase nada — e é isso que a Fase 0 abaixo existe para fazer.

---

## 11. Estrutura de capital

Objetivo: **o menor capital possível em risco**, sem estrangular a rampa, com um ou dois
investidores entrando e o controle e a marca preservados. Modelo em `docs/bp/capital.py`.

Todos os números desta seção **já pagam o pró-labore de R$ 3.500/mês**.

### 11.1 Primeiro reduzir a necessidade, depois dividi-la

| Arranjo | 1ª tranche | **Capital a reservar** | TIR do equity | VPL @ 18% |
|---|---|---|---|---|
| 1. Capex cheio, 100% equity | R$ 454.060 | **R$ 480.111** | 25,6% | R$ 93.429 |
| 2. Capex enxuto, 100% equity | R$ 373.000 | **R$ 399.051** | 33,9% | R$ 165.171 |
| 3. + pré-venda anual dos fundadores | R$ 303.480 | **R$ 374.953** | 34,3% | R$ 164.250 |
| **4. + dívida de R$ 120 mil a 21% a.a.** | **R$ 183.480** | **R$ 276.011** | **39,0%** | **R$ 156.648** |
| 5. + dívida de R$ 150 mil | R$ 153.480 | R$ 252.021 | 40,7% | R$ 154.747 |
| 6. + dívida de R$ 180 mil | R$ 123.480 | R$ 228.068 | 42,9% | R$ 152.846 |

**Do arranjo 1 para o 4: o capital cai 42%** — de R$ 480 mil para R$ 276 mil — e a TIR do
equity sobe de 25,6% para 39,0%.

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
mágica:** o VPL cai de R$ 165 mil para R$ 157 mil, porque 21% é acima da TMA de 18%. Você
troca R$ 8 mil de valor por R$ 99 mil de capital liberado. Com capital escasso, vale.

Onde buscar, em ordem de probabilidade real:

| Fonte | Condição | Observação |
|---|---|---|
| **Cooperativa de crédito local** (Sicoob, Sicredi) | ~21% a.a., 60 meses, 6 de carência | A mais provável para PJ nova em cidade do interior, com aval e relacionamento. **Comece por aqui.** |
| Banco comercial com aval | ~26% a.a. | Caro: derruba o VPL para R$ 144 mil. Último recurso. |
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
Peça por escrito junto das outras exigências da seção 12.

### 11.3 O pró-labore adiado: a alavanca que só você pode decidir

Se você passar os **12 primeiros meses sem retirada**:

| | Com pró-labore do mês 1 | Sem retirada nos 12 primeiros meses |
|---|---|---|
| Capital a reservar | R$ 276.011 | **R$ 244.735** |
| TIR do equity | 39,0% | **46,5%** |
| VPL @ 18% | R$ 156.648 | **R$ 195.090** |

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
| *rota chinesa, sem Finame* | *R$ 328.000* | *R$ 276.011* | *39,0%* | *R$ 156.648* |

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
| Capex | R$ 328.000 (enxuto) | R$ 328.000 (enxuto) |
| Capital de giro | R$ 45.000 | R$ 45.000 |
| Dívida — cooperativa local | — | R$ 120.000 a ~21% a.a., 60 meses, 6 de carência |
| Pré-venda de 80 fundadores | R$ 69.520 | R$ 69.520 |
| **Capital a reservar (equity)** | **R$ 374.953** | **R$ 276.011** |
| 1ª tranche, na assinatura | R$ 303.480 | R$ 183.480 |
| A chamar durante a rampa | R$ 71.473 | R$ 92.531 |
| **TIR do equity** | **34,3%** | **39,0%** |
| **VPL @ 18% a.a.** | **R$ 164.250** | R$ 156.648 |
| Payback | 33 meses | 33 meses |
| EBITDA maduro | R$ 17.341/mês (32,1%) | R$ 17.341/mês (32,1%) |

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
equilíbrio de 232 assinantes e o mínimo de ~400 para pagar a TMA. A estrutura de capital não
muda a operação — muda só quem financia a espera.

#### O cap table em cada um

Na divisão escolhida (25 / 25 / 50 — ver 11.5b), com aporte proporcional e capital chamado em
tranches:

| | Sem dívida | Com dívida |
|---|---|---|
| Investidor A (25%) | R$ 93.738 | R$ 69.003 |
| Investidor B (25%) | R$ 93.738 | R$ 69.003 |
| **Antonio (50%)** | **R$ 187.476** | **R$ 138.006** |
| **Total** | **R$ 374.953** | **R$ 276.011** |
| TIR de todos | **34,3%** | **39,0%** |

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
| Compromisso | R$ 69.003 | R$ 138.006 | R$ 138.006 |
| 1ª tranche, na assinatura | R$ 45.870 | R$ 91.740 | R$ 91.740 |
| **TIR** | **39,0%** | **39,0%** | **39,0%** |
| Payback | 33 meses | 33 meses | 33 meses |
| Distribuição madura | R$ 3.350/mês | R$ 6.701/mês | R$ 6.701/mês |
| Caixa em 60 meses | R$ 156.720 | R$ 313.441 | R$ 313.441 |
| Sobre o capital | 2,27x | 2,27x | 2,27x |
| VPL @ 18% | R$ 39.162 | R$ 78.324 | R$ 78.324 |

**Dinheiro igual, quota igual, retorno igual: 39,0% para os dois lados.** É a estrutura mais
simples de explicar e de vender — e é mais generosa com os investidores que a recomendação
anterior (que dava a eles 48% por R$ 150 mil, ou seja, menos quota por mais dinheiro).

O retorno de 39,0% dos dois lados **depende do capital ser chamado em tranches**, proporcional
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

**4. Capital chamado em tranches.** R$ 183.480 na assinatura e o restante em chamadas de
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

## 12. Fase 0 — os 90 dias antes de comprar a máquina

| Prazo | Ação | Por que decide |
|---|---|---|
| 7 dias | Baixar a planilha do Senatran e confirmar a frota de Piumhi | É a premissa de demanda do plano inteiro |
| 7 dias | Busca de anterioridade no INPI e definição do nome | Trava o gasto com fachada e adesivagem |
| 7 dias | Parecer do contador: Anexo III ou V, CNAE e tratamento do pró-labore | Vale R$ 47 mil por ano |
| 15 dias | CEMIG: tensão no ponto e prazo de aumento de carga | Define 220 V ou 380 V no pedido da máquina |
| 15 dias | SAAE Piumhi: tarifa comercial de água e esgoto | Linha de custo variável, para sempre |
| 15 dias | Prefeitura: licença ambiental e exigência de caixa separadora | Pode mudar a obra civil inteira |
| 30 dias | Três orçamentos locais de obra civil, elétrica e separadora | Valida ou derruba os R$ 399 mil |
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
e responde à pergunta de R$ 276 mil. Se as 80 reservas não saírem em Piumhi — cidade
onde você nasceu e tem rede — o problema não é a campanha.

A franqueadora não entra em nenhuma linha desta tabela. Ela é a Fase 2, e só começa a
ser formatada quando esta unidade tiver doze meses de número auditável.
