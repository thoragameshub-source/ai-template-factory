---
quando_ler: criar ou alterar endpoint, webhook ou integração pública
modulo: codigo   # nucleo | saas | codigo | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🔌 Contratos de API

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Padrões
- Estilo: <REST / GraphQL / tRPC> · Base: `/api/v1` · Formato: JSON
- Autenticação: <ex.: sessão para o app; token por tenant para API pública>
- Erros: `{ "erro": { "codigo": "NOTA_INVALIDA", "mensagem": "..." } }` com status HTTP correto
- Paginação: <ex.: cursor, `limite` máx. 100>
- Versionamento: mudança incompatível = nova versão; nunca quebrar `v1` em uso

## Endpoints
| Método | Rota | Quem pode | Entrada | Saída | Observações |
|---|---|---|---|---|---|
| <método> | <rota> | <papel> | <campos> | <campos> | |
| **Exemplo:** POST | `/api/v1/notas` | membro | arquivo XML | `{id, status}` | Assíncrono; status via webhook |

## Webhooks (enviados e recebidos)
| Evento | Direção | Payload | Assinatura/validação | Reenvio |
|---|---|---|---|---|
| <evento> | <entra/sai> | <campos> | <HMAC?> | <política> |
