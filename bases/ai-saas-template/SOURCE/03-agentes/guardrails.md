---
quando_ler: ANTES de qualquer ação com efeito fora do rascunho
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🛡️ Guardrails

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## ⛔ Nunca fazer
1. Editar `SOURCE/` quando `MODO.md` estiver em EXECUÇÃO (propor em `_propostas-source/`), ou alterar `MODO.md`, `AGENTS.md` e `CLAUDE.md` em qualquer modo.
2. <Ação proibida>
3. **Exemplo:** Enviar e-mail/mensagem em nome de alguém sem aprovação.
4. **Exemplo:** Inserir senhas, chaves ou dados pessoais reais em arquivos ou logs.

## ✋ Exige aprovação humana antes
| Ação | Quem aprova |
|---|---|
| <Ação> | <Papel> |
| **Exemplo:** Alterar planilha oficial compartilhada | Líder da área |
| **Exemplo:** Executar script que apaga/move arquivos | Responsável técnico |

## ✅ Pode fazer sozinho
- Ler o SOURCE, gerar rascunhos, rodar testes locais, registrar logs.

## Dados sensíveis
- <O que é sensível neste projeto e como tratar.>
- **Exemplo:** CPF/CNPJ de terceiros: mascarar nos exemplos e logs (`***.***.***-12`).

## Quando em dúvida
Pare, descreva a dúvida em uma frase e pergunte ao usuário.

## 🏢 Regras específicas de SaaS
- ⛔ Executar migração, script ou deploy em **produção**.
- ⛔ Ler, copiar ou usar **dados reais de clientes** (use dados fictícios).
- ⛔ Alterar preços, planos ou regras de cobrança fora de `00-produto/planos-e-precos.md`.
- ⛔ Criar consulta sem filtro de `tenant_id`.
- ⚠️ Com aprovação humana: novas dependências pagas, novos suboperadores de dados, mudanças de permissão.
