from .day02 import get_hand, hand_score, is_win, round_score, star1, star2


def test_is_win():
    assert is_win("A", "Y") is True
    assert is_win("B", "X") is False
    assert is_win("C", "Z") is False


def test_round_score():
    assert round_score("A", "Y") == 6
    assert round_score("B", "X") == 0
    assert round_score("C", "Z") == 3


def test_hand_score():
    assert hand_score("X") == 1
    assert hand_score("Y") == 2
    assert hand_score("Z") == 3


def test_star1():
    input = """A Y
B X
C Z""".split(
        "\n"
    )
    assert star1(input) == 15


def test_get_hand():
    assert get_hand("A", "X") == "Z"
    assert get_hand("A", "Y") == "X"
    assert get_hand("B", "X") == "X"
    assert get_hand("C", "Z") == "X"


def test_star2():
    input = """A Y
B X
C Z""".split(
        "\n"
    )
    assert star2(input) == 12
