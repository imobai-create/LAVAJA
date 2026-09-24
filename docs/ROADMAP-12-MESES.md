# Roadmap do produto digital — 12 meses (com os gates até o mês 24)

Este documento traduz o roadmap de 24 meses do Plano de Franquia (set/2026) em um plano de
trabalho **do produto digital**: site, aplicativo, dados e ferramentas de gestão. Ele não repete o
plano de obra nem o plano financeiro — só diz o que precisa existir em software, quando, e qual
condição do negócio libera cada entrega.

> **Gate legal que atravessa tudo:** enquanto a Circular de Oferta de Franquia (COF) não estiver
> pronta, **nenhuma página, formulário, anúncio ou material digital pode vender, ofertar ou
> receber pagamento de franquia** (Lei nº 13.966/2019, art. 2º e 4º). Até lá, a única coisa
> publicável sobre expansão é uma página institucional de "quem somos / interesse em conversar no
> futuro", sem preço, sem taxa, sem projeção de retorno e sem botão de compra. Venda feita antes
> disso é anulável, com devolução corrigida e perdas e danos.

---

## Mês a mês — meses 1 a 12 (o que este repositório entrega)

### Mês 1 — Landing de pré-venda no ar
- Landing de Piumhi publicada, mobile-first, com formulário de reserva e consentimento LGPD.
- Deploy no Railway com Postgres, domínio próprio e HTTPS (ver [DEPLOY.md](DEPLOY.md)).
- Política de Privacidade publicada com os dados reais da empresa preenchidos.
- Painel de leads protegido por token; exportação em CSV funcionando.
- **Gate para divulgar:** [CHECKLIST-PRE-VENDA.md](CHECKLIST-PRE-VENDA.md) com todos os itens
  fechados — principalmente preço final, quem responde o WhatsApp e em quanto tempo.

### Mês 2 — Medição e primeira campanha
- Parâmetros de origem (UTM) gravados em cada lead: sem isso não existe custo por lead confiável.
- Painel mostrando reservas por dia, por plano e por origem.
- Campanha local (Meta Ads geolocalizado em Piumhi) com orçamento pequeno e teto definido.
- Relatório semanal simples: leads, custo por lead, tempo médio de resposta no WhatsApp.

### Mês 3 — Marca e proteção
- Pedido de registro da marca **JatoJá no INPI, classes 35 e 37** (37 = lavagem de veículos;
  35 = franquia/serviços de gestão comercial). Sem a marca pedida, a franquia não se formata:
  a COF precisa informar a situação da marca no INPI.
- Registro do domínio no CNPJ da empresa, não no CPF de ninguém.
- Contas de e-mail no domínio próprio.

### Mês 4 — Escolha do white-label de assinatura
- Definir a plataforma de assinatura/agendamento (faixa de R$ 1–3 mil/mês, conforme o plano).
- Critérios de escolha, nessa ordem: cobrança recorrente com PIX e cartão; **exportação total
  dos dados do cliente** (sem isso você fica refém); API para ler faturamento; suporte em
  português; contrato sem multa alta de saída — no ano 2 a migração para o app próprio é provável.
- Piloto interno com 5 a 10 assinantes de teste antes da inauguração.

### Mês 5 — Integração obra + tecnologia
- **LPR (leitura de placa) especificada e cabeada durante a obra.** Passar cabo e energia depois
  é caro e feio; a decisão de LPR é do mês 5, não do mês 12.
- Definir como a liberação da lavagem acontece na prática: LPR, QR code no celular ou código
  digitado. Ter um plano B que funcione sem internet no dia da inauguração.
- Checkout da assinatura ligado à landing: quem reservou recebe um link e vira assinante pagante.

### Mês 6 — Inauguração digital
- Conversão da lista de fundadores em assinantes pagantes (ver taxa esperada no checklist).
- Página de FAQ e de "como funciona" atualizadas com a operação real, não com a promessa.
- Google Business Profile da unidade criado, com fotos reais, horário e telefone.
- Primeira medição de churn programada para 30, 60 e 90 dias.

### Meses 7 a 9 — Operação e KPIs auditáveis
- **Cinco números, medidos toda semana, sempre pela mesma fonte:** assinantes ativos, churn
  mensal, lavagens por dia, ticket médio, receita por box. Esses números são o que entra na COF
  no mês 13 — planilha manual não serve, precisa sair do sistema.
- Conciliação entre o que o white-label cobrou e o que entrou na conta. Divergência recorrente
  aqui é sinal de que a plataforma escolhida não serve.
- Alertas simples: queda de assinantes, falha de cobrança, máquina parada.

### Meses 10 a 12 — Processos viram manual
- Cada rotina digital documentada (abrir o dia, tratar cobrança recusada, atender pedido de
  cancelamento, responder pedido de exclusão de dados pela LGPD, exportar relatório mensal).
- Esses textos são o rascunho do **Manual de Operação** da franquia — escrever depois, do zero,
  custa meses.
- Backup testado: restaurar o banco em ambiente separado pelo menos uma vez.
- Fechamento do ano 1 com 12 meses de dados consistentes. **É isso que libera a Fase 1.**

---

## Meses 10 a 15 — Formatação (a franqueadora nasce)

- Franqueadora constituída como PJ separada; contabilidade dela limpa desde o dia 1.
- COF redigida por advogado, com os números reais de Piumhi — os do mês a mês acima.
- **Decisão white-label vs app próprio**, com base em dados e não em vontade. Critérios objetivos:
  - custo mensal do white-label × número de unidades previstas para os anos 2 e 3;
  - o white-label suporta repasse automático de royalties (6%) e fundo (2%) por unidade?
  - suporta multiunidade com visão consolidada da franqueadora?
  - qual o custo de migrar depois (exportação de base, histórico de cobrança, cartões tokenizados)?
  - o app próprio é orçado no plano em ~R$ 350 mil e entra no pico de consumo de caixa dos anos
    2–3 (~R$ 720 mil) — se a decisão for adiantar, o caixa precisa comportar.
- Site institucional da franqueadora: **só institucional**. Nada de "seja um franqueado, invista
  R$ X" antes da COF pronta. Formulário de interesse, se existir, deve dizer com todas as letras
  que não é oferta e que nenhum valor será cobrado nessa etapa.

## Meses 15 a 20 — Capitólio e landing por praça

- Landing por praça, reaproveitando a de Piumhi (o campo `origem` do banco já separa por cidade).
- Unidade de Capitólio (modelo Prime) com pré-venda de fundadores local antes da obra — mesmo
  gate de conversão usado em Piumhi.
- **Só depois da COF entregue e dos 10 dias de carência legal cumpridos**, a página de franquia
  pode virar página de venda, com os números da COF e nada além deles.
- Painel da franqueadora: receita por unidade, royalties apurados, NPS.

## Meses 20 a 24 — App próprio

- Desenvolvimento do app da rede (cadastro e placa, assinatura, agendamento, LPR, carteira,
  indicação, avisos), dashboards de franqueado e visão consolidada da franqueadora.
- Migração dos assinantes do white-label — planejada com meses de antecedência e com plano de
  rollback. Migração de base de cobrança recorrente é o momento de maior risco de churn do plano
  inteiro: cartão que não migra é assinante perdido.
- O app vira o principal ativo intangível da franqueadora e o que justifica o royalty.

---

## Riscos digitais que merecem atenção agora

| Risco | Por que importa | Como reduzir |
|---|---|---|
| Ficar refém do white-label | Sem exportar a base, migrar no ano 2 fica caro ou impossível | Exigir exportação completa em contrato, antes de assinar |
| Dados de lead sem UTM | Sem custo por lead não há decisão de mídia | Gravar origem desde o primeiro anúncio |
| Reserva grátis com conversão baixa | Lista grande e caixa vazio na inauguração | Ver [CHECKLIST-PRE-VENDA.md](CHECKLIST-PRE-VENDA.md) |
| Publicar algo que pareça oferta de franquia | Passivo legal da Lei 13.966 e contrato anulável | Revisão jurídica de qualquer página sobre expansão |
| LPR decidido tarde | Obra refeita custa caro | Especificar no mês 5, durante a obra |
| Marca não registrada | Trava a formatação e a COF | Pedido no INPI no mês 3 |
