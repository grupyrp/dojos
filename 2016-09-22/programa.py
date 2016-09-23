#!/usr/bin/env python3

import unittest


class TestCases(unittest.TestCase):

    def test_pedra_ganha_tesoura(self):
        self.assertEqual(jokenpo('pedra','tesoura'), 'pedra ganhou \o/')
        self.assertEqual(jokenpo('tesoura', 'pedra'), 'pedra ganhou \o/')

    def test_papel_ganha_pedra(self):
        self.assertEqual(jokenpo('papel', 'pedra'), 'papel ganhou \o/')
        self.assertEqual(jokenpo('pedra', 'papel'), 'papel ganhou \o/')

    def test_tesoura_ganha_papel(self):
        self.assertEqual(jokenpo('tesoura','papel'), 'tesoura ganhou \o/')
        self.assertEqual(jokenpo('papel', 'tesoura'), 'tesoura ganhou \o/')

    def test_empate(self):
        self.assertEqual(jokenpo('tesoura','tesoura'), 'empate =/')
        self.assertEqual(jokenpo('pedra','pedra'), 'empate =/')
        self.assertEqual(jokenpo('papel','papel'), 'empate =/')

    def test_valida_entrada_jogador_1(self):
        self.assertNotEqual(jokenpo('qualquer', 'diferente'),
                'qualquer ganhou \o/')
        self.assertEqual(jokenpo('qualquer', 'diferente'),
                'trapaceiro na area')

    def test_valida_entrada_jogador_2(self):
        self.assertNotEqual(jokenpo('pedra', 'diferente'),
                'diferente ganhou \o/')
        self.assertEqual(jokenpo('pedra', 'diferente'),
                'trapaceiro na area')

dict_ftw = {
    'pedra': 'tesoura',
    'tesoura': 'papel',
    'papel': 'pedra',
}


def jokenpo(jogador_1, jogador_2):
    jogadas = dict_ftw.keys()
    if jogador_1 not in jogadas or jogador_2 not in jogadas:
        return 'trapaceiro na area'

    if jogador_1 == jogador_2:
        return 'empate =/'
    elif dict_ftw[jogador_1] == jogador_2:
        return '{} ganhou \o/'.format(jogador_1)
    else:
        return '{} ganhou \o/'.format(jogador_2)

if __name__ == "__main__":
    unittest.main()
