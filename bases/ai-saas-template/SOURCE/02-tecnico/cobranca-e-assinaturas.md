---
quando_ler: assinatura, pagamento, trial, limite de plano ou nota fiscal da assinatura
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧾 Cobrança e assinaturas

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Provedor
<ex.: Stripe, Asaas, Iugu, Pagar.me> · Métodos: <cartão, Pix, boleto> · Ambiente de teste: <sandbox>

## Fonte da verdade da assinatura
O **provedor** é a fonte de verdade; o banco guarda uma cópia sincronizada por webhook (`assinatura.status`, `plano`, `fim_do_periodo`).

## Estados da assinatura
| Estado | Acesso | Transições |
|---|---|---|
| `trial` | completo | → `ativa`, `expirada` |
| `ativa` | completo | → `inadimplente`, `cancelada` |
| `inadimplente` | <restrito?> | → `ativa`, `cancelada` |
| `cancelada` | <somente leitura até X dias> | — |

## Webhooks tratados
| Evento do provedor | Ação no sistema |
|---|---|
| <evento> | <ação> |

## Regras
1. Webhook é **idempotente** (mesmo evento duas vezes não duplica efeito).
2. Limites de plano vêm de `00-produto/planos-e-precos.md`.
3. Nota fiscal da assinatura: <emitida por quem, quando>.
4. Nenhum dado de cartão passa pelos nossos servidores.
