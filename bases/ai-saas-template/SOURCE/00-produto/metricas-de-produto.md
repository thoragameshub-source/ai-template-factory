---
quando_ler: instrumentar eventos, montar painel ou medir sucesso de uma feature
modulo: saas   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 📈 Métricas de produto

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## North Star
<Métrica única que representa valor entregue.> **Exemplo:** notas conferidas por semana por conta ativa.

## Funil
| Etapa | Evento | Meta |
|---|---|---|
| Visita → cadastro | `conta_criada` | <ex.: 5%> |
| Cadastro → ativação | `primeira_nota_enviada` | <ex.: 40% em 7 dias> |
| Trial → pago | `assinatura_iniciada` | <ex.: 15%> |
| Retenção | `nota_enviada` no mês 2 | <ex.: 70%> |

## Eventos (padrão de nomes: `objeto_acao` no passado)
| Evento | Quando dispara | Propriedades | Sem dados pessoais? |
|---|---|---|---|
| <evento> | <gatilho> | <props> | ✅ |

## Métricas de negócio
MRR, churn de logo e de receita, CAC, LTV, ticket médio: <fonte e frequência de cálculo>.
