# AGENTS.md

Este projeto é um **jogo** e usa **SOURCE / ARTEFATO** com dois modos: **PLANEJAMENTO** e **EXECUÇÃO**.

## Antes de tudo
1. **Leia `MODO.md`** e obedeça o valor de `modo:`. Se estiver ausente ou inválido, aja como **EXECUCAO**.
2. Leia `SOURCE/contexto-master.md` (jogo, pilares, estado atual, mapa "leia quando...").
3. Respeite `SOURCE/05-agentes/guardrails.md`. Em dúvida, pergunte.
4. Leia `nivel:` no `MODO.md` e trabalhe **só com os arquivos do nível** (`niveis.json`). Não crie arquivos de níveis superiores sem o usuário pedir.

## Se o modo for PLANEJAMENTO
- Edite arquivos de `SOURCE/` (inclusive CSV/JSON de dados) **somente quando o usuário indicar por prompt**, um arquivo por vez.
- Mantenha o template, troque exemplos pelos dados do usuário e **não invente** (use `a confirmar`).
- Não escreva em `ARTEFATO/jogo/`. Protótipos greybox descartáveis só em `ARTEFATO/_rascunhos/`.
- Registre cada edição em `ARTEFATO/_logs/changelog-source.md`.

## Se o modo for EXECUÇÃO
- **Nunca edite `SOURCE/`.** Erros ou lacunas (inclusive de balanceamento) viram proposta em `ARTEFATO/_propostas-source/`.
- O projeto da engine fica em `ARTEFATO/jogo/`. **Nenhum valor de balanceamento no código**: leia de `SOURCE/04-dados-de-design/`.
- Sistemas se comunicam **só por eventos** (`contrato-de-eventos.md`) e seguem `mapa-cenas-nodos.md`.
- A build **sempre abre e roda** ao fim de cada mudança; mudanças pequenas, uma por vez.
- Todo asset novo entra em `ARTEFATO/arte/manifesto-de-assets.csv` (origem + licença).
- Gere em `_rascunhos/`, aplique `skills/revisar-entrega.md` e só então mova. Registre em `changelog-ia.md`, `estado-da-build.md` e `bugs-conhecidos.md`.

## Sempre
- Nunca edite `MODO.md`, `AGENTS.md`, `CLAUDE.md`, `niveis.json` nem a pasta `tools/`, nem altere o valor de `modo:`.
- Só humanos marcam `status: aprovado`.
