# 🎨 arte

Briefs, conceitos e artes exportadas.

## Manifesto de assets (obrigatório)
Todo asset (arte, áudio, fonte, modelo) deve ter uma linha em `manifesto-de-assets.csv`:

| Coluna | Significado |
|---|---|
| `id` | nome do asset conforme convenção |
| `arquivo` | caminho dentro do projeto |
| `origem` | humano / ia / loja / tutorial / domínio-publico |
| `ferramenta_ou_fonte` | ex.: Aseprite, ferramenta de IA, URL da loja |
| `prompt_ou_referencia` | prompt usado ou referência (nunca obra protegida) |
| `licenca` | ex.: própria, CC0, CC-BY, comercial-loja |
| `uso_comercial` | sim / não / verificar |
| `status` | rascunho / revisado / aprovado |

> Antes do lançamento, filtre `uso_comercial != sim` e `origem = ia` para revisão de direitos.
