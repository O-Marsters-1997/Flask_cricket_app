import unittest
from models.game import Game
from models.team import Team

import repositories.group_1_game_repository as group_1_game_repository
import repositories.group_2_game_repository as group_2_game_repository

class TestGame(unittest.TestCase):
    def setUp(self):
        self.team_1 = Team("England", 4, 4)
        self.team_2 = Team("Australia", 2, 2)
        self.game = Game(self.team_1, self.team_2, 58, 56, "2021-11-08 00:00:00.00")

    # @unittest.skip("Delete this line to run the test")
    def test_game__has_teams(self):
        self.assertEqual("England and Australia", f"{self.game.team_1.name} and {self.game.team_2.name}")

    # @unittest.skip("Delete this line to run the test")
    def test_game__teams_have_runs(self):
        self.assertEqual("58, 56", f"{self.game.team_1_runs}, {self.game.team_2_runs}")

    # @unittest.skip("Delete this line to run the test")
    def test_game__has_date(self):
        self.assertEqual("2021-11-08 00:00:00.00", self.game.game_date)

    # @unittest.skip("Delete this line to run the test")
    def test_game__has_winner(self):
        self.assertEqual("The winner is England", self.game.determine_winner(self.game))
        self.game = Game(self.team_1, self.team_2, 54, 55, "2021-11-08 00:00:00.00")
        self.assertEqual("The winner is Australia", self.game.determine_winner(self.game))
        self.game = Game(self.team_1, self.team_2, 55, 55, "2021-11-08 00:00:00.00")
        self.assertEqual(f"The winner is {None}", self.game.determine_winner(self.game))