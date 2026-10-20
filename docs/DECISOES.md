# Registro de decisões técnicas (ADR)

Cada decisão registrada com contexto, escolha, consequências e o que faria a gente mudar de
ideia. Formato curto, em ordem cronológica. Quando uma decisão for revista, não apague: acrescente
um novo registro e marque o antigo como substituído.

**Contexto comum a todas:** site de pré-venda de um lava jato por assinatura em Piumhi/MG (cidade
de ~40 mil habitantes). Público majoritariamente mobile, muitas vezes em 4G instável. Equipe de
manutenção: praticamente ninguém — o dono não é de TI. O site precisa continuar funcionando
sozinho por meses sem que ninguém toque nele.

---

## ADR-001 — Express 4 + Postgres, sem framework pesado

**Status:** aceito · **Data:** set/2026

**Contexto.** O servidor faz três coisas: entregar arquivos estáticos, gravar um lead e devolver
uma contagem de vagas. Havia a opção de usar Next.js, NestJS, Rails, Laravel ou um
Backend-as-a-Service (Firebase, Supabase).

**Decisão.** Express 4 com Postgres, duas dependências ao todo (`express`, `pg`).

**Por quê.**
- O problema é pequeno e estável. Framework grande cobra o preço da sua complexidade todo mês,
  em atualização e em build quebrado — e aqui não entrega nada em troca.
- Postgres é o banco padrão do Railway, tem backup, exportação em CSV e qualquer desenvolvedor
  sabe mexer. Os dados de lead são o ativo da campanha: precisam ser portáveis.
- Express 4 (e não o 5, recém-lançado) porque a documentação, os exemplos e as respostas de fórum
  que qualquer pessoa vai encontrar daqui a dois anos são de Express 4.
- O servidor cai para armazenamento em memória se não houver `DATABASE_URL`, o que faz o projeto
  rodar na máquina de qualquer pessoa sem instalar banco nenhum.

**Consequências.** Nada de ORM, migrations ou painel pronto: a criação da tabela é um
`CREATE TABLE IF NOT EXISTS` no start. Se o modelo de dados crescer muito, isso vira limitação.

**O que mudaria a decisão.** Se o produto passar a ter contas de usuário, cobrança recorrente e
agendamento próprios (o app do ano 2 do plano), aí sim vale um framework com autenticação,
migrations e background jobs — e provavelmente um projeto separado deste.

---

## ADR-002 — HTML estático servido direto, em vez de React/SPA

**Status:** aceito · **Data:** set/2026

**Contexto.** A landing precisa carregar rápido em celular no interior e aparecer bem no Google.
O padrão de mercado hoje seria React (Next.js, Vite, Astro).

**Decisão.** HTML escrito à mão em `public/`, CSS em um arquivo, JavaScript mínimo e sem build.

**Por quê.**
- **Velocidade.** Uma SPA típica manda de 80 a 200 KB de JavaScript antes de desenhar a primeira
  letra. Esta página desenha com HTML e CSS. Em 4G ruim, isso é a diferença entre ler a oferta e
  fechar o navegador — e o visitante que fecha antes de carregar é dinheiro de anúncio queimado.
- **SEO.** O conteúdo está no HTML que o Google recebe, sem depender de renderização de JS. Para
  busca local ("lava jato Piumhi"), isso é o caminho mais curto e mais confiável.
- **Sem build.** Não existe `npm run build`, nem bundler que quebra numa atualização, nem
  dependência que fica desatualizada. Daqui a dois anos o arquivo abre e edita do mesmo jeito.
- **Manutenção por quem não é programador.** Mudar um preço é abrir o HTML e trocar o número.
  Em React seria mexer em componente, rodar build e publicar.

**Consequências.** Trechos repetidos entre páginas (cabeçalho, rodapé) são copiados à mão. Com
muitas landings por praça (Fase 2 do plano), isso passa a doer.

**O que mudaria a decisão.** A partir de umas 4 ou 5 landings por cidade, vale um gerador estático
simples (Astro, Eleventy) que mantém HTML na saída — não uma SPA. A regra permanece: o que o
visitante recebe tem que continuar sendo HTML pronto.

---

## ADR-003 — Sem dependências além de `express` e `pg`

**Status:** aceito · **Data:** set/2026

**Contexto.** Seria natural instalar `helmet`, `express-rate-limit`, `dotenv`, `joi`, `winston`,
`csv-stringify`. Cada um resolve um problema pequeno deste projeto.

**Decisão.** Não instalar. Cabeçalhos de segurança, rate limit por IP, validação de entrada e
geração de CSV são ~200 linhas escritas no próprio repositório, em `src/`.

**Por quê.**
- **Superfície de ataque e manutenção.** Cada dependência traz as dependências dela. Um projeto
  que ninguém vai atualizar por meses é melhor com 2 pacotes do que com 20 — supply chain de npm
  é risco real, e alerta de vulnerabilidade que ninguém lê é pior que ausência de alerta.
- **Build reproduzível.** Menos pacote é build mais rápido, imagem Docker menor e menos chance de
  um deploy quebrar por causa de uma versão nova de algo periférico.
- **Legibilidade.** O rate limit daqui cabe em 20 linhas e qualquer pessoa entende lendo. A
  configuração de uma biblioteca equivalente não é mais simples que isso.

**Consequências.** O rate limit é por processo e em memória: reiniciou, zerou; com duas réplicas,
cada uma conta o seu. É suficiente para conter envio repetido de formulário, e não substitui um
WAF. Está documentado como limitação consciente, não como esquecimento.

**O que mudaria a decisão.** Ataque real de volume, várias réplicas em produção, ou necessidade de
pagamento/antifraude — aí entram ferramentas maduras, e não código próprio.

---

## ADR-004 — Painel admin protegido por token, não por login

**Status:** aceito · **Data:** set/2026

**Contexto.** O painel lista as reservas (nome, WhatsApp, plano) e exporta CSV. São dados pessoais
sob a LGPD e precisam de controle de acesso. Um sistema de login exigiria tabela de usuários,
hash de senha, sessão ou JWT, "esqueci minha senha" (que exige serviço de e-mail), bloqueio por
tentativa e uma tela de cadastro.

**Decisão.** Acesso por um segredo único no cabeçalho `x-admin-token`, guardado na variável de
ambiente `ADMIN_TOKEN`. Sem a variável configurada, as rotas administrativas **não liberam nada**
— falham fechado.

**Por quê.**
- **Existe exatamente um usuário administrador:** o dono. Um sistema de contas para um usuário só
  é complexidade sem benefício — e cada peça dele (recuperação de senha, sessão) é uma porta a
  mais para invadir.
- **Um token aleatório de 32 bytes é mais forte que a senha que a maioria das pessoas escolhe**, e
  não pode ser reusado de outro site vazado.
- O segredo fica em variável de ambiente, fora do código e fora do Git.
- Comparação do token feita em tempo constante e sem registrar o valor em log.

**Consequências e limites — conheça antes de confiar.**
- Vazou o token, vazou o acesso: não há segundo fator. Se houver suspeita, troque a variável no
  Railway (o acesso antigo morre na hora).
- Não há registro de "quem acessou": só existe uma credencial. Se um dia mais de uma pessoa
  precisar entrar, isso deixa de ser aceitável.
- O token nunca deve ir em link, mensagem de WhatsApp ou planilha. Cabeçalho de requisição e
  gerenciador de senhas, só.

**O que mudaria a decisão.** Mais de uma pessoa com acesso, necessidade de trilha de auditoria por
pessoa, ou o painel passando a mostrar dados de franqueados (Fase 2 do plano). Aí entram contas
individuais, perfis de permissão e log de acesso — requisito, inclusive, para levar isso a sério
com dados de terceiros.

---

## ADR-005 — Deploy por Docker no Railway

**Status:** aceito · **Data:** set/2026

**Contexto.** O Railway consegue detectar um projeto Node e publicar sem `Dockerfile` (Nixpacks).
Havia também a opção de PaaS gratuitos e de VPS.

**Decisão.** `Dockerfile` multi-stage explícito (node:22-alpine, `npm ci --omit=dev`, usuário
não-root, healthcheck em `/health`), publicado no Railway com plano pago.

**Por quê.**
- **Previsibilidade.** A versão do Node está fixada no `Dockerfile` e no `.nvmrc`; a mesma imagem
  roda na máquina do desenvolvedor, no CI e em produção. Detecção automática muda de comportamento
  entre versões da plataforma, sem aviso.
- **Portabilidade.** Se o Railway ficar caro ou mudar de política, a mesma imagem sobe em Fly.io,
  Render ou qualquer VPS. Isso é seguro contra lock-in por US$ 0.
- **Segurança básica de graça:** processo como usuário não-root, imagem sem ferramentas de build,
  `.dockerignore` impedindo que `.env`, `.git` e `docs/` entrem na imagem.
- **Plano pago, e não free tier**, porque os gratuitos dormem: a primeira visita depois da
  inatividade espera 30 a 60 segundos. Em campanha paga, isso custa mais que os US$ 5 do plano.
  Comparação completa em [DEPLOY.md](DEPLOY.md).

**Consequências.** Build um pouco mais lento que a detecção automática, e o `Dockerfile` precisa
ser atualizado quando o Node 22 sair do suporte (LTS até 2027).

**O que mudaria a decisão.** Custo do Railway subindo muito com a escala, ou necessidade de rodar
vários serviços juntos (app, painel, workers) — aí vale reavaliar entre VPS gerenciado e outro PaaS.

---

## ADR-006 — Railway em vez de Vercel

> **REVOGADA em out/2026 pela [ADR-013](#adr-013--vercel-em-vez-de-railway-revoga-a-adr-006).**
> O empreendedor decidiu ir de Vercel. O texto abaixo fica como histórico do raciocínio
> original, não como recomendação vigente.

**Status:** aceito · **Data:** set/2026

**Contexto.** O dono já tinha conta na Vercel e importou o repositório para lá, o que levantou a
pergunta de qual das duas plataformas hospeda o site.

**Decisão.** O site oficial fica no **Railway**. O projeto importado na Vercel deve ser apagado,
para não existirem dois endereços e alguém divulgar o errado.

**Por quê.**
- **Arquitetura.** Este projeto é um servidor Express de processo longo com Postgres. A Vercel
  executa funções serverless: rodar lá exigiria um wrapper em `api/`, `vercel.json` com rewrites e
  atenção a conexão de banco por invocação. É trabalho para resolver um problema que não existe no
  Railway, onde o `Dockerfile` já pronto sobe sem tocar em código.
- **Banco.** O Railway sobe Postgres no mesmo projeto, com a variável injetada por referência. Na
  Vercel o banco seria de um terceiro (Neon, Supabase), somando mais um fornecedor, mais uma conta
  e mais um lugar onde os dados de clientes ficam guardados — o que a LGPD obriga a declarar.
- **Custo e enquadramento.** O plano gratuito da Vercel é destinado a projeto pessoal, não
  comercial; um site de captação de clientes se enquadra no plano pago (da ordem de US$ 20/mês por
  usuário). O Railway Hobby custa US$ 5/mês com o banco no mesmo projeto.
- **Estado em memória.** Rate limit e cache de vagas vivem na memória do processo. Em servidor
  único isso funciona; em serverless, cada instância teria a sua cópia, enfraquecendo o limite de
  requisições sem ganho nenhum.

**Consequências.** O site depende de uma plataforma paga desde o primeiro dia — o que já era
verdade pelo ADR-005. Em compensação, nenhuma linha de código muda para publicar.

**O que mudaria a decisão.** Se o site virasse estático de verdade (sem formulário próprio, com
captação por serviço externo), a Vercel passaria a ser a escolha óbvia e gratuita. Também mudaria
se a rede crescesse a ponto de justificar mover a API para funções, com banco gerenciado à parte —
decisão para o ano 2, junto com o app próprio.

---

## ADR-007 — Nome da marca: FastCarWash

**Status:** aceito, com ressalva registrada · **Data:** out/2026

**Contexto.** A marca mudou três vezes em duas semanas: LavaJá → JatoJá → FastCarWash. O domínio
`fastcarwash.com.br` foi registrado. A troca no código é barata e já foi feita; o que não é barato
é o registro da marca, que o Plano de Franquia define como ativo central da franqueadora.

**Decisão.** O site passa a usar **FastCarWash**, grafado em caixa camel no logotipo
(`Fast` em tinta, `CarWash` em azul), com o domínio `fastcarwash.com.br`.

**Ressalva — risco de registrabilidade no INPI.** "Fast car wash" descreve literalmente o serviço
prestado. O art. 124, VI da Lei 9.279/96 veda registro de sinal "de caráter genérico, necessário,
comum, vulgar ou simplesmente descritivo, quando tiver relação com o produto ou serviço a
distinguir (...) salvo quando revestidos de suficiente forma distintiva". O
[Manual de Marcas do INPI](https://manualdemarcas.inpi.gov.br/projects/manual/wiki/5%C2%B709_An%C3%A1lise_do_requisito_de_distintividade_do_sinal_marc%C3%A1rio)
determina que sinal em língua estrangeira seja analisado pelo seu significado, considerando o
conhecimento do consumidor médio do serviço — e "car wash" é expressão de uso corrente no setor.

Consequências prováveis:

- Pedido **nominativo** (só a palavra) tende à recusa.
- Pedido **misto** (logotipo + palavra) tende a ser concedido **com apostila**: a proteção recai
  sobre o conjunto, sem exclusividade sobre os termos isolados.
- Na prática, **um concorrente em Formiga pode abrir uma "Fast Car Wash" e a rede não terá como
  impedir**. Para uma franqueadora cujo contrato promete território exclusivo e cuja tese é a
  marca, isso é estrutural, não cosmético.

**O que fazer antes de gastar com fachada, uniforme e adesivagem:** busca de anterioridade e
parecer com agente de propriedade industrial, e decisão consciente entre (a) seguir com a marca
mista aceitando a baixa proteção, ou (b) acrescentar um elemento distintivo que torne o conjunto
registrável com força.

**O que mudaria a decisão.** Parecer do INPI ou de agente apontando recusa também na forma mista,
ou a existência de registro anterior de terceiros em classe 37 — aí a troca de nome volta à mesa,
e é melhor que volte antes da primeira placa impressa do que depois.

> **Atualização — out/2026: a decisão mudou.** Apareceu um anúncio patrocinado de licenciamento de
> uma **Fast Wash / Fast Car Wash** operando e se expandindo no Brasil, no mesmo segmento
> (touchless, 24h, leitura de placa). Deixa de ser só o problema de marca descritiva descrito acima
> e passa a ser **risco de conflito com marca anterior de terceiro**. A recomendação agora é
> **trocar o nome**, não apenas registrá-lo como marca mista. Levantamento em
> [CONCORRENTES.md](CONCORRENTES.md). O código segue em FastCarWash até que o nome novo seja
> definido — a renomeação é um script e roda em minutos.

**Custo das trocas até aqui.** No código, baixo: a renomeação é um script e roda em minutos. Fora
do código, cada troca invalida material gráfico, domínio registrado e qualquer peça já divulgada.
A recomendação é travar o nome agora e só mexer se o INPI obrigar.

---

## ADR-008 — Retirar o formato BOX da oferta de franquia

**Data:** out/2026. **Status:** **aceito** — o empreendedor decidiu retirar o Box em
out/2026. O formato não aparece mais em nenhum documento, modelo ou planilha do projeto.

O Plano de Franquia previa três formatos: Box (R$ 215 mil), Express (R$ 416 mil) e Prime
(R$ 720 mil). Modelado o fluxo de caixa de cada um por 60 meses, com rampa de maturação,
capex de manutenção e valor residual (ver [BUSINESS-PLAN.md](BUSINESS-PLAN.md)):

| Formato | Payback | TIR | VPL @ 18% |
|---|---|---|---|
| BOX | 56 meses | 9,4% | −R$ 45.400 |
| EXPRESS | 37 meses | 29,6% | +R$ 122.738 |
| PRIME | 39 meses | 26,4% | +R$ 152.868 |

**O BOX destrói valor.** TIR de 9,4% contra TMA de 18%, e payback de 56 meses dentro de
um contrato de 60. O franqueado do BOX paga R$ 215 mil, trabalha cinco anos e termina com
menos do que teria na renda fixa.

O payback de 42 meses do plano original considera apenas o capex — ignora a taxa de
franquia (R$ 35 mil) e o capital de giro (R$ 25 mil). Com o desembolso real, são 56.

**Por que é problema da franqueadora, não só do franqueado.** O BOX é a porta de entrada
mais barata e, portanto, a que mais vende. É também a que produz franqueado insatisfeito:
não renova, não indica, atrasa royalty e reclama em público. É passivo de marca com desconto.

**Alternativas avaliadas.** Reprecificar (taxa a R$ 15 mil e royalty a 4%) eleva a TIR para
a casa dos 15% — ainda abaixo da TMA. Manter o BOX apenas como segundo ponto de franqueado
já operante, onde a estrutura fixa é compartilhada, fecha — mas é caso particular, não
formato de catálogo.

**O que mudaria a decisão.** Receita madura do BOX acima de R$ 19 mil/mês comprovada em
operação, ou capex abaixo de R$ 120 mil com fornecedor nacional.

---

## ADR-009 — Avaliar a franqueadora em 10 anos, não em 5

**Data:** out/2026. **Status:** aceito.

Rodado o plano de expansão num horizonte de 60 meses, a franqueadora tem **TIR negativa**
(−6,2% com Box, −12,9% sem) e VPL de −R$ 246 mil. No mês 60 o caixa acumulado ainda é
negativo em R$ 109 mil.

Isso não significa que a franqueadora não funciona — significa que 5 anos é o horizonte
errado. A estrutura (equipe de campo, app, formatação, marketing) é montada nos anos 1 a 3;
o royalty recorrente só supera essa estrutura depois. Medir em cinco anos é medir a rede
exatamente no ano em que ela acabou de pagar o investimento.

Em 120 meses, com 65 unidades no ano 10: **TIR 49,4%**, **VPL R$ 1,265 mi**, caixa positivo
no mês 61, EBITDA de R$ 1,657 mi no ano 10.

Consequência prática: **toda apresentação a investidor da franqueadora usa 10 anos**, e deixa
explícito que o capital é paciente e que o vale de caixa dos anos 2 e 3 (pico de −R$ 714 mil)
é o risco central. Apresentar a franqueadora em 5 anos seria apresentar um projeto de TIR
negativa.

Validação cruzada relevante: o modelo reproduziu de forma independente o pico de consumo de
caixa de ≈ R$ 720 mil citado no Plano de Franquia (obtivemos R$ 714 mil). Nesse ponto o plano
original está internamente consistente.

---

## ADR-010 — Piumhi primeiro, franquia depois

**Data:** out/2026. **Status:** aceito.

A versão anterior do plano pedia **R$ 815 mil**: o pico de caixa consolidado da unidade
própria **mais** a franqueadora rodando ao mesmo tempo por dez anos. O número era
correto para o que media, e inútil como pedido — misturava dois projetos com riscos,
prazos e decisões diferentes, e ninguém conseguia separar o que era capex de implantação
do que era vale de caixa da formatação da rede.

**Decisão:** sequenciar. Fase 1 é a loja modelo de Piumhi, isolada, com capital próprio
de **R$ 475 mil**. Fase 2 é a franqueadora, e só começa a ser formatada depois de **doze
meses de número auditável** em Piumhi — assinantes, churn, lavagens/dia, uso real do
plano Ilimitada, EBITDA.

**Gate explícito:** abaixo de **~400 assinantes** no mês 12, a Fase 2 não começa. Esse é o
número em que a unidade empata a 18% a.a.

**Por que isto é melhor, e não só mais simples.** Formatar franquia custa COF, manual,
software e equipe de campo — centenas de milhares de reais que não voltam se a premissa
de demanda estiver errada. A Fase 1 testa a premissa por R$ 22 mil de campanha de
fundadores. Gastar na ordem inversa é o erro que mais mata rede iniciante.

Efeito colateral bom: sequenciado e sem o BOX, o consolidado fica **mais barato e vale
mais** que a versão anterior — R$ 540 mil de pico contra R$ 815 mil, e VPL de R$ 1,74 mi
contra R$ 1,62 mi. O pico cai para o **mês 9**, ainda dentro da Fase 1.

**O que mudaria a decisão.** Nada que se saiba hoje. Um master franqueado regional
disposto a comprar território com a unidade modelo ainda em obra adiantaria caixa, mas
seria vender franquia sem COF — e isso é ilegal, não arriscado (Lei nº 13.966/2019).

---

## ADR-011 — Não comprar o imóvel das praças com capital da franquia

**Data:** out/2026. **Status:** recomendado, pendente de decisão do empreendedor.

**A ideia avaliada:** a franqueadora compra o terreno de cada praça, constrói a baia, e o
franqueado aluga tudo pronto. Tornaria a rede um negócio misto de franquia e imobiliário.

**O que ela resolve de verdade — e é um problema real.** Com o capex de implantação de
R$ 399 mil, o franqueado entra com R$ 504 mil e faz **TIR de 13,4%** numa praça de
R$ 48 mil/mês de receita madura. Isso é menos que o CDI: **a franquia, como está, não é
vendável.** Com o ponto construído pela rede, o ticket do franqueado cai para R$ 310 mil
e a TIR dele vai a **27,3%**. A ideia ataca o problema certo.

**Por que ainda assim não se deve fazer com capital próprio.** A franqueadora sai de
**42,6% de TIR sobre R$ 653 mil** de capital para **15,6% sobre R$ 32,5 milhões** — 50
vezes mais capital para menos da metade do retorno. O VPL fica negativo nas três
variantes, inclusive com 50% de dívida. E a TIR de 15,6% depende inteiramente de um
valor residual de R$ 47,5 milhões em terrenos valorizados: **sem residual, a TIR é
−62%.** Não é um negócio de lava jato com imóvel, é uma aposta em terra.

A razão é aritmética. Um ponto de R$ 500 mil alugado a R$ 4.000/mês rende 6,9% a.a. de
caixa líquido mais ~2,5 pp de valorização: **9,5% total, com a Selic a 14%**. Dívida não
salva: a 14% de juro contra 14,6% de yield desalavancado, o spread é de 0,6 ponto.

**A janela onde os dois lados fecham é estreita mas existe:** aluguel entre **R$ 5.000**
(mínimo para a franqueadora fazer 18%) e **R$ 5.500** (máximo que o franqueado suporta
fazendo 18%). A R$ 6.000 o franqueado cai para 17,1%.

**Recomendação: build-to-suit com investidor local.** Em cada praça, um investidor
imobiliário da região compra o terreno e constrói no nosso projeto padrão, em contrato de
10 a 15 anos, **com a locação em nome da franqueadora** e sublocação ao franqueado. A
R$ 5.000/mês ele faz 11,6% nominal com inquilino de prazo longo — acima do yield
comercial típico no interior, e dentro do hurdle de um investidor imobiliário (IPCA + 6 a
7% real). A franqueadora fica com **capital zero no imóvel e o ponto sob contrato**: se o
franqueado sair, entra outro operador em semanas sem perder a praça.

**O prêmio estratégico que a ideia buscava é o controle do ponto, não a propriedade
dele** — e o build-to-suit entrega o controle por R$ 0.

**Se o empreendedor quiser o imóvel de todo jeito:** é decisão legítima, mas é outro
investimento, com outro hurdle. Como uso de capital da franquia a 18% de TMA, destrói
valor. Como investimento imobiliário em **holding patrimonial separada**, com hurdle de
IPCA + 6 a 7% real, a R$ 5.000/mês de aluguel é um bom negócio. Mesmo ativo, dois
vereditos opostos — porque o custo de oportunidade é diferente. O que não se pode é
misturar o resultado das duas PJs: foi essa mistura que produziu o R$ 815 mil que não
fazia sentido para ninguém.

**O que mudaria a decisão.** Selic abaixo de 11% a.a., ou terreno abaixo de R$ 180 mil
em praça com aluguel de R$ 5.000. Nesse ponto comprar passa a competir com asset-light —
e aí já se compra com histórico de aluguel pago, que é o que o banco financia barato.

**Também vale para Piumhi.** Comprar o terreno em vez de alugar a R$ 3.000 rende 17,3%
a.a. em 60 meses: abaixo da TMA e pouco acima da Selic. Alugar é a decisão certa — mas
**36% do capex (R$ 142 mil) é benfeitoria que fica no terreno de terceiro**, então o
contrato tem de ter prazo de 10 anos, **opção de compra com preço travado hoje**,
indenização de benfeitoria e direito de preferência. A opção de compra custa zero assinar
e vale muito se o juro cair.


---

## ADR-012 — Estrutura de capital da Fase 1

**Data:** out/2026. **Status:** recomendado, pendente de negociação com os investidores.

**Objetivo declarado pelo empreendedor:** o menor capital possível em risco, com um ou dois
investidores entrando.

**Duas correções que vieram antes da recomendação.**

A primeira: **o BP não remunerava o operador.** Com pró-labore de R$ 3.500/mês, o cenário base
de capex cheio e 100% capital próprio sai de **37,5% para 25,6% de TIR** e de R$ 235 mil para
**R$ 93 mil de VPL**. O número publicado antes estava otimista por omissão, e o número de
referência para investidor passa a ser o que paga quem trabalha.

A segunda: **o "capital a reservar" é o pico de caixa, não o desembolso inicial.** Com dívida,
o serviço do empréstimo durante a rampa abre uma diferença de R$ 60 a R$ 90 mil entre a
primeira tranche e o pico. Prometer só a primeira tranche é como o projeto morre no mês 6.

**Decisão: reduzir a necessidade de capital antes de dividi-la.** Quatro alavancas, em ordem
de valor:

| Alavanca | Efeito no capital | Efeito na TIR | Efeito no VPL |
|---|---|---|---|
| Capex enxuto (R$ 328 mil) | −R$ 81 mil | +8,3 pp | +R$ 72 mil |
| Dívida de R$ 120 mil a 21% a.a. | −R$ 99 mil | +4,7 pp | **−R$ 8 mil** |
| Pré-venda anual de 80 fundadores | −R$ 24 mil | +0,4 pp | −R$ 1 mil |
| Prazo 30/70 do fornecedor | desloca o pico | — | — |

Resultado: **capital a reservar cai de R$ 480 mil para R$ 276 mil (−42%)** e a TIR do equity
sobe de 25,6% para 39,0%, já pagando o pró-labore.

A dívida **destrói um pouco de valor** (21% contra TMA de 18%) e isso está registrado de
propósito: é uma troca consciente de R$ 8 mil de VPL por R$ 99 mil de capital liberado.

**Cap table recomendado:** dois investidores de R$ 75 mil por 24% cada, Antonio com R$ 126 mil
por **52%**. Retornos de 20,7% para eles e 29,2% para ele, mais pró-labore e 100% da
franqueadora.

**Antonio fica acima de 50%, sempre.** A alternativa de dois investidores a R$ 90 mil por 27,5%
cada rende mais para ele (33,6%), e foi recusada: a 45% ele perde o controle da sociedade que
vai ser a unidade padrão da rede, a vitrine da COF e a referência de todos os indicadores.

**A cláusula que vale mais que a taxa:** a marca fica na **PJ 1, 100% do Antonio**, com o
pedido no INPI em nome dela **antes de os investidores assinarem**, e com contrato de licença
para a PJ 2 declarado na entrada (0% de royalty nos primeiros 24 meses, 6% depois). A
franqueadora vale R$ 1,26 milhão de VPL sozinha; com a marca dentro da PJ 2, vender 48% da
operação é vender 48% da rede por R$ 150 mil.

**Hipótese que foi testada e não se confirmou:** comprar máquina **nacional** credenciada para
destravar o BNDES Finame (Selic + 0,75% + spread, até 100% do equipamento, até 10 anos). O
ponto de indiferença é **máquina nacional a R$ 134.400** — praticamente o custo da chinesa
posta em Piumhi (R$ 132.600 com interface e kit). Acima disso, o Finame não compensa o preço
maior do equipamento. A rota nacional reserva R$ 10 a R$ 16 mil menos de capital, e custa VPL.
Vale as duas ligações (Grupo MF, Covre), não vale como tese.

**Também descartado por ora:** BDMG Pronampe investimento, que tem a melhor condição do mercado
(Selic + 5,50% a.a., 72 meses, 12 de carência) mas exige 30% da receita bruta do ano anterior,
limitado a R$ 250 mil — **PJ nova não acessa. Entra no ano 2.**

**O que mudaria a decisão.** Proposta de cooperativa acima de 24% a.a. ou com menos de 6 meses
de carência derruba a alavancagem. Campanha de fundadores abaixo de 50 adesões derruba a
pré-venda **e a premissa de demanda** — e aí a decisão não é de estrutura de capital, é de
revisar o plano antes de comprar a máquina.

---

## ADR-013 — Vercel em vez de Railway (revoga a ADR-006)

**Data:** out/2026. **Status:** aceito — decisão do empreendedor, out/2026.

A [ADR-006](#adr-006--railway-em-vez-de-vercel) recomendava Railway e descartava a Vercel. O
empreendedor decidiu ir de Vercel. **Esta ADR revoga a 006**; ela fica no documento como
histórico, não como recomendação vigente.

**O que mudou no código.** A aplicação é Express 4 com `pg`, feita para um processo que fica de
pé. Na Vercel ela roda em função serverless, que sobe e desce. Quatro adaptações:

1. **`api/index.js`** embrulha o mesmo `criarApp()` de `server.js`. O app é construído uma vez
   por instância e `db.iniciar()` roda no máximo uma vez, numa promessa única.
2. **`public/` é servido pela CDN**, não pelo Express. Mais rápido para a landing — que é a
   página que converte fundador — mas os cabeçalhos de segurança passam a existir em dois
   lugares. `test/vercel.test.js` compara `vercel.json` com `seguranca.cabecalhos` e falha se
   divergirem.
3. **`admin.html` saiu de `public/` para `views/`.** Em `public/` a CDN o entregaria direto,
   **sem o nonce do CSP** — e arquivo estático vence rewrite na Vercel. Fora de `public/`, o
   `/admin` só existe pela função.
4. **As migrações não rodam no boot** (`config.migrarNoBoot` é falso em serverless). Rodar
   dezenas de DDLs a cada processo novo é desperdício e dá corrida de concorrência.
   `npm run migrar` faz o trabalho, e `npm run migrar -- --imprimir` gera
   [migracoes.sql](migracoes.sql) para colar no SQL Editor do Neon.

**Banco: Neon, com a connection string *pooled*.** A Vercel não hospeda Postgres. Em serverless
cada instância abre conexão, então o pool do `pg` vai a `max: 1` com `allowExitOnIdle`, e a
string tem de ser a do pooler (`-pooler` no endereço). Com a string direta, o Postgres bate o
limite de conexões exatamente quando houver movimento.

**O que piorou, e está registrado porque o empreendedor precisa saber:**

| | Efeito |
|---|---|
| **Rate limit por IP** | É contado em memória de processo. Em serverless há vários processos, então o limite perde força proporcionalmente. No volume de uma cidade de 38 mil habitantes quase sempre há um processo só e ele funciona; sob ataque, não. Correção, se virar problema: contar no Postgres. |
| **Sal do hash de IP** | Sem `IP_SALT` nem `ADMIN_TOKEN`, o sal é aleatório **por processo**, e o mesmo IP gera hashes diferentes. Virou aviso explícito em `config.avisoDeAmbiente()`. |
| **Fallback em memória** | Com `DATABASE_URL` errada, o site fica de pé e aceita cadastro, mas o dado some. O `/health` denuncia e o log avisa; o guia de deploy põe essa conferência como teste nº 1. |
| **Termos de Uso** | O plano Hobby da Vercel é para projeto **não comercial**. Site que vende assinatura é uso comercial. O risco é real e é do empreendedor; a saída é o Pro a US$ 20/mês. Recomendação: entrar no Pro quando a campanha de fundadores for ao ar. |

**O que melhorou:** CDN global para a landing (a página que converte), HTTPS e preview por
branch de graça, deploy em segundos, e **custo inicial de R$ 0** contra US$ 5 a 10/mês do
Railway — o que, numa fase em que cada real conta ([ADR-012](#adr-012--estrutura-de-capital-da-fase-1)),
não é irrelevante.

**A saída de emergência continua montada.** O `Dockerfile` da [ADR-005](#adr-005--deploy-por-docker-no-railway)
fica no repositório e o mesmo código roda em qualquer host com Docker, sem alteração. Se a
Vercel incomodar — por Termos de Uso, por rate limit ou por qualquer outra razão — a volta
custa um deploy.

**O que mudaria a decisão.** Aviso da Vercel sobre uso comercial no plano Hobby (aí sobe para
Pro, não sai da plataforma). Ou necessidade de processo de longa duração — fila, worker, cron
pesado — que a função serverless não serve; nada no roadmap de 12 meses pede isso.
