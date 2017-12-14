#!/usr/bin/env python

import unittest


class SaboresNaoBatem(Exception):
    pass


class ProgramaTestCase(unittest.TestCase):
    def test_check_qty_items(self):
        dict_a = {'presunto': 1, 'mussarela': 2}
        dict_b = {'presunto': 1, 'mussarela': 2}
        self.assertTrue(check_qty_items(dict_a, dict_b))

    def test_check_sabores(self):
        dict_a = {'presunto': 1, 'mussarela': 2}
        dict_b = {'presunto': 3, 'mussarela': 2}
        self.assertTrue(check_sabores(dict_a, dict_b))

    def test_calcula_tci(self):
        dict_a = {'presunto': 1, 'mussarela': 2}
        dict_b = {'presunto': 3, 'mussarela': 2}
        self.assertEqual(calcula_tci(dict_a, dict_b), 2)

    def test_distancia_sabores(self):
        self.assertEqual(distancia_sabores(1,5), 4)

    def test_mais_parecido(self):
        pessoas = {
            'jacare': {'presunto': 1, 'mussarela': 2},
            'washington': {'presunto': 5, 'mussarela': 3},
            'carla': {'presunto': 2, 'mussarela': 2}
        }
        pessoa = {'presunto': 1, 'mussarela': 2}
        self.assertEqual(mais_parecido(pessoas, pessoa), 'jacare')

    def test_mais_parecido_sabor_diferente(self):
        pessoas = {
            'jacare': {'presunto': 1, 'mussarela': 2},
        }
        pessoa = {'presunto': 2, 'frango': 2}
        with self.assertRaises(SaboresNaoBatem):
            mais_parecido(pessoas, pessoa)


def check_qty_items(a, b):
    return len(a.items()) == len(b.items())

def check_sabores(a, b):
    return set(a.keys()) == set(b.keys())

def distancia_sabores(x, y):
    return abs(x - y)

def calcula_tci(a, b):
    tci = 0
    for sabor, nota in a.items():
       tci += distancia_sabores(nota, b[sabor])
    return tci

def mais_parecido(colegas, pessoa):
    menor_tci = None
    pessoa_mais_parecida = None

    for colega, sabores_colega in colegas.items():
        if not check_sabores(pessoa, sabores_colega):
            raise SaboresNaoBatem()
        tci = calcula_tci(sabores_colega, pessoa)
        if menor_tci is None:
            menor_tci = tci
            pessoa_mais_parecida = colega 
        else:
            if tci < menor_tci:
                menor_tci = tci
                pessoa_mais_parecida = colega

    return pessoa_mais_parecida


if __name__ == '__main__':
    unittest.main()



