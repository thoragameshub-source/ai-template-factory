---
quando_ler: criar, revisar ou descrever fases, mapas ou geração procedural
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🗺️ Níveis e Mundo

## Estrutura do mundo
<Mapa geral, hub, regiões.> **Exemplo:** Hub (farol) + 5 ilhas de bioma diferente.

## Modelo de cada nível/bioma
| Campo | Conteúdo |
|---|---|
| Nome | <Ilha das Névoas> |
| Objetivo do jogador | <ex.: achar a chave do farol> |
| Mecânica em destaque | <qual MEC-xx é ensinada/testada> |
| Inimigos | <lista, ver dados> |
| Duração alvo | <min> |
| Estética | <link p/ art-bible> |

## Regras de geração procedural (se houver)
- <Regras de conexão, salas obrigatórias, seeds>
- **Exemplo:** 5–7 salas por ilha; sala de descanso obrigatória na 4ª.

## Ritmo (tensão ao longo do nível)
<Combate → exploração → pico → alívio>

## Checklist de nível
- [ ] Ensina ou exige uma mecânica
- [ ] Tem ponto de descanso
- [ ] Caminho crítico claro
