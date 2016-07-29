#!/usr/bin/env python3

import unittest


class TestCases(unittest.TestCase):

    def test_inteiro_para_romano_menor_que_10(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(9), 'IX')

    def test_inteiro_para_romano_numeros_compostos(self):
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(23), 'XXIII')
        self.assertEqual(int_to_roman(99), 'XCIX')
        self.assertEqual(int_to_roman(2), 'II')
        self.assertEqual(int_to_roman(47), 'XLVII')

    def test_encontra_menor(self):
        self.assertEqual(encontra_menor(30), (10, 'X'))
        self.assertEqual(encontra_menor(600), (500, 'D'))
        self.assertEqual(encontra_menor(2), (1, 'I'))

    def test_romano_para_inteiro(self):
        self.assertEqual(romanito_para_interito('X'), 10)


PRIMITIVOS = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

def encontra_menor(valor):
    chaves = list(PRIMITIVOS.keys())
    chaves.sort(reverse=True)
    for i in chaves:
        if valor >= i:
            return i, PRIMITIVOS[i]

def int_to_roman(valor):
    if valor in PRIMITIVOS:
        return PRIMITIVOS[valor]

    retorno = str()
    while valor > 0:
        arb, rom = encontra_menor(valor)
        valor -= arb
        retorno += rom
    return retorno

def romanito_para_interito(romanito):
    primitivos = PRIMITIVOS.items()
    for item in primitivos:


if __name__ == "__main__":
    unittest.main()
