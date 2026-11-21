#!/usr/bin/env python3
"""Startup building: cria o projeto a partir do template (somente biblioteca padrão).

Uso (na raiz do template, depois que o diagnóstico foi APROVADO por um humano):
  python tools/startup.py pontuar 1,2,0,1,2          # nível recomendado pelas 5 respostas (0, 1 ou 2)
  python tools/startup.py aplicar --nivel MEDIO --nome saas-minha-ideia [--remover caminho1,caminho2] [--simular]
  python tools/startup.py concluir                    # remove o startup e renomeia a pasta para o nome do projeto
  python tools/startup.py checar                      # (CI do template) confere zips x niveis.json x STARTUP.md
  python tools/startup.py status

O agente só roda `aplicar` e `concluir` depois que a pessoa aprovar o diagnóstico.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIVEIS = ["SIMPLES", "MEDIO", "COMPLEXO"]
NOME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# arquivos que existem só no template (saem do projeto ao aplicar)
SO_TEMPLATE = ["STARTUP.md", "niveis", "README.md", "MODO.md", "AGENTS.md", "CLAUDE.md",
               ".claude/commands/startup.md", ".github/workflows/checar-template.yml"]
BACKUP = ".startup-backup"


def p(*partes):
    return os.path.join(RAIZ, *partes)


def carregar():
    with open(p("niveis", "niveis.json"), encoding="utf-8") as f:
        return json.load(f)


def front(texto, chave):
    m = re.search(r"^" + chave + r":\s*([A-Za-z0-9À-ú_\-]+)", texto, re.M)
    return m.group(1).strip() if m else None


def ler(caminho):
    with open(caminho, encoding="utf-8") as f:
        return f.read()


def gravar(caminho, texto):
    os.makedirs(os.path.dirname(caminho) or ".", exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)


def set_front(texto, chave, valor):
    padrao = r"^" + chave + r":[^\n#]*"
    if re.search(padrao, texto, re.M):
        return re.sub(padrao, f"{chave}: {valor}   ", texto, count=1, flags=re.M)
    return texto.replace("---\n", f"---\n{chave}: {valor}\n", 1)


# ------------------------------------------------------------------ pontuar
def recomendar(cfg, respostas):
    pt = cfg["pontuacao"]
    total = sum(respostas)
    nivel = next(n for n, (a, b) in pt["faixas"].items() if a <= total <= b)
    motivos = [f"soma {total} → faixa {nivel}"]
    idx = NIVEIS.index(nivel)
    for piso in pt.get("pisos", []):
        r = respostas[piso["pergunta"] - 1]
        if r >= piso["a_partir_de"] and NIVEIS.index(piso["minimo"]) > idx:
            idx = NIVEIS.index(piso["minimo"])
            motivos.append(f"piso: pergunta {piso['pergunta']} = {r} → mínimo {piso['minimo']} ({piso['motivo']})")
    if respostas.count(2) >= pt.get("tres_respostas_2", 3) and idx < 2:
        idx = 2
        motivos.append("três ou mais respostas 2 → COMPLEXO")
    return NIVEIS[idx], total, motivos


def cmd_pontuar(cfg, a):
    try:
        resp = [int(x) for x in a.respostas.split(",")]
    except ValueError:
        print("ERRO: use 5 números separados por vírgula, ex.: 1,2,0,1,2")
        return 1
    if len(resp) != len(cfg["pontuacao"]["perguntas"]) or any(r not in (0, 1, 2) for r in resp):
        print("ERRO: informe 5 respostas, cada uma 0, 1 ou 2")
        return 1
    nivel, total, motivos = recomendar(cfg, resp)
    for i, (q, r) in enumerate(zip(cfg["pontuacao"]["perguntas"], resp), 1):
        print(f"  {i}. {q['tema']}: {r} ({q['opcoes'][r]})")
    for m in motivos:
        print("  →", m)
    print(f"NIVEL_RECOMENDADO={nivel} PONTOS={total}")
    return 0


# ------------------------------------------------------------------ aplicar
def validar_nome(cfg, nome):
    if not NOME_RE.match(nome) or len(nome) > 40:
        return "use minúsculas, números e hífens (máx. 40 caracteres), sem acento"
    pref = nome.split("-")[0]
    if pref not in cfg["prefixos"] or "-" not in nome:
        return "comece com um prefixo válido: " + ", ".join(f"{k}-" for k in cfg["prefixos"])
    return None


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)


def limpar_mapa():
    cm = p("SOURCE", "contexto-master.md")
    if not os.path.exists(cm):
        return 0
    novas, cortadas = [], 0
    for ln in ler(cm).split("\n"):
        m = re.match(r"^\| `([^`]+)` \|", ln)
        if m:
            alvo = p("SOURCE", m.group(1))
            if "*" in alvo:
                alvo = os.path.dirname(alvo)
            if not os.path.exists(alvo):
                cortadas += 1
                continue
        novas.append(ln)
    gravar(cm, "\n".join(novas))
    return cortadas


def remover_vazios():
    base = p("SOURCE")
    for d, _, _ in os.walk(base, topdown=False):
        if d != base and not os.listdir(d):
            os.rmdir(d)


def cmd_aplicar(cfg, a):
    modo = front(ler(p("MODO.md")), "modo") or ""
    if modo.upper() != "STARTUP":
        print(f"ERRO: MODO.md está em '{modo}'. O startup só roda em modo STARTUP.")
        return 1
    nivel = a.nivel.upper()
    erro = validar_nome(cfg, a.nome)
    if erro:
        print("ERRO no nome:", erro)
        return 1
    pacote = p("niveis", nivel.lower() + ".zip")
    if not os.path.exists(pacote):
        print("ERRO: pacote não encontrado:", pacote)
        return 1
    opc = set(cfg["niveis"][nivel].get("opcionais", []))
    remover = [x.strip() for x in (a.remover or "").split(",") if x.strip()]
    remover = [x if x.startswith("SOURCE/") else "SOURCE/" + x for x in remover]
    invalidos = [x for x in remover if x not in opc]
    if invalidos:
        print("ERRO: só arquivos opcionais do nível podem ser removidos:", ", ".join(invalidos))
        print("Opcionais de", nivel, ":", ", ".join(sorted(opc)) or "(nenhum)")
        return 1
    diag = p(a.diagnostico)
    print(f"Projeto: {a.nome}  |  tipo: {cfg['repo']}  |  nível: {nivel}")
    print(f"Pacote: niveis/{nivel.lower()}.zip  |  opcionais removidos: {len(remover)}")
    print("Diagnóstico:", "encontrado" if os.path.exists(diag) else "AUSENTE (recomendado gravar antes)")
    if a.simular:
        print("(simulação) nada foi alterado")
        return 0

    # 1) ponto de restauração
    if os.path.isdir(p(".git")):
        if git("rev-parse", "HEAD").returncode == 0:
            git("tag", "-f", "template-original")
            print("Tag git 'template-original' criada.")
        else:
            print("AVISO: repositório git sem commits; faça um commit para ter ponto de restauração.")
    bkp = p(BACKUP)
    os.makedirs(bkp, exist_ok=True)

    # 2) tira os arquivos do template
    for item in SO_TEMPLATE:
        src = p(item)
        if os.path.exists(src):
            dst = os.path.join(bkp, item)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
    for d in (".claude/commands", ".claude", ".github/workflows", ".github"):
        if os.path.isdir(p(d)) and not os.listdir(p(d)):
            os.rmdir(p(d))

    # 3) extrai o pacote do nível
    with zipfile.ZipFile(os.path.join(bkp, "niveis", nivel.lower() + ".zip")) as z:
        for nome in z.namelist():
            if nome.endswith("/"):
                continue
            destino = p(nome)
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with z.open(nome) as fz, open(destino, "wb") as fd:
                shutil.copyfileobj(fz, fd)

    # 4) opcionais que o diagnóstico decidiu não manter
    for x in remover:
        if os.path.exists(p(x)):
            os.remove(p(x))
    remover_vazios()
    cortadas = limpar_mapa()

    # 5) MODO.md do projeto
    hoje = datetime.date.today().isoformat()
    t = ler(p("MODO.md"))
    for k, v in (("modo", "PLANEJAMENTO"), ("nivel", nivel), ("projeto", a.nome),
                 ("alterado_em", hoje), ("alterado_por", "startup (diagnóstico aprovado)")):
        t = set_front(t, k, v)
    gravar(p("MODO.md"), t)

    # 6) diagnóstico, pendências e changelog
    logs = p("ARTEFATO", "_logs")
    os.makedirs(logs, exist_ok=True)
    if os.path.exists(diag):
        shutil.move(diag, os.path.join(logs, "diagnostico-startup.md"))
    pend = os.path.join(logs, "pendencias-startup.md")
    if not os.path.exists(pend):
        gravar(pend, "# Pendências do startup\n\n> Itens `a confirmar` deixados pelo startup. Resolva no modo PLANEJAMENTO e risque aqui.\n\n| # | Pendência | Arquivo do SOURCE | Bloqueia EXECUÇÃO? |\n|---|---|---|---|\n")
    cl = os.path.join(logs, "changelog-source.md")
    reg = (f"\n| {hoje} | startup | estrutura criada: nível {nivel}, projeto {a.nome}, "
           f"{len(remover)} opcional(is) removido(s) | tools/startup.py (diagnóstico aprovado) |\n")
    with open(cl, "a", encoding="utf-8") as f:
        f.write(reg)
    gi = p(".gitignore")
    linhas = ler(gi) if os.path.exists(gi) else ""
    if BACKUP not in linhas:
        with open(gi, "a", encoding="utf-8") as f:
            f.write(("\n" if linhas and not linhas.endswith("\n") else "") + BACKUP + "/\n")

    print(f"OK: estrutura {nivel} aplicada; {cortadas} linha(s) do mapa do contexto-master removidas; modo=PLANEJAMENTO.")
    print("Próximos passos: 1) pré-preencher o SOURCE (STARTUP.md, seção 7)  2) python tools/startup.py concluir")
    return 0


# ------------------------------------------------------------------ concluir
def cmd_concluir(cfg, a):
    t = ler(p("MODO.md"))
    if (front(t, "modo") or "").upper() == "STARTUP":
        print("ERRO: rode 'aplicar' primeiro.")
        return 1
    nome = front(t, "projeto")
    if not nome or nome == "A_DEFINIR":
        print("ERRO: MODO.md sem 'projeto:'.")
        return 1
    script = os.path.abspath(__file__)
    pai = os.path.dirname(RAIZ)
    novo = os.path.join(pai, nome)
    os.chdir(pai)
    try:
        os.remove(script)
        if os.path.isdir(os.path.dirname(script)) and not os.listdir(os.path.dirname(script)):
            os.rmdir(os.path.dirname(script))
    except OSError:
        print("AVISO: não foi possível apagar tools/startup.py; apague manualmente.")
    if os.path.basename(RAIZ) == nome:
        print(f"OK: a pasta já se chama '{nome}'.")
        return 0
    if os.path.exists(novo):
        print(f"ERRO: já existe uma pasta '{novo}'. Renomeie manualmente.")
        return 1
    try:
        os.rename(RAIZ, novo)
    except OSError as e:
        print(f"AVISO: não consegui renomear ({e}). Feche a sessão/editor e rode:")
        print(f'  mv "{RAIZ}" "{novo}"   (Windows: ren "{RAIZ}" {nome})')
        return 0
    print(f"OK: pasta renomeada para {novo}")
    print("Reabra a sessão do agente nessa pasta e continue no modo PLANEJAMENTO.")
    return 0


# ------------------------------------------------------------------ checar (CI do template)
def cmd_checar(cfg, a):
    erros = []
    startup = ler(p("STARTUP.md")) if os.path.exists(p("STARTUP.md")) else ""
    manifestados = set()
    for ln in startup.split("\n"):
        m = re.match(r"^\s*- `([^`]+/)`: (.*)$", ln)
        if m:
            manifestados |= {m.group(1) + x for x in re.findall(r"`([^`]+)`", m.group(2))}
        elif re.match(r"^\s*- `[^`]+`(, `[^`]+`)*$", ln):
            manifestados |= set(re.findall(r"`([^`]+)`", ln))
    for nivel in NIVEIS:
        z = p("niveis", nivel.lower() + ".zip")
        if not os.path.exists(z):
            erros.append(f"pacote ausente: niveis/{nivel.lower()}.zip")
            continue
        n = cfg["niveis"][nivel]
        with zipfile.ZipFile(z) as zz:
            nomes = set(zz.namelist())
            esperados = set(n["obrigatorios"]) | set(n.get("opcionais", []))
            source = {x for x in nomes if x.startswith("SOURCE/") and not x.endswith("/")}
            for f in sorted(esperados - source):
                erros.append(f"{nivel}: falta no zip {f}")
            for f in sorted(source - esperados):
                erros.append(f"{nivel}: sobra no zip {f}")
            for f in ("MODO.md", "AGENTS.md", "niveis.json", "tools/nivel.py"):
                if f not in nomes:
                    erros.append(f"{nivel}: falta {f}")
            if "MODO.md" in nomes:
                nv = front(zz.read("MODO.md").decode("utf-8"), "nivel")
                if (nv or "").upper() != nivel:
                    erros.append(f"{nivel}: MODO.md do zip com nivel={nv}")
            if "niveis.json" in nomes and json.loads(zz.read("niveis.json"))["niveis"] != cfg["niveis"]:
                erros.append(f"{nivel}: niveis.json do zip diferente de niveis/niveis.json")
        for f in n["obrigatorios"]:
            if f.replace("SOURCE/", "", 1) not in manifestados:
                erros.append(f"STARTUP.md: manifesto sem {f}")
    for e in erros:
        print("ERRO:", e)
    print("OK" if not erros else f"{len(erros)} erro(s)")
    return 1 if erros else 0


def cmd_status(cfg, a):
    t = ler(p("MODO.md"))
    print("modo:", front(t, "modo"), "| nivel:", front(t, "nivel"), "| projeto:", front(t, "projeto"))
    return 0


def main():
    cfg = carregar() if os.path.exists(p("niveis", "niveis.json")) else None
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("pontuar"); s.add_argument("respostas")
    s = sub.add_parser("aplicar")
    s.add_argument("--nivel", required=True, choices=NIVEIS + [n.lower() for n in NIVEIS])
    s.add_argument("--nome", required=True)
    s.add_argument("--remover", default="")
    s.add_argument("--diagnostico", default="diagnostico-startup.md")
    s.add_argument("--simular", action="store_true")
    sub.add_parser("concluir")
    sub.add_parser("checar")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "concluir":
        return cmd_concluir(cfg, a)
    if a.cmd == "status":
        return cmd_status(cfg, a)
    if cfg is None:
        print("ERRO: niveis/niveis.json não encontrado (o startup já foi aplicado?)")
        return 1
    return {"pontuar": cmd_pontuar, "aplicar": cmd_aplicar, "checar": cmd_checar}[a.cmd](cfg, a)


if __name__ == "__main__":
    sys.exit(main())
