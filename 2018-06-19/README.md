Problema
========
Um vulcão acaba de entrar em erupção, provocando uma nuvem de cinzas que se alastra impedindo a circulação aérea. O governo está muito preocupado e deseja saber quando que a nuvem de cinzas irá atingir todos os aeroportos do país.

Está disponível um mapa detalhando a situação atual. O mapa é retangular, dividido em pequenos quadrados. Neste mapa existem três tipos de quadrados: nuvem (indicando que esta região do mapa já está coberto por nuvens), aeroportos (indicando a localização de um aeroporto) e todas as outras (indicando locais onde a nuvem ainda não chegou).

A cada dia, a nuvem expande-se um quadrado na horizontal e um quadrado na vertical. Ou seja, ao fim de cada dia, todos os quadrados adjacentes (vertical ou horizontalmente) a uma nuvem, também passam a conter nuvens. Por exemplo:

. . * . . . * *      . * * * . * * *     * * * * * * * *
. * * . . . . .      * * * * . . * *     * * * * * * * *
* * * . A . . A      * * * * A . . A     * * * * * . * *
. * . . . . . .  ->  * * * . . . . .  -> * * * * . . . .
. * . . . . A .      * * * . . . A .     * * * * . . A .
. . . A . . . .      . * . A . . . .     * * * A . . . .
. . . . . . . .      . . . . . . . .     . * . . . . . .
     Dia 1                Dia 2               Dia 3

Para preparar os planos de contingência, o governo necessita saber: quantos dias demorará para ao menos um aeroporto ficar coberto pelas nuvens e daqui quantos dias todos os aeroportos estarão cobertos pelas nuvens.

Dados um quadriculado com L linhas e C colunas, além da indicação inicial das nuvens e dos aeroportos, desenvolva uma programa que informe o número de dias até um primeiro aeroporto ficar debaixo da nuvem de cinzas e o número de dias até que todos os aeroportos ficarem cobertos pelas cinzas.

Retrospectiva:
==============

Positivos:
----------
* Pessoal aprendendo quase baby steps
* Galera usou o vim
* Pessoas novas
* Pessoas que codaram pela primeira vez no dojo
* Aprendemos a configurar watchmed: watchmedo shell-command --command="python programa.py" -R

Negativos:
----------
* Algumas pessoas ignorando o baby steps
* Pessoal apanhando de Vim e do teclado do Mac
* Não lembravamos como configurar watchmedo
* Nem todo mundo participou
* Atrasou o after

Participantes:
==============

* [muriloviana](https://github.com/muriloviana)
* [vanderlei](https://github.com/hdelei)
* [marcelo-theodoro](https://github.com/marcelo-theodoro)
* [josecostamartins](https://github.com/josecostamartins)
* [girol](https://github.com/girol)
* [hugopenna](https://github.com/hugopenna)
