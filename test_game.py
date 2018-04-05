from unittest import TestCase
import Game


class TestGame(TestCase):

    def test_update(self):
        test_game = Game.Game()
        cell_no = 0
        test_game.update(cell_no, test_game.playerX)
        self.assertEqual(test_game.cells[0], 'X')

    def test_is_winner(self):
        test_game = Game.Game()
        test_game.update(0, test_game.playerX)
        test_game.update(1, test_game.playerX)
        test_game.update(2, test_game.playerX)
        test_game.update(3, test_game.playerO)
        test_game.update(4, test_game.playerO)
        self.assertTrue(test_game.is_winner(test_game.playerX) and test_game.cells[0] == "X")

    def test_is_tie(self):
        test_game = Game.Game()
        test_game.update(0, test_game.playerX)
        test_game.update(1, test_game.playerX)
        test_game.update(2, test_game.playerO)
        test_game.update(3, test_game.playerO)
        test_game.update(4, test_game.playerO)
        test_game.update(5, test_game.playerX)
        test_game.update(6, test_game.playerX)
        test_game.update(7, test_game.playerX)
        test_game.update(8, test_game.playerO)
        self.assertTrue(test_game.is_tie())

    def test_whose_turn(self):
        test_game = Game.Game()
        test_game.playerX = "testPlayerX"
        test_game.playerO = "testPlayerO"
        test_game.update(0, test_game.playerX)
        test_game.update(2, test_game.playerO)
        test_game.update(1, test_game.playerX)
        test_game.update(3, test_game.playerO)
        expected_player = test_game.playerX
        self.assertEqual(test_game.whose_turn(), expected_player)

    def test_reset(self):
        test_game = Game.Game()
        test_game.update(0, test_game.playerX)
        test_game.update(1, test_game.playerX)
        test_game.update(2, test_game.playerO)
        test_game.update(3, test_game.playerO)
        test_game.update(4, test_game.playerO)
        test_game.update(5, test_game.playerX)
        test_game.update(6, test_game.playerX)
        test_game.update(7, test_game.playerX)
        test_game.update(8, test_game.playerO)
        test_game.reset()
        expected_cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(test_game.cells, expected_cells)


if __name__ == '__main__':
    TestCase.main()

