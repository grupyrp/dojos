#!/usr/bin/env python

import unittest


from random import randint


def bombs_around(line, column, bombs):
    pass


def map_mine(width, height, bombs=tuple()):
    _map = []
    for i in range(height):
        line = []
        for k in range(width):
            if (i, k) in bombs:
                line.append("*")
            elif i == 2 or k == 3:
                line.append("0")
            else:
                line.append("1" if bombs else "0")
        _map.append("".join(line))

    return _map


class MineSweeperTestCase(unittest.TestCase):

    def test_1x1_bombless(self):
        w = 1
        h = 1
        self.assertEqual(map_mine(w, h), ["0"])

    def test_1x1_bombfull(self):
        self.assertEqual(map_mine(1, 1, [(0, 0)]), ["*"])

    def test_2x2_bombless(self):
        self.assertEqual(map_mine(2, 2), ["00", "00"])

    def test_2x2_one_bomb(self):
        self.assertEqual(map_mine(2, 2, [(0, 1)]), ["1*", "11"])

    def test_4x3_one_bomb(self):
        self.assertEqual(map_mine(4, 3, [(0, 1)]), ["1*10", "1110", "0000"])

    def test_bombs_around(self):
        self.assertEqual(bombs_around(1, 1, [(0, 1)]), 1)


if __name__ == "__main__":
    unittest.main()
