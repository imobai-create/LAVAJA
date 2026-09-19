# Como colocar o site no ar (passo a passo)

Guia escrito para quem **não é de TI**. Leia até o fim antes de começar: dá para fazer tudo em
uma tarde. Onde aparecer `[algo a preencher]`, é informação que só você tem.

> Resumo do caminho recomendado: código no **GitHub** → hospedagem no **Railway** (site + banco de
> dados) → domínio no **registro.br**. Custo realista: **US$ 5 a US$ 10 por mês** de hospedagem
> (cobrado no cartão em dólar) + **R$ 40 por ano** de domínio.

---

## Antes de começar, tenha em mãos

- Um cartão de crédito internacional (o Railway cobra em dólar; entra IOF na fatura).
- CPF ou CNPJ, para registrar o domínio no registro.br.
- Uma conta no GitHub com este repositório já enviado.
- O número de WhatsApp que vai atender os clientes, já funcionando.

---

## Parte 1 — Subir o site no Railway

### 1. Criar a conta

1. Acesse <https://railway.com> e clique em **Login** → **Login with GitHub**.
2. Autorize o Railway a ver seus repositórios.
3. Vá em **Account → Plans** e assine o plano **Hobby (US$ 5/mês)**. O plano de teste (Trial)
   não serve para um site que precisa ficar no ar 24h — ele pausa sozinho.

### 2. Criar o projeto a partir do repositório

1. Clique em **New Project → Deploy from GitHub repo**.
2. Escolha o repositório do site (ex.: `lavaja-site`) e confirme.
3. O Railway lê o `Dockerfile` deste repositório e monta o site sozinho. O primeiro build leva
   de 1 a 3 minutos. Enquanto isso, a aba **Deployments** mostra o andamento.

> Se o build falhar dizendo algo sobre `package-lock.json`, é porque esse arquivo não foi enviado
> ao GitHub. Ele **precisa** estar versionado — veja a seção "Erros comuns".

### 3. Adicionar o banco de dados Postgres

1. Dentro do mesmo projeto, clique em **New → Database → Add PostgreSQL**.
2. Espere o serviço ficar verde. Pronto, o banco existe — falta ligar o site nele.

### 4. Ligar o site ao banco e configurar as variáveis

No projeto, clique no serviço **do site** (não no do banco) → aba **Variables** → **New Variable**.
Crie estas quatro:

| Nome | Valor | Para que serve |
|---|---|---|
| `DATABASE_URL` | `${{Postgres.DATABASE_URL}}` | Endereço do banco. Digitando `${{` o Railway sugere sozinho — escolha o Postgres na lista, não copie a senha na mão. |
| `ADMIN_TOKEN` | um segredo longo (veja abaixo) | Senha que protege a lista de reservas. Sem isso, a lista fica inacessível — o que é o comportamento seguro. |
| `FOUNDERS_LIMIT` | `80` | Quantas vagas de fundador existem. Muda o contador do site. |
| `WHATSAPP_NUMERO` | `55[DDD][número]` só com dígitos, ex.: `5531987474828` | Número que recebe as mensagens dos botões de WhatsApp. Já vem com o provisório (31) 98747-4828; defina a variável quando trocar para o número do negócio. |

**Não crie a variável `PORT`.** O Railway injeta essa sozinho e o site já respeita.

**Como gerar o `ADMIN_TOKEN`:** no terminal do seu computador (no Mac/Linux, o app Terminal;
no Windows, o PowerShell), rode um destes:

```bash
openssl rand -base64 32
```

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

Copie o resultado, cole no Railway e **guarde em um gerenciador de senhas**. Não mande por
WhatsApp, não coloque em planilha, não coloque dentro do código.

Depois de salvar as variáveis, o Railway reinicia o site sozinho.

### 5. Gerar o endereço público

1. No serviço do site: **Settings → Networking → Public Networking → Generate Domain**.
2. O Railway devolve um endereço tipo `lavaja-site-production.up.railway.app`. Abra no celular.
3. Teste: `SEU-ENDERECO/health` deve responder `{"ok":true}`. Se responder isso, o servidor está
   vivo. Se o site abrir mas o formulário der erro, o problema é o banco (volte ao passo 4).

Guarde esse endereço: ele continua funcionando mesmo depois que o domínio próprio entrar no ar.

---

## Parte 2 — Registrar o domínio `lavaja.com.br`

### 1. Registrar

1. Acesse <https://registro.br>, pesquise `lavaja.com.br` e veja se está livre.
2. Crie a conta com CPF ou CNPJ (recomendo CNPJ quando a empresa existir — o domínio é um ativo
   da empresa, não seu).
3. Pague. Um `.com.br` custa **cerca de R$ 40 por ano**, pago de uma vez, por ano (há desconto
   contratando 3 ou 5 anos de uma vez). Ative a renovação automática ou anote a data: domínio
   vencido sai do ar e pode ser pego por outra pessoa.

### 2. Apontar o domínio para o site

No Railway: serviço do site → **Settings → Networking → Custom Domain** → digite
`www.lavaja.com.br`. O Railway mostra um valor de **CNAME** (algo como `xyz.up.railway.app`).

No registro.br: **Painel → seu domínio → DNS → Editar Zona**, e crie:

| Tipo | Nome | Valor |
|---|---|---|
| CNAME | `www` | o valor que o Railway mostrou |

Aguarde de 15 minutos a algumas horas (propagação de DNS). Quando `www.lavaja.com.br` abrir o
site com cadeado (HTTPS, gerado automaticamente pelo Railway), está pronto.

**Sobre o domínio "sem www"** (`lavaja.com.br`, chamado de raiz ou apex): o padrão de DNS não
permite CNAME na raiz, e o registro.br não tem "ALIAS". Duas saídas honestas:

- **Mais simples:** divulgue só `www.lavaja.com.br`. Funciona, mas quem digitar sem o `www` não
  chega ao site.
- **Recomendada:** crie uma conta grátis na **Cloudflare**, adicione o domínio lá, troque os
  servidores DNS no registro.br pelos da Cloudflare e configure na Cloudflare um CNAME da raiz
  apontando para o endereço do Railway (a Cloudflare resolve isso com "CNAME flattening") mais um
  redirecionamento de `lavaja.com.br` para `www.lavaja.com.br`. Continua custando R$ 0.

### 3. Atualizar o site depois que o domínio existir

Troque o domínio em `public/sitemap.xml` e em `public/robots.txt` (os dois estão com
`https://lavaja.com.br` como padrão e têm aviso no topo). Depois, cadastre o site no
**Google Search Console** (<https://search.google.com/search-console>) e envie o sitemap:
`https://lavaja.com.br/sitemap.xml`.

---

## Quanto custa por mês, de verdade

| Item | Custo | Observação |
|---|---|---|
| Railway Hobby | **US$ 5/mês** | Já inclui US$ 5 de uso. Site pequeno + Postgres pequeno normalmente cabem nesse valor. |
| Uso acima do incluso | US$ 0 a ~US$ 5/mês | Só se o tráfego crescer muito. Dá para pôr limite de gasto em **Settings → Usage Limits**. |
| Domínio `.com.br` | **~R$ 40/ano** | Pagamento anual no registro.br. |
| **Total esperado** | **~R$ 30 a R$ 60/mês + R$ 40/ano** | Depende do dólar e do IOF do cartão. |

Configure o **Usage Limit** no Railway logo no primeiro dia. É o que impede uma surpresa na
fatura se algo sair do controle.

---

## Alternativas mais baratas (e o que você perde em cada uma)

### Render (plano gratuito)

- **Ganha:** custo zero, mesmo jeito de publicar (conecta no GitHub).
- **Perde:** o site **dorme** depois de ~15 minutos sem visita. A primeira pessoa que entrar
  depois disso espera de 30 a 60 segundos numa tela branca — em campanha paga, isso derruba
  conversão. O Postgres gratuito do Render também **expira** (hoje, 30 dias) e depois precisa ser
  recriado, perdendo os dados se não houver backup.
- **Quando usar:** só para testar antes de divulgar, nunca durante a campanha dos 80 fundadores.

### Vercel / Netlify / GitHub Pages (grátis)

- **Ganha:** hospedagem de graça, rápida, sem manutenção.
- **Perde:** essas plataformas servem arquivos estáticos. O formulário de reserva, o contador de
  vagas e a lista de leads **param de funcionar** do jeito que estão — teria que reescrever o
  servidor como funções serverless e contratar um banco separado (ex.: Neon, que tem plano grátis
  limitado). Dá trabalho de programação e não economiza tanto assim.
- **Quando usar:** se você decidir que a reserva vai ser feita só por WhatsApp, sem formulário.
  Aí o site vira um cartão de visita estático e a hospedagem é realmente de graça.

### Um servidor VPS (Hetzner, DigitalOcean, Contabo)

- **Ganha:** ~US$ 5/mês com muito mais capacidade.
- **Perde:** você vira o administrador do servidor — atualização de segurança, backup, certificado
  HTTPS, reinício quando cair. **Não recomendo** sem alguém de TI por perto.

**Veredito:** para uma campanha que vai receber tráfego pago e precisa estar no ar quando o
cliente clicar no anúncio, o Railway com plano Hobby é a escolha certa. Economizar US$ 5/mês
dormindo o site custa mais em leads perdidos do que economiza.

---

## Depois que estiver no ar

**Baixar as reservas (leads):**

```bash
curl -H "x-admin-token: SEU_TOKEN" "https://www.lavaja.com.br/api/leads?formato=csv" -o leads.csv
```

O arquivo abre no Excel. Não deixe essa planilha circulando em grupo de WhatsApp: são dados
pessoais, e a Política de Privacidade do site promete o contrário.

**Backup do banco:** no Railway, serviço Postgres → aba **Data** permite exportar. Faça isso ao
menos uma vez por semana durante a campanha. O Railway tem backup próprio, mas backup que você
nunca testou não é backup.

**Publicar uma alteração:** qualquer mudança enviada ao GitHub (branch principal) é publicada
automaticamente pelo Railway em 1 a 3 minutos. Se algo quebrar, em **Deployments** dá para clicar
em uma versão antiga e fazer **Rollback**.

---

## Erros comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Build falha citando `npm ci` ou `package-lock.json` | O `package-lock.json` não foi enviado ao GitHub | Confirme que o arquivo está no repositório (ele **não** pode estar no `.gitignore`). |
| Site abre, mas o formulário dá erro ao enviar | `DATABASE_URL` ausente ou errada | Refaça o passo 4 usando a referência `${{Postgres.DATABASE_URL}}`, não a senha copiada. |
| As reservas somem quando o site reinicia | Está rodando sem banco (modo memória) | Mesma causa acima: o site avisa isso no log (aba **Logs**). |
| `/api/leads` responde "Não autorizado" | `ADMIN_TOKEN` não configurado ou token errado no comando | Confira a variável no Railway e o cabeçalho `x-admin-token`. |
| Healthcheck falha no deploy | O site não subiu | Abra **Logs** e leia a última linha em vermelho. |
| Domínio não abre depois de horas | CNAME errado ou ainda propagando | Confira o valor no registro.br; teste em <https://dnschecker.org>. |

---

## Documentos relacionados

- [Decisões técnicas](DECISOES.md) — por que a stack é essa.
- [Roadmap de 12 meses do produto digital](ROADMAP-12-MESES.md).
- [Checklist de pré-venda](CHECKLIST-PRE-VENDA.md) — o que decidir **antes** de divulgar o site.
