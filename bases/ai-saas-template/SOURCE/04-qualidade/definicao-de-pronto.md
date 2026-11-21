---
quando_ler: for declarar uma entrega como concluída
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# ✅ Definição de Pronto

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

Uma entrega só está **pronta para revisão humana** quando:

- [ ] Atende ao requisito indicado (ID: `RF-xx`)
- [ ] Segue `02-tecnico/convencoes.md`
- [ ] Todos os números/normas têm fonte
- [ ] Possui cabeçalho de rastreabilidade completo
- [ ] Passou pela skill `revisar-entrega`
- [ ] Registrada em `ARTEFATO/_logs/changelog-ia.md`
- [ ] <Critério específico do projeto>

**Exemplo específico:** planilha abre sem erro e as fórmulas não têm `#REF!`.

## Estados de um artefato
| Status | Significado | Quem muda |
|---|---|---|
| `rascunho` | Em construção | Agente |
| `revisado` | Passou pelo checklist | Agente revisor |
| `aprovado` | Validado por pessoa | **Humano** |
