#!/usr/bin/env python

import unittest

class Rougeth():

    def __init__(self, initial_pos, facing):
        self.x = initial_pos[0]
        self.y = initial_pos[1]
        self.facing = facing

    def run(self):
        if self.facing == 'N':
            self.y += 1
        elif self.facing == 'S':
            self.y -= 1
        elif self.facing == 'E':
            self.x += 1
        elif self.facing == 'W':
            self.x -= 1

    def validate(self, path):
        valid = 'ALR'
        for chr in path.upper():
            if chr not in valid:
                return False
        return True

    def turn(self, dir):
        if self.facing == 'N':
            if dir == 'L':
                self.facing = 'W'
            elif dir == 'R':
                self.facing = 'E'
        elif self.facing == 'S':
            if dir == 'L':
                self.facing = 'E'
            elif dir == 'R':
                self.facing = 'W'
        elif self.facing == 'E':
            if dir == 'L':
                self.facing = 'N'
            elif dir == 'R':
                self.facing = 'S'
        elif self.facing == 'W':
            if dir == 'L':
                self.facing = 'S'
            elif dir == 'R':
                self.facing = 'N'

    def start(self, path):
        if self.validate(path):
            for chr in path:
                if chr == 'A':
                    self.run()
                else:
                    self.turn(chr)
            return 'x={}, y={}, facing={}'.format(self.x, self.y, self.facing)
        return 'Erro'



class ProgramaTestCase(unittest.TestCase):
    def test_create_rougeth(self):
        rougeth = Rougeth([0,0], 'N')
        self.assertEqual(rougeth.x, 0)
        self.assertEqual(rougeth.y, 0)
        self.assertEqual(rougeth.facing, 'N')

    def test_run_N(self):
        rougeth = Rougeth([0,0], 'N')
        rougeth.run()
        self.assertEqual(rougeth.x, 0)
        self.assertEqual(rougeth.y, 1)


    def test_turn(self):
        rougeth = Rougeth([0,0], 'N')
        rougeth.turn('L')
        self.assertEqual(rougeth.facing, 'W')

    def test_turn_4_times(self):
        rougeth = Rougeth([0,0], 'N')
        rougeth.turn('L')
        rougeth.turn('R')
        rougeth.turn('R')
        rougeth.turn('R')
        self.assertEqual(rougeth.facing, 'S')

    def test_validate_string(self):
        rougeth = Rougeth([0, 0], 'N')
        self.assertFalse(rougeth.validate('ABOBORA'))
        self.assertFalse(rougeth.validate('rLWA'))
        self.assertTrue(rougeth.validate('RALLALARA'))

    def test_turn_twice(self):
        rougeth = Rougeth([0,0], 'N')
        rougeth.turn('L')
        rougeth.turn('R')
        self.assertEqual(rougeth.facing, 'N')

    def test_run_S(self):
        rougeth = Rougeth([0,0], 'S')
        rougeth.run()
        self.assertEqual(rougeth.x, 0)
        self.assertEqual(rougeth.y, -1)

    def test_run_W(self):
        rougeth = Rougeth([0,0], 'W')
        rougeth.run()
        self.assertEqual(rougeth.x, -1)
        self.assertEqual(rougeth.y, 0)

    def test_run_E(self):
        rougeth = Rougeth([0,0], 'E')
        rougeth.run()
        self.assertEqual(rougeth.x, 1)
        self.assertEqual(rougeth.y, 0)

    def test_start_only_turn(self):
        rougeth = Rougeth([0,0], 'E')
        rougeth.start('R')
        self.assertEqual(rougeth.x, 0)
        self.assertEqual(rougeth.y, 0)
        self.assertEqual(rougeth.facing, 'S')

    def test_start_only_walk(self):
        rougeth = Rougeth([0,0], 'N')
        response = rougeth.start('A')
        self.assertEqual(response, 'x=0, y=1, facing=N')

    def test_start_only_moonwalk(self):
        rougeth = Rougeth([0,0], 'N')
        response = rougeth.start('RLAAARALL')
        self.assertEqual(response, 'x=1, y=3, facing=W')

    def test_start_error(self):
        rougeth = Rougeth([0,0], 'N')
        response = rougeth.start(':wq')
        self.assertEqual(response, 'Erro')

    def test_start_with_lowers(self):
        rougeth = Rougeth([0,0], 'N')
        response = rougeth.start('rlaaarall')
        self.assertEqual(response, 'x=1, y=3, facing=W')


if __name__ == '__main__':
    unittest.main()
