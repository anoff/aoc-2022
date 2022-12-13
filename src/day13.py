from __future__ import annotations
import json
from typing import TypeAlias, Union

packet: TypeAlias = Union[int, list]


def is_correct_order(p1: packet, p2: packet) -> Union[bool, None]:
    """Return true if two packets are in correct order.

    Returns None if no decision can be made."""

    if isinstance(p1, list) and isinstance(p2, list):
        for ix, one in enumerate(p1):
            if ix > len(p2) - 1:
                return False
            two = p2[ix]
            response = is_correct_order(one, two)
            if isinstance(response, bool):
                return response
        return True
    elif isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return True
        if p1 > p2:
            return False
    elif isinstance(p1, int) and isinstance(p2, list):
        response = is_correct_order([p1], p2)
        if isinstance(response, bool):
            return response
    elif isinstance(p1, list) and isinstance(p2, int):
        response = is_correct_order(p1, [p2])
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


def star2(lines: list[str]) -> int:
    """Part2."""
    return 0


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
