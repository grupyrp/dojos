#!/usr/bin/env python

import itertools
import unittest


class BattleShipTest(unittest.TestCase):
    def test_board_size(self):
        game = BattleShip()
        assert game.get_size() == 100

    def test_ships_qt(self):
        game = BattleShip()
        assert len(game.get_all_ships()) == 10

    def test_create_board(self):
        board = Board(10, 10)
        assert board.cols == 10
        assert board.rows == 10

    def test_create_board_small(self):
        board = Board(2, 3)
        matrix = [[0, 0],
                  [0, 0],
                  [0, 0]]
        assert board.matrix == matrix

    def test_create_matrix(self):
        matrix = [[0 for i in range(10)] for j in range(10)]
        board = Board(10, 10)
        assert board.matrix == matrix

    def test_ship_counts(self):
        ships = {
            1: 5,   # porta-avioes
            2: 4,   # encouracado
            3: 3,   # destroier
            4: 3,   # submarino
            5: 2    # barco de patrulha
        }
        board = Board(10, 10)
        flat_board = list(itertools.chain(*board.matrix))
        assert flat_board.count(0) == 100
        assert ships[1] == flat_board.count(1)


class Board(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.create_matrix()

    def create_matrix(self):
        self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]


class BattleShip(object):
    size = [10, 10]
    boards = ()

    def get_size(self):
        return self.size[0] * self.size[1]

    def get_all_ships(self):
        return range(10)

    def create_board(self):
        return [self.size[0], self.size[1]]


if __name__ == '__main__':
    unittest.main()
