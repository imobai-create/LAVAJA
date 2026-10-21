# Business plan — índice

O plano está em duas peças, porque o negócio tem duas fases com decisões e capitais
distintos. **A Fase 2 não começa antes de a Fase 1 ter doze meses de número auditável.**

| | |
|---|---|
| **[BP-PIUMHI.md](BP-PIUMHI.md)** | **Fase 1 — loja modelo de Piumhi/MG.** Área alugada a R$ 3.000/mês, capex só de implantação, sem terreno. Unidade própria: sem taxa de franquia, royalty, fundo nem taxa de tecnologia. Horizonte de 60 meses. |
| **[BP-REDE.md](BP-REDE.md)** | **Fase 2 — plano macro da rede**, com a análise das estruturas de ponto comercial (asset-light, imóvel próprio, locação longa + sublocação, over no aluguel). Horizonte de 120 meses. |
| **[CENARIOS.md](CENARIOS.md)** | **Tabela mestra:** todos os cenários simulados num lugar só — arranjos de capital da loja (100% equity até dívida de R$ 180 mil), as divisões de equity (50/50, 33,33 × 3, 25/25/50, 50,5/24,75/24,75), as quatro estruturas de ponto da rede e o consolidado. |
| **[PLANO-IMPLANTACAO.md](PLANO-IMPLANTACAO.md)** | **Quem faz o quê, em que ordem:** Fase 0 (90 dias), Fase 1 (loja, mês a mês até o mês 12) e Fase 2 (rede), com os gates verificáveis entre elas. |
| **[RESUMO-INVESTIDOR.md](RESUMO-INVESTIDOR.md)** | Uma página para conversa com investidor. |

## Os números, em uma tela

Todos já pagam o **pró-labore de R$ 3.500/mês** do operador — correção feita em out/2026, que
derrubou a TIR publicada antes (35,9% sem pró-labore). Ver [BP-PIUMHI seção 4](BP-PIUMHI.md).

**Dois arranjos de capital seguem em aberto para a Fase 1.** A escolha entre eles não é
financeira — o VPL é quase empate — e sim de caixa. Ver [BP-PIUMHI seção 11.5](BP-PIUMHI.md).

| Fase 1 (Piumhi) | **Sem dívida** | **Com dívida de R$ 120 mil** |
|---|---|---|
| **Capital a reservar** | **R$ 372.353** | **R$ 274.178** |
| 1ª tranche | R$ 299.405 | R$ 179.405 |
| **TIR do equity** (60 meses) | **32,9%** | **37,1%** |
| **VPL @ 18% a.a.** | **+R$ 147.622** | +R$ 140.020 |
| Payback | 36 meses | 35 meses |

Comum aos dois: **capex de R$ 323.925 — dentro do teto de R$ 325 mil** — mais giro de
R$ 45.000, pré-venda de 80 fundadores de R$ 69.520, EBITDA maduro de R$ 16.745/mês (31,0%),
equilíbrio operacional em 134 assinantes (1,0% da frota) e **mínimo de 399 assinantes
(2,9%) para pagar a TMA de 18%** — este último é o gate que manda em tudo.

| Fase 1 + Fase 2 | |
|---|---|
| Capital a reservar | R$ 540 mil a R$ 720 mil |
| TIR (120 meses) | 42,6% a.a. |
| VPL @ 18% a.a. | +R$ 1.744.248 |

Sem nenhuma alavanca — capex no teto, sem pré-venda, sem dívida — o projeto exige
**R$ 395.871** e rende **32,4%**. Com a lista de capex completa de R$ 399.060, exigiria
**R$ 481 mil** para render **24,0%**: R$ 75 mil a mais de capital para 8 pontos a menos de
retorno. Por isso o teto de R$ 325 mil não é só restrição de caixa — é a decisão de
investimento melhor ([BP-PIUMHI seção 2](BP-PIUMHI.md)).

### Cap table da Fase 1 — divisão 25 / 25 / 50

Com aporte proporcional e capital chamado em tranches, **a TIR é a mesma para todos**: é a TIR
do projeto. A divisão decide quanto cada um põe e quem manda, não quanto cada um ganha.

| | Sem dívida | Com dívida | % da PJ 2 |
|---|---|---|---|
| Investidor A | R$ 93.088 | R$ 68.544 | 25% |
| Investidor B | R$ 93.088 | R$ 68.544 | 25% |
| **Antonio** | **R$ 186.177** | **R$ 137.089** | **50%** + pró-labore + 100% da franqueadora |
| **TIR de todos** | **32,9%** | **37,1%** | |

**A marca fica na PJ 1, 100% do Antonio, com registro no INPI em nome dela antes de qualquer
assinatura.** Os investidores compram a loja de Piumhi, não a rede.

## Decisões já tomadas

- **O formato BOX saiu da oferta** — TIR de 9,4% contra TMA de 18% ([ADR-008](DECISOES.md)).
- **A franqueadora é avaliada em 10 anos, não em 5** ([ADR-009](DECISOES.md)).
- **Piumhi primeiro, franquia depois** ([ADR-010](DECISOES.md)).
- **Não compramos o imóvel das praças com capital da franquia** — build-to-suit com
  investidor local ([ADR-011](DECISOES.md)).
- **Estrutura de capital da Fase 1:** capex enxuto + dívida + pré-venda, com o Antonio acima
  de 50% e a marca fora da sociedade dos investidores ([ADR-012](DECISOES.md)).

## As planilhas

Toda conta deste plano está em duas planilhas, com **fórmulas vivas**:

| Planilha | O que tem |
|---|---|
| **Modelo-Economico-Piumhi.xlsx** | A loja. Abas `Premissas`, `Resumo`, `Capital` e `Fluxo` |
| **Modelo-Economico-Rede.xlsx** | A rede. Abas `Premissas`, `Franqueado`, `Franqueadora`, `Cronograma` |

As abas mensais usam `IRR`, `NPV` e `MATCH` de verdade, apontando para a aba `Premissas`.
**As células em bege são as únicas para editar:** mudar a TMA, a receita madura, o aluguel,
a tarifa de energia ou o aporte de cada sócio recalcula tudo na hora — inclusive a TIR, o
VPL e o payback. É a forma de testar qualquer cenário que não esteja nestes documentos,
sem depender de ninguém.
