# 🚀 <Nome do Projeto>

> <Uma frase: o que é e para quem.>

## O que é este repositório
Template **SOURCE / ARTEFATO** para produtos **SaaS** feitos com IA (Claude, GPT, Cursor, Copilot etc.), com **dois modos**:

| Modo | O que acontece |
|---|---|
| 📝 **PLANEJAMENTO** | Você constrói o `SOURCE/` e a IA **edita os arquivos** por prompts diretos (tabela no guia) |
| ⚙️ **EXECUÇÃO** | O `SOURCE/` fica **congelado**; a IA produz o `ARTEFATO/` e só **propõe** mudanças |

O modo está em [`MODO.md`](MODO.md) e **só humanos o alteram**.

## Começar em 6 passos
1. Confirme que `MODO.md` está em `PLANEJAMENTO`.
2. Abra a sessão com o prompt **P0** e gere cada arquivo na ordem da tabela de prompts (`PROMPTS-PLANEJAMENTO.md`).
3. Preencha o **núcleo** e apague os módulos que o projeto não usa.
4. Rode **PC** (consistência) e **PG** (gate) e corrija pendências.
5. Congele: commit + tag `source-v1.0` e mude `MODO.md` para `EXECUCAO`.
6. Peça tarefas à IA, revise o `ARTEFATO/` e aprove.

## Nível do projeto
O nível foi definido no *Startup building* e está no `MODO.md` (`nivel:`). Arquivos de cada nível, pontuação e promoção: [`NIVEIS.md`](NIVEIS.md). Nomes de repositórios, branches e commits: [`NOMENCLATURA.md`](NOMENCLATURA.md). Pendências do startup: `ARTEFATO/_logs/pendencias-startup.md`.

## Estrutura
```
📦 saas-<nome>/
├── 📄 README.md · AGENTS.md · CLAUDE.md · MODO.md · NIVEIS.md · NOMENCLATURA.md · PROMPTS-PLANEJAMENTO.md
├── 📄 niveis.json · 📁 tools/ · 📁 .github/ · 📁 .claude/
│
├── 📁 SOURCE/                    → 🔒 FONTE DE VERDADE
│   ├── 📄 contexto-master.md
│   ├── 📁 00-produto/            visao-e-escopo · requisitos · personas-e-jornadas · planos-e-precos · metricas-de-produto
│   ├── 📁 01-dominio/            glossario · regras-de-negocio · fontes-de-verdade
│   ├── 📁 02-tecnico/            stack · arquitetura · convencoes · modelo-de-dados · contratos-de-api
│   │                             multi-tenancy · autenticacao-e-permissoes · cobranca-e-assinaturas · infra-e-observabilidade
│   ├── 📁 03-agentes/            guardrails · papeis-e-fluxo · skills/ (implementar-endpoint, criar-migracao, escrever-codigo, revisar-entrega…)
│   ├── 📁 04-qualidade/          definicao-de-pronto · checklist-revisao · seguranca-e-lgpd · estrategia-de-testes
│   ├── 📁 05-referencias/        exemplos-de-saida/ · schemas/ · templates/
│   ├── 📁 06-decisoes/           ADR-000-modelo · ADR-001-exemplo
│   └── 📁 07-operacao/           roadmap-e-releases · suporte-e-incidentes
│
└── 📁 ARTEFATO/                  → ✍️ SAÍDA (codigo/ · documentos/ · automacoes/ · _rascunhos/ · _propostas-source/ · _logs/)
```

## Regras de ouro
1. A IA só edita o `SOURCE/` em **PLANEJAMENTO**; em EXECUÇÃO ela **propõe** em `_propostas-source/`.
2. Todo artefato tem **cabeçalho de rastreabilidade** e um `status`.
3. Só **pessoas** aprovam, e só pessoas trocam o modo.

## Documentação
- 👉 [`GUIA-DA-ARQUITETURA-SAAS.md`](GUIA-DA-ARQUITETURA-SAAS.md) (manual completo + tabela de prompts)
- 👉 [`PROMPTS-PLANEJAMENTO.md`](PROMPTS-PLANEJAMENTO.md)
