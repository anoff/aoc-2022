# flake8: noqa
from .day12 import star1, star2

TEST_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split(
    "\n"
)


def test_star1() -> None:
    assert star1(TEST_INPUT) == 31


def test_star2() -> None:
    assert star2(TEST_INPUT) == 0
