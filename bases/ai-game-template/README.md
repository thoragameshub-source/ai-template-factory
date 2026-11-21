# 🎮 <Nome do Jogo>

> <Uma frase: gênero, plataforma e fantasia do jogador.>

## Como abrir e rodar
| Item | Valor |
|---|---|
| Engine e versão | <ex.: Godot 4.3> |
| Abrir o projeto | <ex.: abrir `ARTEFATO/jogo/project.godot`> |
| Rodar | <ex.: F5> |
| Controles | <ex.: WASD mover, Espaço pulso de luz> |
| Estado da build | ver `ARTEFATO/_logs/estado-da-build.md` |
| Bugs conhecidos | ver `ARTEFATO/_logs/bugs-conhecidos.md` |

## O que é este repositório
Template **SOURCE / ARTEFATO para criação de jogos com IA**, com **dois modos**:

| Modo | O que acontece |
|---|---|
| 📝 **PLANEJAMENTO** | Você constrói o `SOURCE/` e a IA **edita os arquivos** por prompts diretos (tabela no guia) |
| ⚙️ **EXECUÇÃO** | O `SOURCE/` fica **congelado**; a IA produz o `ARTEFATO/` e só **propõe** mudanças |

O modo está em [`MODO.md`](MODO.md) e **só humanos o alteram**.

## Começar em 7 passos
1. Confirme `MODO.md` em `PLANEJAMENTO`.
2. Abra a sessão com o prompt **P0** e gere os arquivos do SOURCE na ordem da tabela (`PROMPTS-PLANEJAMENTO.md`).
3. Escolha o perfil (Vibe/Jam ~12 arquivos, ou Produção) e apague os módulos que não usa.
4. Crie o projeto da engine **em `ARTEFATO/jogo/`** e rode `git lfs install`.
5. Rode **PC** e **PG**, congele (commit + tag `source-v1.0`) e mude `MODO.md` para `EXECUCAO`.
6. Peça features à IA (skills: greybox, implementar-feature, juice, bugfix).
7. Faça playtest, registre em `ARTEFATO/playtests/` e aprove.

## Nível do projeto
O nível foi definido no *Startup building* e está no `MODO.md` (`nivel:`). Arquivos de cada nível, pontuação e promoção: [`NIVEIS.md`](NIVEIS.md). Nomes de repositórios, branches e commits: [`NOMENCLATURA.md`](NOMENCLATURA.md). Pendências do startup: `ARTEFATO/_logs/pendencias-startup.md`.

## Estrutura
```
🎮 raiz-do-jogo/
├── 📄 README.md                      → porta de entrada para humanos
├── 📄 AGENTS.md · CLAUDE.md          → ponteiros para agentes de IA
├── 📄 GUIA-DA-ARQUITETURA-GAMES.md   → manual completo + tabela de prompts
├── 🚦 MODO.md                        → PLANEJAMENTO ou EXECUÇÃO (só humanos alteram)
├── 📄 PROMPTS-PLANEJAMENTO.md        → prompts diretos para gerar cada arquivo do SOURCE
├── 📄 NIVEIS.md                  → nível do projeto (simples/médio/complexo), checklist e arquivos por nível
├── 📄 NOMENCLATURA.md            → nomes de repositórios, branches, commits e tags
├── 📄 niveis.json · 📁 tools/    → arquivos por nível e ferramenta nivel.py (humanos)
├── 📁 .github/workflows/         → verificação automática do template
├── 📄 .gitignore · .gitattributes    → ignora builds; Git LFS para assets
├── 📁 .claude/                       → (opcional) adaptador do Claude Code
│
├── 📁 SOURCE/                        → 🔒 FONTE DE VERDADE (humano edita, agente lê)
│   ├── 📄 contexto-master.md
│   ├── 📁 00-conceito/               game-concept · pilares-e-experiencia · publico-e-mercado
│   ├── 📁 01-design/                 core-loop · mecanicas · progressao-e-economia ·
│   │                                 niveis-e-mundo · narrativa-e-personagens · controles-e-ux
│   ├── 📁 02-direcao-arte-audio/     art-bible · direcao-de-audio · ui-style-guide · convencoes-de-assets
│   ├── 📁 03-tecnico/                engine-e-stack · arquitetura-de-codigo · mapa-cenas-nodos · contrato-de-eventos ·
│   │                                 performance-e-plataformas ·
│   │                                 pipeline-de-build · multiplayer-e-rede
│   ├── 📁 04-dados-de-design/        entidades.json · habilidades.csv · inimigos.csv  (números do jogo)
│   ├── 📁 05-agentes/                guardrails · papeis-e-fluxo · skills/ (prototipar-greybox · juice-e-feel · corrigir-bug ...)
│   ├── 📁 06-qualidade/              definicao-de-pronto · playtest-e-balanceamento · checklist-revisao
│   ├── 📁 07-producao/               escopo-mvp · roadmap-e-marcos
│   ├── 📁 08-referencias/            jogos-referencia · exemplos-de-saida/ · templates/
│   └── 📁 09-decisoes/               ADR-000-modelo · ADR-001-exemplo
│
└── 📁 ARTEFATO/                      → ✍️ SAÍDA (agente escreve, humano aprova)
    ├── 📁 design/      📁 jogo/ (raiz do projeto da engine)    📁 arte/ (+ manifesto)
    ├── 📁 audio/       📁 niveis/      📁 automacoes/           📁 playtests/
    ├── 📁 builds/ (fora do Git)
    └── 📁 _rascunhos/  📁 _propostas-source/  📁 _logs/ (changelogs · estado-da-build · bugs-conhecidos)
```

## Regras de ouro
1. A IA só edita o `SOURCE/` em **PLANEJAMENTO**; em EXECUÇÃO ela **propõe** (inclusive balanceamento).
2. **Nenhum número de balanceamento no código**; tudo vem de `04-dados-de-design/`.
3. **Todo asset tem origem e licença** no `manifesto-de-assets.csv`.
4. A build **sempre roda**; mudanças pequenas; comunicação só por eventos.
5. Só **pessoas** aprovam e trocam o modo.

## Documentação
- 👉 [`GUIA-DA-ARQUITETURA-GAMES.md`](GUIA-DA-ARQUITETURA-GAMES.md) (manual + tabela de prompts)
- 👉 [`PROMPTS-PLANEJAMENTO.md`](PROMPTS-PLANEJAMENTO.md)
