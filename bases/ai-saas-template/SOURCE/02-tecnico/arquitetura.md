---
quando_ler: criar ou alterar estrutura técnica, dados ou integração
modulo: codigo   # nucleo | codigo | cowork | multiagente
responsavel: <nome ou time>
modo_de_edicao: IA edita só em PLANEJAMENTO; em EXECUCAO é somente leitura
ultima_revisao: AAAA-MM-DD
---


# 🏗️ Arquitetura

> 📝 **Como preencher:** substitua o que está entre `< >` e apague as linhas de exemplo quando tiver o conteúdo real.

## Visão geral
<Descreva em 1 parágrafo como as partes se conectam.>

## Diagrama
```mermaid
flowchart LR
    U[Usuário] --> A[Agente]
    A --> B[(Base de dados)]
    A --> C[API externa]
```
> Substitua pelo desenho real do seu projeto.

## Componentes
| Componente | Responsabilidade | Tecnologia |
|---|---|---|
| <Nome> | <O que faz> | <Tech> |

## Integrações e conectores (APIs, ERPs, MCPs)
| Sistema | Tipo | Autenticação | O agente pode... | O agente NÃO pode... |
|---|---|---|---|---|
| <Sistema> | API/MCP/Arquivo | <como> | ler | escrever |
| **Exemplo:** ERP | API | token (vault) | consultar fornecedores | lançar títulos |

## Modelo de dados (resumo)
<Entidades principais e relacionamentos.>

## Decisões relevantes
Veja `06-decisoes/` — ex.: `ADR-001`.
