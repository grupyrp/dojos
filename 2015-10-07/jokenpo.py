#!/usr/bin/env python

import unittest

entradas = ["s,s", "s,p", "s,r", "r,r", "r,p"]


class JokenpoTeste(unittest.TestCase):

    def test_empate(self):
        assert jokenpo('s,s') == 'empate'
        assert jokenpo('r,r') == 'empate'
        assert jokenpo('p,p') == 'empate'

    def test_entrada_invalida(self):
        assert jokenpo('r') == 'invalido'
        assert jokenpo(4) == 'invalido'
        assert jokenpo('r,r,r') == 'invalido'
        assert jokenpo('f,g') == 'invalido'
        assert jokenpo('m,m') == 'invalido'
        assert jokenpo() == 'invalido'

    def test_first_player_win(self):
        assert jokenpo('s,p') == 'player 1 ganhou'
        assert jokenpo('p,r') == 'player 1 ganhou'
        assert jokenpo('r,s') == 'player 1 ganhou'
        
    def test_second_player_win(self):
        assert jokenpo('p,s') == 'player 2 ganhou'
        assert jokenpo('r,p') == 'player 2 ganhou'
        assert jokenpo('s,r') == 'player 2 ganhou'
  

def jokenpo(entrada=''):
    try:
        j1, j2 = entrada.split(',')
    except:
        return 'invalido'

    win_dict = {
        'p': 'r',
        'r': 's',
        's': 'p',
    }

    if j1 not in win_dict or j2 not in win_dict:
        return 'invalido'
        
    if win_dict.get(j1) == j2:
        return 'player 1 ganhou'
    elif win_dict.get(j2) == j1:
        return 'player 2 ganhou'
    
    # Nenhum dos casos retorna empate
    return 'empate'

if __name__ == '__main__':
    unittest.main()