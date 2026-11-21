---
quando_ler: criar ou alterar cenas, entidades, colisões ou a hierarquia do jogo
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real.


# 🌳 Mapa de Cenas e Nós

> Contrato de estrutura: o código gerado por IA **deve** respeitar esta hierarquia.

## Árvore de cenas
```
Main (scn_main)
├── World
│   ├── Level (carregado por fase)
│   ├── Player (scn_player)
│   └── Enemies (grupo)
├── UI (scn_ui)
│   ├── HUD
│   └── Menus
└── Audio (bus e players globais)
```
> Substitua pela árvore real do seu jogo.

## Cenas reutilizáveis
| Cena | Contém | Quem instancia | Observação |
|---|---|---|---|
| <scn_player> | <corpo, sprite, colisor, componentes> | Main/World | |
| **Exemplo:** scn_enemy_sombra | corpo, sprite, hurtbox, IA | Level | uma cena por tipo de inimigo |

## Camadas de colisão
| Camada | Nome | Colide com |
|---|---|---|
| 1 | mundo | jogador, inimigos |
| 2 | jogador | mundo, itens, ataque_inimigo |
| 3 | inimigo | mundo, ataque_jogador |
| <n> | <nome> | <lista> |

## Grupos / tags
| Grupo | Uso |
|---|---|
| `inimigos` | contagem, spawns, efeitos globais |
| `luz` | objetos afetados pelo pulso de luz |

## Regras de composição
1. Cada entidade é **uma cena autocontida** (sem depender de caminhos absolutos).
2. Comportamentos pequenos em **componentes** reutilizáveis, não em heranças profundas.
3. Cena não conhece UI; ela emite eventos (ver `contrato-de-eventos.md`).
4. Nomes de nós em `PascalCase`; arquivos de cena conforme `convencoes-de-assets.md`.
