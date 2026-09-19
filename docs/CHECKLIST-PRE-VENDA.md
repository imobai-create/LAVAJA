# Checklist de pré-venda — campanha dos 80 fundadores

Checklist operacional para **antes de divulgar o site** e para **durante** a campanha. É curto de
propósito: cada item aqui é uma decisão que, se ficar em aberto, aparece como problema na frente
do cliente.

---

## Parte 1 — O que precisa estar DECIDIDO antes de divulgar

Divulgar sem estes sete itens fechados é o jeito mais rápido de queimar a lista de contatos da
cidade. Você só divulga uma primeira vez.

### 1. Preço final, com data de validade
- [ ] Preço do plano de fundador definido e **travado por escrito** (por quanto tempo vale o preço
      travado: para sempre? 12 meses? 24 meses?). Se o site diz "para sempre", é para sempre.
- [ ] Preços dos demais planos e da lavagem avulsa definidos.
- [ ] Decidido o que acontece com o preço quando as 80 vagas acabarem.
- [ ] Conferido se o preço fecha a conta: com 80 assinantes no plano de fundador, qual é a receita
      mensal e ela cobre o custo fixo da unidade?

### 2. Número de WhatsApp de atendimento
- [ ] Número **exclusivo do negócio**, não o celular pessoal. Trocar depois significa perder
      conversas e refazer anúncio.
- [ ] WhatsApp Business instalado, com mensagem de saudação, horário de atendimento e catálogo.
- [ ] Número configurado na variável `WHATSAPP_NUMERO` do servidor (ver [DEPLOY.md](DEPLOY.md)).

### 3. Quem responde, e em quanto tempo
- [ ] Nome da pessoa responsável por responder — uma pessoa, não "a gente vê".
- [ ] Tempo de resposta prometido internamente (sugestão: **até 2 horas em horário comercial**).
      Lead de anúncio esfria rápido; quem responde no dia seguinte perde a venda.
- [ ] Quem cobre fim de semana, feriado e horário de almoço.
- [ ] Roteiro de resposta pronto: primeira mensagem, resposta às 5 perguntas mais comuns,
      mensagem de follow-up para quem não responde em 3 dias.

### 4. O que exatamente o fundador ganha
Escrito em uma frase que caiba em um print de WhatsApp, e igual no site, no anúncio e na boca de
quem atende.
- [ ] O benefício está claro (preço travado? mês grátis? brinde? prioridade na inauguração?).
- [ ] Está claro o que **não** está incluído (quais serviços, quantas lavagens, quais veículos).
- [ ] Está claro se a vaga é transferível e se vale para mais de um carro.
- [ ] Está claro que a reserva é gratuita e **não gera cobrança agora**.

### 5. Como a cobrança vai ser feita na inauguração
Este é o item que costuma ser deixado para depois e que decide a conversão.
- [ ] Meio de cobrança definido e **testado** (cartão recorrente, PIX automático, boleto).
- [ ] Plataforma de assinatura contratada e funcionando antes da inauguração — não no dia.
- [ ] Definido o dia de vencimento e o que acontece com quem entra no meio do mês.
- [ ] Definido o roteiro de conversão: quem liga/manda mensagem para os 80, em que ordem, com
      qual texto, e em quantos dias a vaga expira se a pessoa não responder.
- [ ] Definida a política de cancelamento (fidelidade? multa? cancelamento pelo WhatsApp?).

### 6. O que acontece se a obra atrasar
- [ ] Definido o que é comunicado, por quem e quando — silêncio é o que mata a lista.
- [ ] Definido se a vaga e o preço travado continuam valendo (a resposta honesta é: sim).
- [ ] Texto de aviso de atraso já escrito, para não ter que improvisar no dia.
- [ ] **O site não promete data de inauguração.** Fala em "assim que a unidade abrir". Promessa de
      data que não se cumpre vira reclamação pública e pedido de reembolso.

### 7. LGPD e o básico legal
- [ ] Política de Privacidade publicada com razão social, CNPJ, endereço e e-mail reais.
- [ ] Definido quem atende pedidos de exclusão de dados e em quanto tempo (a política promete 15 dias).
- [ ] A lista de leads não vai circular em grupo de WhatsApp nem em planilha solta no Drive.
- [ ] Nenhuma peça da campanha fala em franquia, investimento ou retorno — a campanha dos
      fundadores é para **cliente final**. (Lei nº 13.966/2019: sem COF, não existe oferta de franquia.)

---

## Parte 2 — O que medir, desde o primeiro dia

Se não for medido, a decisão sobre gastar mais ou menos em anúncio vira palpite.

| Indicador | Como calcular | Para que serve |
|---|---|---|
| **Leads (reservas)** | Total no painel | Volume bruto da campanha |
| **Custo por lead (CPL)** | Gasto em anúncio ÷ reservas | Diz se a mídia está cara |
| **Origem do lead** | Campo `origem`/UTM de cada reserva | Diz **qual** anúncio funciona |
| **Taxa de resposta no WhatsApp** | Quantos respondem o primeiro contato | Mede a qualidade do lead |
| **Tempo médio de resposta** | Da reserva até a sua primeira mensagem | O indicador mais correlacionado com conversão |
| **Conversão reserva → pagante** | Assinantes pagantes ÷ reservas | **O número que importa de verdade** |
| **Custo de aquisição (CAC)** | Gasto total ÷ assinantes pagantes | Compare com a mensalidade: em quantos meses paga? |
| **Churn dos 30/60/90 dias** | Cancelamentos ÷ base | Diz se o produto segura o cliente |

Monte uma planilha simples com uma linha por semana: gasto, leads, CPL, conversas iniciadas,
assinantes pagantes. Cinco minutos por semana.

---

## Parte 3 — A verdade sobre a reserva grátis

**Reserva grátis, sem cartão, converte pouco.** É o preço de não colocar barreira: a pessoa se
inscreve num impulso, sem compromisso nenhum, e some quando chega a hora de pagar. Como regra
prática de campanhas de pré-venda (não é número do seu negócio, é ordem de grandeza para
planejar), espere algo entre **10% e 30%** da lista virando assinante pagante — e o que decide
onde você cai nessa faixa é o tempo de resposta e o quanto a pessoa lembra de ter se inscrito.

O que isso significa na prática:

- Para fechar **80 fundadores pagantes**, planeje capturar **entre 300 e 800 reservas**. Tratar
  80 reservas como 80 clientes é o erro clássico — e ele aparece justamente no mês da
  inauguração, quando o caixa mais precisa entrar.
- **Lista grande não é caixa.** Só assinatura ativa com cobrança aprovada é caixa.
- Quanto maior o intervalo entre a reserva e a inauguração, pior a conversão. Cada mês de atraso
  esfria a lista. Se a obra atrasar, mantenha contato mensal, curto, com foto do andamento.

### Como aumentar a conversão (em ordem de eficácia)

1. **Responder rápido.** Contato em minutos converte muito mais que contato em dias. É de graça.
2. **Pedir um sinal simbólico** (ex.: R$ 10 a R$ 20 por PIX, abatidos na primeira mensalidade, com
   devolução garantida por escrito). Isso derruba o número de reservas e **sobe muito** a
   conversão — a lista fica menor e real. Se optar por isso, o site precisa dizer com clareza o
   valor, que é abatido, e como pedir de volta. Decida isso **antes** de divulgar: mudar a regra
   no meio da campanha com gente já inscrita gera briga.
3. **Manter contato** durante a obra: uma mensagem por mês, com foto do andamento.
4. **Dar prazo à vaga** ("sua vaga fica reservada por X dias após a inauguração") — cria a decisão.
5. **Pedir indicação** logo na confirmação: quem reserva costuma ter mais de um carro na família.

### Sinais de alerta durante a campanha

- CPL subindo semana após semana: o público local saturou; troque a peça, não o orçamento.
- Muitas reservas e pouca resposta no WhatsApp: o anúncio está atraindo curioso, ou o número
  está errado. Teste enviando uma mensagem para si mesmo.
- Reservas concentradas em um único plano bem mais barato: o preço dos outros planos não está
  sendo entendido.
- Pedidos de exclusão de dados acima do normal: a mensagem de abordagem está parecendo spam.
