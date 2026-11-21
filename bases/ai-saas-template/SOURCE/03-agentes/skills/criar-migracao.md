---
quando_ler: criar ou alterar estrutura do banco de dados
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧬 Skill: criar migração

1. Leia `02-tecnico/modelo-de-dados.md`; se a mudança não estiver lá, crie uma proposta em `ARTEFATO/_propostas-source/`.
2. Gere a migração com a ferramenta do projeto (nunca SQL manual em produção).
3. Garanta compatibilidade para trás: adicionar coluna como opcional, preencher dados, só depois tornar obrigatória.
4. Inclua `tenant_id` e índices necessários em tabelas de negócio.
5. Escreva o passo de reversão (down) ou explique por que não existe.
6. **Nunca** execute migração em produção: isso é feito pelo pipeline após aprovação humana.
