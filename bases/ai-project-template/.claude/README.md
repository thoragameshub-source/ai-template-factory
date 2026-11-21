# .claude/ (opcional)

Adaptadores do Claude Code. O conteúdo real continua em `SOURCE/`; aqui ficam só ponteiros finos e reforços.

## Skills nativas (ponteiros)
```
.claude/skills/revisar-entrega/SKILL.md
---
name: revisar-entrega
description: Revisa rascunhos contra o checklist antes de entregar
---
Siga SOURCE/<pasta-de-agentes>/skills/revisar-entrega.md
```

## Reforço dos modos (opcional)
A pasta `exemplos/` traz dois arquivos de permissão:
- `settings.execucao.json` — bloqueia edição de `SOURCE/`, `MODO.md`, `AGENTS.md` e `CLAUDE.md`.
- `settings.planejamento.json` — bloqueia só `MODO.md`, `AGENTS.md` e `CLAUDE.md`.

Para usar, copie o arquivo do modo atual para `.claude/settings.json` (e troque ao mudar de modo).
**Valide a sintaxe na documentação de permissões do Claude Code.** Isto é um reforço, não substitui a regra do `MODO.md`; comandos de shell podem contornar bloqueios de edição.

Se o projeto não usar Claude Code, apague esta pasta.
