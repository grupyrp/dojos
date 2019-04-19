#!/usr/bin/env python

import unittest

notas_disponiveis = [100, 50, 20, 10]


def sacar_rec(valor, saque):
    if valor == 0:
        return saque

    for nota in notas_disponiveis:
        if valor >= nota:
            saque.append(nota)
            valor -= nota
            return sacar_rec(valor, saque)


def sacar(valor):
    saque = []
    return sacar_rec(valor, saque)


def sacar2(valor):

    if valor <= 0:
        return None

    if valor % 10 > 0:
        return None

    saque = []
    for nota in notas_disponiveis:
        while valor:
            if valor >= nota:
                valor -= nota
                saque.append(nota)
            else:
                break

    return saque


class ProgramaTestCase(unittest.TestCase):
    def test_multiplo_10(self):
        self.assertEqual(sacar(105), None)

    def test_sacar100(self):
        self.assertEqual(sacar(100), [100])

    def test_sacar200(self):
        self.assertEqual(sacar(200), [100, 100])

    def test_sacar150(self):
        self.assertEqual(sacar(150), [100, 50])

    def test_sacar160(self):
        self.assertEqual(sacar(160), [100, 50, 10])

    def test_sacar180(self):
        self.assertEqual(sacar(180), [100, 50, 20, 10])

    def test_sacar310(self):
        self.assertEqual(sacar(310), [100, 100, 100, 10])

    def test_menos100(self):
        self.assertEqual(sacar(-100), None)


if __name__ == "__main__":
    unittest.main()
