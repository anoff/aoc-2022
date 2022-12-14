from .day03 import (
    get_duplicate_item,
    split_string,
    get_score,
    star1,
    get_badge,
    star2,
)


TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
    "\n"
)


def test_get_duplicate_item() -> None:
    assert get_duplicate_item("vJrwpWtwJgWr", "hcsFMMfFFhFp") == "p"
    assert get_duplicate_item("PmmdzqPrV", "vPwwTWBwg") == "P"


def test_split_string() -> None:
    assert split_string("vJrwpWtwJgWrhcsFMMfFFhFp") == ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
    assert split_string("PmmdzqPrVvPwwTWBwg") == ("PmmdzqPrV", "vPwwTWBwg")


def test_get_score() -> None:
    assert get_score("p") == 16
    assert get_score("P") == 42


def test_star1() -> None:
    assert star1(TEST_INPUT) == 157


def test_get_badge() -> None:
    assert (
        get_badge(
            """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg""".split(
                "\n"
            )
        )
        == "r"
    )
    assert (
        get_badge(
            """wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
                "\n"
            )
        )
        == "Z"
    )


def test_star2() -> None:
    assert star2(TEST_INPUT) == 70
