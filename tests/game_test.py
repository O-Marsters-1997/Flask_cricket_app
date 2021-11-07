import unittest
from models.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("England", "West Indies", 55, 56, "England")

    # @unittest.skip("Delete this line to run the test")
    def test_game__has_teams(self):
        self.assertEqual("England and West Indies", f"{self.game.team_1} and {self.game.team_2}")

    # @unittest.skip("Delete this line to run the test")
    # def test_game__has_winner(self):
    #     game = Game("England", "West Indies", 56, 55, "England")
    #     self.assertEqual("England", self.game.determine_winner(game))
    #     game = Game("England", "West Indies", 54, 55, "England")
    #     self.assertEqual("West Indies", self.game.determine_winner(game))
    #     game = Game("England", "West Indies", 55, 55, "England")
    #     self.assertEqual(None, self.game.determine_winner(game))