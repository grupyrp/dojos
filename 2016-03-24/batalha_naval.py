#!/usr/bin/env python

import itertools
import unittest
import random
from copy import deepcopy


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
        board = Board(3, 2)
        matrix = [[0, 0],
                  [0, 0],
                  [0, 0]]
        assert board.matrix == matrix

    def test_create_matrix(self):
        matrix = [[0 for i in range(10)] for j in range(10)]
        board = Board(10, 10)
        assert board.matrix == matrix

    def test_ship_init_count(self):
        board = Board(10, 10)
        flat_board = list(itertools.chain(*board.matrix))
        assert flat_board.count(0) == 100

    def test_ship_count_with_ships(self):
        board = Board(10, 10)
        board.add_ships(_random=False)
        flat_board = list(itertools.chain(*board.matrix))
        for key, value in Board.ships.items():
            self.assertEqual(value, flat_board.count(key))

    def test_ship_random_count_with_ships(self):
        board = Board(10, 10)
        board.add_ships(_random=True)
        flat_board = list(itertools.chain(*board.matrix))
        for key, value in Board.ships.items():
            self.assertEqual(value, flat_board.count(key))

    def test_validatepos(self):
        board = Board(10, 10)
        self.assertTrue(board.validate_pos(0, 0))
        board.matrix[2][3] = 1
        self.assertFalse(board.validate_pos(2, 3))

    def test_constants(self):
        self.assertEqual(Board.CARRIER, 1)
        self.assertEqual(Board.BATTLESHIP, 2)
        self.assertEqual(Board.DESTROYER, 3)
        self.assertEqual(Board.SUBMARINE, 4)
        self.assertEqual(Board.PATROL_BOAT, 5)

    def test_miss_attack(self):
        board = Board(10, 10)
        self.assertEqual(board.receive_attack(0, 0), False)

    def test_hit_attack(self):
        board = Board(10, 10)
        board.add_ships()
        self.assertEqual(board.receive_attack(0, 0), True)

    def test_empty_attack_list(self):
        board = Board(10, 10)
        self.assertEqual(len(board.history), 0)

    def test_insert_attack_list_empty_board(self):
        board = Board(10, 10)
        board.receive_attack(0, 0)
        self.assertEqual(board.history[0], (0, 0, False))

    def test_insert_attack_list_full_board(self):
        board = Board(10, 10)
        board.add_ships()
        board.receive_attack(0, 0)
        self.assertEqual(board.history[0], (0, 0, True))

    def test_gameover_false(self):
        board = Board(10, 10)
        board.add_ships()
        self.assertFalse(board.game_over())

    def test_plot_empty_board(self):
        board = Board(10, 10)
        board_str = """------------
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
------------"""
        self.assertEqual(board_str, board.plot())

    def test_plot_full_board(self):
        board = self._get_full_board()
        board_str = """------------
|11111~~~~~|
|2222~~~~~~|
|333~~~~~~~|
|444~~~~~~~|
|55~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
------------"""
        self.assertEqual(board_str, board.plot())

    def test_plot_full_board_with_shots(self):
        board = self._get_full_board()
        board.receive_attack(1, 1)
        board.receive_attack(2, 2)
        board.receive_attack(8, 0)
        board.receive_attack(9, 0)
        board.receive_attack(4, 1)
        board.receive_attack(1, 4)

        board_str = """------------
|11111~~~~~|
|2x22o~~~~~|
|33x~~~~~~~|
|444~~~~~~~|
|5x~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|o~~~~~~~~~|
|o~~~~~~~~~|
------------"""
        self.assertEqual(board_str, board.plot())

    def test_plot_full_board_with_shots_without_ship(self):
        board = self._get_full_board()
        board.receive_attack(1, 1)
        board.receive_attack(2, 2)
        board.receive_attack(8, 0)
        board.receive_attack(9, 0)
        board.receive_attack(4, 1)
        board.receive_attack(1, 4)

        board_str = """------------
|~~~~~~~~~~|
|~x~~o~~~~~|
|~~x~~~~~~~|
|~~~~~~~~~~|
|~x~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|o~~~~~~~~~|
|o~~~~~~~~~|
------------"""
        self.assertEqual(board_str, board.plot(show_ships=False))

    def test_add_ships(self):
        board = Board(10, 10)
        self.assertTrue(board.add_ship(0, 0, board.HORIZONTAL, board.CARRIER))
        self.assertTrue(board.add_ship(1, 0, board.VERTICAL, board.BATTLESHIP))

    def test_add_ship_same_place_fail(self):
        board = Board(10, 10)
        self.assertTrue(board.add_ship(0, 0, board.HORIZONTAL, board.CARRIER))
        self.assertFalse(board.add_ship(0, 0, board.HORIZONTAL, board.CARRIER))

    def test_add_ship_out_of_board_matrix_restore(self):
        board = Board(10, 10)
        board.add_ship(9, 9, board.HORIZONTAL, board.CARRIER)
        flat_board = list(itertools.chain(*board.matrix))
        self.assertEquals(100, flat_board.count(0))

    def test_add_ship_colliding_ships_matrix_restore(self):
        board = Board(10, 10)
        board.add_ship(0, 1, board.HORIZONTAL, board.CARRIER)
        current_matrix = deepcopy(board.matrix)

        board.add_ship(0, 0, board.HORIZONTAL, board.CARRIER)
        self.assertEquals(current_matrix, board.matrix)

    def test_fail_add_ships_out_of_boards(self):
        board = Board(10, 10)
        self.assertFalse(board.add_ship(10, 0, board.VERTICAL,
                                        board.SUBMARINE))
        self.assertFalse(board.add_ship(9, 0, board.VERTICAL, board.CARRIER))

    def test_matrix_fail_add_ships(self):
        board = Board(10, 10)
        matrix = deepcopy(board.matrix)
        board.add_ship(10, 0, board.VERTICAL, board.SUBMARINE)
        self.assertEqual(matrix, board.matrix)

    def _get_full_board(self):
        board = Board(10, 10)
        board.add_ship(0, 0, board.HORIZONTAL, board.CARRIER)
        board.add_ship(1, 0, board.HORIZONTAL, board.BATTLESHIP)
        board.add_ship(2, 0, board.HORIZONTAL, board.DESTROYER)
        board.add_ship(3, 0, board.HORIZONTAL, board.SUBMARINE)
        board.add_ship(4, 0, board.HORIZONTAL, board.PATROL_BOAT)
        return board


class Board(object):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'

    CARRIER = 1
    BATTLESHIP = 2
    DESTROYER = 3
    SUBMARINE = 4
    PATROL_BOAT = 5

    ships = {
        CARRIER: 5,   # porta-avioes
        BATTLESHIP: 4,   # encouracado
        DESTROYER: 3,   # destroier
        SUBMARINE: 3,   # submarino
        PATROL_BOAT: 2    # barco de patrulha
    }

    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.create_matrix()
        self.history = []
        self.attacks = {}

    def add_ship(self, row, col, orientation, ship):
        matrix = deepcopy(self.matrix)
        result = True

        ship_size = self.ships[ship]

        if (orientation == self.VERTICAL and row + ship_size > self.rows) or \
           (orientation == self.HORIZONTAL and col + ship_size > self.cols):
            return False

        if orientation == self.HORIZONTAL:
            for i in range(col, col + self.ships[ship]):
                if self.matrix[row][i] == 0:
                    self.matrix[row][i] = ship
                else:
                    result = False
                    break
        else:
            for i in range(row, row + self.ships[ship]):
                if self.matrix[i][col] == 0:
                    self.matrix[i][col] = ship
                else:
                    result = False
                    break

        if not result:
            self.matrix = matrix

        return result

    def add_ships(self, _random=False):
        if _random:
            for key, value in self.ships.items():
                consegui = False
                while not consegui:
                    x = random.randint(0, self.rows - 1)
                    y = random.randint(0, self.cols - 1)
                    orientation = random.choice([self.HORIZONTAL,
                                                 self.VERTICAL])
                    consegui = self.add_ship(x, y, orientation, key)
        else:
            i = 0
            for key, value in self.ships.items():
                self.add_ship(i, 0, self.HORIZONTAL, key)
                i += 1

    def validate_pos(self, x, y):
        return self.matrix[x][y] == 0

    def create_matrix(self):
        self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def receive_attack(self, row, col):
        value = self.matrix[row][col]
        self.history.append((row, col, bool(value)))
        key = '{}-{}'.format(row, col)
        self.attacks[key] = bool(value)
        return bool(value)

    def game_over(self):
        shipcount = sum(self.ships.values())
        hitcount = len(filter(lambda x: x[2], set(self.history)))
        return hitcount == shipcount

    def plot(self, show_ships=True):
        if list(itertools.chain(*self.matrix)).count(0) == 100:
            return """------------
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
|~~~~~~~~~~|
------------"""

        else:
            plot = []
            start = '-' * 12 + '\n'
            end = '-' * 12
            for ridx, row in enumerate(self.matrix):
                plot.append('|')

                for cidx, col in enumerate(row):
                    key = '{}-{}'.format(ridx, cidx)
                    if key in self.attacks:
                        if self.attacks[key]:
                            v = 'x'
                        else:
                            v = 'o'
                    else:
                        if show_ships:
                            v = "~" if col == 0 else str(col)
                        else:
                            v = "~"
                    plot.append(v)
                plot.append('|\n')

        return start + "".join(plot) + end


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
