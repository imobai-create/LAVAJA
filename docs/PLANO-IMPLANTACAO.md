# Plano de implantação — loja própria e rede

Quem faz o quê, em que ordem, e qual condição libera cada etapa. Os números estão em
[BP-PIUMHI.md](BP-PIUMHI.md), [BP-REDE.md](BP-REDE.md) e [CENARIOS.md](CENARIOS.md); o roadmap
do software está em [ROADMAP-12-MESES.md](ROADMAP-12-MESES.md). Data: 2026-10-20.

**Regra que atravessa o documento:** cada fase tem um **gate** — uma condição verificável que
libera a próxima. Gate não cumprido não é motivo para acelerar; é motivo para parar e revisar.

---

## Fase 0 — Os 90 dias antes de comprar a máquina

Custo desta fase: cerca de **R$ 30 mil** (campanha de fundadores, honorários, deslocamentos).
É o trecho mais barato e o que mais muda decisão.

| Prazo | Ação | Responsável | Por que decide |
|---|---|---|---|
| 7 dias | Baixar a planilha "Frota por Município e Tipo" no portal do Ministério dos Transportes e confirmar Piumhi | Antonio | É o denominador do plano inteiro; hoje vem de uma reportagem |
| 7 dias | **Registrar a marca no INPI (classes 35 e 37) em nome da PJ 1** | Antonio + agente de PI | Antes de qualquer conversa com investidor. Sem isso, vender quota da operação é vender quota da rede |
| 7 dias | Busca de anterioridade no INPI (há uma "Fast Wash" operando) | Agente de PI | Pode obrigar troca de nome antes da primeira fachada |
| 7 dias | Parecer do contador: Anexo III ou V do Simples, CNAE e tratamento do pró-labore | Contador | Vale R$ 47 mil/ano; no Anexo V o projeto cai abaixo da TMA |
| 15 dias | CEMIG: tensão entregue no ponto e prazo de aumento de carga | Antonio | Define 220 V ou 380 V no pedido da máquina |
| 15 dias | SAAE Piumhi: tarifa comercial de água e esgoto | Antonio | Linha de custo variável, todo mês, para sempre |
| 15 dias | Prefeitura: licença ambiental e exigência de caixa separadora | Antonio | Pode mudar a obra civil inteira |
| 15 dias | Grupo MF e Covre: têm modelo sem escova? É credenciado no BNDES? Preço? | Antonio | Abaixo de R$ 134 mil muda a decisão da máquina |
| 15 dias | Cooperativa de crédito: proposta de R$ 120 mil, 60 meses, 6–12 de carência | Antonio | Só se a opção for o arranjo com dívida ([CENARIOS.md](CENARIOS.md) §1.1) |
| 30 dias | Três orçamentos locais de obra civil, elétrica e caixa separadora | Antonio | Valida ou derruba os R$ 328 mil de capex |
| 30 dias | Negociar o aluguel do terreno: 10 anos, **opção de compra com preço travado**, indenização de benfeitoria, **autorização expressa de sublocação** | Antonio + advogado | Protege R$ 142 mil de benfeitoria e habilita a estrutura da rede depois |
| 30 dias | Ligar para o distribuidor brasileiro do fabricante | Antonio | Números reais de operação no Brasil, com a mesma máquina |
| **30 dias** | **Site no ar + campanha dos 80 fundadores** | Claude (deploy) / Antonio (campanha) | Transforma a premissa de demanda em evidência **e** levanta R$ 69,5 mil |
| 45 dias | Acordo de quotistas e contrato de licença PJ 1 → PJ 2 | Advogado | Declarado na entrada é legítimo; combinado depois é contestável |
| 60 dias | Fechar o fornecedor: 60 Hz, tensão, Modbus, kit de peças, garantia, Incoterm | Antonio | Destrava a obra e o cronograma |
| 90 dias | Constituir a PJ 1 (franqueadora) e a PJ 2 (operação) | Contador + advogado | Para contratar, faturar e emitir nota |

### Gate da Fase 0 → Fase 1

Quatro condições, todas verificáveis:

1. **50 ou mais reservas de fundador** confirmadas (meta: 80).
2. **Frota de Piumhi confirmada** na tabela do Senatran.
3. **Parecer do contador** indicando Anexo III, ou o modelo rerrodado no Anexo V e ainda acima
   da TMA.
4. **Orçamento de obra dentro de R$ 360 mil** de capex total.

Menos de 50 reservas → **não compre a máquina.** Revise preço, oferta ou praça. O capital
grande ainda não saiu, e é exatamente para isso que a Fase 0 existe.

---

## Fase 1 — A loja própria de Piumhi

Capital: **R$ 376 mil** (100% equity) ou **R$ 278 mil** (com dívida de R$ 120 mil). Divisão do
equity em [CENARIOS.md](CENARIOS.md) §2.

| Mês | Marco | Responsável | Depende de |
|---|---|---|---|
| 1 | Pedido da máquina assinado, 30% pago | Antonio | Gate da Fase 0 |
| 1 | Contrato de locação assinado; projeto arquitetônico contratado | Antonio | Negociação da Fase 0 |
| 1–2 | Protocolo de licenciamento ambiental e alvará | Antonio | Projeto |
| 2 | Entrada de energia: pedido de aumento de carga na CEMIG | Antonio | Tensão confirmada |
| 2–4 | Obra civil: pátio, baia, piso com caimento, caixa separadora | Empreiteiro | Alvará |
| 3 | Instalação elétrica, quadro, ART, laudo NR-12 | Eletricista + eng. mecânico | Obra |
| 3–4 | Máquina embarcada, desembaraçada e transportada | Despachante | 70% pago contra BL |
| 4 | Totem de pagamento, câmera de placa, CFTV, rede | Integrador | Obra e energia |
| 4 | Montagem e comissionamento da máquina com o técnico do fabricante | Fabricante | Tudo acima |
| 4 | Contratação e treinamento do atendente | Antonio | — |
| 4 | **Dimensionar pátio e entrada de energia para DUAS máquinas** | Projeto | Decisão de projeto, custa pouco agora |
| 5 | Inauguração. Fundadores ativados; cobrança recorrente rodando | Antonio | Comissionamento |
| 5–8 | Rampa: meta de 300 assinantes no mês 8 | Antonio | Marketing local |
| 6 | Boxes de alta pressão e aspiradores instalados, pagos pelo caixa | Antonio | Caixa positivo |
| 9–12 | Rampa: meta de 450+ no mês 12 | Antonio | — |
| 12 | **Fechamento do ano com número auditável** | Contador | — |

### O que medir desde o primeiro dia

Sem isso a Fase 2 não tem base, e o número que falta é sempre o mais importante:

- assinantes ativos, por plano
- **cancelamentos por mês** (churn) — o número que mais mata assinatura
- lavagens por dia, e **lavagens por assinante do plano Ilimitada** (a premissa mais frágil)
- consumo real de água (m³) e energia (kWh) por lavagem
- horas de gente por semana na operação — define se o franqueado precisa de gerente
- custo por lead e por assinante adquirido
- tempo de máquina parada

### As três travas do plano Ilimitada — antes da primeira venda

1. Uso justo em contrato: 1 lavagem por veículo por dia, teto de 12 por mês.
2. Uma placa, um plano: a câmera liga a lavagem ao veículo cadastrado.
3. Prazo na trava de preço do fundador: 24 ou 36 meses, não "para sempre".

Mudar qualquer uma depois de vender é quebra de promessa.

### Gate da Fase 1 → Fase 2

| Condição | Mínimo |
|---|---|
| Assinantes ativos no mês 12 | **~400** |
| Churn mensal | abaixo de 5% |
| Lavagens/mês por assinante Ilimitada | **abaixo de 8** |
| EBITDA dos últimos 3 meses | positivo e consistente |
| Doze meses de demonstrativo contábil | fechados |

Abaixo de 400 assinantes a Fase 2 **não começa** — e não começar não é fracasso: é a loja
própria rodando com 34% de TIR enquanto a tese de rede espera dados melhores.

---

## Fase 2 — A rede

**Nenhuma linha desta fase acontece antes do gate da Fase 1.** Formatar franquia custa COF,
manual, software e equipe de campo: centenas de milhares que não voltam se a premissa estiver
errada.

| Mês | Marco | Responsável |
|---|---|---|
| 13 | PJ 1 (franqueadora) ativada; a unidade passa a pagar royalty como qualquer franqueado | Contador |
| 13–15 | Conversar com 3 investidores imobiliários locais sobre build-to-suit na 2ª praça | Antonio |
| 14–16 | Manual de operação e manual de implantação, escritos a partir do que Piumhi aprendeu | Antonio |
| 15 | **COF** com advogado especializado, sobre o balanço real da franqueadora | Advogado |
| 15–17 | Software de rede: painel multiunidade, cobrança, indicadores comparáveis | Claude |
| 16 | Definição do perfil do franqueado: **operador, nunca investidor ausente** | Antonio |
| 18 | **Primeira franquia vendida — nunca antes** | Antonio |
| 18–24 | 2ª e 3ª unidades em operação; ajuste do manual com o que elas ensinarem | — |

### A estrutura do ponto comercial, decidida

Das quatro avaliadas ([CENARIOS.md](CENARIOS.md) §3), a recomendação é **build-to-suit com
investidor imobiliário local**: ele compra o terreno e constrói no projeto padrão, em contrato
de 10 a 15 anos, **com a locação em nome da franqueadora** e sublocação ao franqueado.

- O investidor local faz ~11,6% a.a. nominal com inquilino de prazo longo — bom negócio para o
  hurdle dele.
- A franqueadora fica com **capital zero no imóvel** e o ponto sob contrato: franqueado que sai
  não leva a praça.
- O franqueado entra com **R$ 310 mil** em vez de R$ 504 mil, e faz 27,3% em vez de 13,3%.

Comprar o imóvel com capital da franqueadora está descartado: 15,6% sobre R$ 32,5 milhões
contra 42,6% sobre R$ 653 mil ([ADR-011](DECISOES.md)). O **over no aluguel** (modelo
McDonald's) volta à mesa se alguma praça provar receita madura acima de **R$ 64 mil/mês**.

### Gate da Fase 2 → expansão

| Condição | Antes de vender a 4ª franquia |
|---|---|
| Unidades franqueadas com 6+ meses | 3 |
| EBITDA médio delas | dentro de 15% do projetado |
| Churn médio da rede | abaixo de 6% |
| Nenhuma unidade em recuperação ou litígio | — |

---

## As duas empresas

| PJ | Papel | Dono |
|---|---|---|
| **PJ 1 — Franqueadora** | Marcas, software, licenciamento, royalty e taxa de tecnologia. É o balanço dela que vai para a COF | **100% Antonio** |
| **PJ 2 — Operação Piumhi** | A loja. Do mês 13 em diante paga royalty como qualquer franqueado | Antonio + investidores |
| PJ 3 (só se houver compra de imóvel) | Holding patrimonial, aluga a mercado, resultado separado | a definir |

A separação é exigência legal (a COF pede o balanço da franqueadora) e proteção patrimonial
(risco cruzado). **A marca na PJ 1 antes de qualquer assinatura de investidor** é a cláusula
mais valiosa do projeto.

---

## O que pode atrasar tudo, em ordem de probabilidade

| Risco de prazo | Efeito | Mitigação |
|---|---|---|
| Licenciamento ambiental | 30 a 90 dias | Protocolar no mês 1, antes da obra |
| Aumento de carga na CEMIG | 30 a 60 dias | Pedir no mês 2, com projeto pronto |
| Desembaraço da máquina no porto | 15 a 45 dias | Despachante contratado antes do embarque |
| Máquina em 50 Hz ou tensão errada | **meses** | 60 Hz e tensão por escrito no pedido — o erro clássico |
| Obra civil | 30 dias de folga | Contrato com multa por atraso |
| Câmbio entre pedido e pagamento final | R$ 10 a 20 mil | Travar câmbio ou orçar a R$ 5,60 |

O cronograma da Fase 1 tem **inauguração no mês 5** e já embute folga. Prometer mês 3 a
investidor é como se perde credibilidade na primeira reunião de acompanhamento.
