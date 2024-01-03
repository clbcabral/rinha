CREATE EXTENSION IF NOT EXISTS "btree_gist";

CREATE OR REPLACE FUNCTION ar_tostring (ar varchar[])
    RETURNS text
    AS $CODE$
BEGIN
    RETURN ARRAY_TO_STRING(ar, ' ');
END
$CODE$
LANGUAGE plpgsql IMMUTABLE;

CREATE TABLE IF NOT EXISTS PESSOA (
    id uuid UNIQUE NOT NULL,
    apelido VARCHAR(32) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL,
    stack VARCHAR(32)[],
    termos VARCHAR GENERATED ALWAYS AS (apelido || ' ' || nome || ' ' || ar_tostring(stack)) STORED,
    PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS index_termos ON PESSOA USING GIST (termos);