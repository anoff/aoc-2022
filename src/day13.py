from __future__ import annotations
import json
from typing import TypeAlias, Union
import functools

packet: TypeAlias = Union[int, list]


def is_correct_order(
    p1: packet, p2: packet, is_nested: bool = False
) -> Union[bool, None]:
    """Return true if two packets are in correct order.

    Returns None if no decision can be made.

    Args:
        is_nested: set to True if this is a nested call."""

    if isinstance(p1, list) and isinstance(p2, list):
        for ix, one in enumerate(p1):
            if ix > len(p2) - 1:
                return False
            two = p2[ix]
            response = is_correct_order(one, two, is_nested=True)
            if isinstance(response, bool):
                return response
        if not is_nested:
            # only return true if this is outermost loop
            return True
    elif isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return True
        if p1 > p2:
            return False
    elif isinstance(p1, int) and isinstance(p2, list):
        response = is_correct_order([p1], p2, is_nested=True)
        if isinstance(response, bool):
            return response
    elif isinstance(p1, list) and isinstance(p2, int):
        response = is_correct_order(p1, [p2], is_nested=True)
        if isinstance(response, bool):
            return response


def star1(lines: list[str]) -> int:
    """Part1."""
    packets = parse_input(lines)
    count = 0
    for ix, p in enumerate(packets):
        if is_correct_order(p[0], p[1]):
            count += ix + 1
    return count


def sort_packets(packets: list[packet]) -> list[packet]:
    """Sort that from top to bottom the order is correct."""

    # def compare(a: packet, b: packet) -> int:
    #     result = is_correct_order(a, b)
    #     if result is True:
    #         return -1
    #     if result is False:
    #         return 1
    #     return 0

    # key_fn = functools.cmp_to_key(compare)

    # sorted_packets = sorted(packets, key=key_fn)

    cnt = 0
    is_sorted = False
    while not is_sorted and cnt < 100000:
        cnt += 1
        for ix, n in enumerate(packets[:-1]):
            result = is_correct_order(packets[ix], packets[ix + 1])
            if result is False:
                put_away = packets.pop(ix)
                packets.append(put_away)
                break
        if result != False:
            is_sorted = True

    return packets


def star2(lines: list[str]) -> int:
    """Part2."""
    packets = [[[2]], [[6]]]
    for p in parse_input(lines):
        packets.append(p[0])
        packets.append(p[1])

    s_list = sort_packets(packets)
    divider = 1
    for ix, p in enumerate(s_list):
        if p == [[2]] or p == [[6]]:
            divider *= ix + 1

    return divider


# 23165 too high


def parse_input(text: list[str]) -> list[list[packet]]:
    """Convert text."""
    out = []
    for pair in "\n".join(text).split("\n\n"):
        parts = pair.split("\n")
        out.append([json.loads(parts[0]), json.loads(parts[1])])
    return out


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r", encoding="utf8") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day13.txt'))}")
    print(f"Star2: {star2(read_input('./day13.txt'))}")
