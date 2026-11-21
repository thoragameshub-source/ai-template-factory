---
quando_ler: SEMPRE — é o primeiro arquivo que todo agente lê
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧠 Contexto Master — <Nome do Projeto>

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

> ⚠️ Mantenha este arquivo com **no máximo 1–2 páginas**. Detalhe vai nos outros arquivos; aqui só o essencial e o mapa.

## 0. 🚦 Modo do projeto
**Antes de tudo, leia `MODO.md`.** `PLANEJAMENTO` = a IA edita o SOURCE por prompt direto. `EXECUCAO` = SOURCE somente leitura; a IA gera artefatos e propõe mudanças.

## 1. Objetivo do produto (3–5 linhas)
<O que este projeto entrega, para quem e qual resultado de negócio gera.>

**Exemplo:** Assistente que confere notas fiscais de serviço recebidas, extrai os dados para planilha e aponta divergências de impostos, para o time Fiscal reduzir o retrabalho de conferência manual em 60%.

## 2. Quem usa
| Perfil | O que faz com o resultado |
|---|---|
| <Perfil> | <Uso> |
| Analista Fiscal | Revisa e aprova a planilha gerada |
| Líder da área | Acompanha divergências do mês |

## 3. Regras inegociáveis (máx. 7)
1. **Leia `MODO.md` antes de agir.** Em PLANEJAMENTO a IA edita o SOURCE só por prompt direto; em EXECUÇÃO o SOURCE é **somente leitura** e mudanças vão para `ARTEFATO/_propostas-source/`.
2. Tudo que o agente gerar vai para `ARTEFATO/` com o cabeçalho de rastreabilidade.
3. <Regra específica do projeto>
4. **Exemplo:** Nunca inventar valores, alíquotas ou números de nota; se faltar dado, perguntar.

## 4. Mapa do SOURCE — "leia quando..."
| Arquivo | Leia quando... |
|---|---|
| `00-produto/visao-e-escopo.md` | precisar entender o que está dentro/fora do escopo |
| `00-produto/requisitos.md` | for construir ou validar uma funcionalidade |
| `01-dominio/glossario.md` | encontrar um termo do negócio que não conhece |
| `01-dominio/regras-de-negocio.md` | aplicar cálculo, regra ou restrição |
| `01-dominio/fontes-de-verdade.md` | duas fontes divergirem |
| `02-tecnico/stack.md` | escolher biblioteca, linguagem ou versão |
| `02-tecnico/arquitetura.md` | criar/alterar estrutura técnica ou integração |
| `02-tecnico/convencoes.md` | for nomear, formatar, testar ou tratar erros |
| `03-agentes/guardrails.md` | antes de qualquer ação com efeito externo |
| `03-agentes/skills/*.md` | a tarefa casar com uma skill (código, documento, revisão) |
| `04-qualidade/definicao-de-pronto.md` | for declarar uma entrega como concluída |
| `05-referencias/exemplos-de-saida/` | precisar do padrão-ouro de uma entrega |
| `06-decisoes/` | houver dúvida do tipo "por que foi feito assim?" |

## 5. Onde gravar o que você gerar
| Tipo | Pasta |
|---|---|
| Textos, relatórios, specs | `ARTEFATO/documentos/` |
| Código e testes | `ARTEFATO/codigo/` |
| Automações, fluxos, scripts | `ARTEFATO/automacoes/` |
| Não revisado | `ARTEFATO/_rascunhos/` |
| Sugestão de mudança no SOURCE | `ARTEFATO/_propostas-source/` |
| Registro do que você fez | `ARTEFATO/_logs/` |

## 6. Como trabalhar (resumo do ciclo)
1. Leia `MODO.md`, depois este arquivo, e consulte só o que o mapa indicar.
2. Se faltar informação, **pergunte** em vez de supor.
3. Gere em `_rascunhos/`, passe pela skill `revisar-entrega`, e só então mova para a pasta final.
4. Registre em `_logs/changelog-ia.md`.
