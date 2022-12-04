from .day04 import (
    star1,
    star2,
)


TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split(
    "\n"
)


def test_star1():
    assert star1(TEST_INPUT) == 2


def test_star2():
    assert star2(TEST_INPUT) == 4
