---
quando_ler: for nomear, formatar, testar ou tratar erros
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 📏 Convenções

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Nomenclatura
| Item | Padrão | Exemplo |
|---|---|---|
| Arquivos | minúsculo-com-hifen | `extrai-nota.py` |
| Pastas | minúsculo, sem acento | `automacoes` |
| Variáveis | <padrão> | `valor_liquido` |
| Documentos entregues | `AAAA-MM-DD_tipo_nome.md` | `2026-11-21_relatorio_divergencias.md` |

## Estilo e formatação
- <Linter/formatter, tamanho de linha, idioma dos comentários...>

## Tratamento de erros
- <Regra: nunca engolir exceção; logar contexto; mensagem amigável ao usuário.>

## Testes
- <O que deve ter teste, cobertura mínima, onde ficam.>
- **Exemplo:** Toda regra de negócio (RN-xx) tem ao menos 1 teste nomeado com o ID.

## Git (se aplicável)
- Branches: `feat/...`, `fix/...`
- Commits: <padrão, ex.: Conventional Commits>

## Idioma
- Documentos e comentários: <pt-BR>; nomes de código: <inglês/português>.
