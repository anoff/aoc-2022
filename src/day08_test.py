# flake8: noqa
from .day08 import star1, star2, check_visibility, parse_input

TEST_INPUT = """30373
25512
65332
33549
35390""".split(
    "\n"
)


def test_check_visibility():
    trees = parse_input(TEST_INPUT)
    visible = check_visibility(trees, (1, 0))
    assert visible[0][0] == True
    assert visible[1][0] == True
    assert visible[2][0] == True
    assert visible[3][0] == True
    assert visible[4][0] == True
    assert visible[1][1] == True
    assert visible[1][2] == False
    assert visible[1][3] == False
    assert visible[2][1] == False
    assert visible[2][2] == False
    assert visible[2][3] == False
    assert visible[3][2] == True
    visible = check_visibility(trees, (-1, 0))
    assert visible[0][0] == False
    assert visible[1][0] == False
    assert visible[2][0] == True
    assert visible[3][4] == True
    assert visible[4][4] == True
    assert visible[1][1] == False
    assert visible[1][2] == True
    assert visible[1][3] == False
    assert visible[2][1] == True
    assert visible[2][2] == False
    assert visible[2][3] == True
    assert visible[3][2] == False
    visible = check_visibility(trees, (0, 1))
    assert visible[0][0] == True
    assert visible[0][1] == True
    assert visible[0][2] == True
    assert visible[0][3] == True
    assert visible[0][4] == True
    assert visible[1][0] == False
    assert visible[2][0] == True
    assert visible[1][1] == True
    assert visible[1][2] == True
    assert visible[1][3] == False
    assert visible[2][1] == False
    assert visible[2][2] == False
    assert visible[2][3] == False
    assert visible[3][2] == False
    visible = check_visibility(trees, (0, -1))
    assert visible[4][0] == True
    assert visible[4][1] == True
    assert visible[4][2] == True
    assert visible[4][3] == True
    assert visible[4][4] == True
    assert visible[1][0] == False
    assert visible[2][0] == True
    assert visible[1][1] == False
    assert visible[1][2] == False
    assert visible[1][3] == False
    assert visible[2][1] == False
    assert visible[2][2] == False
    assert visible[2][3] == False
    assert visible[3][2] == True


def test_star1():
    assert star1(TEST_INPUT) == 21


def test_star2():
    pass
