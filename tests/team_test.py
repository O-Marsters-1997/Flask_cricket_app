import unittest
from models.team import Team


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("England", 4)

    # Attribute Tests

    # @unittest.skip("Delete this line to run the test")
    def test_team_has_name(self):
        self.assertEqual("England", self.team.name)

    # @unittest.skip("Delete this line to run the test")
    def test_team_has_points(self):
        self.assertEqual(4, self.team.points)

    # @unittest.skip("Delete this line to run the test")
    def test_team_add_points(self):
        self.team.victory(self.team)
        self.assertEqual(6, self.team.points)

    # Crud action Tests

