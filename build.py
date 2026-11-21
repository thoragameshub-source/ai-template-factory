#!/usr/bin/env python3
"""ai-template-factory: gera os templates (genérico, games, SaaS) com os pacotes por nível.

Uso:  python build.py            # gera dist/<repo>/ e dist/<repo>-v4.zip para cada config/*.json
Edite só bases/<repo>/ (estrutura completa) e config/<repo>.json (níveis, pontuação, textos).
Nunca edite dist/ à mão: rode o build de novo.
"""
import glob
import json
import os
import re
import shutil
import sys
import zipfile

F = os.path.dirname(os.path.abspath(__file__))
NIVEIS = ["SIMPLES", "MEDIO", "COMPLEXO"]
ROT = {"SIMPLES": "🟢 SIMPLES", "MEDIO": "🟡 MÉDIO", "COMPLEXO": "🔴 COMPLEXO"}
VERSAO = "4.0"
DATA_FIXA = (2026, 1, 1, 0, 0, 0)


# ------------------------------------------------------------------ util
def ler(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def gravar(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(t.rstrip("\n") + "\n")


def zipar(origem, destino):
    """zip determinístico (ordem e datas fixas), conteúdo na raiz do zip."""
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    arquivos = []
    for d, dirs, fs in os.walk(origem):
        dirs.sort()
        for f in sorted(fs):
            arquivos.append(os.path.join(d, f))
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for a in arquivos:
            rel = os.path.relpath(a, origem).replace(os.sep, "/")
            info = zipfile.ZipInfo(rel, DATA_FIXA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(a, "rb") as fh:
                z.writestr(info, fh.read())


def acumulado(cfg):
    """níveis cumulativos: MEDIO herda SIMPLES etc."""
    out, base = {}, []
    for n in NIVEIS:
        d = cfg["niveis"][n]
        base = base + [x for x in d["adiciona"] if x not in base]
        out[n] = {"obrigatorios": list(base), "opcionais": list(d.get("opcionais", []))}
    return out


def niveis_json(cfg):
    return {
        "tipo": cfg["tipo"], "repo": cfg["repo"], "versao_template": VERSAO,
        "niveis": acumulado(cfg),
        "limite_linhas_contexto_master": cfg["limite_linhas_contexto_master"],
        "ignorar_placeholders": cfg["ignorar_placeholders"],
        "pontuacao": cfg["pontuacao"],
        "prefixos": cfg["prefixos"],
    }


def curto(path):
    return path.replace("SOURCE/", "", 1)


# ------------------------------------------------------------------ textos
def tabela_perguntas(cfg):
    rows = ["| # | Pergunta | 0 ponto | 1 ponto | 2 pontos |", "|---|---|---|---|---|"]
    for i, q in enumerate(cfg["pontuacao"]["perguntas"], 1):
        rows.append(f"| {i} | **{q['tema']}** | {q['opcoes'][0]} | {q['opcoes'][1]} | {q['opcoes'][2]} |")
    return "\n".join(rows)


def regras_pontuacao(cfg):
    pt = cfg["pontuacao"]
    fx = pt["faixas"]
    linhas = [f"| {a} a {b} | {ROT[n]} |" for n, (a, b) in fx.items()]
    pisos = [f"- Pergunta {x['pergunta']} com resposta **{x['a_partir_de']}{' ou mais' if x['a_partir_de'] < 2 else ''}**: no mínimo **{x['minimo']}** ({x['motivo']})."
             for x in pt["pisos"]]
    return ("| Pontos | Nível |\n|---|---|\n" + "\n".join(linhas) + "\n\n**Ajustes obrigatórios**\n\n" + "\n".join(pisos) +
            f"\n- Três ou mais respostas **2**: **COMPLEXO**.\n- Na dúvida entre dois níveis, fique no **menor** e promova depois (é barato; o inverso gera retrabalho).")


def matriz(niv):
    todos = sorted({x for n in NIVEIS for x in niv[n]["obrigatorios"] + niv[n]["opcionais"]})
    rows = ["| Arquivo | 🟢 Simples | 🟡 Médio | 🔴 Complexo |", "|---|:-:|:-:|:-:|"]
    for x in todos:
        m = ["✅" if x in niv[n]["obrigatorios"] else ("➖" if x in niv[n]["opcionais"] else "—") for n in NIVEIS]
        rows.append(f"| `{curto(x)}` | {' | '.join(m)} |")
    return "\n".join(rows)


def manifesto(niv):
    """lista compacta por pasta, em deltas, para o STARTUP.md."""
    def agrupar(lista):
        g = {}
        for x in lista:
            c = curto(x)
            pasta, _, arq = c.rpartition("/")
            g.setdefault(pasta or "(raiz)", []).append(arq)
        return "\n".join(f"  - `{k}/`: " + ", ".join(f"`{v}`" for v in vs) if k != "(raiz)" else "  - " + ", ".join(f"`{v}`" for v in vs)
                         for k, vs in g.items())
    out, ant = [], []
    for n in NIVEIS:
        novos = [x for x in niv[n]["obrigatorios"] if x not in ant]
        cab = f"**{ROT[n]}** — {len(niv[n]['obrigatorios'])} obrigatórios" + ("" if n == "SIMPLES" else f" (= nível anterior +)")
        out.append(cab + "\n" + agrupar(novos))
        if niv[n]["opcionais"]:
            out.append(f"  - *opcionais (vêm no pacote; o diagnóstico decide se ficam):* " + ", ".join(f"`{curto(x)}`" for x in niv[n]["opcionais"]))
        ant = niv[n]["obrigatorios"]
    return "\n\n".join(out)


def prompt_arquivo(path, inputs, instr):
    dados = "; ".join("[[" + i + "]]" for i in inputs)
    return (f"Modo PLANEJAMENTO: edite {path}. Dados: {dados}. {instr} Siga o template do arquivo, troque os exemplos pelos meus dados, "
            f"não invente (use 'a confirmar') e registre no ARTEFATO/_logs/changelog-source.md.")


def prompt_unico(cfg, niv):
    arqs = ", ".join(curto(x) for x in niv["SIMPLES"]["obrigatorios"])
    lim = cfg["limite_linhas_contexto_master"]["SIMPLES"]
    return (f"Modo PLANEJAMENTO, nível SIMPLES. O startup já pré-preencheu parte do SOURCE. Complete somente estes arquivos do SOURCE: {arqs}. "
            f"Dados: {cfg['unico_dados']}. Siga o template de cada arquivo, não invente (use 'a confirmar'), mantenha o contexto-master em até "
            f"{lim} linhas, atualize ARTEFATO/_logs/pendencias-startup.md e registre tudo em ARTEFATO/_logs/changelog-source.md.")


def controles(cfg):
    return f"""| Momento | Prompt direto |
|---|---|
| **P0 — Abrir sessão de planejamento** | Leia MODO.md e AGENTS.md. Confirme em uma linha o modo e o nível. Liste os arquivos do SOURCE que ainda têm placeholders <...> e as pendências de ARTEFATO/_logs/pendencias-startup.md. Não edite nada até eu indicar o arquivo. |
| **PC — Checar consistência** | Modo PLANEJAMENTO. Leia todo o SOURCE e escreva em ARTEFATO/_rascunhos/relatorio-consistencia.md: contradições entre arquivos, lacunas, termos fora do glossário e números duplicados. Não edite o SOURCE. |
| **PG — Gate de congelamento** | Aplique o checklist de congelamento de MODO.md ({cfg['gate_extra']}) e responda se o SOURCE está pronto para EXECUÇÃO, listando pendências. Não altere o MODO.md. |
| **PE — Abrir sessão de execução** | Leia MODO.md e AGENTS.md. Confirme que o modo é EXECUCAO. Não edite nada em SOURCE. Se encontrar erro ou lacuna, crie uma proposta em ARTEFATO/_propostas-source/. Tarefa: [[tarefa]]. |
| **PV — Voltar ao planejamento** | (Primeiro eu mudo MODO.md para PLANEJAMENTO.) Modo PLANEJAMENTO retomado. Motivo: [[motivo]]. Edite apenas [[arquivo(s)]] com base em [[propostas aceitas / decisão]] e registre no changelog-source. |"""


def prompts_planejamento(cfg, niv, nivel):
    existentes = set(niv[nivel]["obrigatorios"]) | set(niv[nivel]["opcionais"])
    rows = ["| # | Arquivo | Informações cruciais a fornecer | Prompt direto (copie e preencha os [[campos]]) |", "|---|---|---|---|"]
    n = 0
    for path, inputs, instr in cfg["prompts"]:
        if path in existentes:
            n += 1
            rows.append(f"| {n} | `{path}` | {'; '.join(inputs)} | {prompt_arquivo(path, inputs, instr)} |")
    if nivel == "SIMPLES":
        bloco = "### 🟢 Prompt único do nível SIMPLES\nUse este prompt primeiro; a tabela por arquivo serve para refinar um arquivo específico.\n\n> " + prompt_unico(cfg, niv)
    elif nivel == "MEDIO":
        linhas = ["| Pasta | Prompt direto |", "|---|---|"]
        for pasta, arqs, info in cfg["pastas"]:
            linhas.append(f"| `{pasta}` | Modo PLANEJAMENTO, nível MEDIO. Edite em SOURCE/{pasta}/ somente: {arqs}. Dados: {info} [[preencha com seus dados]]. "
                          f"Siga os templates, não invente (use 'a confirmar') e registre em ARTEFATO/_logs/changelog-source.md. |")
        bloco = "### 🟡 Um prompt por pasta (nível MÉDIO)\nExecute na ordem; use a tabela por arquivo para refinar.\n\n" + "\n".join(linhas)
    else:
        bloco = "### 🔴 Nível COMPLEXO\nUse a tabela por arquivo, **na ordem** (ela segue as dependências). Antes de congelar, rode **PC** e **PG**."
    return f"""# 🧩 Prompts de planejamento — nível {ROT[nivel]}

> Gerado para o nível do projeto: só aparecem os arquivos que existem no seu SOURCE. Troque os `[[campos]]` pelos seus dados.
> O startup já pré-preencheu o que você respondeu; comece pelo **P0** para ver o que falta.

## Prompts de controle

{controles(cfg)}

## Planejamento do nível

{bloco}

## Prompts por arquivo

""" + "\n".join(rows) + """

**Como usar bem**
1. Um arquivo (ou uma pasta, no MÉDIO) por vez; revise antes de seguir.
2. Dado que falta vira `a confirmar` e entra em `ARTEFATO/_logs/pendencias-startup.md`.
3. Ao final, reexecute o prompt do `contexto-master.md` para atualizar o mapa.
"""


def niveis_md(cfg, niv):
    c = {n: len(niv[n]["obrigatorios"]) for n in NIVEIS}
    ex = cfg["exemplos"]
    sinais = "\n".join(f"- {s}" for s in cfg["sinais"])
    lim = cfg["limite_linhas_contexto_master"]
    return f"""# 🎚️ Níveis de complexidade — `{cfg['repo']}`

> Objetivo: **agilidade e economia de tokens**. Quanto menos arquivos a IA lê e mantém, menos contexto gasto e menos retrabalho. Cada projeto usa **o menor nível que o protege de erros**. O nível é definido no **Startup building** (veja a seção 4).

## 1. Os três níveis

| | 🟢 SIMPLES | 🟡 MÉDIO | 🔴 COMPLEXO |
|---|---|---|---|
| **Exemplos** | {ex['SIMPLES']} | {ex['MEDIO']} | {ex['COMPLEXO']} |
| **Arquivos obrigatórios no SOURCE** | {c['SIMPLES']} | {c['MEDIO']} | {c['COMPLEXO']} (+ módulos opcionais) |
| **Congelamento do SOURCE** | opcional | por tag | gate completo (PC + PG), revisão humana |
| **Prompts de planejamento** | 1 prompt único | 1 por pasta | 1 por arquivo |
| **Limite do `contexto-master.md`** | {lim['SIMPLES']} linhas | {lim['MEDIO']} linhas | {lim['COMPLEXO']} linhas |

> As permissões do `MODO.md` valem **nos três níveis**: em EXECUÇÃO a IA nunca edita o SOURCE.

## 2. Pontuação (5 perguntas)

Cada resposta vale 0, 1 ou 2 pontos.

{tabela_perguntas(cfg)}

{regras_pontuacao(cfg)}

## 3. Arquivos por nível

✅ obrigatório · ➖ opcional (vem no pacote; mantenha só se usar) · — não existe neste nível

{matriz(niv)}

> Fonte: `niveis.json` (gerado pela factory). Não edite à mão.

## 4. Como o nível é definido

**Automático (recomendado): Startup building.** O template nasce em `modo: STARTUP`. Ao abrir o projeto e digitar `/startup` (Claude Code) ou "startup" (Cowork/outros agentes), o agente faz até 2 rodadas de perguntas, calcula a pontuação com `tools/startup.py pontuar`, mostra o **diagnóstico** para você aprovar, cria a estrutura do nível a partir de `niveis/<nivel>.zip`, pré-preenche o SOURCE, renomeia a pasta e entra em **PLANEJAMENTO**.

**Manual:** baixe `niveis/<nivel>.zip` do repositório do template, descompacte numa pasta com o nome do projeto (`NOMENCLATURA.md`) e preencha `projeto:` no `MODO.md`.

## 5. Prompts por nível
Os prompts do seu nível estão em `PROMPTS-PLANEJAMENTO.md` (gerado só com os arquivos que você tem).

## 6. Promoção de nível

**Quando promover**

{sinais}

**Como promover** (humano roda; baixe `niveis/complexo.zip` do template):
```
python tools/nivel.py promover --nivel MEDIO --origem complexo.zip
python tools/nivel.py promover --nivel MEDIO --origem complexo.zip --aplicar
```
1. O comando copia os arquivos que faltam e atualiza o `nivel:` do `MODO.md`.
2. Volte `modo:` para `PLANEJAMENTO` (registre o motivo no `MODO.md`).
3. Gere só os arquivos novos com os prompts do novo nível e atualize o mapa do `contexto-master.md`.
4. Rode `verificar`, congele de novo e incremente a versão do SOURCE.

## 7. Regras de economia de tokens

1. **Contexto-master curto**: respeite o limite do nível; detalhe vai nos outros arquivos.
2. **Mapa "leia quando..."**: a IA lê só o que a tarefa pede.
3. **Um arquivo por vez** em PLANEJAMENTO (no MÉDIO, uma pasta por vez).
4. **Sem duplicação**: um fato mora em um arquivo; os outros apontam para ele.
5. **Sem arquivo vazio**: módulo opcional que você não usa deve ser apagado, junto com a linha dele no mapa do `contexto-master.md`.
6. **Exemplos reais curtos** valem mais que instruções longas.
7. **Não reexplique o projeto na conversa**: melhore o SOURCE em PLANEJAMENTO e congele.

## 8. Conformidade automática

| Comando | O que faz |
|---|---|
| `python tools/nivel.py verificar` | Confere `modo:` e `nivel:`, arquivos obrigatórios, placeholders `<...>` (erro em EXECUÇÃO, aviso em PLANEJAMENTO) e tamanho do contexto-master |
| `python tools/nivel.py proteger --base origin/main` | Se a base está em EXECUÇÃO, **bloqueia** PRs que alterem `SOURCE/`, `niveis.json` ou `tools/` |

O workflow `.github/workflows/verificar-nivel.yml` roda os dois a cada push e PR. Ative **branch protection** na `main` exigindo esse check.
"""


def startup_md(cfg, niv):
    pt = cfg["pontuacao"]
    blocoC = ["| # | Pergunta | A (0) | B (1) | C (2) |", "|---|---|---|---|---|"]
    for i, q in enumerate(pt["perguntas"], 1):
        blocoC.append(f"| C{i} | {q['tema']} | {q['opcoes'][0]} | {q['opcoes'][1]} | {q['opcoes'][2]} |")
    rota = "\n".join(f"| {k} | `{v}` |" for k, v in cfg["roteamento"].items())
    tecnicas = "\n".join(f"| D{i} | {t} | {o} |" for i, (t, o) in enumerate(cfg["perguntas_tecnicas"], 1))
    extras = "\n".join(f"- {x}" for x in cfg["rodada2_extras"])
    prefill = "\n".join(f"| `{curto(x)}` | {cfg['prefill'][x]} |" for x in cfg["prefill"])
    prefixos = " · ".join(f"`{k}-` ({v})" for k, v in cfg["prefixos"].items())
    return f"""---
tipo_template: {cfg['repo']}
versao_template: {VERSAO}
---

# 🚀 STARTUP — modo "Startup building" · `{cfg['repo']}`

> **Agente:** este é o **único** arquivo que você lê para iniciar o projeto (além de `MODO.md` e `AGENTS.md`). **Não abra `niveis/*.zip`** e não crie arquivos do SOURCE à mão: a estrutura vem pronta do pacote do nível.

## 0. Regras do modo STARTUP
1. **Gatilho:** `MODO.md` com `modo: STARTUP`, o comando `/startup` ou o usuário escrever "startup".
2. Até o diagnóstico ser **aprovado**, não crie, edite, mova nem apague nada.
3. **Formulário:** use a ferramenta de perguntas com opções quando existir (até 4 perguntas por bloco); senão, numere as perguntas e peça respostas curtas.
4. **No máximo 2 rodadas.** Só é bloqueante a dúvida que muda o **tipo**, a **pontuação** ou o **nome**. O resto vira `a confirmar` e entra nas pendências.
5. **Não invente.** Use só o que o usuário respondeu.
6. Os passos 5 e 6 precisam de terminal (Claude Code, Cowork, Codex). Sem terminal, entregue o diagnóstico e os **passos manuais** da seção 7.

## 1. Fluxo
1. Rodada 1 (seção 2) → 2. Rodada 2, se preciso (seção 3) → 3. Pontuação (seção 4) → 4. **Diagnóstico para aprovação** (seção 6) → 5. Aplicar estrutura (seção 7) → 6. Pré-preencher e concluir (seção 7) → 7. Modo **PLANEJAMENTO**.

## 2. Rodada 1

**Bloco A — Tipo (opções).** Se a resposta não for deste template, **pare** e indique o template certo:

| Tipo de projeto | Template |
|---|---|
{rota}

**Bloco B — Identidade (texto curto):** B1 nome provisório · B2 objetivo em 1 a 3 frases · B3 quem usa e qual problema resolve · B4 prazo da primeira entrega.

**Bloco C — Pontuação (opções):**

""" + "\n".join(blocoC) + f"""

**Bloco D — Contexto técnico (opções + "não sei"):**

| # | Pergunta | Opções sugeridas |
|---|---|---|
{tecnicas}

## 3. Rodada 2 (só se necessário)
Pergunte apenas o que ficou bloqueante e complete o contexto base:
- Fora do escopo (até 3 itens) · regras inegociáveis (até 3) · métrica de sucesso · quem aprova as entregas
{extras}

## 4. Pontuação
Rode `python tools/startup.py pontuar C1,C2,C3,C4,C5` (ex.: `pontuar 1,2,0,1,2`) e use o `NIVEL_RECOMENDADO`. Sem terminal, aplique a tabela:

{regras_pontuacao(cfg)}

O usuário pode **sobrescrever** o nível no diagnóstico; registre o motivo.

## 5. Manifesto de níveis (arquivos do SOURCE criados pelo pacote)

{manifesto(niv)}

## 6. Diagnóstico (mensagem para aprovação)

```
🩺 DIAGNÓSTICO DO STARTUP
Projeto: <nome provisório>  →  pasta/repositório: <prefixo-nome>
Tipo: <tipo> (template {cfg['repo']})
Objetivo: <1 a 3 frases>
Usuários e problema: <resumo>
Pontuação: C1=<n> C2=<n> C3=<n> C4=<n> C5=<n>  → total <n>
Regras aplicadas: <faixa, pisos, 3×2>
Nível recomendado: <NIVEL>   (sobrescrito? <não | sim: motivo>)
Arquivos do SOURCE: <n> obrigatórios; opcionais mantidos: <lista ou nenhum>; opcionais removidos: <lista>
Contexto técnico: <respostas do bloco D>
Pré-preenchimento previsto: <arquivos da seção 7>
Premissas: <o que assumi a partir das respostas>
Pendências (a confirmar): <lista>
Responda "aprovado" ou diga o que ajustar.
```

## 7. Aplicar (somente depois de "aprovado")
1. Se for repositório git com commits, o script cria a tag `template-original`. Sem git, ele guarda o template em `.startup-backup/`.
2. Grave o diagnóstico aprovado em `diagnostico-startup.md` (na raiz).
3. Rode: `python tools/startup.py aplicar --nivel <NIVEL> --nome <prefixo-nome> [--remover caminho1,caminho2]` (`--remover` só aceita opcionais do nível).
4. **Pré-preencha** com as respostas, um arquivo por vez. Troque `<...>` só onde houver dado; o resto fica para o planejamento e entra em `ARTEFATO/_logs/pendencias-startup.md`. Registre cada arquivo em `ARTEFATO/_logs/changelog-source.md` com origem `startup`. Respeite o limite do contexto-master do nível.

| Arquivo (se existir no nível) | O que preencher |
|---|---|
{prefill}

5. Rode `python tools/startup.py concluir`: apaga o script de startup e **renomeia a pasta** para o nome do projeto.
6. Mensagem final: resumo do que foi criado, pendências e o **próximo prompt** (P0 de `PROMPTS-PLANEJAMENTO.md`). Avise que a sessão deve ser reaberta na pasta nova.

**Passos manuais (sem terminal):** descompacte `niveis/<nivel>.zip` numa pasta nova `<prefixo-nome>`; no `MODO.md` dela preencha `projeto:` e `modo: PLANEJAMENTO`; apague os opcionais não mantidos e as linhas deles no mapa do `contexto-master.md`; cole o diagnóstico em `ARTEFATO/_logs/diagnostico-startup.md`.

## 8. Nomenclatura (pasta e repositório)
Padrão `<prefixo>-<nome-curto>`: minúsculas, números e hífens, sem acento, até 40 caracteres. Prefixos deste template: {prefixos}. Exemplos: {cfg['exemplos_nome']}. O repositório no GitHub é criado só depois, já em PLANEJAMENTO, com o mesmo nome.
"""


def raiz_modo(cfg):
    return f"""---
modo: STARTUP              # STARTUP | PLANEJAMENTO | EXECUCAO
nivel: A_DEFINIR           # definido no startup
projeto: A_DEFINIR         # nome da pasta/repositório (NOMENCLATURA)
tipo: {cfg['tipo']}
---

# 🚦 MODO — template em STARTUP

Este repositório é o **template** `{cfg['repo']}`. Ele ainda não é um projeto.

| Modo | Quem faz o quê |
|---|---|
| 🚀 **STARTUP** | O agente segue `STARTUP.md`: perguntas → pontuação → **diagnóstico aprovado por humano** → estrutura do nível |
| 📝 **PLANEJAMENTO** | Começa automaticamente quando o startup é aplicado (a aprovação do diagnóstico é a autorização humana) |
| ⚙️ **EXECUÇÃO** | Só um humano muda, depois de congelar o SOURCE |

> Antes da aprovação do diagnóstico, o agente não cria, edita nem apaga nada.
"""


def raiz_agents(cfg):
    return f"""# AGENTS.md — template `{cfg['repo']}` (modo STARTUP)

1. Leia `MODO.md`. Se `modo: STARTUP`, ou se o usuário pedir "startup" ou `/startup`, siga **`STARTUP.md`** (modo *Startup building*).
2. Não leia outros arquivos nem abra `niveis/*.zip`: tudo o que você precisa está em `STARTUP.md`.
3. Nada é criado, alterado ou apagado antes do usuário **aprovar o diagnóstico**.
4. Quem cria a estrutura é `tools/startup.py`; você não monta pastas à mão.
5. Nunca edite `STARTUP.md`, `MODO.md`, `AGENTS.md`, `niveis/` nem `tools/`.
"""


def raiz_readme(cfg, niv):
    c = {n: len(niv[n]["obrigatorios"]) for n in NIVEIS}
    outros = ", ".join(f"`{v}`" for k, v in cfg["roteamento"].items() if v != cfg["repo"])
    return f"""# 🧩 {cfg['repo']}

> Template para {cfg['descricao']}. Arquitetura **SOURCE / ARTEFATO**, modos **PLANEJAMENTO / EXECUÇÃO** e **3 níveis de complexidade** escolhidos automaticamente no *Startup building*.

## Como iniciar um projeto
1. No GitHub, **Use this template** → *Download ZIP* (ou clone) e abra a pasta **localmente**.
2. Abra o agente na pasta:
   - **Claude Code:** digite `/startup`
   - **Cowork / Codex / outros:** digite `startup`
3. Responda as perguntas (até 2 rodadas) e **aprove o diagnóstico**.
4. O agente cria a estrutura do nível, pré-preenche o SOURCE, renomeia a pasta (ex.: {cfg['exemplos_nome']}) e entra em **PLANEJAMENTO**.
5. Termine o planejamento e só então suba o projeto para o GitHub com o mesmo nome.

## Níveis

| Nível | Exemplos | Arquivos no SOURCE |
|---|---|---|
| 🟢 SIMPLES | {cfg['exemplos']['SIMPLES']} | {c['SIMPLES']} |
| 🟡 MÉDIO | {cfg['exemplos']['MEDIO']} | {c['MEDIO']} |
| 🔴 COMPLEXO | {cfg['exemplos']['COMPLEXO']} | {c['COMPLEXO']} + opcionais |

## Estrutura do template
```
📦 {cfg['repo']}/
├── 📄 README.md         → este arquivo (humanos)
├── 🚀 STARTUP.md        → instruções do Startup building (o agente lê só ele)
├── 🚦 MODO.md           → modo: STARTUP
├── 📄 AGENTS.md · CLAUDE.md · .claude/commands/startup.md
├── 📁 niveis/           → simples.zip · medio.zip · complexo.zip · niveis.json
├── 📁 tools/startup.py  → aplica o nível, renomeia a pasta, checa os pacotes
└── 📁 .github/workflows/checar-template.yml
```

## Uso manual (sem agente)
Baixe `niveis/<nivel>.zip`, descompacte numa pasta `<prefixo>-<nome>` e siga o `README.md` de dentro do pacote.

## Outros templates
{outros}

## Manutenção
Os pacotes são **gerados** pelo repositório `ai-template-factory` (`python build.py`). Não edite os zips à mão; o check `checar-template` falha se pacote, `niveis.json` e `STARTUP.md` divergirem.
"""


CMD_STARTUP = """---
description: Inicia o modo Startup building (cria o projeto a partir do template)
---
Leia `STARTUP.md` e execute o modo **Startup building** a partir da seção 0, seguindo o fluxo da seção 1.
Informações já dadas pelo usuário (se houver): $ARGUMENTS
"""

WF_TEMPLATE = """name: checar-template
on:
  push:
  pull_request:
jobs:
  checar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Pacotes x niveis.json x STARTUP.md
        run: python tools/startup.py checar
"""


# ------------------------------------------------------------------ montagem
def limpar_mapa(raiz):
    cm = os.path.join(raiz, "SOURCE", "contexto-master.md")
    linhas = ler(cm).split("\n")
    out = []
    for ln in linhas:
        m = re.match(r"^\| `([^`]+)` \|", ln)
        if m:
            alvo = os.path.join(raiz, "SOURCE", m.group(1))
            if "*" in alvo:
                alvo = os.path.dirname(alvo)
            if not os.path.exists(alvo):
                continue
        out.append(ln)
    gravar(cm, "\n".join(out))


def montar_nivel(cfg, niv, nivel, tmp):
    base = os.path.join(F, "bases", cfg["repo"])
    shutil.rmtree(tmp, ignore_errors=True)
    shutil.copytree(base, tmp)
    manter = set(niv[nivel]["obrigatorios"]) | set(niv[nivel]["opcionais"])
    faltando = [x for x in manter if not os.path.exists(os.path.join(tmp, x))]
    assert not faltando, f"{cfg['repo']}: base sem {faltando}"
    for d, _, fs in os.walk(os.path.join(tmp, "SOURCE")):
        for f in fs:
            rel = os.path.relpath(os.path.join(d, f), tmp).replace(os.sep, "/")
            if rel not in manter:
                os.remove(os.path.join(d, f))
    for d, _, _ in os.walk(os.path.join(tmp, "SOURCE"), topdown=False):
        if not os.listdir(d):
            os.rmdir(d)
    limpar_mapa(tmp)
    m = os.path.join(tmp, "MODO.md")
    gravar(m, re.sub(r"^nivel:[^\n#]*", f"nivel: {nivel}   ", ler(m), count=1, flags=re.M))
    gravar(os.path.join(tmp, "niveis.json"), json.dumps(niveis_json(cfg), ensure_ascii=False, indent=2))
    gravar(os.path.join(tmp, "NIVEIS.md"), niveis_md(cfg, niv))
    gravar(os.path.join(tmp, "PROMPTS-PLANEJAMENTO.md"), prompts_planejamento(cfg, niv, nivel))
    os.makedirs(os.path.join(tmp, "tools"), exist_ok=True)
    shutil.copyfile(os.path.join(F, "comum", "nivel.py"), os.path.join(tmp, "tools", "nivel.py"))
    gravar(os.path.join(tmp, ".github", "workflows", "verificar-nivel.yml"), ler(os.path.join(F, "comum", "verificar-nivel.yml")))


def construir(cfg):
    niv = acumulado(cfg)
    dist = os.path.join(F, "dist", cfg["repo"])
    shutil.rmtree(dist, ignore_errors=True)
    os.makedirs(dist)
    tmp = os.path.join(F, "dist", "_tmp")
    for n in NIVEIS:
        montar_nivel(cfg, niv, n, tmp)
        zipar(tmp, os.path.join(dist, "niveis", n.lower() + ".zip"))
    shutil.rmtree(tmp)
    base = os.path.join(F, "bases", cfg["repo"])
    for extra in (".gitignore", ".gitattributes"):
        if os.path.exists(os.path.join(base, extra)):
            shutil.copyfile(os.path.join(base, extra), os.path.join(dist, extra))
    gravar(os.path.join(dist, "niveis", "niveis.json"), json.dumps(niveis_json(cfg), ensure_ascii=False, indent=2))
    gravar(os.path.join(dist, "STARTUP.md"), startup_md(cfg, niv))
    gravar(os.path.join(dist, "MODO.md"), raiz_modo(cfg))
    gravar(os.path.join(dist, "AGENTS.md"), raiz_agents(cfg))
    gravar(os.path.join(dist, "CLAUDE.md"), "@AGENTS.md")
    gravar(os.path.join(dist, "README.md"), raiz_readme(cfg, niv))
    gravar(os.path.join(dist, ".claude", "commands", "startup.md"), CMD_STARTUP)
    gravar(os.path.join(dist, ".github", "workflows", "checar-template.yml"), WF_TEMPLATE)
    os.makedirs(os.path.join(dist, "tools"), exist_ok=True)
    shutil.copyfile(os.path.join(F, "comum", "startup.py"), os.path.join(dist, "tools", "startup.py"))
    return niv


def main():
    for c in sorted(glob.glob(os.path.join(F, "config", "*.json"))):
        cfg = json.loads(ler(c))
        niv = construir(cfg)
        print(cfg["repo"], {n: len(niv[n]["obrigatorios"]) for n in NIVEIS})
    return 0


if __name__ == "__main__":
    sys.exit(main())
