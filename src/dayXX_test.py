# flake8: noqa
from .day11 import star1, star2

TEST_INPUT = """
""".split(
    "\n"
)


def test_star1() -> None:
    assert star1(TEST_INPUT) == 0


def test_star2() -> None:
    assert star2(TEST_INPUT) == 0
