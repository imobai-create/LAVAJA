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
