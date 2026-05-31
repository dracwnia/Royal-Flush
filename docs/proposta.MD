# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Royal Flush

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Maria Clara Fernandes Benatti
- Sofia Liva Mendes Faria

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Tipo escolhido pelo grupo:

Jogo de memória.

## 4. Descrição geral do jogo

Uma interface gráfica inspirada em uma mesa de feltro verde de cassino (poker). Na tela, o jogador visualiza um grid de cartas de baralho viradas para baixo, com designs baseados nos quatro naipes. Na parte superior ou lateral da tela, há um painel de controle exibindo o placar com a quantidade de moedas de poker acumuladas, o nível atual e o contador de "vidas" restantes (erros permitidos). O jogador controla apenas o cursor do mouse. Toda a jogabilidade é baseada em cliques com o botão esquerdo para selecionar, revelar e interagir com as cartas na tela e com os menus do jogo. O jogador deve clicar nas cartas para virá-las, duas por vez, tentando memorizar suas posições através de um sistema de tentativa e erro. O objetivo principal é encontrar os pares perfeitos (cartas com o mesmo número/classe E o mesmo naipe) para eliminá-las do tabuleiro e avançar de nível. O jogador tem um máximo de 3 erros totais (combinações totalmente erradas) por rodada. Se as vidas zerarem, é Game Over. O maior perigo do tabuleiro. Clicar no Coringa funciona como uma armadilha que zera instantaneamente todas as moedas acumuladas na rodada. Se o jogador não memorizar a posição do Coringa e clicar nele uma segunda vez na mesma rodada, a partida é encerrada imediatamente em derrota. 

## 5. Objetivo do jogador

O objetivo do jogador é conseguir memorizar o local de todas as cartas em um sistema de tentativa e erro para completar a fase, e principalmente evitar a carta do coringa que pode tirar todas as suas moedas ganhas na rodada. 

## 6. Regras principais

- Acertos de Naipe fazem as cartas virarem novamente, mas acrescentam uma ficha à sua bolsa. (ex: 2 de copas e 7 de copas).
- Acertos de Número ou Classe (rei, rainha…) fazem as cartas virarem novamente, mas acrescentam uma ficha à sua bolsa. (ex: rainha de paus e rainha de ouros).
- Acertos de Número e Naipe fazem as cartas permanecerem viradas, contando elas como fora da rodada e acrescenta dez pontos à sua bolsa. 
- Clicar na carta do Coringa faz com que você perca todos seus pontos (e é acumulativo). 
- Tem um limite máximo de erros “vidas” que são 3 erros totais (acertos de Naipe e Acertos de Número não contam como erros)

## 7. Condição de vitória

A vitória deve acontecer quando todos os pares perfeitos (Número + Naipe) forem revelados e fixados na tela. 

## 8. Condição de derrota ou encerramento

A derrota se dá quando o número de vidas chega a zero, ou, quando você clica no Coringa duas vezes na mesma rodada. 

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Escreva aqui.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Escreva aqui.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Escreva aqui.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> Escreva aqui.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:
- Tecla/comando:
- Tecla/comando:

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> Escreva aqui.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Escreva aqui.

Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1:
- Dificuldade 2:
- Dificuldade 3:

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> Escreva aqui.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:
- Melhoria 2:
- Melhoria 3: