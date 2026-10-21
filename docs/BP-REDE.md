# Fase 2 — Plano macro da rede, com a questão imobiliária

Business plan da franqueadora. **Só começa a ser formatada depois de doze meses de
número auditável em Piumhi** ([BP-PIUMHI.md](BP-PIUMHI.md)).

Horizonte de 120 meses, TMA de 18% a.a. Planilha: `Modelo-Economico-Rede.xlsx`.
Data da versão: 2026-10-20.

---

## 0. Duas mudanças em relação à versão anterior

**O formato BOX saiu.** TIR de 9,4% contra TMA de 18%, VPL negativo, payback de 56 meses
num contrato de 60. Não existe mais em nenhuma linha deste plano. Decisão em
[DECISOES.md](DECISOES.md), ADR-008.

**Os números da franqueadora foram reconstruídos e ficaram menores.** A versão anterior
apontava EBITDA de R$ 1,657 milhão no ano 10 e TIR de 49,4%. Este modelo chega a
**R$ 865 mil e 42,6%**. A diferença não é pessimismo — são duas correções:

1. **O fundo de marketing de 2% deixou de ser margem.** Ele é vinculado: entra e sai em
   campanha. Tratá-lo como receita da franqueadora inflava o resultado.
2. **Tributação da franqueadora em Lucro Presumido**, a ~16% sobre serviços (royalty e
   taxa de tecnologia) e ~11,5% sobre aluguel, em vez de uma estimativa única.

O número menor é o número certo. Use este.

---

## 1. O problema que a Fase 2 tem de resolver

Com o capex real de implantação (R$ 399 mil) mais taxa de franquia de R$ 50 mil e giro,
**o franqueado entra com R$ 504 mil**. Numa praça típica de 30 a 80 mil habitantes, com
receita madura de R$ 48 mil/mês:

| Franqueado na estrutura atual | |
|---|---|
| Investimento | R$ 504.060 |
| Aluguel que ele paga a terceiro | R$ 3.000 |
| EBITDA maduro/mês | R$ 12.836 (26,7%) |
| Payback | 51 meses |
| **TIR** | **13,4%** |
| **VPL @ 18%** | **−R$ 56.541** |

**Esta franquia não é vendável.** TIR de 13,4% é menos que o CDI com a Selic a 14%.
Nenhum candidato com R$ 504 mil e um contador decente assina. E se assinar, quebra ou
reclama — e o problema volta para a marca.

> **Correção de out/2026, e ela é pesada: o modelo do franqueado também não remunerava quem
> administra a unidade.** Com pró-labore de R$ 3.500/mês para o operador:
>
> | | Sem pró-labore | **Com pró-labore de R$ 3.500** |
> |---|---|---|
> | A — ele constrói tudo (R$ 504 mil) | TIR 13,3% / VPL −R$ 57 mil | **TIR 1,7% / VPL −R$ 198 mil** |
> | B1 — nós construímos o ponto (R$ 310 mil) | TIR 27,3% / VPL +R$ 74 mil | **TIR 9,5% / VPL −R$ 68 mil** |
>
> **Nem o build-to-suit salva a franquia se o franqueado tiver de pagar um gerente.** Isso
> segmenta a oferta de forma decisiva:
>
> - **Franqueado operador**, que administra a própria unidade: o pró-labore é o salário dele e
>   o retorno de capital vem em cima. Para esse público, a estrutura B1 com ticket de
>   R$ 310 mil funciona — ele compra um emprego com retorno, e é um bom negócio.
> - **Franqueado investidor**, ausente, que contrata um gerente: **não fecha em praça de
>   R$ 48 mil/mês, em nenhuma estrutura.** Não venda para esse perfil, nem deixe a COF sugerir
>   que funciona.
>
> **Consequência prática para a Fase 2:** o perfil deixa de ser "quem tem R$ 310 mil" e passa a
> ser "quem tem R$ 310 mil **e vai operar**". É um funil muito mais estreito e muda o plano de
> captação. A alternativa é a praça entregar bem mais que R$ 48 mil/mês — o que remete ao
> limiar de R$ 64 mil da seção 4b.

É aqui que a ideia imobiliária entra, e é por isso que ela merece ser levada a sério: ela
não é um apêndice patrimonial, é **a solução de um problema comercial real**.

---

## 2. As três estruturas de ponto

| | **A — asset-light** | **B1 — compramos o imóvel** | **B2 — alugamos longo e sublocamos** |
|---|---|---|---|
| O que a franqueadora faz | só licencia marca e sistema | compra o terreno e constrói a baia | aluga por 10–15 anos, constrói a baia, subloca pronta |
| Capital da franqueadora por ponto | R$ 0 | R$ 500 mil (R$ 280 mil terreno + R$ 220 mil obra) | R$ 220 mil (só a obra) |
| O que o franqueado compra | tudo: ponto, obra, máquina | só máquina, totem, boxes, fachada, software | idem |

### O que acontece com o franqueado

| | A: aluga de terceiro | **B1: compramos** | B2: sublocamos |
|---|---|---|---|
| Investimento do franqueado | R$ 504.060 | **R$ 310.100** | R$ 310.100 |
| Aluguel que ele paga | R$ 3.000 | **R$ 4.000** | R$ 6.500 |
| EBITDA maduro/mês | R$ 12.836 | **R$ 11.836** | R$ 9.336 |
| Margem EBITDA | 26,7% | 24,7% | 19,4% |
| Payback | 51 meses | **38 meses** | 48 meses |
| **TIR** | **13,4%** | **27,3%** | **14,6%** |
| VPL @ 18% | −R$ 56.541 | **+R$ 73.946** | −R$ 27.378 |

**O ponto construído resolve o problema comercial.** Tirando R$ 194 mil do investimento
do franqueado e cobrando R$ 1.000 a mais de aluguel, a TIR dele **dobra: 13,4% → 27,3%**.
Agora é uma franquia que se vende.

A coluna B2 mostra o outro lado: a R$ 6.500 de aluguel, o franqueado volta a 14,6%. **O
desconto no investimento não pode ser cobrado de volta no aluguel.**

### O que acontece com a franqueadora

65 unidades no ano 10, 120 meses:

| | Capital no imóvel | Pico de caixa | Caixa zera | **TIR** | VPL @ 18% |
|---|---|---|---|---|---|
| **A — asset-light** | **R$ 0** | −R$ 652.658 | mês 83 | **42,6%** | **+R$ 1.263.923** |
| B1 — compra, sem dívida | R$ 32.500.000 | −R$ 23.283.377 | mês 120 | 15,6% | −R$ 1.196.797 |
| B1 — compra, 50% financiado a 14% | R$ 32.500.000 | −R$ 17.655.073 | mês 120 | 16,1% | −R$ 645.262 |
| B2 — locação longa + sublocação | R$ 14.300.000 | −R$ 6.710.376 | mês 120 | 17,6% | −R$ 83.027 |

E sem contar valor residual — ou seja, só o caixa que a operação gera em dez anos:

| | TIR | VPL @ 18% |
|---|---|---|
| A — asset-light | **31,8%** | **+R$ 437.980** |
| B1 — compra, sem dívida | **−62,0%** | −R$ 10.279.577 |
| B1 — compra, 50% financiado | −97,5% | −R$ 7.567.205 |
| B2 — locação longa | −19,5% | −R$ 3.267.493 |

---

## 3. O veredicto, sem rodeio

**Colocar o nosso capital no imóvel de cada unidade destrói valor.** Os números:

- A franqueadora sai de **42,6% de TIR sobre R$ 653 mil** de capital para **15,6% sobre
  R$ 32,5 milhões**. Cinquenta vezes mais capital para menos de metade do retorno.
- O VPL fica **negativo** nas três variantes imobiliárias, inclusive com dívida.
- A TIR de 15,6% do B1 depende inteiramente de um valor residual de R$ 47,5 milhões em
  terrenos valorizados. Sem o residual, a TIR é **−62%**. Ou seja: **não é um negócio de
  lava jato, é uma aposta em terra** que só paga quando se vende o terreno.

A razão é aritmética, não opinião. Um ponto de R$ 500 mil alugado a R$ 4.000/mês rende:

| Aluguel | Caixa líquido a.a. | Com valorização do terreno | Total |
|---|---|---|---|
| R$ 4.000 | 6,9% | +2,5 pp | **9,5%** |
| R$ 5.000 | 9,1% | +2,5 pp | **11,6%** |
| R$ 6.000 | 11,2% | +2,5 pp | **13,7%** |
| R$ 7.000 | 13,3% | +2,5 pp | **15,8%** |

**Com a Selic a 14% a.a., imóvel comercial no Brasil não se paga.** Nem com dívida: a 14%
de juro contra 14,6% de yield desalavancado, o spread é de 0,6 ponto — não sobra nada
para o risco. Dívida só ajudaria com juro abaixo de 11%.

### A janela onde a conta fecha é estreita, mas existe

| | Precisa de | Suporta até |
|---|---|---|
| Franqueadora (TIR ≥ 18%) | **R$ 5.000/mês** | — |
| Franqueado (TIR ≥ 18%) | — | **R$ 5.500/mês** |

**Entre R$ 5.000 e R$ 5.500 os dois lados pagam a TMA.** A R$ 5.250, a franqueadora faz
~19,4% e o franqueado ~21%. Funciona — e é frágil: qualquer erro de 10% na receita da
unidade fecha a janela dos dois lados ao mesmo tempo.

---

## 4. Recomendação: build-to-suit com capital de terceiro

Preserve exatamente o que a sua ideia queria — **o ponto sob controle da rede e o
franqueado entrando com R$ 310 mil** — sem pôr o nosso capital ali:

**Em cada praça, um investidor imobiliário local compra o terreno e constrói a baia no
nosso projeto padrão, em contrato de build-to-suit de 10 a 15 anos, com a locação em nome
da franqueadora e sublocação ao franqueado.**

Quem ganha o quê:

| | O que recebe | Por que aceita |
|---|---|---|
| **Investidor local** | R$ 5.000/mês sobre R$ 500 mil = 11,6% a.a. + valorização, em contrato longo com garantia | É **acima** do yield comercial típico no interior, com inquilino de prazo longo. Para o hurdle de um investidor imobiliário (IPCA + 6 a 7% real), isto é um bom negócio |
| **Franqueadora** | O ponto sob contrato, capital zero no imóvel, TIR de 42,6% preservada | Se o franqueado sair ou quebrar, **a locação é nossa**: entra outro operador em semanas, sem perder a praça |
| **Franqueado** | Ticket de R$ 310 mil em vez de R$ 504 mil, TIR de 27,3% | É o que torna a franquia vendável |

**O prêmio estratégico que você estava buscando é o controle do ponto, não a propriedade
dele.** O build-to-suit entrega o controle por R$ 0. É assim que a maioria das redes
brasileiras resolve isso, e é por isso que elas conseguem abrir trinta unidades com o
capital de três.

### E se você quiser o imóvel de todo jeito

Aí é uma decisão legítima, mas é **outro investimento, com outro dono do dinheiro e outro
hurdle:**

- Como **uso de capital da franquia**, a 18% de TMA: destrói valor. Está provado acima.
- Como **investimento imobiliário pessoal**, numa holding patrimonial separada, com hurdle
  de investidor imobiliário (IPCA + 6 a 7% real ≈ 11 a 12% nominal): a R$ 5.000/mês de
  aluguel o ponto rende 11,6% nominal com inquilino de prazo longo. **É um bom negócio
  imobiliário.**

Mesmo ativo, dois vereditos opostos — porque o custo de oportunidade é diferente. Se você
quer ser o investidor imobiliário das praças da sua própria rede, **seja — mas em PJ
separada, com contrato de mercado e aluguel de mercado**, e não misture o resultado dela
com o da franqueadora. Misturar é como o plano vira aquele número de R$ 815 mil que não
fazia sentido para ninguém.

**Ordem prática:** faça as primeiras 5 a 8 praças em build-to-suit com terceiros. Se em
três anos o juro cair para a casa de 10% e a rede estiver provada, comprar os pontos
seguintes passa a fazer sentido — e aí você compra com histórico de aluguel pago, que é
o que o banco financia barato.

---

## 4b. O modelo McDonald's — o que dele serve, e a partir de que receita

O McDonald's é a referência do modelo misto franquia + imobiliário, e vale saber o que ele é
de fato antes de copiar.

**Como funciona.** Em 1956 Harry Sonneborn criou a *Franchise Realty Corporation*: a empresa
assinava a locação ou comprava o ponto **com hipoteca**, e sublocava ao franqueado com
**margem de 20%, depois 40%**, sobre o próprio custo de locação. O aluguel cobrado era o
**maior entre essa margem e um percentual das vendas**. A trava de controle era o contrato:
franqueado que não seguisse o padrão rompia a locação e podia ser despejado.

Hoje o imobiliário é a maior parte do negócio. No 10-K de 2024, das receitas de restaurantes
franqueados de **US$ 15,7 bilhões**, **US$ 10,0 bi são aluguel** e US$ 5,6 bi royalty — ou seja,
**o aluguel é 64% e o royalty 36%**. 95% dos restaurantes são franqueados, e a empresa
"geralmente possui ou garante uma locação de longo prazo do terreno e do prédio".

### O teste no nosso modelo: a estrutura não fecha a R$ 48 mil/mês

Modelamos exatamente isso — estrutura **B3**: a franqueadora assina
a locação principal (R$ 3.000/mês), constrói a baia (R$ 220 mil) com **70% de dívida a 14%
a.a.**, e subloca pelo maior entre uma base e um percentual das vendas.

| Base + % das vendas | Aluguel maduro | Franqueado TIR | Franqueadora TIR | Franqueadora VPL @ 18% |
|---|---|---|---|---|
| 3.800 + 8% | R$ 3.840 | 28,2% | −62,1% | −R$ 3.501.344 |
| 3.800 + 10% | R$ 4.800 | 24,6% | −14,3% | −R$ 2.438.104 |
| 4.200 + 12% | R$ 5.760 | 20,2% | +5,4% | −R$ 1.229.507 |
| 4.500 + 13% | R$ 6.240 | 17,9% | +12,4% | −R$ 599.553 |

**Não existe nível de aluguel em que os dois lados fechem**, e a estrutura é **pior que comprar
o terreno** (B1, 15,6%) e pior que o aluguel fixo (B2, 17,6%). O motivo é direto: a franqueadora
passa a pagar R$ 3.000 de locação principal **mais** R$ 2.330 de serviço da dívida por ponto —
R$ 5.330 de saída contra R$ 4.800 de aluguel recebido a 10% das vendas. **Locação principal é
despesa perpétua; propriedade é ativo que valoriza.** Se for fazer o imobiliário, comprar é
melhor que alugar-e-construir.

### Mas há um limiar, e ele é um número concreto

Variando a receita madura da unidade, com base de R$ 3.800 + 10% das vendas:

| Receita madura da unidade | Aluguel | Franqueado TIR | Franqueadora TIR | Franqueadora VPL |
|---|---|---|---|---|
| R$ 48.000 | R$ 4.800 | 24,6% | −14,3% | −R$ 2.438.104 |
| R$ 54.000 | R$ 5.400 | 35,4% | +4,7% | −R$ 1.294.691 |
| R$ 60.000 | R$ 6.000 | 46,1% | +16,8% | −R$ 134.912 |
| **R$ 64.000** | **R$ 6.400** | **52,9%** | **+23,2%** | **+R$ 638.274** |
| R$ 70.000 | R$ 7.000 | 63,1% | +31,3% | +R$ 1.802.323 |

**A estrutura McDonald's passa a fechar a partir de ~R$ 64 mil/mês de receita madura por
unidade.** O cenário base de Piumhi é R$ 54,1 mil; o otimista é R$ 72,3 mil. Então não é um
"nunca" — é um "não com R$ 48 mil, e talvez sim se a operação provar R$ 64 mil".

### A razão de fundo: aluguel sobre o valor do imóvel

| | Aluguel bruto anual / valor do imóvel |
|---|---|
| McDonald's, imobilizado ao custo (US$ 44,2 bi) | **22,7%** |
| McDonald's, imobilizado líquido (US$ 25,3 bi) | **40,6%** |
| Ponto de lava jato de R$ 500 mil a R$ 5.000/mês | **12,0%** |
| Ponto de lava jato de R$ 500 mil a R$ 6.000/mês | 14,4% |

**O McDonald's cobra duas a três vezes mais aluguel por real de imóvel do que um lava jato
consegue cobrar.** Um restaurante gera venda por metro quadrado muito acima de uma baia de
lavagem, e é isso — não a engenharia financeira — que sustenta o modelo imobiliário deles.
Copiar a estrutura sem ter a venda por metro quadrado é copiar o custo sem a receita.

### O que copiar agora, de graça

1. **A locação principal em nome da franqueadora, com o franqueado construindo.** É o
   Sonneborn de 1956 sem a parte do prédio: capital zero, e se o franqueado sai, o ponto fica
   na rede. Em contrato de locação brasileiro isso exige **autorização expressa de sublocação**
   (Lei 8.245/91, art. 13) — sem ela, a sublocação permite despejo.
2. **Aluguel percentual**: o maior entre uma base e um percentual das vendas. Reajusta sozinho
   com o crescimento e com a inflação, sem renegociação, e alinha o interesse dos dois lados.
   Usar como mecanismo de indexação e controle, não como motor de lucro.
3. **A margem sobre a locação principal.** Sonneborn cobrava 20% a 40%. Em contrato de
   R$ 3.000, uma margem de 20% é R$ 600/mês por ponto de margem com **capital zero** — em 65
   pontos, R$ 39 mil/mês. É a parte mais rentável do modelo deles e a mais barata de copiar.

### O que não copiar agora

- **Financiar a construção da baia.** Tabela acima: não fecha a R$ 48 mil/mês.
- **Comprar o terreno.** 15,6% sobre R$ 32,5 milhões contra 42,6% sobre R$ 653 mil (ADR-011).
- **A escala.** O McDonald's amortiza um time imobiliário próprio em 40 mil lojas.

**Risco que a locação principal cria e que o McDonald's também carrega:** 65 pontos a R$ 3.000
são **R$ 195 mil/mês de obrigação fixa**, com ou sem franqueado dentro. Se 10% ficarem vagos,
são R$ 19,5 mil/mês de sangria. Só assumir a locação principal em praça já provada, e com o
franqueado como fiador ou garantidor da sublocação.

---

## 5. O plano recomendado em números

**Fase 1 + Fase 2 asset-light, com build-to-suit de terceiros nos pontos:**

| | |
|---|---|
| **Pico de caixa consolidado** | **−R$ 536.818** (mês 9) |
| Caixa acumulado vira positivo | mês 64 |
| **TIR em 120 meses** | **42,6%** |
| **VPL @ 18% a.a.** | **+R$ 1.744.248** |

**Capital total a reservar: R$ 540 mil** — e o pico acontece no **mês 9**, ainda dentro da
Fase 1. A partir do ano 2, o EBITDA de Piumhi (R$ 20,8 mil/mês) cobre a maior parte do
vale da franqueadora. Não existe um segundo cheque grande.

**Mas isso depende de Piumhi entregar o cenário base.** Com Piumhi no cenário
conservador (380 assinantes), o consolidado fica assim: pico de **R$ 718.965 no mês 45**,
caixa positivo no mês 76, TIR de 35,8%, VPL de R$ 1,37 milhão. Continua um bom negócio —
mas o pico de caixa sobe R$ 182 mil e muda de lugar: sai do mês 9 (Fase 1) para o mês 45
(meio da Fase 2), porque a unidade deixa de cobrir o vale da franqueadora.

A leitura prática: **R$ 540 mil se Piumhi for bem, R$ 720 mil se for mediano.** Reserve
conforme o apetite — e lembre que o segundo número só é cobrado três ou quatro anos à
frente, com a Fase 1 já operando e informando a decisão.

Compare com o que foi apresentado antes:

| | Capital | TIR | VPL @ 18% |
|---|---|---|---|
| Versão anterior (unidade + franqueadora juntas, com BOX) | R$ 815 mil | 45,1% | R$ 1,62 mi |
| **Plano recomendado (sem BOX, build-to-suit)** | **R$ 540 mil** | **42,6%** | **R$ 1,74 mi** |
| Com imóvel próprio em todas as praças (B1) | R$ 21,8 mi | 16,6% | −R$ 716 mil |
| Com locação longa + sublocação (B2) | R$ 5,59 mi | 19,9% | +R$ 397 mil |

**R$ 275 mil menos de capital e R$ 481 mil mais de VPL** que a versão anterior. A melhora
vem de três lugares: tirar o BOX, sequenciar as fases em vez de rodar as duas de uma vez,
e não comprar imóvel.

---

## 6. Expansão da franqueadora — asset-light

| Ano | Unidades | Receita da franqueadora | EBITDA |
|---|---|---|---|
| 1 | 0 (só a loja própria) | — | −R$ 135.000 |
| 2 | 2 | R$ 42.235 | −R$ 300.522 |
| 3 | 7 | R$ 169.285 | −R$ 361.801 |
| 4 | 12 | R$ 373.256 | −R$ 310.465 |
| 5 | 19 | R$ 616.970 | −R$ 201.745 |
| 6 | 27 | R$ 920.182 | −R$ 43.047 |
| 7 | 35 | R$ 1.258.794 | +R$ 145.387 |
| 8 | 45 | R$ 1.633.672 | +R$ 340.284 |
| 9 | 55 | R$ 2.056.792 | +R$ 599.705 |
| 10 | 65 | R$ 2.486.392 | +R$ 864.569 |

Receita por unidade/mês para a franqueadora: royalty de 6% (R$ 2.880) + taxa de
tecnologia (R$ 700) = **R$ 3.580**, mais R$ 40 mil de taxa de franquia na assinatura. O
fundo de 2% não aparece: é vinculado a marketing.

**O vale dos anos 2 a 6 é o risco central da Fase 2**, e é de caixa, não de modelo. A
franqueadora só fica EBITDA-positiva no **ano 7**, e o caixa acumulado só vira no
**mês 83**. São seis anos de estrutura antes da recorrência sustentar a própria conta.

Por que o pico de caixa é de apenas R$ 653 mil se o EBITDA acumulado negativo passa de
R$ 1,5 milhão: a **taxa de franquia de R$ 40 mil** por unidade entra no caixa na
assinatura, três meses antes de cada inauguração, e financia boa parte do vale. Isso tem
uma consequência desconfortável que precisa ser dita: **a franqueadora depende de vender
franquia para se financiar.** Se a expansão travar no ano 4, o caixa trava com ela. É
exatamente por isso que o gate de doze meses em Piumhi não é burocracia — é o que evita
montar uma estrutura que só se sustenta vendendo mais do mesmo.

Quem cobre o vale é a unidade de Piumhi. Se Piumhi não entregar o cenário base, **a Fase
2 não começa**.

---

## 7. Estrutura societária

| PJ | Papel |
|---|---|
| **1 — Franqueadora** | Dona das marcas e do software. Licencia, cobra royalty e taxa de tecnologia. É o balanço dela que vai para a COF. |
| **2 — Operação Piumhi** | A unidade que lava carro. A partir do mês 13 paga royalty como qualquer franqueado. |
| **3 — Holding patrimonial** (só se você decidir comprar imóvel) | Dona dos pontos. Aluga a mercado. Resultado **separado** da franqueadora. |
| **4+** | Franqueados, território exclusivo por contrato de 5 anos. |

**Não pode ser um CNPJ só.** Dois motivos:

1. **A COF exige o balanço da franqueadora** (Lei nº 13.966/2019, prazo de 10 dias antes
   da assinatura). Com tudo junto, cada candidato — inclusive os que vão desistir —
   recebe o faturamento e as despesas da operação de Piumhi.
2. **Risco cruzado.** Franqueado que processa a franqueadora alcançaria o caixa e os
   equipamentos da operação, e vice-versa. Com imóvel na mesma PJ, alcançaria os
   terrenos.

A unidade própria pagar royalty não é formalidade: é o que faz os indicadores da rede
serem comparáveis desde o primeiro dia e dá histórico limpo à COF.

**Validar com advogado societário e contador antes de constituir.**

---

## 8. Riscos da Fase 2

| Risco | Impacto | Mitigação |
|---|---|---|
| Franquia com TIR de 13,4% não vende | **Crítico** | Build-to-suit baixa o ticket para R$ 310 mil e leva a TIR a 27,3% |
| Franqueado investidor ausente, que paga gerente | **Crítico** | Não fecha em nenhuma estrutura: vender só para franqueado operador (seção 1) |
| Vender franquia antes da COF | **Crítico** | Gate absoluto: 12 meses de operação auditável em Piumhi |
| Caixa da franqueadora nos anos 2 a 4 | Alto | EBITDA de Piumhi; faseamento do app; sócio ou master regional |
| Capital imobilizado em imóvel a 15,6% de TIR | Alto | Build-to-suit com terceiro; holding separada se houver compra |
| Franqueado quebrar e manchar a marca | Alto | Capital próprio mínimo de 40%; pré-venda por praça; locação em nome da rede |
| Marca sem exclusividade / conflito com "Fast Wash" | Alto | Busca de anterioridade e nome distintivo antes de qualquer fachada |
| Máquina importada parada por falta de peça | Alto | Contrato-quadro com SLA e estoque nacional de peças |
| Praça que não chega a R$ 48 mil/mês | Alto | Pré-venda de fundadores em cada praça antes da obra, como em Piumhi |

---

## 9. O que ainda não está provado

1. **A receita madura de R$ 48 mil/mês numa praça que não é Piumhi.** Nenhuma unidade
   operou. É a premissa que a Fase 1 existe para testar.
2. **R$ 280 mil de terreno e R$ 220 mil de obra são estimativas**, não orçamentos. Variam
   muito entre praças, e o B1 é sensível a isso.
3. **A tributação da franqueadora em Lucro Presumido é estimativa** (~16% sobre serviços,
   ~11,5% sobre aluguel). Validar com contador: muda a TIR em pontos inteiros.
4. **O valor residual de 5× EBITDA** para o negócio de franquia é conservador, mas é
   arbitrado. As tabelas sem residual estão na seção 2 justamente por isso.
5. **A valorização de 4,5% a.a. do terreno** é premissa. Em cidade pequena pode ser menos.
6. **A janela de aluguel de R$ 5.000 a R$ 5.500 depende da receita da unidade.** Se a
   unidade madura for R$ 43 mil em vez de R$ 48 mil, a janela fecha.
7. **O pró-labore do franqueado de R$ 3.500 é escolha, não cálculo** — e é a premissa que mais
   move o resultado dele. Medir em Piumhi quantas horas de gente a operação realmente consome
   é um dos entregáveis da Fase 1.

---

## 10. Próximos passos da Fase 2 — nenhum deles é hoje

A Fase 2 tem um gate, e o gate é a Fase 1. A ordem é:

| Quando | Ação |
|---|---|
| Mês 12 de Piumhi | Fechar o ano com número auditável: assinantes, churn, lavagens/dia, uso do Ilimitada, EBITDA real |
| Mês 12 | Comparar com o cenário base. Abaixo de ~400 assinantes, a Fase 2 **não começa** |
| Mês 13 | Constituir a franqueadora como PJ própria; unidade passa a pagar royalty |
| Mês 13–15 | Conversar com 3 investidores imobiliários locais sobre build-to-suit na segunda praça |
| Mês 15 | COF com advogado especializado, sobre o balanço real da franqueadora |
| Mês 15–18 | Manual de operação e de implantação, escritos a partir do que Piumhi aprendeu |
| Mês 18 | Primeira franquia vendida — nunca antes |

**Enquanto a Fase 1 não fechar doze meses, a única coisa a fazer na Fase 2 é não gastar
dinheiro nela.** Formatar franquia com base em projeção é o erro que mais mata rede
iniciante, e é um erro caro: COF, manual, software e equipe de campo somam centenas de
milhares de reais que não voltam se a premissa de demanda estiver errada.
