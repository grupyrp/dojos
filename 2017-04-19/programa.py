#!/usr/bin/env python

import unittest
LIST_NAIPES = ['O', 'C', 'E', 'P']
DICT_CARTAS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

class Carta:
    def __init__(self, valor, naipe):
        self.valor = DICT_CARTAS[valor]
        if not naipe in LIST_NAIPES:
            raise ValueError
        self.naipe = naipe

class Mao:
    def __init__(self, c1, c2, c3, c4, c5):
        pass

class PokerTestCase(unittest.TestCase):
    def test_criar_cartas(self):
        c1 = Carta("2", "P")
        self.assertEqual(c1.valor, 2)
        self.assertEqual(c1.naipe, "P")
        c2 = Carta("8", "O")
        self.assertEqual(c2.valor, 8)
        self.assertEqual(c2.naipe, "O")

    def test_criar_cartas_decimais(self):
        c1 = Carta("10", "P")
        self.assertEqual(c1.valor, 10)
        self.assertEqual(c1.naipe, "P")
        c2 = Carta("J", "E")
        self.assertEqual(c2.valor, 11)
        self.assertEqual(c2.naipe, "E")

    def test_verifica_naipe(self):
        with self.assertRaises(ValueError):
            c1 = Carta("10", "X")

    def test_verifica_carta(self):
        with self.assertRaises(KeyError):
            c1 = Carta("13", "E")

    def test_verifica_mao(self):
        p1 = Mao(("2", "E"), ("2", "P"), ("3", "P"), ("4", "E"), ("5", "E"))


if __name__ == '__main__':
    unittest.main()
