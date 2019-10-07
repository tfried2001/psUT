from tennis import score_tennis

import pytest


@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                        [(0,0, "Love-All"),
                        (1,1,"Fifteen-All"),
                        (2,2,"Thirty-All"),
                        (0,2,"Love-Thirty"),
                        (1,2,"Fifteen-Thirty"),
                        (2,4,"Win for Player 2"),
                        ])
def test_score_tenis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score

