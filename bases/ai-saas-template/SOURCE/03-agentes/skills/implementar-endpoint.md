---
quando_ler: criar ou alterar endpoint, rota de API ou webhook
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🛠️ Skill: implementar endpoint

1. Leia `02-tecnico/contratos-de-api.md`, `multi-tenancy.md` e `autenticacao-e-permissoes.md`.
2. Se o contrato do endpoint não existir no SOURCE, **pare** e crie uma proposta em `ARTEFATO/_propostas-source/`.
3. Implemente: validação de entrada → checagem de permissão no servidor → filtro de `tenant_id` → regra de negócio → resposta no padrão de erro.
4. Testes obrigatórios: sucesso, entrada inválida, sem permissão, **isolamento entre tenants**.
5. Sem segredo no código; variáveis só pelo nome (ver `stack.md`).
6. Passe pela skill `revisar-entrega` antes de mover para a pasta final.
