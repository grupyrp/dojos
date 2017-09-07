#!/usr/bin/env python

import unittest

class MatrixTestCase(unittest.TestCase):
    def test_create_matrix_empty(self):
        matrix = Matrix(0, 0)
        self.assertEqual(matrix.board, [])
        self.assertEqual(matrix.pos, (0, 0))

    def test_initialize_small_matrix(self):
        matrix = Matrix(1, 1)
        self.assertEqual(matrix.board, [[0]])

    def test_walk_left_false(self):
        matrix = Matrix(2, 2)
        self.assertFalse(matrix.left())

    def test_walk_left_true(self):
        matrix = Matrix(2, 2)
        matrix.pos = (1, 1)
        self.assertTrue(matrix.left())
        self.assertEqual(matrix.pos, (1, 0))

    def test_walk_right_false(self):
        matrix = Matrix(2, 2)
        matrix.pos = (1, 1)
        self.assertFalse(matrix.right())

    def test_walk_right_true(self):
        matrix = Matrix(2, 2)
        self.assertTrue(matrix.right())
        self.assertEqual(matrix.pos, (0, 1))

    def test_walk_down_false(self):
        matrix = Matrix(2, 2)
        matrix.pos = (1, 1)
        self.assertFalse(matrix.down())

    def test_walk_down_true(self):
        matrix = Matrix(2, 2)
        matrix.pos = (0, 1)
        self.assertTrue(matrix.down())
        self.assertEqual(matrix.pos, (1, 1))

    def test_walk_up_false(self):
        matrix = Matrix(2, 2)
        self.assertFalse(matrix.up())

    def test_initialize_medium_matrix(self):
        matrix = Matrix(4, 4)
        self.assertEqual(matrix.board, [[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

    def test_build_small_matrix(self):
        matrix = Matrix(1, 1)
        matrix.build()
        self.assertEqual(matrix.board, [[1]])

    def test_build_single_line_matrix(self):
        matrix = Matrix(1, 10)
        matrix.build()
        self.assertEqual(matrix.board, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    # def test_build_multi_line_matrix(self):
    #     matrix = Matrix(2, 4)
    #     matrix.build()
    #     self.assertEqual(matrix.board, [[1, 2, 3, 4],
    #                                     [8, 7, 6, 5]])

DIRECTIONS = ['right', 'down', 'left', 'up']


class WalkerTestCase(unittest.TestCase):

    def setUp(self):
        self.walker = Walker()

    def test_walker_creation(self):
        self.assertEqual(self.walker.current, 1)

    def test_walker_next(self):
        self.walker.next()
        self.assertEqual(self.walker.current, 2)


class Walker:
    def __init__(self, initial=1, increment=1):
        self.increment = increment
        self.current = initial

    def next(self):
        self.current += self.increment
        return self.current


class Matrix:
    def __init__(self, lines, columns, walker = None):
        self.lines = lines
        self.columns = columns
        self.matrix = [[0 for e in range(columns)] for i in range(lines)]
        self.walker = walker or Walker()
        self.pos = (0, 0)

    def left(self):
        if self.pos[1] - 1 < 0:
            return False
        nextpos = (self.pos[0], self.pos[1] - 1)
        nextval = self.matrix[nextpos[0]][nextpos[1]]

        if not nextval:  # Yes, we can
            self.pos = nextpos
            self.nextval = self.walker.current
            self.walker.next()
            return True
        return False

    def right(self):
        nextpos = (self.pos[0], self.pos[1] + 1)
        try:
            nextval = self.matrix[nextpos[0]][nextpos[1]]
        except IndexError:
            return False

        if not nextval:  # Yes, we can
            self.pos = nextpos
            self.nextval = self.walker.current
            self.walker.next()
            return True
        return False

    def down(self):
        nextpos = (self.pos[0] + 1, self.pos[1])
        try:
            nextval = self.matrix[nextpos[0]][nextpos[1]]
        except IndexError:
            return False

        if not nextval:  # Yes, we can
            self.pos = nextpos
            self.nextval = self.walker.current
            self.walker.next()
            return True
        return False

    def up(self):
        if self.pos[0] - 1 < 0:
            return False
        # nextpos = (self.pos[0] - 1, self.pos[1])
        # nextval = self.matrix[nextpos[0]][nextpos[1]]

        # if not nextval:  # Yes, we can
        #     self.pos = nextpos
        #     self.nextval = self.walker.current
        #     self.walker.next()
        #     return True
        # return False

    def build(self):


        for line in range(self.lines):
            for column in range(self.columns):
                self.matrix[line][column] = self.walker.current
                self.walker.next()

    @property
    def board(self):
        return self.matrix


if __name__ == '__main__':
    unittest.main()
