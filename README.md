# Royal Flush

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Maria Clara Fernandes Benatti
- Sofia Liva Mendes Faria
- Pedro Felipe Bastos de Oliveira

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Royal Flush é um jogo de memória com tema de cassino. O jogador visualiza um tabuleiro de cartas de baralho viradas para baixo, dispostas em grid sobre uma mesa de feltro verde. A cada jogada, duas cartas são reveladas e comparadas: se tiverem o mesmo naipe e o mesmo valor (par perfeito), elas são fixadas e saem da jogada; se tiverem apenas o naipe ou apenas o valor em comum, voltam a virar para baixo sem penalidade; se não tiverem nada em comum, o jogador perde uma vida. O tabuleiro também contém uma carta Coringa, que funciona como armadilha.

## Objetivo do jogador

O objetivo é memorizar a posição das cartas e encontrar todos os pares perfeitos (mesmo naipe e mesmo valor) do tabuleiro, avançando de nível, evitando ao máximo errar combinações e clicar na carta Coringa.

## Regras do jogo

- O jogador clica em duas cartas por vez para revelá-las e compará-las.
- Par perfeito (mesmo naipe e mesmo valor): as cartas são fixadas e saem da jogada.
- Par de mesmo naipe (valores diferentes) ou mesmo valor (naipes diferentes): as cartas voltam a virar para baixo, sem perda de vida.
- Combinação totalmente errada (sem naipe nem valor em comum): o jogador perde 1 vida.
- O jogador começa cada rodada com 3 vidas. Ao zerar as vidas, é Game Over.
- A carta Coringa é uma armadilha: no 1º clique, todos os pares perfeitos já fixados voltam à posição original (viradas para baixo); no 2º clique na mesma rodada, a partida é encerrada imediatamente em derrota.
- Ao encontrar todos os pares perfeitos do tabuleiro, o jogador avança de nível, com o grid de cartas aumentando de tamanho.
- A vitória ocorre ao completar o último nível disponível.

## Controles

- Clique esquerdo do mouse: revelar carta / interagir com o tabuleiro.
- R: reiniciar a partida (após vitória ou derrota).
- ESC: sair do jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.