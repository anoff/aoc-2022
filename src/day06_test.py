# flake8: noqa
from .day06 import star1, star2


def test_star1():
    assert star1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert star1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert star1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert star1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert star1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_star2():
    assert star2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert star2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert star2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert star2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert star2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
