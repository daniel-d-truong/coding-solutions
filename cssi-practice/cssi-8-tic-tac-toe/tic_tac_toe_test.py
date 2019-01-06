from tic_tac_toe import Board
import unittest

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        pass

    # Test:
    # 1 2 1
    # 2 1 2
    # 2 1 2
    def test_simple_draw(self):
        board = Board()
        board.reset_board()
        self.assertEqual(0, board.player_move(2,2,2))
        self.assertEqual(0, board.player_move(0,0,1))
        self.assertEqual(0, board.player_move(0,1,2))
        self.assertEqual(0, board.player_move(0,2,1))
        self.assertEqual(0, board.player_move(1,0,2))
        self.assertEqual(0, board.player_move(1,1,1))
        self.assertEqual(0, board.player_move(1,2,2))
        self.assertEqual(0, board.player_move(2,1,1))
        self.assertEqual(-1, board.player_move(2,0,2))

    # Test:
    # 1 1 1
    # 2 2 0
    # 0 0 0
    def test_win_row1(self):
        board = Board()
        board.reset_board()
        self.assertEqual(0, board.player_move(0,0,1))
        self.assertEqual(0, board.player_move(1,0,2))
        self.assertEqual(0, board.player_move(0,1,1))
        self.assertEqual(0, board.player_move(1,1,2))
        self.assertEqual(1, board.player_move(0,2,1))

    # Test:
    # 2 1 1
    # 1 2 0
    # 0 0 2
    def test_win_diag1(self):
        board = Board()
        board.reset_board()
        self.assertEqual(0, board.player_move(1,0,1))
        self.assertEqual(0, board.player_move(0,0,2))
        self.assertEqual(0, board.player_move(0,1,1))
        self.assertEqual(0, board.player_move(1,1,2))
        self.assertEqual(0, board.player_move(0,2,1))
        self.assertEqual(1, board.player_move(2,2,2))

    # Test:
    # 2 1 1
    # 2 1 0
    # 2 0 0
    def test_win_col1(self):
        board = Board()
        board.reset_board()
        self.assertEqual(0, board.player_move(1,1,1))
        self.assertEqual(0, board.player_move(0,0,2))
        self.assertEqual(0, board.player_move(0,1,1))
        self.assertEqual(0, board.player_move(1,0,2))
        self.assertEqual(0, board.player_move(0,2,1))
        self.assertEqual(1, board.player_move(2,0,2))

    # def test_invalid_move(self):
    #     board = Board()
    #     board.reset_board()
    #     self.assertEqual(0, board.player_move(1,1,1))
    #     self.assertEqual(None, board.player_move(1,1,2))

if __name__ == '__main__':
    unittest.main()
