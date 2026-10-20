# Business plan — índice

O plano está em duas peças, porque o negócio tem duas fases com decisões e capitais
distintos. **A Fase 2 não começa antes de a Fase 1 ter doze meses de número auditável.**

| | |
|---|---|
| **[BP-PIUMHI.md](BP-PIUMHI.md)** | **Fase 1 — loja modelo de Piumhi/MG.** Área alugada a R$ 3.000/mês, capex só de implantação, sem terreno. Unidade própria: sem taxa de franquia, royalty, fundo nem taxa de tecnologia. Horizonte de 60 meses. |
| **[BP-REDE.md](BP-REDE.md)** | **Fase 2 — plano macro da rede**, com a análise das três estruturas de ponto comercial (asset-light, imóvel próprio, locação longa + sublocação). Horizonte de 120 meses. |

## Os números, em uma tela

| | Fase 1 (Piumhi) | Fase 1 + Fase 2 (recomendado) |
|---|---|---|
| Capital a reservar | **R$ 475 mil** | **R$ 540 mil** (R$ 720 mil se Piumhi ficar no conservador) |
| Investimento/capex | R$ 399.060 de capex + R$ 55.000 de giro | idem + estrutura da franqueadora |
| EBITDA maduro | R$ 20.841/mês (38,5%) | R$ 865 mil/ano na franqueadora no ano 10 |
| Payback / caixa positivo | 33 meses | mês 64 |
| **TIR** | **37,5% a.a.** (60 meses) | **42,6% a.a.** (120 meses) |
| **VPL @ 18% a.a.** | **+R$ 235.282** | **+R$ 1.744.248** |

## Decisões já tomadas

- **O formato BOX saiu da oferta** — TIR de 9,4% contra TMA de 18% ([ADR-008](DECISOES.md)).
- **A franqueadora é avaliada em 10 anos, não em 5** ([ADR-009](DECISOES.md)).
- **Piumhi primeiro, franquia depois** ([ADR-010](DECISOES.md)).
- **Não compramos o imóvel das praças com capital da franquia** — build-to-suit com
  investidor local ([ADR-011](DECISOES.md)).

## Modelo e planilhas

```
docs/bp/comum.py       funcoes financeiras (VPL, TIR, payback) e tabelas do Simples
docs/bp/piumhi.py      Fase 1 - loja modelo, 3 cenarios, 60 meses
docs/bp/sens_piumhi.py capacidade, ponto de equilibrio e sensibilidades da Fase 1
docs/bp/rede.py        Fase 2 - franqueadora e franqueado nas 3 estruturas, 120 meses
docs/bp/imovel.py      janela de aluguel e comprar-ou-alugar o terreno de Piumhi
docs/bp/mcdonalds.py   estrutura McDonald's: locacao principal + aluguel percentual
docs/bp/planilha.py    gera as planilhas com formulas vivas
```

Rodar: `cd docs/bp && PYTHONPATH=. python3 piumhi.py` (idem para os outros). Sem
dependências externas, exceto `planilha.py`, que precisa de `openpyxl`.

Planilhas: `docs/bp/Modelo-Economico-Piumhi.xlsx` e
`docs/bp/Modelo-Economico-Rede.xlsx`. As abas mensais têm fórmulas que apontam para a aba
`Premissas` — `IRR`, `NPV` e `MATCH` de verdade. Mudar a TMA, a receita madura, o aluguel
ou o número de assinantes recalcula tudo.
