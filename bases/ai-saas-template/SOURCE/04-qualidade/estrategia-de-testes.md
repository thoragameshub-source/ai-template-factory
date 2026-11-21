---
quando_ler: escrever, revisar ou decidir quais testes uma entrega precisa
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧪 Estratégia de testes

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

| Tipo | Ferramenta | O que cobre | Obrigatório quando |
|---|---|---|---|
| Unitário | <ex.: Vitest, pytest> | regras de negócio e cálculos | toda regra de `regras-de-negocio.md` |
| Integração | <ferramenta> | endpoint + banco | todo endpoint novo |
| Isolamento de tenant | <ferramenta> | A não acessa B | todo endpoint com dado de cliente |
| E2E | <ex.: Playwright> | jornada principal | cadastro, primeiro valor, pagamento |

## Regras
- Dados de teste **fictícios** (nunca cópia de produção).
- Teste que falha bloqueia o merge.
- Cobertura mínima: <ex.: 80% nas regras de negócio>.
