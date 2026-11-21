---
quando_ler: o jogo tiver cooperativo, online ou ranking
modulo: multiplayer   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🌐 Multiplayer e Rede

| Item | Decisão |
|---|---|
| Modelo | <cliente-servidor / P2P / lockstep> |
| Servidor | <dedicado / host / serviço> |
| Autoridade | <servidor decide dano? sim/não> |
| Latência alvo | < 100 ms |
| Anti-cheat | <estratégia> |

## O que é sincronizado
<Estado, entradas, eventos.>

## Cenários de teste
<Perda de pacote, lag, desconexão.>
