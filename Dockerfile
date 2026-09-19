# LavaJá — imagem de produção (Railway ou qualquer host com Docker)
# Multi-stage: o primeiro estágio instala as dependências, o segundo só roda a aplicação.

# ---------- 1) dependências ----------
FROM node:22-alpine AS deps
WORKDIR /app

# package-lock.json é obrigatório: `npm ci` só funciona com o lock versionado.
COPY package.json package-lock.json ./
RUN npm ci --omit=dev && npm cache clean --force

# ---------- 2) runtime ----------
FROM node:22-alpine AS runtime
WORKDIR /app

ENV NODE_ENV=production \
    PORT=3000

# node:22-alpine já traz o usuário não-root `node` (uid 1000) — não criamos outro.
COPY --from=deps --chown=node:node /app/node_modules ./node_modules

# O que entra aqui é filtrado pelo .dockerignore (fora: .git, docs, testes, CI, node_modules local).
COPY --chown=node:node . .

USER node

EXPOSE 3000

# O host (Railway) injeta PORT; o healthcheck respeita essa variável.
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
  CMD node -e "fetch('http://127.0.0.1:'+(process.env.PORT||3000)+'/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

CMD ["npm", "start"]
