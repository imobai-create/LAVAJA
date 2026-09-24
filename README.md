# JatoJá — site e landing de pré-venda

Site da **JatoJá**, lava jato automatizado *touchless* por assinatura, unidade modelo em
**Piumhi/MG**. O site capta as reservas da campanha de fundadores, apresenta os planos e guarda os
leads em banco próprio.

> **Aviso importante:** este site é dirigido ao **cliente final** (assinatura de lavagem). Ele
> **não é, e não pode parecer, oferta de franquia**. Pela Lei nº 13.966/2019, oferta de franquia
> exige Circular de Oferta de Franquia (COF) entregue ao candidato no mínimo 10 dias antes de
> qualquer assinatura ou pagamento. Enquanto a COF não existir, nenhuma página pode falar em
> investimento, taxa de franquia, retorno ou "seja um franqueado". Ver
> [docs/ROADMAP-12-MESES.md](docs/ROADMAP-12-MESES.md).

---

## Stack

| Camada | Escolha |
|---|---|
| Runtime | Node.js 22 (`.nvmrc`) |
| Servidor | Express 4 |
| Banco | PostgreSQL (via `DATABASE_URL`); sem ela, roda em memória para teste local |
| Front | HTML + CSS + JS estáticos em `public/`, sem build |
| Deploy | Docker (`Dockerfile`) no Railway (`railway.json`) |
| CI | GitHub Actions: `npm ci`, `npm test` e sanidade dos HTML |

Dependências de produção: só `express` e `pg`. O porquê de cada escolha está em
[docs/DECISOES.md](docs/DECISOES.md).

---

## Rodar na sua máquina

```bash
# Node 22 (se usa nvm: nvm use)
npm install
npm start
# abre http://localhost:3000
```

Sem `DATABASE_URL` o servidor usa armazenamento em memória: serve para ver o site funcionando,
mas **os dados somem ao reiniciar**. Para testar com banco de verdade, exporte a variável
apontando para um Postgres local ou para o banco do Railway.

Rodar os testes:

```bash
npm test
```

Verificar a sanidade dos HTML (é o mesmo check que roda no CI):

```bash
node .github/scripts/checar-html.mjs
```

Subir pelo Docker, igualzinho a produção:

```bash
docker build -t jatoja .
docker run --rm -p 3000:3000 -e ADMIN_TOKEN=teste jatoja
```

---

## Estrutura de pastas

```
.
├── server.js                    # bootstrap do Express (middlewares, estáticos, listen)
├── src/                         # regras de negócio
│   ├── config.js                # tudo que vem de variável de ambiente passa por aqui
│   ├── db.js                    # Postgres (ou memória, no local)
│   ├── leads.js                 # gravação e consulta das reservas
│   ├── rotas.js                 # rotas HTTP (/api/..., /health, painel)
│   ├── seguranca.js             # cabeçalhos, rate limit, token do admin
│   ├── validacao.js             # validação de nome, WhatsApp, plano, consentimento
│   └── csv.js                   # exportação das reservas
├── test/                        # testes automatizados (node:test)
├── public/                      # tudo que vai para o navegador
│   ├── index.html               # landing de pré-venda (Piumhi)
│   ├── franquia.html            # página institucional de expansão (sem oferta)
│   ├── privacidade.html         # Política de Privacidade (LGPD)
│   ├── admin.html               # painel de leads (noindex, protegido por token)
│   ├── robots.txt               # libera tudo menos /admin e /api
│   ├── sitemap.xml              # domínio precisa ser conferido antes de publicar
│   ├── manifest.webmanifest     # PWA: nome, cores e ícones
│   └── assets/                  # css, js e imagens
├── docs/                        # documentação do projeto (ver abaixo)
├── .github/
│   ├── workflows/ci.yml         # CI do GitHub Actions
│   └── scripts/checar-html.mjs  # verificador de sanidade dos HTML
├── Dockerfile / .dockerignore   # imagem de produção
├── railway.json                 # configuração de deploy (healthcheck, restart)
└── .nvmrc                       # Node 22
```

---

## Variáveis de ambiente

Configuradas no Railway em **Variables** (ver [docs/DEPLOY.md](docs/DEPLOY.md)). Nunca coloque
segredo dentro do código nem no Git — `.env` está no `.gitignore`.

| Variável | Obrigatória | Padrão | Para que serve |
|---|---|---|---|
| `PORT` | não | `3000` | Injetada pelo Railway. **Não crie essa variável à mão.** |
| `DATABASE_URL` | sim, em produção | — | Postgres. No Railway, use a referência `${{Postgres.DATABASE_URL}}`. |
| `ADMIN_TOKEN` | sim, em produção | vazio | Protege o painel e a exportação de leads. Vazio = rotas de admin não liberam nada. |
| `FOUNDERS_LIMIT` | não | `80` | Número de vagas de fundador (alimenta o contador). |
| `WHATSAPP_NUMERO` | não | `5531987474828` | Número que recebe as mensagens, só dígitos, com DDI. Hoje aponta para o atendimento provisório (31) 98747-4828. |
| `PGSSL` | não | — | `disable` desliga SSL do Postgres (só para banco local). |
| `RATE_LIMIT_POST` | não | `10` | Envios de formulário por IP por minuto. |
| `RATE_LIMIT_GLOBAL` | não | `600` | Teto global de envios por janela. |
| `RATE_LIMIT_JANELA_MS` | não | `60000` | Tamanho da janela do rate limit, em ms. |
| `CACHE_STATS_MS` | não | `15000` | Cache do contador de vagas, em ms. |
| `CSP_SCRIPT_INLINE` | não | — | `1` afrouxa a CSP para permitir script inline (transição; evite em produção). |

Gerar um `ADMIN_TOKEN`:

```bash
openssl rand -base64 32
```

---

## Painel e exportação dos leads

O painel fica em `/admin` (ou `/admin.html`) e pede o token. Pela linha de comando:

```bash
# reservas da landing (clientes)
curl -H "x-admin-token: SEU_TOKEN" "https://SEU-DOMINIO/api/leads?formato=csv" -o leads.csv

# contatos vindos da página de expansão
curl -H "x-admin-token: SEU_TOKEN" "https://SEU-DOMINIO/api/franquia-leads?formato=csv" -o franquia.csv

# resumo consolidado
curl -H "x-admin-token: SEU_TOKEN" "https://SEU-DOMINIO/api/admin/resumo"
```

São dados pessoais sob a LGPD: a planilha não circula em grupo de WhatsApp nem fica solta no
Drive. Pedido de exclusão precisa ser atendido em até 15 dias — é o que a Política de Privacidade
promete ao visitante.

---

## Documentação

| Documento | Para quê |
|---|---|
| [docs/DEPLOY.md](docs/DEPLOY.md) | Passo a passo para colocar o site no ar (Railway, Postgres, domínio), custos reais e alternativas mais baratas |
| [docs/ROADMAP-12-MESES.md](docs/ROADMAP-12-MESES.md) | O que construir em software, mês a mês, amarrado aos gates do Plano de Franquia |
| [docs/CHECKLIST-PRE-VENDA.md](docs/CHECKLIST-PRE-VENDA.md) | O que precisa estar decidido **antes** de divulgar, e o que medir depois |
| [docs/DECISOES.md](docs/DECISOES.md) | Registro das decisões técnicas e o que faria cada uma mudar |
| [docs/EQUIPAMENTO.md](docs/EQUIPAMENTO.md) | Análise da cotação da máquina, lacunas e perguntas pendentes ao fabricante |
| `docs/plano-franquia-extraido.txt` | Texto integral do Plano de Franquia (set/2026) — referência, não editar |

---

## PENDÊNCIAS DO DONO

Coisas que **só você pode preencher ou decidir**. Enquanto estiverem em aberto, o site não deve
ser divulgado.

### Dados da empresa (hoje estão como marcadores no site)
- [ ] **Razão social** — marcador `[razão social a preencher]` em `public/privacidade.html`.
- [ ] **CNPJ** — marcador `[CNPJ a preencher]` em `public/privacidade.html`.
- [ ] **Endereço completo** — marcador `[endereço a preencher]` em `public/privacidade.html`.
- [ ] **E-mail de contato para privacidade/LGPD** — marcador `[e-mail de contato a preencher]`,
      aparece **3 vezes** em `public/privacidade.html` (seções 1, 8 e rodapé).
- [ ] Confirmar o **prazo de guarda dos dados** declarado na política (hoje: 24 meses) — se mudar
      o prazo, mude o texto.

### Site e domínio
- [ ] **Número de WhatsApp real** do atendimento → variável `WHATSAPP_NUMERO` (hoje há um número
      provisório no código: `5531987474828` — (31) 98747-4828).
- [ ] **Domínio definitivo**. Os arquivos `public/sitemap.xml` e `public/robots.txt` estão com
      `https://jatoja.com.br` e têm aviso no topo: se o domínio for outro, troque nos dois.
- [ ] **Preços finais** de cada plano e da lavagem avulsa, e por quanto tempo o preço de fundador
      fica travado.
- [ ] **`ADMIN_TOKEN`** gerado e guardado em gerenciador de senhas (não em WhatsApp, não em planilha).
- [ ] Ícones `public/assets/img/icon-192.png` e `icon-512.png` — referenciados pelo
      `manifest.webmanifest`; confirmar que existem antes de publicar.

### Decisões de campanha (detalhe em [docs/CHECKLIST-PRE-VENDA.md](docs/CHECKLIST-PRE-VENDA.md))
- [ ] Quem responde o WhatsApp e em quanto tempo.
- [ ] O que exatamente o fundador ganha, em uma frase.
- [ ] Como a cobrança será feita na inauguração (meio de pagamento contratado e testado).
- [ ] O que é comunicado se a obra atrasar.
- [ ] Se haverá sinal simbólico na reserva (muda bastante a taxa de conversão).

### Para depois, mas não muito depois
- [ ] Pedido de registro da marca **JatoJá no INPI, classes 35 e 37**.
- [ ] Registrar o domínio no CNPJ da empresa, não no CPF de uma pessoa.
- [ ] Cadastrar o site no Google Search Console e enviar o sitemap.
