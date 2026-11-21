---
quando_ler: ANTES de qualquer ação com efeito fora do rascunho
modulo: nucleo   # nucleo | arte-audio | narrativa | multiplayer
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---

> 📝 **Como preencher:** substitua o que está entre `< >` e troque as linhas **Exemplo** pelo conteúdo real. O exemplo usa um jogo fictício: *Farol Perdido* (roguelite 2D de ação).


# 🛡️ Guardrails

## ⛔ Nunca fazer
1. Editar `SOURCE/` quando `MODO.md` estiver em EXECUÇÃO (propor em `_propostas-source/`), ou alterar `MODO.md`, `AGENTS.md` e `CLAUDE.md` em qualquer modo.
2. Escrever valores de balanceamento direto no código.
3. Usar/imitar personagens, músicas, arte ou nomes de jogos e marcas existentes.
4. Importar assets sem registrar origem e licença no manifesto.
5. <Ação proibida>
6. Commitar chaves, tokens ou dados pessoais.

## ✋ Exige aprovação humana
| Ação | Quem aprova |
|---|---|
| Adicionar mecânica fora do escopo atual | Game Designer |
| Mudar versão da engine ou plugin | Responsável técnico |
| Incluir asset gerado por IA no build final | Diretor de arte/produto |
| Publicar build | Produtor |

## ✅ Pode fazer sozinho
Gerar rascunhos de design, briefs, código em branch, testes locais e relatórios.

## Quando em dúvida
Parar e perguntar em uma frase.
