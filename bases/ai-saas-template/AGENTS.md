# AGENTS.md

Este projeto usa **SOURCE / ARTEFATO** e dois modos: **PLANEJAMENTO** e **EXECUÇÃO**.

## Antes de tudo
1. **Leia `MODO.md`** e obedeça o valor de `modo:`. Se estiver ausente ou inválido, aja como **EXECUCAO**.
2. Leia `SOURCE/contexto-master.md` e consulte só os arquivos que o mapa indicar.
3. Respeite `SOURCE/03-agentes/guardrails.md`. Em dúvida, pergunte.
4. Leia `nivel:` no `MODO.md` e trabalhe **só com os arquivos do nível** (`niveis.json`). Não crie arquivos de níveis superiores sem o usuário pedir.

## Se o modo for PLANEJAMENTO
- Edite arquivos de `SOURCE/` **somente quando o usuário indicar por prompt** (um arquivo por vez).
- Mantenha a estrutura do template; troque exemplos pelos dados do usuário; **não invente** (use `a confirmar`).
- Não gere entregas finais em `ARTEFATO/` (apenas `_rascunhos/` e relatórios).
- Registre cada edição em `ARTEFATO/_logs/changelog-source.md`.

## Se o modo for EXECUÇÃO
- **Nunca edite `SOURCE/`.** Se achar erro ou lacuna, crie uma proposta em `ARTEFATO/_propostas-source/`.
- Gere em `ARTEFATO/_rascunhos/`, aplique `skills/revisar-entrega.md` e só então mova para a pasta final.
- Todo artefato leva cabeçalho de rastreabilidade. Registre em `ARTEFATO/_logs/changelog-ia.md`.

## Sempre
- Nunca edite `MODO.md`, `AGENTS.md`, `CLAUDE.md`, `niveis.json` nem a pasta `tools/`, e nunca altere o valor de `modo:`.
- Só humanos marcam `status: aprovado`.
