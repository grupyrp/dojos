#!/usr/bin/env python

import unittest


def subconjunto_pa(conjunto):
    if len(conjunto) < 3:
        return []
    subconjuntos = []
    for r in range(1, len(conjunto)+1):
        for i in conjunto:
            parcial = []
            for n in range(1, len(conjunto) + 1):
                an = i + (n - 1) * r
                if an in conjunto:
                    parcial.append(an)
            if len(parcial) >= 3:
                subconjuntos.append(parcial)

    return subconjuntos


class PATestCase(unittest.TestCase):
    # def test_pa_minimo(self):
    #     conjunto = (1, 2)
    #     self.assertEqual(subconjunto_pa(conjunto), [])

    # def test_pa_simples(self):
    #     conjunto = (1, 2, 3)
    #     self.assertEqual(subconjunto_pa(conjunto), [[1, 2, 3]])

    def test_pa_longo(self):
        conjunto = (1, 2, 3, 5)
        self.assertEqual(subconjunto_pa(conjunto), [[1, 2, 3], [1, 3, 5]])


if __name__ == "__main__":
    unittest.main()
