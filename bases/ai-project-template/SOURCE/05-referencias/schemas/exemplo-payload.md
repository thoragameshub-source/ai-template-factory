---
quando_ler: precisar do formato de dados de entrada/saída
modulo: codigo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🧩 Schemas e Payloads de Exemplo

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Estrutura de cada item
- **Nome:** <ex.: nota_extraida>
- **Origem/Destino:** <de onde vem / para onde vai>
- **Campos obrigatórios:** <lista>

## Exemplo JSON
```json
{
  "numero_nota": "1021",
  "data_emissao": "2026-10-15",
  "cnpj_prestador": "00.000.000/0001-00",
  "valor_bruto": 1500.00,
  "retencoes": 150.00,
  "status": "a_confirmar"
}
```

## Exemplo CSV
```csv
numero_nota,data_emissao,valor_bruto
1021,2026-10-15,1500.00
```
> Use dados **fictícios ou mascarados**.
