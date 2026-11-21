---
quando_ler: otimizar, definir requisitos mínimos ou portar para outra plataforma
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# ⚡ Performance e Plataformas

## Metas
| Plataforma | FPS alvo | Resolução | Memória máx. | Tamanho do build |
|---|---|---|---|---|
| PC (mín.) | 60 | 1080p | 2 GB | < 500 MB |
| <Plataforma> | | | | |

## Orçamentos
| Item | Limite |
|---|---|
| Draw calls | <n> |
| Entidades ativas | <n> |
| Tempo de carregamento de fase | < 3 s |

## Regras
- <ex.: object pooling para projéteis; sem alocação por frame no loop principal>

## Como medir
<Ferramentas de profiling e cenário de teste padrão.>
