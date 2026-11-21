---
quando_ler: SEMPRE — primeiro arquivo que todo agente lê
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🧠 Contexto Master — <Nome do Jogo>

> ⚠️ Máximo 1–2 páginas. Detalhe vai nos outros arquivos.

## 0. 🚦 Modo do projeto
**Antes de tudo, leia `MODO.md`.** `PLANEJAMENTO` = a IA edita o SOURCE por prompt direto. `EXECUCAO` = SOURCE somente leitura; a IA gera artefatos e propõe mudanças.

## 1. O jogo em 3–5 linhas
<Gênero, plataforma, fantasia central do jogador e diferencial.>

**Exemplo:** *Farol Perdido* é um roguelite 2D de ação em visão top-down para PC. O jogador é o último guardião de um farol e explora ilhas procedurais para reacender a luz, escolhendo upgrades a cada corrida. Diferencial: a luz do farol é ao mesmo tempo arma e recurso de vida.

## 2. Pilares (máx. 3) — toda decisão deve servir a eles
1. <Pilar>
2. **Exemplo:** Luz é poder (arriscar escuridão = mais recompensa)
3. **Exemplo:** Corridas curtas (15–20 min), decisões rápidas

## 3. Estado atual
| Item | Valor |
|---|---|
| Fase | Conceito / Protótipo / Vertical Slice / Produção / Polimento |
| Engine e versão | <ex.: Godot 4.3> |
| Plataformas-alvo | <PC / Switch / Mobile> |
| Marco atual | <ex.: Vertical Slice em 15/02> |

## 4. Regras inegociáveis
1. **Leia `MODO.md` antes de agir.** Em PLANEJAMENTO a IA edita o SOURCE só por prompt; em EXECUÇÃO o SOURCE é **somente leitura** e mudanças vão para `ARTEFATO/_propostas-source/`.
2. Números de balanceamento vivem **só** em `04-dados-de-design/`; nunca "hardcoded" no código.
3. Todo asset gerado por IA entra no `manifesto-de-assets.csv` com origem e licença.
4. <Regra do projeto>

## 5. Mapa do SOURCE — "leia quando..."
| Arquivo / pasta | Leia quando... |
|---|---|
| `00-conceito/` | precisar entender a visão, o público e os pilares |
| `01-design/core-loop.md` | criar qualquer mecânica ou sistema |
| `01-design/mecanicas.md` | implementar ou ajustar uma mecânica |
| `01-design/progressao-e-economia.md` | mexer em XP, loot, moedas, dificuldade |
| `01-design/niveis-e-mundo.md` | criar ou revisar fases/mapas |
| `01-design/narrativa-e-personagens.md` | escrever diálogo, lore ou missões |
| `02-direcao-arte-audio/` | produzir ou descrever arte, UI ou áudio |
| `03-tecnico/` | escrever código, configurar build ou otimizar |
| `03-tecnico/mapa-cenas-nodos.md` | criar ou alterar cenas, entidades ou colisões |
| `03-tecnico/contrato-de-eventos.md` | criar qualquer comunicação entre sistemas |
| `04-dados-de-design/` | precisar de valores (dano, custo, drop) |
| `05-agentes/guardrails.md` | antes de qualquer ação com efeito externo |
| `05-agentes/skills/` | a tarefa casar com uma skill |
| `06-qualidade/` | validar, testar ou declarar algo pronto |
| `07-producao/` | saber o que está no escopo agora |
| `09-decisoes/` | houver dúvida "por que foi feito assim?" |

## 6. Onde gravar o que gerar
| Tipo | Pasta |
|---|---|
| Design de feature, docs | `ARTEFATO/design/` |
| Projeto da engine (código, cenas) | `ARTEFATO/jogo/` |
| Briefs e artes | `ARTEFATO/arte/` |
| Músicas, SFX, briefs de áudio | `ARTEFATO/audio/` |
| Layouts de fase | `ARTEFATO/niveis/` |
| Ferramentas/scripts de pipeline | `ARTEFATO/automacoes/` |
| Relatórios de playtest | `ARTEFATO/playtests/` |
| Não revisado / sugestões / logs | `_rascunhos/`, `_propostas-source/`, `_logs/` |

## 7. Como trabalhar
1. Leia `MODO.md`, depois este arquivo e só o que o mapa indicar.
2. Antes de criar mecânica nova, confirme que serve a um pilar e está no escopo atual (`07-producao/`).
3. Gere em `_rascunhos/`, revise com `revisar-entrega`, depois mova.
4. Registre em `_logs/changelog-ia.md`.
