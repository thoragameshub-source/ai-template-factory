---
quando_ler: qualquer consulta, job ou arquivo com dado de cliente
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🏢 Multi-tenancy (isolamento entre clientes)

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Estratégia
<Escolha uma:> banco compartilhado com `tenant_id` · schema por tenant · banco por tenant.
**Exemplo:** banco compartilhado com `tenant_id` + Row Level Security no PostgreSQL.

## Regras obrigatórias
1. Toda tabela de negócio tem `tenant_id` e **toda consulta filtra por ele** (de preferência de forma automática: RLS, middleware ou repositório base).
2. O `tenant_id` vem **da sessão autenticada**, nunca de parâmetro enviado pelo cliente.
3. Arquivos em storage ficam em `/<tenant_id>/...`.
4. Jobs e filas carregam o `tenant_id` e o validam ao executar.
5. Logs e métricas levam `tenant_id`, sem dados pessoais.

## Teste obrigatório de isolamento
Para cada endpoint novo: usuário do tenant A **não** lê, altera nem lista dados do tenant B.

## Usuário em vários tenants
<Permitido? Como troca de conta?>
