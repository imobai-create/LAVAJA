# Como colocar o site no ar (passo a passo)

Guia escrito para quem **não é de TI**. Dá para fazer tudo em uma tarde. Onde aparecer
`[algo a preencher]`, é informação que só você tem.

> **Caminho:** código no **GitHub** → site na **Vercel** (grátis no começo) → banco de dados no
> **Neon** (grátis no começo) → domínio no **registro.br** (R$ 40/ano).
>
> Custo realista para começar: **R$ 40 por ano**, só o domínio. Quando o movimento crescer,
> Vercel Pro custa US$ 20/mês e o Neon pago começa em US$ 19/mês — mas isso é problema de
> quando houver movimento.

Decisão e trade-offs em [DECISOES.md](DECISOES.md), ADR-013.

---

## Antes de começar, tenha em mãos

- Uma conta no **GitHub** com este repositório.
- CPF ou CNPJ, para registrar o domínio no registro.br.
- O número de WhatsApp que vai atender os clientes, já funcionando.
- Um cartão de crédito — **não é cobrado agora**, mas a Vercel pede para liberar o domínio
  próprio em alguns casos. O registro.br cobra em real, no boleto ou PIX.

---

## Parte 1 — Banco de dados no Neon (10 minutos, faça primeiro)

O banco guarda os cadastros dos fundadores. **Faça antes do site**, porque o site precisa do
endereço do banco.

1. Entre em **neon.com** e crie a conta com o GitHub.
2. Crie um projeto: nome `fastcarwash`, região **AWS sa-east-1 (São Paulo)**.
   A região importa: banco em São Paulo responde em milissegundos para quem está em Piumhi.
3. Terminada a criação, o Neon mostra a **connection string**. Copie a versão
   **"Pooled connection"** — o endereço dela tem `-pooler` no meio, assim:

   ```
   postgresql://usuario:senha@ep-algo-123456-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require
   ```

   > **Isto é obrigatório, não é detalhe.** A Vercel roda o site em funções que sobem e descem
   > a toda hora, e cada uma abre conexão com o banco. Sem a versão *pooled*, o Postgres atinge
   > o limite de conexões e o formulário começa a dar erro justamente quando houver movimento.
   > Se a string que você copiou **não** tem `-pooler`, volte e pegue a outra.

4. Guarde essa string. Ela é senha: não mande por WhatsApp nem cole em grupo.

---

## Parte 2 — Subir o site na Vercel (15 minutos)

1. Entre em **vercel.com** e crie a conta com o GitHub.
2. **Add New… → Project** e escolha o repositório `LAVAJA`.
3. Na tela de configuração, **não mude nada** em Framework Preset (fica "Other"), Build Command
   (vazio) nem Output Directory. O arquivo `vercel.json` do repositório já diz tudo.
4. Abra **Environment Variables** e cadastre, uma por uma, marcando os três ambientes
   (Production, Preview, Development):

   | Nome | Valor |
   |---|---|
   | `DATABASE_URL` | a connection string *pooled* do Neon (Parte 1) |
   | `ADMIN_TOKEN` | `[invente uma senha longa, 30+ caracteres aleatórios]` |
   | `WHATSAPP_NUMERO` | `5531987474828` |
   | `FOUNDERS_LIMIT` | `80` |

   **`ADMIN_TOKEN` é o que protege o painel e a exportação dos cadastros.** Sem ele, o painel
   responde 503 — de propósito, para nunca ficar aberto por descuido. Guarde num gerenciador de
   senhas, não num papel.

5. Clique em **Deploy** e espere. Ao fim, a Vercel dá um endereço tipo
   `lavaja-abc123.vercel.app`.

---

## Parte 3 — Criar as tabelas do banco (5 minutos, só uma vez)

O site já está no ar, mas o banco está vazio — sem tabelas, o formulário dá erro. Rode as
migrações uma vez:

**Pelo seu computador** (precisa do Node 22 instalado):

```bash
git clone https://github.com/imobai-create/LAVAJA.git
cd LAVAJA
npm ci
DATABASE_URL='cole-aqui-a-string-do-neon' npm run migrar
```

Deve terminar com `[migrar] pronto.`

**Pelo painel do Neon**, se preferir não instalar nada: abra o **SQL Editor** do projeto e cole
o conteúdo do arquivo `docs/migracoes.sql` (gere com `npm run migrar -- --imprimir` ou peça para
mim). É o mesmo resultado.

> **Por que isso não é automático.** Em servidor comum as tabelas são criadas quando o site
> sobe. Na Vercel o site sobe muitas vezes por dia, e rodar dezenas de comandos de banco a cada
> vez é desperdício e dá corrida de concorrência. Então só roda quando você manda. **Repita este
> passo quando um deploy mexer no banco** — eu aviso quando for o caso.

---

## Parte 4 — Conferir se ficou tudo certo (5 minutos)

Abra o endereço `.vercel.app` e faça os seis testes. **Faça todos** — é mais rápido que
descobrir um problema depois de divulgar o site.

| # | O que fazer | O que tem que acontecer |
|---|---|---|
| 1 | Abrir `/health` | JSON com `"banco":"postgres"`. Se vier `"memoria"`, a `DATABASE_URL` está errada e **os cadastros não estão sendo salvos** |
| 2 | Abrir a página inicial | Carrega com as fontes e o CSS certos |
| 3 | Abrir `/privacidade` e `/franquia` | Abrem sem o `.html` no fim |
| 4 | Preencher o formulário com um número de teste | Mensagem de sucesso, e o contador de vagas baixa |
| 5 | Abrir `/admin` | Pede o token; com o token, mostra o cadastro de teste |
| 6 | Abrir o site e apertar **F12 → Console** | **Nenhum erro em vermelho.** Se aparecer algo com "Content Security Policy", me avise com o texto do erro |

O teste 6 existe porque a Vercel entrega as páginas pela CDN, sem passar pelo código do site —
os cabeçalhos de segurança vêm do `vercel.json`. Há um teste automatizado que impede os dois
de divergirem (`test/vercel.test.js`), mas o console do navegador é a confirmação final.

---

## Parte 5 — Registrar e ligar o domínio (30 minutos + espera)

1. Em **registro.br**, pesquise `fastcarwash.com.br`. (Você já registrou — confirme que está
   ativo e no seu CPF/CNPJ.)
2. Na Vercel: **Project → Settings → Domains → Add**, digite `fastcarwash.com.br` e também
   `www.fastcarwash.com.br`.
3. A Vercel mostra os registros de DNS. No painel do registro.br, em **DNS → Editar zona**,
   cadastre o que ela pediu:
   - `fastcarwash.com.br` → registro **A** apontando para o IP que a Vercel informar
   - `www` → registro **CNAME** apontando para `cname.vercel-dns.com`
4. Salve e espere. Costuma levar de 15 minutos a algumas horas (pode chegar a 24h).
5. Quando a Vercel marcar o domínio como **Valid**, o HTTPS é criado automaticamente, de graça.
6. Repita os seis testes da Parte 4, agora em `https://fastcarwash.com.br`.

---

## Quanto custa por mês, de verdade

| Item | Começo | Quando crescer |
|---|---|---|
| Vercel (site) | **R$ 0** — plano Hobby | US$ 20/mês (Pro) |
| Neon (banco) | **R$ 0** — 0,5 GB | US$ 19/mês |
| Domínio | R$ 40/ano | R$ 40/ano |
| **Total** | **~R$ 3,30/mês** | **~R$ 210/mês** |

> **Uma ressalva importante sobre o plano grátis da Vercel.** Os Termos de Uso dizem que o plano
> **Hobby é para projetos não comerciais**. Um site que vende assinatura é uso comercial. Na
> prática a Vercel raramente derruba site pequeno por isso, mas **o risco existe e é seu**: se
> vier aviso, o caminho é migrar para o Pro (US$ 20/mês) na hora. Para um negócio que vai pedir
> R$ 276 mil de investimento, US$ 20/mês não é o problema — considere já começar no Pro quando
> a campanha de fundadores for ao ar.

---

## O que a Vercel faz pior que um servidor comum

Transparência, porque estas três coisas pioraram na mudança e você precisa saber:

1. **O limite de tentativas por IP (rate limit) perde força.** Ele é contado na memória do
   processo, e na Vercel existem vários processos ao mesmo tempo. Com o movimento de uma cidade
   de 38 mil habitantes, quase sempre haverá só um processo ativo e o limite funciona; sob
   ataque, não. Se virar problema, a correção é contar no banco — algumas horas de trabalho.
2. **As tabelas não são criadas sozinhas** (Parte 3).
3. **Se a `DATABASE_URL` estiver errada, o site continua de pé e aceita cadastro**, mas guarda
   na memória do processo — e **o dado some**. O `/health` denuncia (`"banco":"memoria"`) e o
   log do deploy mostra o aviso em letras grandes. **Por isso o teste 1 da Parte 4 é o mais
   importante de todos.**

O Docker (`Dockerfile`) continua no repositório. Se um dia a Vercel não servir, o mesmo código
roda em qualquer host com Docker sem mudança nenhuma — é a saída de emergência.

---

## Erros comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| `/health` diz `"banco":"memoria"` | `DATABASE_URL` ausente ou errada | Confira a variável na Vercel; **tem que ser a string com `-pooler`** |
| Formulário dá erro 500 | Tabelas não criadas | Rode a Parte 3 |
| "too many connections" no log | String sem `-pooler` | Troque pela *pooled* e faça um novo deploy |
| `/admin` responde 503 | `ADMIN_TOKEN` não cadastrado | Cadastre na Vercel e faça um novo deploy |
| `/privacidade` dá 404 | `vercel.json` não subiu | Confirme que o arquivo está no repositório |
| Domínio não valida | DNS ainda propagando | Espere até 24h; depois disso, confira os registros |
| Página sem CSS | Deploy incompleto | Veja o log do deploy na Vercel |

---

## Documentos relacionados

- [DECISOES.md](DECISOES.md) — ADR-013 (por que Vercel), ADR-005 (Docker), ADR-006 (histórico)
- [CHECKLIST-PRE-VENDA.md](CHECKLIST-PRE-VENDA.md) — o que conferir antes de divulgar
- [BP-PIUMHI.md](BP-PIUMHI.md) — a campanha de fundadores que este site existe para servir
