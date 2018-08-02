#!/usr/bin/env python

import unittest
import random


class ProgramaTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 4
        self.y = 4

    def test_cria_mapa(self):
        response = cria_mapa(self.x, self.y)
        mapa_esperado = [
                ['.','.','.','.'],
                ['.','.','.','.'],
                ['.','.','.','.'],
                ['.','.','.','.'],
        ]
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), self.x)
        self.assertEqual(response, mapa_esperado)

    def test_seta_aeroporto(self):
        expected = len(seta_aeroportos(self.x, self.y, 3))
        self.assertEqual(expected, 3)

    def test_min_aeroporto(self):
        expected = len(seta_aeroportos(self.x, self.y))
        self.assertEqual(expected, 1)
        with self.assertRaises(ValueError) as error:
            seta_aeroportos(self.x, self.y, 0)
        # print(error.exception)
        self.assertEqual(str(error.exception), "min aeroportos deve ser 1")

    def test_max_aeroporto(self):
        max_aeroportos = self.x * self.y
        expected = len(seta_aeroportos(self.x, self.y, 3))
        self.assertLessEqual(expected, max_aeroportos)

def cria_mapa(linhas, colunas):
    linha = ['.' for i in range(0, colunas)]
    return [linha for i in range(0, linhas)]

def seta_aeroportos(linha, coluna, qtd=1):
    if qtd < 1:
        raise ValueError("min aeroportos deve ser 1")
    posicoes = [() for i in range(0, qtd)]
    return posicoes


if __name__ == '__main__':
    unittest.main()
