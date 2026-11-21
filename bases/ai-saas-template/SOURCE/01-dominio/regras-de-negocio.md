---
quando_ler: aplicar cálculo, regra ou restrição do negócio
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# ⚙️ Regras de Negócio

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Modelo de cada regra
```
RN-XX — <Nome>
Quando: <condição>
Então: <resultado>
Exceção: <quando não se aplica>
Fonte: <norma/documento/pessoa que valida>
```

## Regras
### RN-01 — <Nome da regra>
- **Quando:** <condição>
- **Então:** <resultado>
- **Exceção:** <se houver>
- **Fonte:** <onde está a base>

### RN-02 — Exemplo: Divergência de valor
- **Quando:** valor da nota ≠ valor do contrato com diferença acima de R$ 0,01
- **Então:** marcar como "divergente" e listar na aba de revisão
- **Exceção:** notas de reembolso
- **Fonte:** Política interna de contas a pagar v3

## Cálculos
| Nome | Fórmula | Exemplo numérico |
|---|---|---|
| <Cálculo> | <Fórmula> | <Entrada → saída> |
| **Exemplo:** Valor líquido | bruto − retenções | 1.000 − 100 = 900 |
