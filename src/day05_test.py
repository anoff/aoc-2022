from .day05 import star1, star2, parse_input


TEST_INPUT = """    [D]    """  # noqa: W291
"""[N] [C]    """  # noqa: W291
"""[Z] [M] [P]"""
""" 1   2   3 """  # noqa: W291
"""
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".split(
    "\n"
)


def test_parse_input():
    crates, moves = parse_input(TEST_INPUT)
    assert crates == [["N", "Z"], ["D", "C", "M"], ["P"]]
    assert moves[0]["from"] == 2
    assert moves[0]["to"] == 1
    assert moves[1]["count"] == 3
    assert moves[3]["to"] == 2


def test_star1():
    assert star1(TEST_INPUT) == "CMZ"


def test_star2():
    assert star2(TEST_INPUT) == 4
