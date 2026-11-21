---
quando_ler: precisar do padrão-ouro de uma spec de feature
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🌟 Exemplo de Saída — Spec de Feature

---
gerado_por: Equipe (exemplo aprovado)
fontes: [SOURCE/01-design/mecanicas.md]
data: 2026-11-01
status: aprovado
---

# MEC-01 — Pulso de Luz

**Resumo:** ataque carregado que revela salas ocultas.
**Pilar:** Luz é poder.

## Regras
1. Segurar B carrega; consome luz conforme `habilidades.csv`.
2. Ao soltar, causa dano em raio proporcional à carga.

## Feedback
Halo dourado, som de sino, tremor leve.

## Casos de borda
Luz = 0 → falha e 5 de dano ao jogador.

## Critérios de aceite
- [ ] Revela sala oculta em até 4 unidades
- [ ] 60 FPS com 20 inimigos
