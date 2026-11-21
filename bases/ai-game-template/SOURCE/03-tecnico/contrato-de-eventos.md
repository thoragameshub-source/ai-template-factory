---
quando_ler: criar ou alterar qualquer comunicação entre sistemas (gameplay, UI, áudio, save)
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real.


# 📡 Contrato de Eventos / Sinais

> Sistemas **só** se comunicam por eventos. Nada de referência direta entre gameplay e UI.

## Eventos
| Evento | Emissor | Payload | Ouvintes |
|---|---|---|---|
| <nome_no_passado> | <sistema> | <campos> | <sistemas> |
| **Exemplo:** `player_died` | Player | `causa`, `sala_id` | UI, Áudio, Save, Estatísticas |
| **Exemplo:** `luz_changed` | Player | `valor_atual`, `valor_max` | HUD |
| **Exemplo:** `enemy_killed` | Enemy | `id`, `posicao`, `drop` | Loot, Score, Áudio |
| **Exemplo:** `room_cleared` | Level | `sala_id` | UI, Níveis |

## Regras
1. Nome em `snake_case` no passado (`score_changed`, não `change_score`).
2. Payload **mínimo**: ids e valores, nunca referências a objetos inteiros.
3. Novo evento ou mudança de payload = atualizar este arquivo (em PLANEJAMENTO) ou propor (em EXECUÇÃO).
4. Quem emite não sabe quem ouve.
