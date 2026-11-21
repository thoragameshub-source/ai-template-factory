# ✍️ ARTEFATO — Zona de saída

Tudo que os agentes produzem mora aqui. **Humanos revisam e aprovam.**

## Subpastas
| Pasta | O que vai aqui |
|---|---|
| `design/` | Specs de feature, GDDs parciais, textos de narrativa |
| `jogo/` | **Projeto da engine** (cenas, scripts, assets importados) |
| `arte/` | Briefs, conceitos, sprites exportados + `manifesto-de-assets.csv` |
| `audio/` | Briefs, músicas e SFX |
| `niveis/` | Layouts e documentos de fases |
| `automacoes/` | Ferramentas e scripts de pipeline (conversores, geradores) |
| `playtests/` | Relatórios de testes com jogadores |
| `builds/` | Builds exportados (**fora do Git**) |
| `_rascunhos/` | Não revisado — nada aqui é aprovado |
| `_propostas-source/` | Sugestões de mudança no SOURCE |
| `_logs/` | `changelog-source`, `changelog-ia`, `estado-da-build`, `bugs-conhecidos` |

## Cabeçalho de rastreabilidade (arquivos `.md`)
```yaml
---
gerado_por: <agente/ferramenta>
fontes: [SOURCE/<caminho>.md]
data: AAAA-MM-DD
status: rascunho        # rascunho | revisado | aprovado
---
```

## Para assets binários (imagens, áudio, modelos)
Não dá para ter cabeçalho dentro do arquivo: registre em `arte/manifesto-de-assets.csv`.

## Ciclo de vida
`_rascunhos/` → `revisar-entrega` → pasta final → **aprovação humana**

## Nomes
Documentos: `AAAA-MM-DD_tipo_nome.md`. Assets: ver `SOURCE/02-direcao-arte-audio/convencoes-de-assets.md`.
