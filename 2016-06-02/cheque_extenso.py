#!/usr/bin/env python
import unittest
import re
import math


class ChequeExtenso(unittest.TestCase):
    def test_digito_extenso(self):
        digito = digito_extenso(1)
        self.assertEqual(digito, 'um')

    def test_dezena_extenso(self):
        dezena = dezena_extenso(1)
        self.assertEqual(dezena, 'dez')
        self.assertEqual(dezena_extenso(9), 'noventa')

    def test_centena_extenso(self):
        centena = centena_extenso(2)
        self.assertEqual(centena, 'duzentos')
        self.assertEqual(centena_extenso(9), 'novecentos')

    def test_numero_extenso_2digitos(self):
        self.assertEqual(extenso(21), 'vinte e um')

    def test_numero_extenso_3digitos(self):
        self.assertEqual(extenso(124), 'cento e vinte e quatro')

    def test_numero_extenso_4digitos(self):
        self.assertEqual(extenso(2234),
                         'dois mil duzentos e trinta e quatro')
    
    def test_numero_extenso_6digitos(self):
        self.assertEqual(extenso(623456), 
                        'seiscentos e vinte e tres mil quatrocentos e cinquenta e seis')
 
    def test_cheque_extenso_2digitos(self):
        self.assertEqual(cheque_extenso(20), 'vinte reais')



def digito_extenso(digito=0):
    digito = int(digito)
    digitos = {
        0: 'zero',
        1: 'um',
        2: 'dois',
        3: 'tres',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
    }

    return digitos[digito]

def dezena_extenso(digito):
    digito = int(digito)
    dezena = {
        0: '',
        1: 'dez',
        2: 'vinte',
        3: 'trinta',
        4: 'quarenta',
        5: 'cinquenta',
        6: 'sessenta',
        7: 'setenta',
        8: 'oitenta',
        9: 'noventa',
    }
    return dezena[digito]

def centena_extenso(digito):
    digito = int(digito)
    centenas = {
        0: '',
        1: 'cento',
        2: 'duzentos',
        3: 'trezentos',
        4: 'quatrocentos',
        5: 'quinhentos',
        6: 'seiscentos',
        7: 'setecentos',
        8: 'oitocentos',
        9: 'novecentos',
    }
    return centenas[digito]


def extenso(numero):
    classificacao = {
            0: ('',''),
            1: ('',''),
            2: ('mil', 'mil'),
            3: ('milhao', 'milhoes'),
            4: ('bilhao', 'bilhoes')
        }
    funcoes = [centena_extenso, dezena_extenso, digito_extenso]
    str_numero = str(numero)
    digitos = list(str_numero)
    tamanho = len(str_numero)
    num_trincas = int(math.ceil(tamanho / 3.))

    if tamanho % 3:
        str_numero = '0' * (3 - tamanho % 3) + str_numero

    resultado_com_e = []

    for trinca in re.findall(r"\d\d\d", str_numero):
        result = []
        if int(trinca[0]):
            result.append(centena_extenso(trinca[0]))
        if int(trinca[1]):
            result.append(dezena_extenso(trinca[1]))
        if int(trinca[2]):
            result.append(digito_extenso(trinca[2]))
        resultado_com_e.append(' e '.join(result))
        if classificacao[num_trincas][0]:
            resultado_com_e.append(classificacao[num_trincas][0])
        num_trincas-=1
    return ' '.join(resultado_com_e)


def cheque_extenso(valor):
    valor_str = "%.2f" % valor
    reais, centavos = valor_str.split('.')
    valor_reais = extenso(reais)
    if int(centavos):
        valor_centavos = extenso(centavos)
    else:
        valor_centavos = ""

    return '%s reais' % valor_reais

if __name__ == '__main__':
    unittest.main()
