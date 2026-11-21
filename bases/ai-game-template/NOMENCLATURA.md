# 🏷️ Nomenclatura

Regra geral: **minúsculo, hífen, sem acento e sem espaço**, até 40 caracteres. A pasta local e o repositório no GitHub têm **o mesmo nome**.

## 1. Repositórios

| Tipo | Padrão | Exemplo |
|---|---|---|
| Templates | `ai-project-template` · `ai-saas-template` · `ai-game-template` | — |
| Fábrica dos templates (manutenção) | `ai-template-factory` | — |
| Projeto criado a partir do template | `<prefixo>-<nome-curto>` | `game-farol-perdido`, `jam-luz-e-sombra` |

Prefixos deste template: `game-` (jogo), `jam-` (game jam ou protótipo).

- O nome é definido no **Startup building** e aplicado à pasta local; o repositório é criado no GitHub **depois**, já em PLANEJAMENTO.
- Projetos começam **privados**. Tópicos sugeridos: `vibe-coding`, `source-artefato`, `jogo`.

## 2. Branches

| Uso | Padrão | Exemplo |
|---|---|---|
| Edição do SOURCE (PLANEJAMENTO) | `plan/<assunto>` | `plan/regras-de-negocio` |
| Nova entrega (EXECUÇÃO) | `feat/<assunto>` | `feat/exportar-relatorio` |
| Correção | `fix/<assunto>` | `fix/calculo-retencao` |
| Congelamento do SOURCE | `freeze/source-vX.Y` | `freeze/source-v1.0` |

## 3. Commits (Conventional Commits com escopo)

`<tipo>(<escopo>): <resumo>` — tipos: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.

| Escopo | Quando | Exemplo |
|---|---|---|
| `startup` | criação do projeto | `chore(startup): estrutura MEDIO aplicada` |
| `source` | mudança no SOURCE | `docs(source): preencher glossario` |
| `artefato` | entrega gerada | `feat(artefato): relatorio de divergencias` |
| `modo` | troca de modo ou nível | `chore(modo): congelar SOURCE v1.0` |

## 4. Tags

| Tag | Significado |
|---|---|
| `template-original` | estado do template antes do startup |
| `source-vX.Y` | SOURCE congelado |
| `vX.Y.Z` | versão do produto (`0.x` = protótipo/MVP) |

## 5. Labels

`modo:planejamento` · `modo:execucao` · `nivel:simples` · `nivel:medio` · `nivel:complexo` · `proposta-source` · `bug` · `feature`

## 6. Arquivos de entrega (ARTEFATO)

`AAAA-MM-DD_tipo_nome.ext` — ex.: `2026-11-21_relatorio_divergencias.md`.
