# Tabela mestra de cenários

Tudo que foi simulado neste projeto, num lugar só. Gerado por `bp/cenarios.py`
(`cd docs/bp && PYTHONPATH=. python3 cenarios.py`). Data: 2026-10-20.

Premissas comuns: TMA de 18% a.a., Selic de referência 14% a.a., pró-labore do operador de
R$ 3.500/mês em todos os números, horizonte de 60 meses na unidade e 120 meses na rede.

---

## 1. A loja própria de Piumhi — arranjos de capital

| Arranjo | 1ª tranche | **Capital a reservar** | TIR do equity | VPL @ 18% |
|---|---|---|---|---|
| A. Capex cheio, 100% equity | R$ 454.060 | R$ 480.111 | 25,6% | R$ 93.429 |
| B. Capex enxuto, 100% equity | R$ 373.000 | R$ 399.051 | 33,9% | R$ 165.171 |
| **C. Enxuto + pré-venda, 100% equity** | **R$ 303.480** | **R$ 374.953** | **34,3%** | **R$ 164.250** |
| D. Enxuto + pré-venda + dívida de R$ 120 mil | R$ 183.480 | R$ 276.011 | 39,0% | R$ 156.648 |
| E. Idem, dívida de R$ 150 mil | R$ 153.480 | R$ 252.021 | 40,7% | R$ 154.747 |
| F. Idem, dívida de R$ 180 mil | R$ 123.480 | R$ 228.068 | 42,9% | R$ 152.846 |

"Capital a reservar" é o **pico de caixa**, não o desembolso inicial: a diferença é chamada
durante a rampa, quando os meses 1 a 4 fecham com EBITDA negativo.

### 1.1 O que 100% equity custa e o que ele ganha

Comparando o arranjo **C** (100% equity) com o **D** (com dívida):

| | C — 100% equity | D — com dívida de R$ 120 mil |
|---|---|---|
| Capital a reservar | **R$ 374.953** | R$ 276.011 |
| TIR do equity | 34,3% | **39,0%** |
| VPL @ 18% | **R$ 164.250** | R$ 156.648 |

**São R$ 99 mil mais de capital e 4,7 pontos menos de TIR — mas R$ 7,6 mil MAIS de valor.**

A dívida a 21% a.a. custa mais que a TMA de 18%: ela compra eficiência de capital e vende
valor. As duas escolhas são defensáveis, e a decisão não é financeira, é de caixa:

- **Tem o dinheiro e não precisa dele para outra coisa:** 100% equity. Rende mais em valor
  absoluto, não tem parcela, não tem aval, não tem covenant, e nada quebra se a rampa atrasar
  dois meses. Para um negócio que nunca operou, **não ter parcela a pagar no mês 3 vale mais do
  que 4,7 pontos de TIR no papel.**
- **O dinheiro é escasso ou tem uso melhor:** a dívida libera R$ 99 mil por R$ 7,6 mil de
  valor — barato.

Com 100% equity você também fica livre de duas coisas que não aparecem na tabela: a
**negociação com a cooperativa** (que leva semanas e pode voltar com taxa pior) e a
**exigência de aval**, que em PJ nova quase sempre significa aval pessoal dos sócios.

---

## 2. Divisão do equity — 100% equity, R$ 374.953

Capital chamado em tranches, proporcional à necessidade real.

| Estrutura | Sócio | Aporte | 1ª tranche | TIR | Caixa em 60 meses |
|---|---|---|---|---|---|
| **50 / 50**, um investidor | Antonio | R$ 187.476 | R$ 151.740 | 34,3% | R$ 412.512 |
| | Investidor | R$ 187.476 | R$ 151.740 | 34,3% | R$ 412.512 |
| **33,33 × 3**, dois investidores | Antonio | R$ 124.984 | R$ 101.160 | 34,3% | R$ 275.008 |
| | Investidor A | R$ 124.984 | R$ 101.160 | 34,3% | R$ 275.008 |
| | Investidor B | R$ 124.984 | R$ 101.160 | 34,3% | R$ 275.008 |
| **25 / 25 / 50**, dois investidores | Antonio | R$ 187.476 | R$ 151.740 | 34,3% | R$ 412.512 |
| | Investidor A | R$ 93.738 | R$ 75.870 | 34,3% | R$ 206.256 |
| | Investidor B | R$ 93.738 | R$ 75.870 | 34,3% | R$ 206.256 |
| **50,5 / 24,75 / 24,75** | Antonio | R$ 189.351 | R$ 153.257 | 34,3% | R$ 416.637 |
| | Investidor A | R$ 92.801 | R$ 75.111 | 34,3% | R$ 204.193 |
| | Investidor B | R$ 92.801 | R$ 75.111 | 34,3% | R$ 204.193 |

**Com aporte proporcional, a TIR é a mesma para todos em qualquer divisão: 34,3%, que é a TIR
do projeto.** A divisão não cria nem destrói retorno — ela decide **quanto cada um põe e quem
decide**. É por isso que a conversa de divisão é jurídica e de caixa, não financeira.

### 2.1 A mesma divisão, com a dívida de R$ 120 mil (arranjo D)

| Estrutura | Antonio | Cada investidor | TIR de todos |
|---|---|---|---|
| 50 / 50 | R$ 138.006 | R$ 138.006 | 39,0% |
| 33,33 × 3 | R$ 92.004 | R$ 92.004 | 39,0% |
| 25 / 25 / 50 | R$ 138.006 | R$ 69.003 | 39,0% |
| 50,5 / 24,75 / 24,75 | R$ 139.386 | R$ 68.313 | 39,0% |

### 2.2 A cláusula de chamada de capital vale 8,3 pontos de TIR

Se o sócio depositar o compromisso inteiro na assinatura e o dinheiro ficar parado em conta até
a obra pedir:

| Fatia | Aporte | TIR com tranches | TIR com tudo no mês 0 | Perda |
|---|---|---|---|---|
| 33,33% | R$ 124.984 | 34,3% | 26,1% | **8,3 pontos** |
| 25,00% | R$ 93.738 | 34,3% | 26,1% | **8,3 pontos** |
| 50,00% | R$ 187.476 | 34,3% | 26,1% | **8,3 pontos** |

Não é detalhe de contrato: é o item mais barato de acertar e o que mais devolve retorno.

### 2.3 Governança de cada divisão — o que realmente diferencia

Na Sociedade Limitada as deliberações se contam por capital. Nenhuma das três divisões que você
listou dá maioria ao Antonio:

| Estrutura | Quem tem maioria | Risco |
|---|---|---|
| 50 / 50 | **ninguém** | Qualquer discordância para o negócio. É a forma mais comum de sociedade de dois sócios morrer |
| 33,33 × 3 | **ninguém**; dois quaisquer somam 66,7% | **Os dois investidores podem votar contra o Antonio.** Pior das três para quem opera |
| 25 / 25 / 50 | **ninguém**; os dois investidores somam 50% | Melhor que as outras: para bloquear, os dois têm de concordar entre si |
| **50,5 / 24,75 / 24,75** | **Antonio** | Nenhum. Custa R$ 1,9 mil de capital a mais que o 25/25/50 |

**Recomendação: 50,5 / 24,75 / 24,75.** Economicamente é indistinguível do 25/25/50 — meio
ponto percentual, R$ 1,9 mil — e resolve a governança inteira. Se o investidor estranhar o
número quebrado, a explicação é honesta e costuma ser bem recebida: *quem opera precisa poder
decidir o dia a dia; o que é estrutural está na lista de matérias reservadas e exige acordo de
todos.*

Se a opção for 50/50 ou 33,33 × 3 de todo jeito, então são obrigatórios no acordo de
quotistas: voto de qualidade do administrador sobre uma lista fechada de matérias
operacionais, e **cláusula buy-sell** (quem propõe um preço aceita vender ou comprar por ele)
para impasse estrutural.

---

## 3. A rede / franqueadora — 65 unidades, 120 meses

| Estrutura do ponto comercial | Capital no imóvel | Pico de caixa | TIR | VPL @ 18% |
|---|---|---|---|---|
| **A. Asset-light** (o franqueado aluga de terceiro) | **R$ 0** | −R$ 652.658 | **42,6%** | **+R$ 1.263.923** |
| B1. Compramos terreno + obra | R$ 32.500.000 | −R$ 23.283.377 | 15,6% | −R$ 1.196.797 |
| B1. Idem, 50% financiado a 14% a.a. | R$ 32.500.000 | −R$ 17.655.073 | 16,1% | −R$ 645.262 |
| B2. Locação longa + obra + sublocação a valor fixo | R$ 14.300.000 | −R$ 6.710.376 | 17,6% | −R$ 83.027 |

### 3.1 B3 — over no aluguel (o modelo McDonald's)

Locação principal em nome da franqueadora + obra da baia com 70% de dívida + sublocação pelo
**maior entre uma base e um percentual das vendas** — a *Franchise Realty* de Sonneborn, 1956.

| Base + % das vendas | Aluguel maduro | Franqueado TIR | Franqueadora TIR | VPL da franqueadora |
|---|---|---|---|---|
| R$ 3.800 + 8% | R$ 3.840 | 28,2% | −62,1% | −R$ 3.501.344 |
| R$ 3.800 + 10% | R$ 4.800 | 24,6% | −14,3% | −R$ 2.438.104 |
| R$ 4.200 + 12% | R$ 5.760 | 20,2% | +5,4% | −R$ 1.229.507 |
| R$ 4.500 + 13% | R$ 6.240 | 17,9% | +12,4% | −R$ 599.553 |

**Não existe nível de aluguel em que os dois lados fechem a R$ 48 mil/mês de receita madura.**

### 3.2 O limiar do B3

| Receita madura da unidade | Franqueado TIR | Franqueadora TIR | VPL da franqueadora |
|---|---|---|---|
| R$ 48.000 | 24,6% | −14,3% | −R$ 2.438.104 |
| R$ 54.000 | 35,4% | +4,7% | −R$ 1.294.691 |
| R$ 60.000 | 46,1% | +16,8% | −R$ 134.912 |
| **R$ 64.000** | **52,9%** | **+23,2%** | **+R$ 638.274** |
| R$ 70.000 | 63,1% | +31,3% | +R$ 1.802.323 |

**O over no aluguel passa a fechar a partir de ~R$ 64 mil/mês por unidade.** O cenário base de
Piumhi é R$ 54,1 mil e o otimista R$ 72,3 mil — então é um "não com R$ 48 mil", não um "nunca".

---

## 4. O franqueado em cada estrutura

Unidade madura a R$ 48.000/mês, 60 meses.

| Estrutura | Investimento dele | Aluguel que paga | EBITDA/mês | TIR | VPL @ 18% |
|---|---|---|---|---|---|
| A. Ele constrói o ponto inteiro | R$ 504.060 | R$ 3.000 | R$ 12.836 | 13,3% | −R$ 56.541 |
| **B1. Nós compramos e alugamos a ele** | **R$ 310.100** | R$ 4.000 | R$ 11.836 | **27,3%** | +R$ 73.946 |
| B2. Nós sublocamos a ele | R$ 310.100 | R$ 6.500 | R$ 9.336 | 14,6% | −R$ 27.378 |

Com pró-labore de R$ 3.500 para quem administra a unidade franqueada:

| Estrutura | EBITDA/mês | TIR | VPL @ 18% |
|---|---|---|---|
| A. Ele constrói o ponto inteiro | R$ 9.336 | **1,7%** | −R$ 198.395 |
| B1. Nós compramos e alugamos a ele | R$ 8.336 | **9,5%** | −R$ 67.907 |

**Nem o ponto construído pela rede salva a franquia se o franqueado tiver de pagar um gerente.**
Vender só para **franqueado operador**, nunca para investidor ausente.

---

## 5. Consolidado — loja própria + franqueadora no mesmo caixa, 120 meses

| Estrutura do ponto | Pico de caixa | Caixa zera | TIR | VPL @ 18% |
|---|---|---|---|---|
| **A. Asset-light** | **−R$ 536.818** | mês 64 | **42,6%** | **+R$ 1.744.248** |
| B2. Locação longa + sublocação | −R$ 5.591.302 | mês 120 | 19,9% | +R$ 397.299 |
| B1. Compra o imóvel | −R$ 21.834.616 | mês 120 | 16,6% | −R$ 716.471 |

---

## 6. A leitura de tudo isso, em cinco linhas

1. **A loja de Piumhi fecha.** Entre 34,3% (100% equity) e 42,9% (com dívida alta), dependendo
   de quanto capital você quer parado.
2. **A divisão do equity não muda retorno nenhum.** Com aporte proporcional, todos ganham a TIR
   do projeto. Ela só muda quanto cada um põe e **quem decide** — e aí o 50,5% resolve.
3. **A rede fecha, mas só asset-light.** 42,6% com capital zero no imóvel, contra 15,6% com
   R$ 32,5 milhões em terra.
4. **O imobiliário resolve um problema real** (o franqueado a R$ 504 mil não compra) **e cria
   outro maior** (capital). A saída é build-to-suit com investidor local: controle do ponto por
   R$ 0.
5. **Nada disso vale sem os doze meses de Piumhi.** Toda a Fase 2 depende de um número que
   ainda não existe.

---

## Onde cada número é calculado

```
bp/piumhi.py       a unidade: receita, custos, três cenários, capacidade
bp/capital.py      arranjos de capital, dívida, pré-venda, divisão do equity
bp/rede.py         a franqueadora e o franqueado nas estruturas A, B1, B2
bp/mcdonalds.py    o over no aluguel (B3) e o limiar de R$ 64 mil
bp/imovel.py       janela de aluguel e comprar-ou-alugar o terreno de Piumhi
bp/sens_piumhi.py  capacidade, equilíbrio e sensibilidades
bp/cenarios.py     esta tabela toda, de uma vez
bp/planilha.py     gera as duas planilhas
```
