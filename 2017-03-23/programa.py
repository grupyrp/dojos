#!/usr/bin/env python

import unittest

def LookAndSay(num):

    contador = 0
    referencia = ''
    retorno = ''
    num = str(num)
    referencia = num[0]
    for indice, char in enumerate(num):
        if referencia != char :
            retorno += str(contador) + referencia
            contador = 1
            referencia = char
        elif referencia == char:
            contador += 1
    retorno += str(contador) + char
    return int(retorno)

class DojoTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_test_num_1(self):
        self.assertEqual(11, LookAndSay(1))

    def test_test_num_11(self):
        self.assertEqual(21, LookAndSay(11))

    def test_test_num_21(self):
        self.assertEqual(1211, LookAndSay(21))

    def test_test_num_111221(self):
        self.assertEqual(312211, LookAndSay(111221))

    def test_test_num_9664025(self):
        self.assertEqual(192614101215, LookAndSay(9664025))



if __name__ == '__main__':
    unittest.main()
