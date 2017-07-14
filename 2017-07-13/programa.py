#!/usr/bin/env python

import unittest


class ProgramaTestCase(unittest.TestCase):

    def test_simple_product(self):
        self.assertEqual(product(1, "1"), 1)

    def test_product_with_two_numbers(self):
        self.assertEqual(product(1, "12"), 2)

    def test_product_with_two_numbers2(self):
        self.assertEqual(product(1, "21"), 2)

    def test_product_with_two_numbers3(self):
        self.assertEqual(product(2, "22"), 4)

    def test_product_with_various_numbers(self):
        self.assertEqual(product(6, "73167176531330624919225119674426574742355349194934"), 23520)

    def test_mawkee(self):
        self.assertEqual(product(2, "0000"), 0)

def product(x, seq):
    retorno = 0
    for m in range(len(seq)-x+1):
        bigger_product = 1
        for i in seq[m:x+m]:
            bigger_product *= int(i)
        if bigger_product > retorno:
            retorno = bigger_product
    return retorno


if __name__ == '__main__':
    unittest.main()
