from unittest import TestCase
from TicTacToeState import *


class Test(TestCase):
    def test_successors(self):
        s = TicTacToeState()
        print(successors(s, 'x'))
        s2 = TicTacToeState(board=[['x', ' ', ' '],
                                   ['o', ' ', ' '],
                                   ['x', ' ', ' ']])
        print(successors(s2, 'o'))


class Test(TestCase):
    def test_score_state(self):
        s = TicTacToeState()
        self.assertEqual(score_state(s), 0)
        s2 = TicTacToeState(board=[['x', ' ', ' '],
                                   ['o', ' ', ' '],
                                   ['x', ' ', ' ']])
        self.assertEqual(score_state(s2), 0)
        s3 = TicTacToeState(board=[['x', ' ', ' '],
                                   ['o', 'x', ' '],
                                   ['x', 'o', 'x']])
        self.assertEqual(score_state(s3), 1)
        s3 = TicTacToeState(board=[['x', 'x', ' '],
                                   ['o', 'o', 'o'],
                                   ['x', 'o', 'x']])
        self.assertEqual(score_state(s3), -1)


class Test(TestCase):
    def test_minimax(self):
        s = TicTacToeState()
        print(minimax(s, 'x'))
