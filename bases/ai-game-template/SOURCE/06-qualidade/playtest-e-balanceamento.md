---
quando_ler: planejar testes com jogadores ou ajustar balanceamento
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🧪 Playtest e Balanceamento

## Plano de playtest
| Campo | Conteúdo |
|---|---|
| Objetivo | <o que queremos descobrir> — **Exemplo:** A ilha 2 está injusta? |
| Perfil dos testadores | <quem> |
| Duração e build | <20 min, build 0.3.1> |
| Perguntas | <lista> |
| Métricas | <taxa de morte por sala, tempo por sala, abandono> |

## Roteiro de observação
- Não explicar o jogo; observar onde o jogador trava.

## Como registrar resultados
Usar `ARTEFATO/playtests/` (modelo no README da pasta).

## Ciclo de balanceamento
1. Coletar dados → 2. Propor ajuste (`_propostas-source/`) → 3. Humano altera `04-dados-de-design/` → 4. Novo playtest.

## Metas (referência)
| Métrica | Alvo |
|---|---|
| Taxa de vitória ilha 1 | 80% |
| Tempo médio por corrida | 15–20 min |
