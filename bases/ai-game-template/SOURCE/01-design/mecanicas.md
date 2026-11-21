---
quando_ler: implementar, ajustar ou descrever uma mecânica
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# ⚔️ Mecânicas

## Modelo de cada mecânica
> ⚠️ **Nunca escreva números aqui.** Use nomes de parâmetros (ex.: `dano_base`); os valores vivem em `04-dados-de-design/`.

```
MEC-XX — <Nome>
Resumo: <1 frase>
Pilar atendido: <qual>
Entrada do jogador: <botão/gesto>
Regras: <passos claros e testáveis>
Feedback: <visual/sonoro/háptico>
Valores: ver 04-dados-de-design/<arquivo>
Casos de borda: <o que acontece se...>
Status: Ideia | Prototipada | Implementada | Cortada
```

## MEC-01 — Exemplo: Pulso de Luz
- **Resumo:** o jogador emite um pulso que causa dano e revela salas ocultas.
- **Pilar atendido:** Luz é poder
- **Entrada:** botão B (segurar para carregar)
- **Regras:** carregar consome `luz_por_segundo`; ao soltar, raio = `alcance_base` × carga; inimigos de sombra recebem `multiplicador_sombra` sobre `dano`.
- **Feedback:** halo dourado, som de sino grave, tremor leve na câmera.
- **Valores:** `04-dados-de-design/habilidades.csv`
- **Casos de borda:** se luz = 0, pulso falha e causa dano ao jogador.
- **Status:** Prototipada

## MEC-02 — <Nome>
<...>
