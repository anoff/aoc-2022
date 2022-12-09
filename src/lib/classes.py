"""Useful classes."""
from __future__ import annotations


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

    def __eq__(self, other: object):
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
