---
quando_ler: precisar de qualquer número: dano, custo, vida, drop, tempo
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 📊 Dados de Design — a planilha é a verdade

> Todos os valores de balanceamento ficam aqui, em **CSV/JSON**. O código **lê** esses arquivos; nunca duplica os números.

## Regras
1. Um arquivo por entidade: `inimigos.csv`, `habilidades.csv`, `itens.csv`...
2. Primeira linha = nomes das colunas; `id` único em minúsculas.
3. Mudança de balanceamento = mudança neste arquivo (por pessoa) + registro em `ARTEFATO/playtests/`.
4. Em PLANEJAMENTO a IA pode editar por prompt; em EXECUÇÃO só **propõe** valores em `_propostas-source/`.

## Arquivos de exemplo
- `habilidades.csv`
- `inimigos.csv`
