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

| | |
|---|---|
| Capex de implantação | **R$ 399.060** |
| Capital de giro | **R$ 55.000** |
| **Investimento total** | **R$ 454.060** |
| **Pico de caixa (cenário conservador)** | **R$ 472.671** no mês 6 |

**Capital a reservar para a Fase 1: R$ 475 mil.** A franqueadora só volta à mesa depois
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
| **Equilíbrio operacional** | **~178** | **1,3%** |
| **Mínimo para TIR ≥ 18%** | **345** | **2,5%** |

É assim que a premissa de demanda deve ser julgada: **precisamos de 2,5% dos carros de
Piumhi para o projeto pagar 18% ao ano.** Não de 46 lavagens por dia abstratas.

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
mais simples e contingência de 5%. **A TIR sobe de 37,5% para 48,1%** — menos capital
parado na largada. O custo é um lançamento menos impressionante, o que em negócio de
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

### Tributação

**Simples Nacional, Anexo III.** A R$ 650 mil de receita anual, a alíquota efetiva é
de **10,8%**.

> **Risco fiscal a resolver com contador, antes de abrir.** Se a atividade for
> enquadrada no **Anexo V** (o que depende da classificação do CNAE 4520-0/05 e de
> incidir ou não o Fator R, com folha de apenas 5% da receita), a alíquota vai para
> **17,9%**. O EBITDA cai de R$ 20.841 para R$ 16.950/mês e a **TIR cai de 37,5% para
> 26,0%**. Não é detalhe contábil: são R$ 47 mil por ano.

---

## 5. Resultado

| | Conservador | **Base** | Otimista |
|---|---|---|---|
| Assinantes | 380 | **500** | 650 |
| Receita madura/mês | R$ 40.760 | **R$ 54.100** | R$ 72.350 |
| Lavagens/dia | 72 | **95** | 126 |
| Custo variável | R$ 12.048 (29,6%) | **R$ 15.876 (29,3%)** | R$ 20.921 (28,9%) |
| EBITDA maduro/mês | R$ 13.130 | **R$ 20.841** | R$ 31.273 |
| Margem EBITDA | 32,2% | **38,5%** | 43,2% |
| Investimento | R$ 454.060 | **R$ 454.060** | R$ 454.060 |
| **Payback** | **48 meses** | **33 meses** | **24 meses** |
| **TIR (60 meses)** | **15,8%** | **37,5%** | **66,5%** |
| **VPL @ 18% a.a.** | **−R$ 25.806** | **+R$ 235.282** | **+R$ 595.064** |
| VPL @ 22% a.a. | −R$ 67.286 | +R$ 173.204 | +R$ 504.966 |
| ROI 5 anos | 161% | 250% | 372% |

**Ponto de equilíbrio:** R$ 19.291/mês — 36% da receita madura, 34 lavagens/dia,
~178 assinantes.

**O cenário conservador não paga a TMA.** A 380 assinantes a TIR é 15,8% e o VPL é
negativo. O projeto precisa de 345 assinantes para empatar a 18% ao ano. Entre 345 e 500
está a diferença entre um negócio bom e um negócio que não valeu o risco.

### Sobre a TMA de 18%

Com a **Selic a 14% a.a.** (agosto/2026) e IPCA em torno de 4,7%, uma TMA de 18% embute
apenas 4 pontos de prêmio de risco sobre o CDI — para um negócio novo, de um produto que
ninguém na cidade ainda comprou, com máquina importada. **É pouco.** A coluna de 22%
está na tabela por isso. O cenário base sobrevive aos dois; o conservador não sobrevive
a nenhum.

---

## 6. Sensibilidade

| Cenário | EBITDA/mês | TIR | VPL @ 18% |
|---|---|---|---|
| **BASE** | R$ 20.841 | 37,5% | R$ 235.282 |
| Receita −15% | R$ 13.943 | 18,1% | R$ 921 |
| Receita −25% | R$ 9.345 | 4,4% | −R$ 155.695 |
| Aluguel a R$ 5.000 | R$ 18.841 | 30,7% | R$ 154.223 |
| Simples no Anexo V | R$ 16.950 | 26,0% | R$ 95.089 |
| Capex +20% (câmbio/obra) | R$ 20.841 | 29,9% | R$ 165.936 |
| Versão enxuta (capex R$ 328 mil) | R$ 20.841 | 48,1% | R$ 307.024 |
| Já pagando royalty 6% + fundo 2% + tecnologia | R$ 15.813 | 22,9% | R$ 58.401 |

**Tolerância de receita: exatamente −15%.** Abaixo disso o projeto encosta na TMA.

### O risco número 1 não é a demanda. É o uso do plano Ilimitada.

| Lavagens/mês por assinante Ilimitada | Lavagens/dia | Custo variável/mês | EBITDA/mês | TIR |
|---|---|---|---|---|
| 4 | 77 | R$ 12.984 | R$ 23.733 | 45,2% |
| 5 | 86 | R$ 14.430 | R$ 22.287 | 41,4% |
| **6 (premissa)** | **95** | **R$ 15.876** | **R$ 20.841** | **37,5%** |
| 8 | 114 | R$ 18.768 | R$ 17.949 | 29,6% |
| 10 | 132 | R$ 21.659 | R$ 15.057 | 21,6% |
| 12 | 150 | R$ 24.551 | R$ 12.165 | **13,2%** |

A receita não muda em nenhuma dessas linhas — só o custo. **O plano Ilimitada é a única
variável que pode matar o projeto sem que a demanda caia um real.** O assinante de
R$ 79 que lava doze vezes por mês consome R$ 63 de água, energia e química: sobra
R$ 16 antes de imposto e custo fixo.

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
| Demanda abaixo de 345 assinantes | Alto | Pré-venda de 80 fundadores **antes** da obra |
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

Nenhum desses pontos invalida a tese. Os itens 1, 3, 4 e 7 se resolvem em trinta dias e
custam quase nada — e é isso que a Fase 0 abaixo existe para fazer.

---

## 11. Fase 0 — os 90 dias antes de comprar a máquina

| Prazo | Ação | Por que decide |
|---|---|---|
| 7 dias | Baixar a planilha do Senatran e confirmar a frota de Piumhi | É a premissa de demanda do plano inteiro |
| 7 dias | Busca de anterioridade no INPI e definição do nome | Trava o gasto com fachada e adesivagem |
| 7 dias | Parecer do contador: Anexo III ou V, e CNAE correto | Vale R$ 47 mil por ano |
| 15 dias | CEMIG: tensão no ponto e prazo de aumento de carga | Define 220 V ou 380 V no pedido da máquina |
| 15 dias | SAAE Piumhi: tarifa comercial de água e esgoto | Linha de custo variável, para sempre |
| 15 dias | Prefeitura: licença ambiental e exigência de caixa separadora | Pode mudar a obra civil inteira |
| 30 dias | Três orçamentos locais de obra civil, elétrica e separadora | Valida ou derruba os R$ 399 mil |
| 30 dias | Negociar o aluguel **com opção de compra** e prazo de 10 anos | Protege R$ 142 mil de benfeitoria |
| 30 dias | Ligar para o distribuidor brasileiro do fabricante | Números reais de operação no Brasil |
| 30 dias | **Site no ar e campanha dos 80 fundadores** | Transforma premissa de demanda em evidência |
| 60 dias | Fechar o fornecedor: 60 Hz, tensão, Modbus, kit de peças, garantia | Destrava a obra e o cronograma |
| 90 dias | Constituir a PJ da operação | Para contratar, faturar e emitir nota |

**A campanha de fundadores é o teste mais barato deste plano.** Custa cerca de R$ 22 mil
e responde à pergunta de R$ 475 mil. Se as 80 reservas não saírem em Piumhi — cidade
onde você nasceu e tem rede — o problema não é a campanha.

A franqueadora não entra em nenhuma linha desta tabela. Ela é a Fase 2, e só começa a
ser formatada quando esta unidade tiver doze meses de número auditável.
