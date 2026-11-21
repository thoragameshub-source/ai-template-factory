---
quando_ler: nomear, organizar, exportar ou importar qualquer asset
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🏷️ Convenções de Assets

## Padrão de nome
`<tipo>_<categoria>_<nome>_<variacao>_v<versao>.<ext>`

| Tipo | Prefixo | Exemplo |
|---|---|---|
| Sprite | `spr_` | `spr_enemy_sombra_idle_v01.png` |
| Animação | `anim_` | `anim_player_run_v02` |
| Som | `sfx_` / `mus_` | `sfx_pulso_carga_v01.ogg` |
| UI | `ui_` | `ui_btn_primario_hover.png` |
| Cena | `scn_` | `scn_ilha_nevoas.tscn` |

## Formatos e limites
| Tipo | Formato | Limite |
|---|---|---|
| Sprites | PNG | ≤ 2048×2048 por atlas |
| Áudio | OGG | ≤ 2 MB por SFX |
| <Tipo> | | |

## Pastas dentro da engine
<Estrutura esperada em `ARTEFATO/jogo/` — ver `03-tecnico/arquitetura-de-codigo.md`.>

## Origem e licença (obrigatório)
Todo asset novo entra em `ARTEFATO/arte/manifesto-de-assets.csv` com **origem** (humano / IA / loja / tutorial) e **licença**.
