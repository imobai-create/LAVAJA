-- FastCarWash — migrações do banco.
-- Gerado por `npm run migrar -- --imprimir`. Não edite à mão:
-- a fonte é MIGRACOES em src/db.js.
-- Idempotente: pode rodar quantas vezes quiser.

CREATE TABLE IF NOT EXISTS leads (
     id SERIAL PRIMARY KEY,
     nome TEXT NOT NULL,
     whatsapp TEXT NOT NULL UNIQUE,
     plano TEXT NOT NULL,
     consentimento BOOLEAN NOT NULL DEFAULT FALSE,
     criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
   );

ALTER TABLE leads ADD COLUMN IF NOT EXISTS origem TEXT DEFAULT 'piumhi';

ALTER TABLE leads ALTER COLUMN origem SET DEFAULT 'piumhi';

ALTER TABLE leads ADD COLUMN IF NOT EXISTS cidade TEXT DEFAULT 'Piumhi';

ALTER TABLE leads ADD COLUMN IF NOT EXISTS utm_source TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS utm_medium TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS utm_campaign TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS referrer TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS user_agent TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS ip_hash TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'novo';

UPDATE leads SET status = 'novo' WHERE status IS NULL;

CREATE UNIQUE INDEX IF NOT EXISTS leads_whatsapp_uidx ON leads (whatsapp);

CREATE INDEX IF NOT EXISTS leads_criado_em_idx ON leads (criado_em);

CREATE TABLE IF NOT EXISTS franquia_leads (
     id SERIAL PRIMARY KEY,
     nome TEXT NOT NULL,
     whatsapp TEXT NOT NULL UNIQUE,
     email TEXT,
     cidade_interesse TEXT,
     capital_disponivel TEXT,
     mensagem TEXT,
     consentimento BOOLEAN NOT NULL DEFAULT FALSE,
     criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
   );

ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS utm_source TEXT;

ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS utm_medium TEXT;

ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS utm_campaign TEXT;

ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS user_agent TEXT;

ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS ip_hash TEXT;

ALTER TABLE franquia_leads ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'novo';

CREATE UNIQUE INDEX IF NOT EXISTS franquia_leads_whatsapp_uidx ON franquia_leads (whatsapp);
