#!/usr/bin/env python3
"""Ferramenta de níveis do template SOURCE/ARTEFATO (somente biblioteca padrão).

Uso (rode na raiz do repositório):
  python tools/nivel.py verificar                      # confere modo, nível e arquivos
  python tools/nivel.py podar --nivel MEDIO            # mostra o que seria removido (simulação)
  python tools/nivel.py podar --nivel MEDIO --aplicar  # remove arquivos fora do nível
  python tools/nivel.py promover --nivel COMPLEXO --origem complexo.zip [--aplicar]   # zip baixado do template (niveis/)
  python tools/nivel.py proteger --base origin/main    # em EXECUCAO, bloqueia mudanças no SOURCE

Quem roda: HUMANOS. Agentes de IA não devem executar `podar`, `promover` nem editar esta pasta.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIVEIS = ["SIMPLES", "MEDIO", "COMPLEXO"]
MODOS = ["PLANEJAMENTO", "EXECUCAO"]
PLACEHOLDER = re.compile(r"<[^<>\n]{2,60}>")


def carregar():
    with open(os.path.join(RAIZ, "niveis.json"), encoding="utf-8") as f:
        return json.load(f)


def ler(p):
    with open(os.path.join(RAIZ, p), encoding="utf-8") as f:
        return f.read()


def front(texto, chave):
    m = re.search(r"^" + chave + r":\s*([A-Za-zÀ-ú_]+)", texto, re.M)
    return m.group(1).strip() if m else None


def estado():
    t = ler("MODO.md")
    return (front(t, "modo") or "").upper(), (front(t, "nivel") or "").upper()


def listar_source():
    base = os.path.join(RAIZ, "SOURCE")
    out = []
    for d, _, fs in os.walk(base):
        for f in fs:
            out.append(os.path.relpath(os.path.join(d, f), RAIZ).replace(os.sep, "/"))
    return sorted(out)


def conjuntos(cfg, nivel):
    n = cfg["niveis"][nivel]
    return set(n["obrigatorios"]), set(n.get("opcionais", []))


def cmd_verificar(cfg, _a):
    modo, nivel = estado()
    erros, avisos = [], []
    if modo not in MODOS:
        avisos.append(f"modo inválido ou ausente ('{modo}'): agentes devem agir como EXECUCAO")
    if nivel not in NIVEIS:
        erros.append(f"nivel inválido ou ausente em MODO.md ('{nivel}'). Use {NIVEIS}")
        return finalizar(erros, avisos)
    obrig, opc = conjuntos(cfg, nivel)
    existentes = set(listar_source())
    for p in sorted(obrig):
        if p not in existentes:
            erros.append(f"arquivo obrigatório ausente: {p}")
    for p in sorted(existentes - obrig - opc):
        avisos.append(f"fora do nível {nivel} (considere remover com 'podar'): {p}")
    ignorar = tuple(cfg.get("ignorar_placeholders", []))
    for p in sorted(obrig & existentes):
        if p.endswith((".json", ".csv")) or p.startswith(ignorar):
            continue
        n = len(PLACEHOLDER.findall(ler(p)))
        if n:
            msg = f"{n} placeholder(s) <...> em {p}"
            (erros if modo == "EXECUCAO" else avisos).append(msg)
    lim = cfg.get("limite_linhas_contexto_master", {}).get(nivel)
    if lim:
        linhas = len(ler("SOURCE/contexto-master.md").splitlines())
        if linhas > lim:
            avisos.append(f"contexto-master tem {linhas} linhas (limite sugerido para {nivel}: {lim})")
    print(f"modo={modo or '?'} nivel={nivel}  obrigatórios={len(obrig)}  presentes={len(obrig & existentes)}")
    return finalizar(erros, avisos)


def finalizar(erros, avisos):
    for a in avisos:
        print("AVISO:", a)
    for e in erros:
        print("ERRO: ", e)
    if not erros:
        print("OK")
    return 1 if erros else 0


def atualizar_nivel(nivel):
    p = os.path.join(RAIZ, "MODO.md")
    t = open(p, encoding="utf-8").read()
    t2 = re.sub(r"^nivel:\s*[A-Za-zÀ-ú_]+", "nivel: " + nivel, t, count=1, flags=re.M)
    open(p, "w", encoding="utf-8").write(t2)


def limpar_mapa(removidos):
    p = os.path.join(RAIZ, "SOURCE", "contexto-master.md")
    if not os.path.exists(p):
        return 0
    linhas = open(p, encoding="utf-8").read().split("\n")
    novas, cortadas = [], 0
    for ln in linhas:
        m = re.match(r"^\| `([^`]+)` \|", ln)
        if m:
            alvo = os.path.join(RAIZ, "SOURCE", m.group(1))
            if "*" in alvo:
                alvo = os.path.dirname(alvo)
            if not os.path.exists(alvo):
                cortadas += 1
                continue
        novas.append(ln)
    open(p, "w", encoding="utf-8").write("\n".join(novas))
    return cortadas


def remover_vazios():
    base = os.path.join(RAIZ, "SOURCE")
    for d, dirs, fs in os.walk(base, topdown=False):
        if d != base and not os.listdir(d):
            os.rmdir(d)


def cmd_podar(cfg, a):
    nivel = a.nivel.upper()
    obrig, opc = conjuntos(cfg, nivel)
    alvo = [p for p in listar_source() if p not in obrig and p not in opc]
    print(f"Nível {nivel}: {len(alvo)} arquivo(s) fora do nível")
    for p in alvo:
        print("  -", p)
    if not a.aplicar:
        print("(simulação) use --aplicar para remover")
        return 0
    for p in alvo:
        os.remove(os.path.join(RAIZ, p))
    remover_vazios()
    cortadas = limpar_mapa(alvo)
    atualizar_nivel(nivel)
    print(f"Removidos {len(alvo)} arquivo(s); {cortadas} linha(s) do mapa do contexto-master atualizadas; nivel={nivel}")
    print("Próximo passo: rode 'verificar' e o prompt de planejamento do nível (NIVEIS.md).")
    return 0


def cmd_promover(cfg, a):
    nivel = a.nivel.upper()
    origem = os.path.abspath(a.origem)
    obrig, opc = conjuntos(cfg, nivel)
    faltam = [p for p in sorted(obrig) if not os.path.exists(os.path.join(RAIZ, p))]
    print(f"Promover para {nivel}: {len(faltam)} arquivo(s) a copiar de {origem}")
    for p in faltam:
        print("  +", p)
    if not a.aplicar:
        print("(simulação) use --aplicar para copiar")
        return 0
    z = zipfile.ZipFile(origem) if origem.endswith(".zip") else None
    for p in faltam:
        os.makedirs(os.path.dirname(os.path.join(RAIZ, p)), exist_ok=True)
        if z is not None:
            if p not in z.namelist():
                print("AVISO: não existe no pacote:", p)
                continue
            with z.open(p) as fz, open(os.path.join(RAIZ, p), "wb") as fd:
                shutil.copyfileobj(fz, fd)
            continue
        src = os.path.join(origem, p)
        if not os.path.exists(src):
            print("AVISO: não existe na origem:", p)
            continue
        shutil.copyfile(src, os.path.join(RAIZ, p))
    atualizar_nivel(nivel)
    print("Promovido. Peça à IA (modo PLANEJAMENTO) para gerar os arquivos novos e atualizar o mapa do contexto-master.")
    return 0


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)


def cmd_proteger(cfg, a):
    base = a.base
    r = git("show", f"{base}:MODO.md")
    if r.returncode != 0:
        print("AVISO: não foi possível ler MODO.md da base; nada a proteger")
        return 0
    modo_base = (front(r.stdout, "modo") or "").upper()
    if modo_base != "EXECUCAO":
        print(f"modo da base = {modo_base or '?'}: SOURCE pode mudar")
        return 0
    d = git("diff", "--name-only", f"{base}...HEAD")
    mudou = [p for p in d.stdout.split() if p.startswith(("SOURCE/", "niveis.json", "tools/"))]
    if mudou:
        print("ERRO: a base está em EXECUCAO e este PR altera arquivos protegidos:")
        for p in mudou:
            print("  -", p)
        print("Reabra o planejamento primeiro (PR separado que muda MODO.md para PLANEJAMENTO).")
        return 1
    print("OK: nenhuma alteração protegida")
    return 0


def main():
    cfg = carregar()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("verificar")
    p = sub.add_parser("podar"); p.add_argument("--nivel", required=True, choices=NIVEIS + [n.lower() for n in NIVEIS]); p.add_argument("--aplicar", action="store_true")
    p = sub.add_parser("promover"); p.add_argument("--nivel", required=True, choices=NIVEIS + [n.lower() for n in NIVEIS]); p.add_argument("--origem", required=True); p.add_argument("--aplicar", action="store_true")
    p = sub.add_parser("proteger"); p.add_argument("--base", default="origin/main")
    a = ap.parse_args()
    if a.cmd in (None, "verificar"):
        return cmd_verificar(cfg, a)
    return {"podar": cmd_podar, "promover": cmd_promover, "proteger": cmd_proteger}[a.cmd](cfg, a)


if __name__ == "__main__":
    sys.exit(main())
