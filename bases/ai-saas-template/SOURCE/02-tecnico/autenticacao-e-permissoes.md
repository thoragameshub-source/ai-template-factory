---
quando_ler: login, cadastro, convite, papel ou permissão
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🔐 Autenticação e permissões

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Autenticação
- Provedor: <ex.: Auth.js, Clerk, Supabase Auth, Cognito>
- Métodos: <e-mail e senha · link mágico · Google · SSO (SAML/OIDC)>
- Sessão: <duração, renovação>; MFA: <obrigatório para admin?>
- Recuperação de conta: <fluxo>

## Papéis
| Papel | Descrição |
|---|---|
| <papel> | <descrição> |
| **Exemplo:** `owner` | Dono da conta; cobrança e exclusão da conta |
| **Exemplo:** `admin` | Gerencia usuários e configurações |
| **Exemplo:** `membro` | Usa as funcionalidades do dia a dia |

## Matriz de permissões
| Ação | owner | admin | membro |
|---|:-:|:-:|:-:|
| Convidar usuário | ✅ | ✅ | ⛔ |
| Alterar plano / pagamento | ✅ | ⛔ | ⛔ |
| <ação> | | | |

> A checagem de permissão acontece **no servidor**; esconder botão na tela não é permissão.
