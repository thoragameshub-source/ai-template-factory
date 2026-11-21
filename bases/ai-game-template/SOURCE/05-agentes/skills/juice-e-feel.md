---
quando_ler: a tarefa for melhorar a sensação do jogo (impacto, resposta, polimento)
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real.


# ✨ Skill — Juice e Game Feel

## Quando usar
A mecânica já funciona e precisa **parecer** boa: golpes sem peso, coleta sem resposta, UI seca.

## Efeitos permitidos
| Efeito | Quando | Limite (parâmetro em `04-dados-de-design/`) |
|---|---|---|
| Screen shake | golpe forte, explosão | `shake_intensidade_max`, `shake_duracao_max` |
| Hitstop | impacto no inimigo | `hitstop_ms_max` |
| Partículas | coleta, dano, morte | `particulas_max_por_efeito` |
| Tween (escala/cor) | UI, coleta | `tween_duracao_ms` |
| Som | toda ação importante | ver `direcao-de-audio.md` |

## Passo a passo
1. Escolher **uma** ação do jogo por vez.
2. Aplicar efeitos pelos parâmetros nomeados (nunca números soltos).
3. Garantir que o efeito pode ser **desligado** (acessibilidade).
4. Conferir performance (`performance-e-plataformas.md`).

## Regras
- Máximo de 3 efeitos por ação; exagero cansa.
- Feedback visual + sonoro em ≤ 100 ms.
