#!/usr/bin/env python

import unittest


GUGA = 0
NADAL = 1

class TenisTestCase(unittest.TestCase):
    def test_new_game_score(self):
        game = Game()
        self.assertEqual(game.score, [0, 0])
    
    def test_game_point_player_a(self):
        game = Game()
        game.add_score(GUGA)
        self.assertEqual(game.score, [15, 0])
        game.add_score(GUGA)
        self.assertEqual(game.score, [30, 0])
        game.add_score(GUGA)
        self.assertEqual(game.score, [40, 0])

    def test_game_point_player_b(self):
        game = Game()
        game.add_score(NADAL)
        self.assertEqual(game.score, [0, 15])
        game.add_score(NADAL)
        self.assertEqual(game.score, [0, 30])
        game.add_score(NADAL)
        self.assertEqual(game.score, [0, 40])

    def test_game_point_player_ab(self):
        game = Game()
        game.add_score(GUGA)
        self.assertEqual(game.score, [15, 0])
        game.add_score(NADAL)
        self.assertEqual(game.score, [15, 15])
        game.add_score(NADAL)
        self.assertEqual(game.score, [15, 30])
        game.add_score(NADAL)
        self.assertEqual(game.score, [15, 40])

    def test_game_winner(self):
        game = Game()
        game.score = [40, 0]
        game.add_score(GUGA)
        self.assertEqual(game.winner, GUGA)

    def test_game_deuce_no_winner(self):
        game = Game()
        game.score = [40, 40]
        game.add_score(GUGA)    
        self.assertEqual(game.winner, None)

    def test_game_deuce_2pts_to_the_glory(self):
        game = Game()
        game.score = [40, 40]
        game.add_score(GUGA)    
        self.assertEqual(game.winner, None)
        game.add_score(GUGA)    
        self.assertEqual(game.winner, GUGA)


class Game:
    SCORE = [0, 15, 30, 40]

    def __init__(self):
        self.score = [0, 0]
        self.winner = None
        self.two_pts = None

    def add_score(self, player):
        cur_score = self.score[player]
        next_point_index = self.SCORE.index(cur_score) + 1
        try:
            self.score[player] = self.SCORE[next_point_index]
        except IndexError:
            if self.score[0] == self.score[1]:
                if self.two_pts == player:
                    self.winner = player
                    return
                self.two_pts = player
            else:
                self.winner = player



if __name__ == '__main__':
    unittest.main()
