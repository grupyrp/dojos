#!/usr/bin/env python
import unittest


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
    digitos = list(str(numero))
    #if len(digitos) > 3:
    #    digitos = digitos[-1:-4]
    funcoes = [digito_extenso, dezena_extenso, centena_extenso]
    results = []

    for funcao in funcoes:
        if not digitos:
            break
        digito = digitos.pop()
        extenso_ = funcao(digito)
        results.insert(0, extenso_)
    
    if digitos:
        milhar = extenso(''.join(digitos)) + ' mil '
    else:
        milhar = ''
    
    return milhar + ' e '.join(results)


if __name__ == '__main__':
    unittest.main()
