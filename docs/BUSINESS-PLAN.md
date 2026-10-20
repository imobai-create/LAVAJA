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
derrubou a TIR publicada antes (37,5% sem pró-labore). Ver [BP-PIUMHI seção 4](BP-PIUMHI.md).

| | Fase 1 (Piumhi) | Fase 1 + Fase 2 |
|---|---|---|
| **Capital a reservar (arranjo recomendado)** | **R$ 276 mil** | R$ 540 mil a R$ 720 mil |
| Capex + giro | R$ 328.000 enxuto + R$ 45.000 | idem + estrutura da franqueadora |
| Dívida | R$ 120 mil a ~21% a.a., 6 meses de carência | — |
| Pré-venda de 80 fundadores | R$ 69.520 no mês 0 | — |
| EBITDA maduro | R$ 17.341/mês (32,1%) | R$ 865 mil/ano no ano 10 |
| Equilíbrio operacional | 232 assinantes (1,7% da frota) | — |
| Mínimo para pagar a TMA de 18% | ~400 assinantes (2,9% da frota) | — |
| **TIR do equity** | **39,0% a.a.** (60 meses) | 42,6% a.a. (120 meses) |
| **VPL @ 18% a.a.** | **+R$ 156.648** | +R$ 1.744.248 |

Sem dívida, sem pré-venda e com capex cheio, o mesmo projeto exige **R$ 480 mil** e rende
**25,6%**. A diferença é toda estrutura de capital: [BP-PIUMHI seção 11](BP-PIUMHI.md).

### Cap table recomendado para a Fase 1

| | R$ | % da PJ 2 | TIR |
|---|---|---|---|
| Investidor A | 75.000 | 24% | 20,7% |
| Investidor B | 75.000 | 24% | 20,7% |
| **Antonio** | **126.011** | **52%** | **29,2%** + pró-labore + 100% da franqueadora |

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

## Modelo e planilhas

```
docs/bp/comum.py       funcoes financeiras (VPL, TIR, payback) e tabelas do Simples
docs/bp/piumhi.py      Fase 1 - loja modelo, 3 cenarios, 60 meses
docs/bp/sens_piumhi.py capacidade, ponto de equilibrio e sensibilidades da Fase 1
docs/bp/rede.py        Fase 2 - franqueadora e franqueado nas 3 estruturas, 120 meses
docs/bp/imovel.py      janela de aluguel e comprar-ou-alugar o terreno de Piumhi
docs/bp/mcdonalds.py   estrutura McDonald's: locacao principal + aluguel percentual
docs/bp/capital.py     estrutura de capital da Fase 1: divida, pre-venda, cap table
docs/bp/cenarios.py    roda TODOS os cenarios de uma vez (tabela mestra)
docs/bp/planilha.py    gera as planilhas com formulas vivas
```

Rodar: `cd docs/bp && PYTHONPATH=. python3 piumhi.py` (idem para os outros). Sem
dependências externas, exceto `planilha.py`, que precisa de `openpyxl`.

Planilhas: `docs/bp/Modelo-Economico-Piumhi.xlsx` e
`docs/bp/Modelo-Economico-Rede.xlsx`. As abas mensais têm fórmulas que apontam para a aba
`Premissas` — `IRR`, `NPV` e `MATCH` de verdade. Mudar a TMA, a receita madura, o aluguel
ou o número de assinantes recalcula tudo.
