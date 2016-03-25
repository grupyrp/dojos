Problem
=======
[Batalha Naval](http://dojopuzzles.com/problemas/exibe/batalha-naval/)

Cada jogador deve dispor de uma área de 10x10 onde ele vai posicionar 5 navios de tamanhos
diferentes: um porta-aviões (comprimento 5), um encouraçado (comprimento 4), um submarino e um
destroyer (ambom de comprimento 3), e barco de patrulha (comprimento 2). Um jogador nunca deve
saber a posição dos navios do oponente. Os navios de um mesmo jogador não podem se cruzar e devem
estar dentro das fronteiras da sua área disponível.

Depois que todas as peças estão posicionadas, os jogadores se alternam em turnos para lançar bombas
sobre o outro oponente especificando qual posição ele deseja atacar. Se algum dos navios do jogador
que está sendo atacado estiver na posição atacada, considera-se que o navio foi atingido. O ataque
falha se o atacante lançar uma bomba em um local onde não existe nenhum navio do oponente.
Caso todos as posições de um navio for atingida, o jogador atacado deve informar o oponente qual
dos seus navios afundou. O jogo continua até que um jogador afunde todos os navios de seu oponente;
este jogador é então considerado vencedor.
Você deve desenvolver um programa que jogue uma partida de batalha naval entre dois oponentes. Você
precisa:

* Definir uma maneira de indicar o estado inicial dos navios dos jogadores;
* Exibir todos os movimentos dos jogadores, informando se os ataques foram bem sucedidos ou não;
* Informar quando um navio é atingido e quando ele é afundado;
* Exibir ao final do jogo um mapa final do posicionamento final dos navios dos jogadores.

Retrospectiva (24/03/2016):
===========================

Implementamos a funcao de plot para os jogadores com e sem navios e os ataques.

Positivos
---------

* Gente nova no dojo.
* Teclado US
* Disseminacao do vim
* Implementacao de uma funcionalidade completa
* Seguimos o TDD
* Flake8
* Testes automaticos com watch

Negativos
---------

* Uso do vim
* Teclado US
* Col row ou row col?
* Atraso no comeco
* Faltou o semaforo

Participantes:
--------------

* [amirelemam](https://github.com/amirelemam)
* [daneoshiga](https://github.com/daneoshiga)
* [guilhermependezza](https://github.com/guilhermependezza)
* [mawkee](https://github.com/mawkee)
* [muriloviana](https://github.com/muriloviana)
* [seocam](https://github.com/seocam)


