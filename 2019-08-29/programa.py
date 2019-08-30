#!/usr/bin/env python

import unittest
from pprint import pprint

ESQUERDA, DIREITA, CIMA, BAIXO = 0, 1, 2, 3

class NegativoProibido(Exception):
    pass


def espiral(largura, altura):
    if 0 in (largura, altura):
        return [[]]
    if largura < 0 or altura < 0:
        raise NegativoProibido()
    matrix = []
    for i in range(altura):
        matrix.append([])
        for j in range(largura):
            matrix[i].append(-1)

    contador = 1
    linha = coluna = 0
    estado = 'D'

    while(contador <= largura * altura):
        matrix[linha][coluna] = contador
        estado,linha,coluna = walk(estado,linha,coluna,matrix) 
        contador += 1
    return matrix

def walk(estado, linha, coluna, matrix):
    if estado == 'D': 
        if(disponivel(linha, coluna + 1, matrix)):
            return estado, linha, coluna + 1
        else:
            return 'B', linha + 1, coluna
    if estado == 'B': 
        if(disponivel(linha + 1, coluna, matrix)):
            return estado, linha + 1, coluna
        else:
            return 'E', linha, coluna - 1
    if estado == 'E': 
        if(disponivel(linha, coluna - 1, matrix)):
            return estado, linha, coluna - 1
        else:
            return 'C', linha - 1, coluna
    
    if estado == 'C': 
        if(disponivel(linha -1, coluna, matrix)):
            return estado, linha -1, coluna
        else:
            return 'D', linha, coluna + 1
    
    


def disponivel(linha, coluna, matrix):
    try:
        return matrix[linha][coluna] == -1
    except:
        return False

class ProgramaTestCase(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(espiral(0, 0), [[]])

    def test_matrix_with_one(self):
        esperado = [[1]]
        self.assertEqual(espiral(1, 1), esperado)

    def test_matrix_1_2(self):
        self.assertEqual(espiral(1, 2), [[1], [2]])

    def test_altura_matrix_3_4(self):
        retorno = espiral(3, 4)
        self.assertEqual(len(retorno), 4)

    def test_largura_matrix_3_4(self):
        retorno = espiral(3, 4)
        for arr in retorno:
            self.assertEqual(len(arr), 3)

    def test_altura_largura_matrix_enormona(self):
        retorno = espiral(33, 44)
        self.assertEqual(len(retorno), 44)
        for arr in retorno:
            self.assertEqual(len(arr), 33)

    def test_matrix_completa_2_1(self):
        retorno = espiral(2, 1)
        self.assertEqual(retorno, [[1, 2]])
    
    def test_matrix_completa_2_3(self):
        retorno = espiral(2, 3)
        self.assertEqual(retorno, [[1, 2], [6, 3], [5, 4]])

    def test_negativo(self):
        with self.assertRaises(NegativoProibido):
            espiral(-1,-1)

if __name__ == "__main__":
    unittest.main()
