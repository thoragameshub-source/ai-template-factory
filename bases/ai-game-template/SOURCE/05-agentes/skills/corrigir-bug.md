---
quando_ler: a tarefa for investigar e corrigir um bug sem reescrever sistemas
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real.


# 🐛 Skill — Corrigir Bug

## Passo a passo
1. **Reproduzir:** descrever os passos mínimos; se não reproduz, pedir mais dados.
2. **Isolar:** achar a menor parte do código/cena envolvida (use `contrato-de-eventos.md` e `mapa-cenas-nodos.md`).
3. **Corrigir o mínimo:** alterar o menor número de linhas possível.
4. **Teste de regressão:** criar ou ajustar um teste/cena que falharia antes da correção.
5. **Registrar:** atualizar `ARTEFATO/_logs/bugs-conhecidos.md` e `changelog-ia.md`.

## Regras
- **Proibido** reescrever um sistema inteiro para corrigir um bug.
- Se a causa for uma regra errada no SOURCE, **pare e proponha** em `_propostas-source/`.
- A build abre e roda ao final.
