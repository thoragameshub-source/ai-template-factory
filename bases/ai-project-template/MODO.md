---
modo: PLANEJAMENTO          # PLANEJAMENTO | EXECUCAO  ← SÓ HUMANOS ALTERAM ESTA LINHA
nivel: COMPLEXO           # SIMPLES | MEDIO | COMPLEXO  (definido no startup; veja NIVEIS.md)
projeto: A_DEFINIR         # nome da pasta/repositório (NOMENCLATURA.md)
tipo: projeto-ia
versao_do_source: 0.1
alterado_em: AAAA-MM-DD
alterado_por: <nome>
---

# 🚦 MODO DO PROJETO

**Modo atual: `PLANEJAMENTO`** (veja a linha `modo:` acima; ela manda mais que este texto)

> ⚠️ Se `modo:` estiver ausente, vazio ou inválido, o agente deve agir como em **EXECUCAO** (modo mais restritivo).

## 1. Permissões por modo

| Ação | 📝 PLANEJAMENTO | ⚙️ EXECUÇÃO |
|---|---|---|
| Editar arquivos de `SOURCE/` | ✅ somente por prompt direto do usuário, um arquivo por vez | ⛔ proibido |
| Gerar entregas finais em `ARTEFATO/` | ⛔ proibido (apenas `_rascunhos/` e relatórios) | ✅ permitido |
| Propor mudança no SOURCE | opcional (pode editar direto) | ✅ **único** canal: `ARTEFATO/_propostas-source/` |
| Editar `MODO.md`, `AGENTS.md`, `CLAUDE.md`, `niveis.json`, `tools/`, `.gitignore` | ⛔ nunca | ⛔ nunca |
| Alterar o valor de `modo:` | ⛔ nunca (só humano) | ⛔ nunca (só humano) |
| Onde registrar o que fez | `ARTEFATO/_logs/changelog-source.md` | `ARTEFATO/_logs/changelog-ia.md` |

> 🎚️ **Nível:** o campo `nivel:` define quantos arquivos o SOURCE tem (ver `NIVEIS.md`). No nível **SIMPLES** o congelamento formal (checklist e tag) é opcional. As permissões acima valem em **todos** os níveis.

> 🚀 **Origem:** o projeto nasceu do *Startup building*. A passagem STARTUP → PLANEJAMENTO foi feita por `tools/startup.py` depois da **aprovação humana do diagnóstico** (registro em `ARTEFATO/_logs/diagnostico-startup.md`). A partir daí, só humanos mudam o `modo:`.

## 2. Regras do modo PLANEJAMENTO
1. Edite **somente** o arquivo indicado no prompt; outros arquivos só se o usuário pedir.
2. Mantenha a estrutura do template; troque os exemplos pelos dados do usuário.
3. **Não invente**: o que faltar vira `a confirmar`.
4. Não implemente nada: planejamento produz o SOURCE, não as entregas.
5. Registre cada edição em `ARTEFATO/_logs/changelog-source.md`.
6. Prompts prontos: tabela no guia (`GUIA-DA-ARQUITETURA*.md`) e em `PROMPTS-PLANEJAMENTO.md`.

## 3. Regras do modo EXECUÇÃO
1. **Nunca** edite nada em `SOURCE/` (inclusive para "corrigir um errinho").
2. Se achar erro, lacuna ou conflito: pare a parte afetada, crie uma proposta em `ARTEFATO/_propostas-source/` e siga com o que não depende dela.
3. Gere em `_rascunhos/`, revise com a skill `revisar-entrega`, depois mova e registre em `changelog-ia.md`.
4. Só humanos marcam `status: aprovado`.

## 4. Como passar de PLANEJAMENTO para EXECUÇÃO (feito por humano)

**Checklist de congelamento**
- [ ] `contexto-master.md` sem placeholders e com mapa igual aos arquivos existentes
- [ ] Nenhum `<placeholder>` restante nos arquivos mantidos
- [ ] Núcleo preenchido; módulos não usados apagados
- [ ] Itens `a confirmar` resolvidos ou aceitos conscientemente
- [ ] Relatório de consistência (prompt **PC**) sem pendências críticas
- [ ] Dono do projeto aprovou o SOURCE
- [ ] Commit "congelar SOURCE" + tag `source-v1.0`
- [ ] Alterar `modo:` para `EXECUCAO` e registrar na tabela abaixo

## 5. Como voltar para PLANEJAMENTO (feito por humano)
1. Revise as propostas em `ARTEFATO/_propostas-source/` e decida o que entra.
2. Altere `modo:` para `PLANEJAMENTO` e registre o motivo abaixo.
3. Edite os arquivos necessários (prompt **PV**), incremente `versao_do_source` e crie nova tag.
4. Repita o checklist de congelamento e volte para EXECUCAO.

## 6. Reforço técnico opcional
Em `.claude/exemplos/` há configurações de exemplo que **bloqueiam edição de SOURCE** no Claude Code quando em EXECUCAO. Valide a sintaxe na documentação da ferramenta. É um reforço, não uma garantia: a regra principal continua sendo este arquivo + revisão humana (ex.: proteger a pasta `SOURCE/` na branch principal).

## 7. Histórico de modo
| Data | De → Para | Versão do SOURCE | Motivo | Responsável |
|---|---|---|---|---|
| AAAA-MM-DD | (início) → PLANEJAMENTO | 0.1 | Criação do projeto | <nome> |
