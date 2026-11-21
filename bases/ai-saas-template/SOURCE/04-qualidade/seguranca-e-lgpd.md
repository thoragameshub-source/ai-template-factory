---
quando_ler: tocar em dado pessoal, segredo, permissão ou exportação de dados
modulo: saas   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🛡️ Segurança e LGPD

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Dados pessoais tratados
| Dado | Finalidade | Base legal (LGPD) | Retenção | Quem acessa |
|---|---|---|---|---|
| <dado> | <finalidade> | <execução de contrato / consentimento / legítimo interesse> | <prazo> | <papéis> |
| **Exemplo:** e-mail do usuário | login e avisos | execução de contrato | até 90 dias após cancelamento | sistema, suporte |

## Direitos do titular
Exportar dados: <como> · Excluir conta e dados: <como e prazo> · Canal do encarregado (DPO): <e-mail>

## Regras de segurança
1. Segredos só em variáveis de ambiente / cofre; nunca no repositório.
2. Senhas com hash forte (ou provedor de autenticação); nunca em log.
3. Dependências com verificação automática de vulnerabilidades.
4. Dados pessoais **não** vão para prompts de IA de terceiros sem anonimização ou base legal.
5. Incidente com dado pessoal: seguir `07-operacao/suporte-e-incidentes.md` e avaliar comunicação à ANPD.

## Suboperadores
| Serviço | Dado compartilhado | País |
|---|---|---|
| <serviço> | <dado> | <país> |
