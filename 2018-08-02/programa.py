#!/usr/bin/env python

import unittest
import random


class Mapa:
    def __init__(self, x, y, aeroportos, nuvens):
        self.nuvens = nuvens
        self.aeroportos = aeroportos

    def count(self):
        distance = []
        for nuvem in self.nuvens:
            x_diff = nuvem[0] - self.aeroportos[0][0]
            y_diff = nuvem[1] - self.aeroportos[0][1]
            distance.append(x_diff + y_diff)
        return min(distance)


class ProgramaTestCase(unittest.TestCase):
    def test_zero_dia(self):
        mapa = Mapa(10, 10, aeroportos=[(0, 0)], nuvens=[(0, 0)])
        self.assertEqual(mapa.count(), 0)

    def test_primeiro_dia(self):
        mapa = Mapa(10, 10, aeroportos=[(0, 0)], nuvens=[(1, 0)])
        self.assertEqual(mapa.count(), 1)

    def test_quarto_dia(self):
        mapa = Mapa(10, 10, aeroportos=[(0, 0)], nuvens=[(2, 2)])
        self.assertEqual(mapa.count(), 4)

    def test_duas_nuvens(self):
        mapa = Mapa(10, 10, aeroportos=[(0, 0)], nuvens=[(1, 0), (2, 0)])

        self.assertEqual(mapa.count(), 1)

    def test_nuvens_distantes(self):
        mapa = Mapa(10, 10, aeroportos=[(0, 0)], nuvens=[(1, 0), (0, 0)])
        self.assertEqual(mapa.count(), 0)

if __name__ == '__main__':
    unittest.main()
