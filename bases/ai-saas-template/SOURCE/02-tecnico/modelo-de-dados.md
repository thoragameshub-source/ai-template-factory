---
quando_ler: criar ou alterar tabela, campo, índice ou migração
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🗄️ Modelo de dados

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Entidades
| Entidade | Descrição | Pertence ao tenant? | Dados pessoais? |
|---|---|---|---|
| <entidade> | <descrição> | ✅/⛔ | <quais> |
| **Exemplo:** `tenant` | Empresa cliente que assina | — | Razão social, CNPJ |
| **Exemplo:** `usuario` | Pessoa com login | ✅ | Nome, e-mail |
| **Exemplo:** `nota` | Nota fiscal enviada | ✅ | — |

## Campos padrão de toda tabela de negócio
`id` (UUID) · `tenant_id` · `criado_em` · `atualizado_em` · `excluido_em` (soft delete, se usar)

## Relacionamentos
```mermaid
erDiagram
  TENANT ||--o{ USUARIO : tem
  TENANT ||--o{ NOTA : possui
```

## Regras de migração
1. Toda mudança de schema é uma migração versionada em `ARTEFATO/codigo/` (nunca alteração manual no banco).
2. Migrações são **compatíveis para trás** (adicionar antes de remover; remover só na release seguinte).
3. <Ferramenta de migração: ex.: Prisma, Alembic>
