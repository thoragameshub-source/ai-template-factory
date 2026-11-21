---
quando_ler: entender por que a extração usa leitura de PDF com texto
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧭 ADR-001 — Exemplo: Extração via PDF com texto (sem OCR)

- **Status:** Aceita
- **Data:** 2026-11-01
- **Decisores:** Líder da área, Responsável técnico

## Contexto
95% das notas chegam em PDF com texto selecionável; OCR aumentaria custo e erro.

## Decisão
Extrair texto direto do PDF; arquivos sem texto vão para fila manual.

## Alternativas consideradas
| Opção | Prós | Contras |
|---|---|---|
| Texto do PDF | Simples, preciso | Não lê imagens |
| OCR em tudo | Cobre 100% | Lento e menos preciso |

## Consequências
- Positivas: rápido e barato.
- Negativas/riscos: ~5% das notas exigem tratamento manual.
