---
quando_ler: criar um prompt reutilizável para uma tarefa
modulo: nucleo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 💬 Template de Prompt

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

```
PAPEL: <quem o agente é nesta tarefa>
OBJETIVO: <resultado desejado em 1 frase>
CONTEXTO: leia SOURCE/contexto-master.md e <arquivos específicos>
ENTRADA: <o que está sendo fornecido>
REGRAS: <restrições; ex.: não inventar dados>
FORMATO DE SAÍDA: <tabela/markdown/json> em ARTEFATO/<pasta>/
CRITÉRIO DE PRONTO: <como saber que terminou>
```

**Exemplo preenchido:**
```
PAPEL: Analista Fiscal assistente
OBJETIVO: Conferir as notas de outubro e listar divergências
CONTEXTO: leia SOURCE/contexto-master.md e 01-dominio/regras-de-negocio.md
ENTRADA: 412 PDFs em /entrada
REGRAS: não inventar valores; dúvida = "a confirmar"
FORMATO DE SAÍDA: tabela markdown em ARTEFATO/documentos/
CRITÉRIO DE PRONTO: passa no checklist-revisao.md
```
