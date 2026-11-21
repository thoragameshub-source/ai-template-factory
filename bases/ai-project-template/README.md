# 🚀 <Nome do Projeto>

> <Uma frase: o que é e para quem.>

## O que é este repositório
Template **SOURCE / ARTEFATO** para projetos com IA (Claude, GPT, Cursor, Copilot etc.), com **dois modos**:

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
📦 raiz-do-projeto/
├── 📄 README.md                  → porta de entrada para humanos
├── 📄 AGENTS.md                  → ponteiro universal para agentes de IA
├── 📄 CLAUDE.md                  → ponteiro para o Claude Code
├── 📄 GUIA-DA-ARQUITETURA.md     → manual completo + tabela de prompts
├── 🚦 MODO.md                    → PLANEJAMENTO ou EXECUÇÃO (só humanos alteram)
├── 📄 PROMPTS-PLANEJAMENTO.md    → prompts diretos para gerar cada arquivo do SOURCE
├── 📄 NIVEIS.md                  → nível do projeto (simples/médio/complexo), checklist e arquivos por nível
├── 📄 NOMENCLATURA.md            → nomes de repositórios, branches, commits e tags
├── 📄 niveis.json · 📁 tools/    → arquivos por nível e ferramenta nivel.py (humanos)
├── 📁 .github/workflows/         → verificação automática do template
├── 📁 .claude/                   → (opcional) adaptador nativo do Claude
│
├── 📁 SOURCE/                    → 🔒 FONTE DE VERDADE (humano edita, agente lê)
│   ├── 📄 contexto-master.md
│   ├── 📁 00-produto/            visao-e-escopo.md · requisitos.md
│   ├── 📁 01-dominio/            glossario.md · regras-de-negocio.md · fontes-de-verdade.md
│   ├── 📁 02-tecnico/            stack.md · arquitetura.md · convencoes.md
│   ├── 📁 03-agentes/            guardrails.md · papeis-e-fluxo.md · skills/
│   ├── 📁 04-qualidade/          definicao-de-pronto.md · checklist-revisao.md
│   ├── 📁 05-referencias/        exemplos-de-saida/ · schemas/ · templates/
│   └── 📁 06-decisoes/           ADR-000-modelo.md · ADR-001-exemplo.md
│
└── 📁 ARTEFATO/                  → ✍️ SAÍDA (agente escreve, humano aprova)
    ├── 📁 documentos/   📁 codigo/   📁 automacoes/
    ├── 📁 _rascunhos/   📁 _propostas-source/   📁 _logs/
```

## Regras de ouro
1. A IA só edita o `SOURCE/` em **PLANEJAMENTO**; em EXECUÇÃO ela **propõe** em `_propostas-source/`.
2. Todo artefato tem **cabeçalho de rastreabilidade** e um `status`.
3. Só **pessoas** aprovam, e só pessoas trocam o modo.

## Documentação
- 👉 [`GUIA-DA-ARQUITETURA.md`](GUIA-DA-ARQUITETURA.md) (manual completo + tabela de prompts)
- 👉 [`PROMPTS-PLANEJAMENTO.md`](PROMPTS-PLANEJAMENTO.md)
