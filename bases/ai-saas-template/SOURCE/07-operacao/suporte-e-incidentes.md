---
quando_ler: houver erro em produção, indisponibilidade ou chamado de cliente
modulo: saas   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🚨 Suporte e incidentes

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Canais de suporte
<e-mail, chat, horário, prazo de primeira resposta>

## Severidade
| Nível | Exemplo | Resposta | Quem é acionado |
|---|---|---|---|
| SEV1 | Produto fora do ar ou vazamento de dados | imediata | <pessoa> |
| SEV2 | Funcionalidade principal quebrada | até 4 h | <pessoa> |
| SEV3 | Erro com contorno | próximo dia útil | <pessoa> |

## Durante um incidente
1. Registrar início, impacto e tenants afetados.
2. Comunicar clientes afetados em <canal> (modelo de mensagem: <link>).
3. Corrigir ou fazer rollback; **IA não faz deploy em produção**.
4. Pós-incidente sem culpados em `ARTEFATO/documentos/incidentes/` em até 5 dias.
