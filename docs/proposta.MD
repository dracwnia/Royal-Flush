# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

Royal Flush

## 2. Integrantes do grupo

- Maria Clara Fernandes Benatti
- Sofia Liva Mendes Faria
- Pedro Felipe Bastos de Oliveira

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

Jogo de memória.

## 4. Descrição geral do jogo

Uma interface gráfica inspirada em uma mesa de feltro verde de cassino (poker). Na tela, o jogador visualiza um grid de cartas de baralho viradas para baixo, com designs baseados nos quatro naipes. Na parte superior ou lateral da tela, há um painel de controle exibindo o nível atual e o contador de "vidas" restantes (erros permitidos). O jogador controla apenas o cursor do mouse. Toda a jogabilidade é baseada em cliques com o botão esquerdo para selecionar, revelar e interagir com as cartas na tela e com os menus do jogo. O jogador deve clicar nas cartas para virá-las, duas por vez, tentando memorizar suas posições através de um sistema de tentativa e erro. O objetivo principal é encontrar os pares perfeitos (cartas com o mesmo número/classe E o mesmo naipe) para eliminá-las do tabuleiro e avançar de nível. O jogador tem um máximo de 3 erros totais (combinações totalmente erradas) por rodada. Se as vidas zerarem, é Game Over. O maior perigo do tabuleiro. Clicar no Coringa funciona como uma armadilha que zera todos os acertos da rodada (virando as cartas novamente para baixo). Se o jogador não memorizar a posição do Coringa e clicar nele uma segunda vez na mesma rodada, a partida é encerrada imediatamente em derrota. 

## 5. Objetivo do jogador

O objetivo do jogador é conseguir memorizar o local de todas as cartas em um sistema de tentativa e erro para completar a fase, e principalmente evitar a carta do coringa que pode reverter todos seus acertos na rodada. 

## 6. Regras principais

- Acertos de Naipe  fazem as cartas voltarem ao original, mas não perde vidas (ex: 2 de copas e 7 de copas).
- Acertos de Número ou Classe (rei, rainha…) fazem as cartas voltarem ao original, mas não perde vidas (ex: rainha de paus e rainha de ouros).
- Acertos de Número e Naipe fazem as cartas permanecerem viradas, contando elas como fora da rodada e acrescenta dez pontos à sua bolsa. 
- Clicar na carta do Coringa faz com que você perca todos seus pontos (e é acumulativo). 
- Tem um limite máximo de erros “vidas” que são 3 erros totais, ou seja a carta é totalmente diferente em naipe e número (acertos de Naipe e Acertos de Número não contam como erros)

## 7. Condição de vitória

A vitória deve acontecer quando todos os pares perfeitos (Número + Naipe) forem revelados e fixados na tela. 

## 8. Condição de derrota ou encerramento

A derrota se dá quando o número de vidas chega a zero, ou, quando você clica no Coringa duas vezes na mesma rodada. 

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

O jogador não possui um personagem visual. Toda a interação é feita pelo cursor do mouse, que representa a ação do jogador sobre o tabuleiro.

## Obstáculos, inimigos ou desafios

A carta Coringa é o principal elemento de perigo: Clicar nela pela primeira vez retorna as cartas para a posicao original. Clicar nela uma segunda vez na mesma rodada encerra a partida imediatamente em derrota. Além disso, o próprio tabuleiro funciona como desafio, pois as cartas são posicionadas aleatoriamente, exigindo memorização das posições para evitar erros e para evitar o Coringa.

## Itens, alvos ou objetos de interação

- Cartas de baralho: distribuídas em grid, viradas para baixo. O jogador às revela duas por vez;
- Par de naipe (mesmo naipe, valores diferentes): as cartas viram novamente, mas não se perde vidas
- Par de valor (mesmo valor, naipes diferentes): as cartas viram novamente, mas não se perde vidas
- Par perfeito (mesmo naipe e mesmo valor): as cartas são fixadas no tabuleiro, removidas da jogada
- Carta Coringa: armadilha que retorna todas as cartas ja fixas para a posicao original no 1º clique e encerra a partida no 2º clique na mesma rodada.

## Pontuação, vidas, tempo ou progresso

O jogador inicia cada rodada com 3 vidas. Apenas combinações completamente erradas (sem naipe nem valor em comum) consomem uma vida, acertos parciais de naipe ou valor não são penalizados com perda de vida. O placar exibe o nível atual e as vidas restantes. Ao completar todos os pares perfeitos do tabuleiro, o jogador avança de nível, com o grid aumentando progressivamente.

## 10. Controles previstos

- Clique esquerdo do mouse: revelar carta/selecionar opção no menu
- ESC: sair do jogo ou pausar

## 11. Organização inicial do código

- `main.py`: inicia o jogo e chama o loop principal;
- `src/jogo.py`: contém o loop principal e o controle de estados do jogo (menu, rodada, game over);
- `src/tabuleiro.py`: gerencia a criação, embaralhamento e exibição do grid de cartas;
- `src/carta.py`: define a estrutura de cada carta (naipe, valor, estado) e suas funções de comparação;
- `src/pontuacao.py`: controla moedas, vidas, nível e lógica de progressão;
- `src/arquivos.py`: funções de leitura e escrita de arquivos (ranking, configurações);
- `src/config.py`: constantes do jogo, como tamanho da tela, cores e configurações de grid por nível.


## 12. Recursos externos previstos

- Imagens para as cartas;
- Fonte personalizada;
- Sons de efeito, caso haja tempo para implementação.

## 13. Principais dificuldades esperadas

- Gerenciar o estado de cada carta (virada, revelada temporariamente, fixada como par ou identificada como Coringa) sem conflitos durante a jogada;
- Implementar a lógica de comparação parcial (só naipe ou só valor) separada da lógica de par perfeito, garantindo que as recompensas e os efeitos corretos sejam aplicados em cada caso;
- Controlar o comportamento do Coringa em dois estágios (virar as cartas acertadas de volta para a posição original 1º clique, game over no 2º) dentro da mesma rodada sem que o estado se perca entre turnos;
- Escalar o grid dinamicamente entre os níveis, ajustando o tamanho e o posicionamento das cartas na tela conforme o tabuleiro cresce;
- Manter o código organizado em funções e módulos desde o início para facilitar testes e a integração com a parte desenvolvida pela outra integrante.

## 14. Escopo mínimo para a entrega final

A versão mínima do jogo terá um tabuleiro funcional com cartas embaralhadas e mecânica de revelar duas por vez, sistema de comparação com os três resultados possíveis (par de naipe, par de valor e par perfeito), carta Coringa com seus dois efeitos, sistema de 3 vidas com perda apenas em erros totais, placar com moedas e nível exibido na tela, condição de vitória ao completar todos os pares perfeitos, condição de derrota por vidas zeradas ou segundo clique no Coringa, e pelo menos dois níveis com grids de tamanhos diferentes.

## 15. Possíveis melhorias, caso haja tempo

- Sistema de combo que exibe mensagem ao acertar pares perfeitos consecutivos;
- Animação de virar carta;
- Tela inicial e tela de game over com estética de cassino;
- Ranking salvo em arquivo com as maiores pontuações;
- Sons de efeito para acerto, erro e Coringa;
- Aumento progressivo de dificuldade com mais Coringas nos níveis avançados.
