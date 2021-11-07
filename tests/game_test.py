import unittest
from models.game import Game
from models.team import Team

class TestGame(unittest.TestCase):
    def setUp(self):
        self.team_1 = Team("England", 4)
        self.team_2 = Team("Australia", 2)
        self.game = Game(self.team_1, self.team_2, 55, 56, "England")

    # @unittest.skip("Delete this line to run the test")
    def test_game__has_teams(self):
        self.assertEqual("England and Australia", f"{self.game.team_1.name} and {self.game.team_2.name}")

    # @unittest.skip("Delete this line to run the test")
    def test_game__teams_have_runs(self):
        self.assertEqual("55, 56", f"{self.game.team_1_runs}, {self.game.team_2_runs}")


    # @unittest.skip("Delete this line to run the test")
    # def test_game__has_winner(self):
    #     game = Game("England", "West Indies", 56, 55, "England")
    #     self.assertEqual("England", self.game.determine_winner(game))
    #     game = Game("England", "West Indies", 54, 55, "England")
    #     self.assertEqual("West Indies", self.game.determine_winner(game))
    #     game = Game("England", "West Indies", 55, 55, "England")
    #     self.assertEqual(None, self.game.determine_winner(game))