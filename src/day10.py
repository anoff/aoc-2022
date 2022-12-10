from __future__ import annotations
from typing import Callable, TypeAlias

OpCode: TypeAlias = tuple[str, int]


class Enigma:
    """My own calculation machine."""

    x: int
    n_cycle: int  # cycle counter
    hooks: list[
        tuple[Callable[[int], bool], Callable[[Enigma], None]]
    ]  # some hooks that run on cycle updates

    def __init__(self, start_value: int = 1):
        self.x = start_value
        self.n_cycle = 0
        self.hooks = []

    def exec(self, opcode: OpCode) -> None:
        """Execute one operation."""
        op, val = opcode
        if op == "addx":
            self.cycle()
            self.cycle()
            self.x += val
        elif op == "noop":
            self.cycle()

    def cycle(self) -> int:
        """Execute one cycle."""
        self.n_cycle += 1
        for h in self.hooks:
            fn = h[0]
            if fn(self.n_cycle):
                h[1](self)
        return self.n_cycle

    def register_hook(
        self, fn_check: Callable[[int], bool], fn_fire: Callable[[Enigma], None]
    ) -> None:
        """Register a hook that will be checked each time the enigma cycles once.

        Args:
            fn_check: A function that returns true if it should fire
                gets passed the current cycle count
            fn_fire: the function that should fire if the first function returns true
                gets the enigma as argument
        """
        self.hooks.append((fn_check, fn_fire))


class CRT:
    """Multiline monitor."""

    image: list[list[str]]
    n_rows: int
    n_cols: int
    cursor: list[int]  # x,y

    def __init__(self, rows: int = 6, cols: int = 40):
        self.n_cols = cols
        self.n_rows = rows
        self.cursor = [0, 0]
        self.image = []
        for _ in range(rows):
            self.image.append([" " for _ in range(cols)])

    def print(self) -> None:
        """Print CRT screen to terminal."""
        for line in self.image:
            print("".join(line))

    def draw(self, sprite_center: int) -> None:
        """Update image."""
        if self.cursor[0] >= sprite_center - 1 and self.cursor[0] <= sprite_center + 1:
            self.image[self.cursor[1]][self.cursor[0]] = "#"
        else:
            self.image[self.cursor[1]][self.cursor[0]] = "."

    def move_cursor(self) -> None:
        """Move cursor to next position."""
        if self.cursor[0] >= self.n_cols - 1:
            self.cursor[0] = 0
            self.cursor[1] += 1
            if self.cursor[1] > self.n_rows - 1:
                self.cursor[1] = 0
        else:
            self.cursor[0] += 1


def star1(lines: list[str]) -> int:
    """Part1."""
    opcodes = parse_input(lines)
    e = Enigma()
    signals = []

    def hook(e: Enigma) -> None:
        signals.append(e.x * e.n_cycle)

    e.register_hook(lambda cycle: (cycle - 20) % 40 == 0, hook)
    for opcode in opcodes:
        e.exec(opcode)

    return sum(signals)


def star2(lines: list[str]) -> str:
    """Part2."""
    opcodes = parse_input(lines)
    e = Enigma()
    c = CRT()

    def hook(e: Enigma) -> None:
        c.draw(e.x)
        c.move_cursor()

    e.register_hook(lambda cycle: True, hook)
    for opcode in opcodes:
        e.exec(opcode)

    c.print()
    return "--CHECK PRINT OUTPUT FOR LETTERS--"


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
    print(f"Star1: {star1(read_input('./day10.txt'))}")
    print(f"Star2: {star2(read_input('./day10.txt'))}")
