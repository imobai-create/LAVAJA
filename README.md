# LavaJá — Landing de pré-venda (Fundadores)

Site de captação da campanha Fundadores da unidade de Piumhi/MG: 80 vagas do plano Ilimitada a R$ 79/mês (preço travado), reserva grátis, pagamento só na inauguração.

**Stack:** Node 18+ · Express · Postgres (Railway). Frontend estático em `public/`.

## O que tem pronto

- Landing completa mobile-first (`public/index.html`): planos, posicionamento honesto, FAQ e formulário de reserva com consentimento LGPD.
- `POST /api/leads` — grava a reserva (nome, WhatsApp normalizado com DDI 55, plano, consentimento). WhatsApp é único: bloqueia reserva duplicada. Rate limit de 10 envios/minuto por IP.
- `GET /api/stats` — vagas restantes (limite `FOUNDERS_LIMIT`, padrão 80). Alimenta o contador do hero.
- `GET /api/leads` — lista de leads (JSON) ou `?formato=csv` para baixar. Protegido pelo header `x-admin-token`.
- `GET /health` — healthcheck para o Railway.
- Sem `DATABASE_URL`, o servidor roda com armazenamento em memória (só para teste local — os dados somem ao reiniciar).

## Rodar local

```bash
npm install
npm start
# abre http://localhost:3000
```

## Deploy no Railway (passo a passo)

1. Suba este diretório para um repositório no GitHub (ex.: `lavaja-site`).
2. No Railway: **New Project → Deploy from GitHub repo** → selecione o repositório. O build detecta Node e usa `npm start` automaticamente.
3. No mesmo projeto: **New → Database → PostgreSQL**. No serviço do site, em **Variables**, adicione a referência `DATABASE_URL` do Postgres (Railway sugere com um clique: `${{Postgres.DATABASE_URL}}`).
4. Ainda em **Variables**, defina:
   - `ADMIN_TOKEN` — um segredo longo seu (é o que protege a lista de leads).
   - `FOUNDERS_LIMIT` — opcional, padrão 80.
5. Em **Settings → Networking**, gere o domínio público. Depois aponte um domínio próprio (ex.: `lavaja.com.br`) por CNAME quando registrar.

## Baixar os leads

```bash
curl -H "x-admin-token: SEU_TOKEN" https://SEU-DOMINIO/api/leads?formato=csv -o leads.csv
```

## Ajustes rápidos

- Preços, textos e FAQ: tudo em `public/index.html`.
- Limite de vagas: variável `FOUNDERS_LIMIT`.
- Quando a campanha da segunda praça começar, duplique a landing trocando cidade e origem (`origem` na tabela `leads` já existe para isso).

## LGPD

O formulário só grava com consentimento marcado, o texto informa a finalidade (contato sobre reserva e inauguração) e o pedido de exclusão deve ser atendido apagando a linha do lead (`DELETE FROM leads WHERE whatsapp = '...'`). Não coloque esses dados em planilhas soltas.
