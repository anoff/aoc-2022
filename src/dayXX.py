from __future__ import annotations
from typing import Callable, TypeAlias

OpCode: TypeAlias = tuple[str, int]


def star1(lines: list[str]) -> int:
    """Part1."""
    return 0


def star2(lines: list[str]) -> str:
    """Part2."""
    return 0


def parse_input(text: list[str]) -> list[OpCode]:
    """Convert text into list of operation codes."""
    out = []
    for line in text:
        parts = line.split(" ")
        if len(parts) > 1:
            out.append((parts[0], int(parts[1])))
        else:
            out.append((parts[0], 0))
    return out


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r", encoding="utf8") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day11.txt'))}")
    print(f"Star2: {star2(read_input('./day11.txt'))}")
