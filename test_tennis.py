import unittest
from tennis import score_tennis



class TennisTest(unittest.TestCase):

    def test_score_tennis(self):
        test_cases = [
            (0,0, "Love-All"),
            (0,1,"Fifteen-All"),
            (2,2,"Thirty-All"),
            (0,2,"Love-Thirty"),
            (1,2,"Fifteen-Thirty"),
            (2,4,"Win for Player 2"),
        ]
        for player1_points, player2_points, expected_score in test_cases:
            with self.subTest(f"{player1_points}, {player2_points} -> {expected_score}"):
                self.assertEqual(expected_score, score_tennis(player1_points, player2_points))

    def test_0_0_love_all(self):
        self.assertEqual("Love-All", score_tennis(0, 0))

    def test_1_1_fifteen_all(self):
        self.assertEqual("Fifteen-All", score_tennis(1, 1))

    def test_2_2_thirty_all(self):
        self.assertEqual("Thirty-All", score_tennis(2, 2))

