# flake8: noqa
from .day13 import parse_input, sort_packets, star1, star2, is_correct_order

TEST_INPUT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split(
    "\n"
)


def test_is_correct_order() -> None:
    assert (
        is_correct_order(
            [[6]],
            [
                [[], 2, 9, 4],
                [],
                [[[], [0]], [[7, 0, 10, 8], [10, 5, 5, 4, 1], 0, 6]],
                [],
            ],
        )
        == False
    )
    assert is_correct_order([[4, 4], 4, 4, 4], [[4, 4], 4, 4]) == False
    assert is_correct_order([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == True
    assert is_correct_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == True
    assert is_correct_order([[1], [2, 3, 4]], [[1], 4]) == True
    assert is_correct_order([9], [[8, 7, 6]]) == False
    assert (
        is_correct_order(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
        )
        == False
    )


def test_star1() -> None:
    assert star1(TEST_INPUT) == 13


def test_sort_packets() -> None:
    packets = [[[2]], [[6]]]
    for p in parse_input(TEST_INPUT):
        packets.append(p[0])
        packets.append(p[1])

    s_list = sort_packets(packets)
    assert s_list[0] == []
    assert s_list[3] == [1, 1, 3, 1, 1]
    assert s_list[7] == [1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
    assert s_list[9] == [[2]]


def test_star2() -> None:
    assert star2(TEST_INPUT) == 140
