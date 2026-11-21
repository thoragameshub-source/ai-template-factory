---
quando_ler: SEMPRE — é o primeiro arquivo que todo agente lê
modulo: nucleo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧠 Contexto Master — <Nome do SaaS>

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

> ⚠️ Respeite o limite de linhas do nível (SIMPLES 40, MÉDIO 80, COMPLEXO 120). Detalhe vai nos outros arquivos; aqui só o essencial e o mapa.

## 0. 🚦 Modo do projeto
**Antes de tudo, leia `MODO.md`.** `PLANEJAMENTO` = a IA edita o SOURCE por prompt direto. `EXECUCAO` = SOURCE somente leitura; a IA gera artefatos e propõe mudanças.

## 1. Produto em 3–5 linhas
<Qual problema o SaaS resolve, para quem, e qual resultado o cliente compra.>

**Exemplo:** SaaS que recebe as notas fiscais de serviço de pequenos escritórios, confere retenções e avisa divergências antes do fechamento, para reduzir multas e retrabalho do contador.

## 2. Clientes e usuários
| Perfil | Quem é | O que faz no produto |
|---|---|---|
| <Perfil> | <descrição> | <uso> |
| Dono do escritório (admin) | Assina e paga | Convida a equipe, vê o painel de divergências |
| Analista (membro) | Usa no dia a dia | Envia notas e resolve divergências |

## 3. Regras inegociáveis (máx. 7)
1. **Leia `MODO.md` antes de agir.** Em EXECUÇÃO o SOURCE é **somente leitura**; mudanças vão para `ARTEFATO/_propostas-source/`.
2. Todo dado de cliente pertence a um `tenant`; **nenhuma consulta sem filtro de tenant**.
3. Nunca usar dados reais de clientes em testes, exemplos ou prompts.
4. <Regra específica do produto>

## 4. Mapa do SOURCE — "leia quando..."
| Arquivo | Leia quando... |
|---|---|
| `00-produto/visao-e-escopo.md` | precisar entender o que está dentro/fora do escopo |
| `00-produto/requisitos.md` | for construir ou validar uma funcionalidade |
| `00-produto/personas-e-jornadas.md` | desenhar fluxo, tela ou onboarding |
| `00-produto/planos-e-precos.md` | algo depender de plano, limite ou preço |
| `00-produto/metricas-de-produto.md` | instrumentar eventos ou medir sucesso |
| `01-dominio/glossario.md` | encontrar um termo do negócio que não conhece |
| `01-dominio/regras-de-negocio.md` | aplicar cálculo, regra ou restrição |
| `01-dominio/fontes-de-verdade.md` | duas fontes divergirem |
| `02-tecnico/stack.md` | escolher biblioteca, linguagem ou versão |
| `02-tecnico/arquitetura.md` | criar/alterar componente ou integração |
| `02-tecnico/convencoes.md` | for nomear, formatar, testar ou tratar erros |
| `02-tecnico/modelo-de-dados.md` | criar/alterar tabela, campo ou migração |
| `02-tecnico/contratos-de-api.md` | criar/alterar endpoint ou webhook |
| `02-tecnico/multi-tenancy.md` | qualquer consulta ou dado de cliente |
| `02-tecnico/autenticacao-e-permissoes.md` | login, convite, papel ou permissão |
| `02-tecnico/cobranca-e-assinaturas.md` | assinatura, pagamento, trial ou limite de plano |
| `02-tecnico/infra-e-observabilidade.md` | deploy, ambiente, log, alerta ou custo |
| `03-agentes/guardrails.md` | antes de qualquer ação com efeito externo |
| `03-agentes/skills/*.md` | a tarefa casar com uma skill |
| `04-qualidade/definicao-de-pronto.md` | for declarar uma entrega como concluída |
| `04-qualidade/seguranca-e-lgpd.md` | tocar em dado pessoal, segredo ou permissão |
| `04-qualidade/estrategia-de-testes.md` | escrever ou revisar testes |
| `07-operacao/roadmap-e-releases.md` | priorizar ou planejar uma release |
| `07-operacao/suporte-e-incidentes.md` | houver erro em produção ou chamado de cliente |
| `06-decisoes/` | houver dúvida do tipo "por que foi feito assim?" |

## 5. Onde gravar o que você gerar
| Tipo | Pasta |
|---|---|
| Código, migrações e testes | `ARTEFATO/codigo/` |
| Specs, textos, documentação | `ARTEFATO/documentos/` |
| Scripts e automações | `ARTEFATO/automacoes/` |
| Não revisado | `ARTEFATO/_rascunhos/` |
| Sugestão de mudança no SOURCE | `ARTEFATO/_propostas-source/` |
| Registro do que você fez | `ARTEFATO/_logs/` |

## 6. Como trabalhar
1. Leia `MODO.md`, depois este arquivo, e consulte só o que o mapa indicar.
2. Se faltar informação, **pergunte** em vez de supor.
3. Gere em `_rascunhos/`, passe pela skill `revisar-entrega` e só então mova para a pasta final.
4. Registre em `_logs/changelog-ia.md`.
