# 🏭 ai-template-factory

Repositório de **manutenção** que gera os três templates da organização:

| Template | Para |
|---|---|
| `ai-project-template` | automações, agentes de IA, cowork e ferramentas internas |
| `ai-saas-template` | produtos SaaS |
| `ai-game-template` | jogos |

Cada template sai com `STARTUP.md` (Startup building), `niveis/simples.zip`, `medio.zip`, `complexo.zip` e `tools/startup.py`.

## Estrutura
```
ai-template-factory/
├── build.py                 → gera dist/ (rode: python build.py)
├── config/<repo>.json       → níveis, pontuação, perguntas, prefixos, prompts, pré-preenchimento
├── bases/<repo>/            → estrutura COMPLETA de cada template (todos os arquivos, nível COMPLEXO + opcionais)
├── comum/                   → startup.py, nivel.py e workflow usados pelos três
├── .github/workflows/       → build + checagem dos pacotes a cada PR
└── dist/                    → saída (não edite; fora do Git): uma pasta por template
```

## Como mudar um template
1. Edite o arquivo em `bases/<repo>/` (conteúdo) ou `config/<repo>.json` (níveis, perguntas, textos).
2. Rode `python build.py`.
3. Rode `python dist/<repo>/tools/startup.py checar` (o CI faz isso).
4. Copie o conteúdo de `dist/<repo>/` para o repositório do template no GitHub e faça commit.

## Regras
- Um arquivo novo no SOURCE precisa entrar em `bases/` **e** no nível certo em `config/` (senão o build falha ou o arquivo não entra em nenhum pacote).
- Arquivo com linha no mapa do `contexto-master.md` some do mapa automaticamente nos níveis que não o têm.
- Os zips são determinísticos: mesmo conteúdo gera o mesmo zip.
