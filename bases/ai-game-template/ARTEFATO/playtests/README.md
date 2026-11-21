# 🧪 playtests

Relatórios de testes com jogadores. Um arquivo por sessão: `AAAA-MM-DD_playtest_<tema>.md`.

## Modelo de relatório
```markdown
---
gerado_por: <agente/pessoa>
fontes: [SOURCE/06-qualidade/playtest-e-balanceamento.md]
data: AAAA-MM-DD
status: rascunho
---
# Playtest — <tema> (build 0.3.1)

**Objetivo:** <o que queríamos descobrir>
**Testadores:** <nº e perfil>

## Métricas
| Métrica | Resultado | Meta |
|---|---|---|
| Taxa de morte na sala 3 | 62% | < 40% |

## Principais achados
1. <achado + evidência>

## Propostas de ajuste
- <ajuste> → registrar em `_propostas-source/`
```
