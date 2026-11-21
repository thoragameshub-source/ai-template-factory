---
quando_ler: entender por que a engine foi escolhida
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧭 ADR-001 — Exemplo: Engine Godot 4

- **Status:** Aceita
- **Data:** 2026-11-01
- **Decisores:** Líder técnico, Game Designer

## Contexto
Jogo 2D, equipe pequena, necessidade de builds leves e sem royalties.

## Decisão
Usar Godot 4 com GDScript.

## Alternativas
| Opção | Prós | Contras |
|---|---|---|
| Godot | Leve, gratuita, ótima para 2D | Menos plugins de console |
| Unity | Ecossistema enorme | Build maior, licenciamento |

## Consequências
- Positivas: iteração rápida, builds pequenos.
- Riscos: portar para console exigirá parceiro.
