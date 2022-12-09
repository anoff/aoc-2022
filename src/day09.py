from __future__ import annotations
from typing import TypeAlias


Move: TypeAlias = tuple[str, int]


class P2D:
    """Two dimensional point."""

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: P2D) -> P2D:
        """Add to another point."""
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: P2D) -> P2D:
        """Substract another point."""
        self.x -= other.x
        self.y -= other.y
        return self

    def __eq__(self, other: object) -> bool:
        """Compare equality."""
        if isinstance(other, P2D):
            return self.x == other.x and self.y == other.y
        return self == other

    def distance(self, other: P2D) -> int:
        """Calculate the (Manhattan) distance to another point."""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def distancexy(self, other: P2D) -> P2D:
        """Return the distance **from** self to the other point."""
        return P2D(other.x - self.x, other.y - self.y)

    def copy(self) -> P2D:
        """Return a copy of itself.

        Useful if you want to store the current location."""
        return P2D(self.x, self.y)

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


class Rope:
    head: P2D
    tail: P2D
    tail_history: list[P2D]  # list of all positions the tail has been

    def __init__(self, x: int, y: int):
        self.head = P2D(x, y)
        self.tail = P2D(x, y)
        self.tail_history = [self.tail.copy()]

    def move(self, direction: str) -> Rope:
        """Move Rope by one step.

        Args:
            dir: U(p), D(own), L(eft), R(ight)
        """
        assert len(direction) == 1
        assert direction in "UDLR"
        if direction == "U":
            self.head.y += 1
        elif direction == "D":
            self.head.y -= 1
        elif direction == "L":
            self.head.x -= 1
        elif direction == "R":
            self.head.x += 1
        self._check_tail()
        return self

    def _check_tail(self) -> None:
        """Check tail distance and move if necessary.

        Also update self.tail_history if moving."""
        vec = self.tail.distancexy(self.head)
        dist = abs(vec.x) + abs(vec.y)
        if dist > 1:
            if vec.x != 0 and vec.y != 0:
                if dist > 2:
                    # if diagonal difference move diagonally
                    self.tail.x += vec.x // abs(vec.x)
                    self.tail.y += vec.y // abs(vec.y)
            else:
                self.tail.x += vec.x // max(abs(vec.x), 1)
                self.tail.y += vec.y // max(abs(vec.y), 1)
            # update tail history
            if self.tail not in self.tail_history:
                self.tail_history.append(self.tail.copy())

    def __repr__(self) -> str:
        return f"H[{self.head.x}, {self.head.y}], T[{self.tail.x}, {self.tail.y}]"


class Rope10:
    ropes: list[Rope]

    def __init__(self, x: int, y: int):
        self.ropes = []
        for _ in range(9):
            r = Rope(x, y)
            self.ropes.append(r)

    def move(self, direction: str) -> Rope10:
        """Move Rope by one step.

        Args:
            dir: U(p), D(own), L(eft), R(ight)
        """
        assert len(direction) == 1
        assert direction in "UDLR"
        if direction == "U":
            self.ropes[0].head.y += 1
        elif direction == "D":
            self.ropes[0].head.y -= 1
        elif direction == "L":
            self.ropes[0].head.x -= 1
        elif direction == "R":
            self.ropes[0].head.x += 1
        self.ropes[0]._check_tail()
        for n, r in enumerate(self.ropes[1:]):
            r.head.x = self.ropes[n].tail.x
            # n starts at 0, so ropes[n] refers to the previous element
            r.head.y = self.ropes[n].tail.y
            r._check_tail()

        return self


def star1(lines: list[str]) -> int:
    """Part1."""
    moves = parse_input(lines)
    rope = Rope(0, 0)
    for move in moves:
        for _ in range(move[1]):
            rope.move(move[0])
    return len(rope.tail_history)


def star2(lines: list[str]) -> int:
    """Part2."""
    moves = parse_input(lines)
    rope = Rope10(0, 0)
    for move in moves:
        for _ in range(move[1]):
            rope.move(move[0])
    return len(rope.ropes[-1].tail_history)


# 2296 too low
def parse_input(text: list[str]) -> list[Move]:
    """Convert text into list of moves."""
    out = []
    for line in text:
        direction, steps = line.split(" ")
        out.append((direction, int(steps)))
    return out


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r", encoding="utf8") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day09.txt'))}")
    print(f"Star2: {star2(read_input('./day09.txt'))}")
