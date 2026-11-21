---
quando_ler: gerar build, versionar, publicar ou configurar CI
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🚢 Pipeline de Build

## Versionamento
`MAJOR.MINOR.PATCH` — ex.: `0.3.1` (protótipo = `0.x`).

## Etapas
1. Rodar testes
2. Exportar build por plataforma
3. Verificar tamanho e smoke test
4. Publicar em <canal de testes (ex.: itch.io privado)>

## Git
- Branches: `main` (estável), `feat/...`, `fix/...`
- Git LFS para: `*.png *.psd *.ogg *.wav *.fbx` (ver `.gitattributes`)
- Builds **não** são versionados (pasta `ARTEFATO/builds/` no `.gitignore`)

## Checklist de release
- [ ] Notas de versão
- [ ] Teste em hardware mínimo
- [ ] Chaves/segredos fora do repositório
