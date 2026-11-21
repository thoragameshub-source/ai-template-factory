---
quando_ler: deploy, ambientes, variáveis, logs, alertas ou custo de infraestrutura
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# ☁️ Infraestrutura e observabilidade

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Ambientes
| Ambiente | Onde | Banco | Quem faz deploy | Dados |
|---|---|---|---|---|
| local | máquina do dev | <docker> | dev | fictícios |
| staging | <ex.: Vercel preview> | <banco> | CI | fictícios |
| produção | <ex.: Vercel + Neon> | <banco> | CI após aprovação | reais |

## Deploy
<Fluxo: PR → CI (testes) → staging → aprovação → produção.> Rollback: <como>.

## Observabilidade
| Item | Ferramenta | Regra |
|---|---|---|
| Logs | <ex.: Axiom> | estruturados, com `tenant_id`, **sem dados pessoais** |
| Erros | <ex.: Sentry> | alerta em erro novo |
| Uptime | <ex.: Better Stack> | alerta se cair por mais de 2 min |
| Custos | <painel> | alerta acima de <R$> por mês |

## Backups
Frequência: <diária> · Retenção: <dias> · Teste de restauração: <mensal>
