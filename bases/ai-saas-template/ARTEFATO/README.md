# ✍️ ARTEFATO — Zona de saída

Tudo que os agentes produzem mora aqui. **Humanos revisam e aprovam.**

## Subpastas
| Pasta | O que vai aqui |
|---|---|
| `documentos/` | Relatórios, planos, specs, textos finais |
| `codigo/` | Aplicações, scripts, testes |
| `automacoes/` | Fluxos, integrações, rotinas |
| `_rascunhos/` | Qualquer coisa ainda não revisada |
| `_propostas-source/` | Sugestões de mudança no SOURCE |
| `_logs/` | `changelog-source` (planejamento) e `changelog-ia` (execução) |

## Cabeçalho obrigatório (rastreabilidade)
```yaml
---
gerado_por: <agente/ferramenta>
fontes: [SOURCE/<caminho>.md]
data: AAAA-MM-DD
status: rascunho        # rascunho | revisado | aprovado
---
```

## Ciclo de vida
`_rascunhos/` → revisão (`revisar-entrega`) → pasta final → **aprovação humana** (`status: aprovado`)

## Nome dos arquivos
`AAAA-MM-DD_tipo_nome.ext` — ex.: `2026-11-21_relatorio_divergencias.md`
