from __future__ import annotations
from typing import TypeAlias, Union

Height: TypeAlias = int


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


class Node:
    """Single node for graph.

    f: total cost of the node
    g: distance between the current node and the start node
    h: (heuristic) estimated distance from the current node to the target"""

    parent: Union[Node, None]
    pos: P2D
    g: int
    h: int
    f: int

    def __init__(self, pos: P2D, parent: Union[Node, None] = None):
        self.pos = pos
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other: object) -> bool:
        """Check if two nodes are identical (position)."""
        if isinstance(other, Node):
            return self.pos == other.pos
        elif isinstance(other, P2D):
            return self.pos == other
        return super().__eq__(other)


class Hoshi:
    """A*-ish implementation."""

    area: list[str]
    open: list[Node]
    closed: list[Node]
    distance: int  # distance between neighboring nodes

    def __init__(self, area: list[str]):
        self.area = area
        self.open = []
        self.closed = []
        self.distance = 1

    def estimate_cost(self, source: Node, target: Node) -> int:
        """H: heuristic estimate distance cost to target.

        Manhattan distance"""
        return source.pos.distance(target.pos)

    def get_children(self, node: Node) -> list[Node]:
        """Calculate all possible children.

        Only checks if within area boundary,
        not if they are reachable or already passed."""
        # possible directions to move in x,y
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nodes = []
        for d in dirs:
            x = node.pos.x + d[0]
            y = node.pos.y + d[1]
            pos = P2D(x, y)
            if self.is_pos_in_bounds(pos):
                nodes.append(Node(pos, node))
        return nodes

    def add_open(self, node: Node) -> None:
        """Add new node to open list.

        If node already exists in open list, keep the one
        that has shortest distance from start (g-value)."""
        if node in self.open:
            for existing in self.open:
                if existing == node:
                    if existing.f > node.f:
                        self.open.remove(existing)
                        self.open.append(node)
        else:
            self.open.append(node)

    def is_pos_in_bounds(self, pos: P2D) -> bool:
        """Check if a position is within map bounds."""
        x = pos.x
        y = pos.y
        return (x >= 0 and x < len(self.area[0])) and (y >= 0 and y < len(self.area))

    def is_valid_move(self, start: Node, target: Node) -> bool:
        """Check if target node can be reached from start node."""
        target_h = self.area[target.pos.y][target.pos.x]
        start_h = self.area[start.pos.y][start.pos.x]
        if start_h == "S":
            return True
        if target_h == "E":
            if start_h == "z":
                return True
            return False
        return ord(target_h) - ord(start_h) <= 1

    @staticmethod
    def get_path(node: Node) -> list[Node]:
        """Backtrack the complete path to a node."""
        current = node

        if not isinstance(current, Node):
            return []
        path = [current]
        while current.parent:
            path.append(current.parent)
            current = current.parent
        return path[::-1]

    def find_path(self, start: P2D, target: P2D) -> Node:
        """Do the path finding thing.

        Returns:
            list of all nodes in path"""
        self.open = [Node(start)]
        self.closed = []
        while len(self.open) > 0:
            self.open.sort(key=lambda n: n.f)
            current = self.open.pop(0)
            self.closed.append(current)

            if current == target:
                return current  # TODO: get_path by going back all parents

            children = self.get_children(current)
            for child in children:
                if child not in self.closed:
                    if self.is_valid_move(current, child):
                        child.g = current.g + self.distance
                        child.h = child.pos.distance(target)
                        child.f = child.g + child.f
                        self.add_open(child)


def step_size(source: str, target: str) -> int:
    """Height of the step from source to target."""
    return ord(target) - ord(source)


def find_start_goal(lines: list[str]) -> tuple[P2D]:
    """Extract start and end points from list."""
    start = P2D(-1, -1)
    end = P2D(-1, -1)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = P2D(x, y)
            elif c == "E":
                end = P2D(x, y)
    return (start, end)


def star1(lines: list[str]) -> int:
    """Part1.

    Well..guess A-star was a bit too much for this.
    Turns out you can just step from a..b..c
    Did not realize you have to move a->z before going to the end
    """
    start, goal = find_start_goal(lines)
    star = Hoshi(lines)
    node = star.find_path(start, goal)
    p = Hoshi.get_path(node)
    # for n in p:
    #     print(n.pos)
    return len(p) - 1


def star2(lines: list[str]) -> str:
    """Part2.

    This should be prettier..but smart brute force might work?
    Realized there are too many a's, but the pattern is that
    there is only few bs and each b has an a next to it.
    So finding the closest b + 1 should give the answer.
    """
    start, goal = find_start_goal(lines)
    star = Hoshi(lines)

    possible_starts = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "b":
                possible_starts.append(P2D(x, y))

    node = star.find_path(start, goal)
    p = Hoshi.get_path(node)
    shortest_path = len(p) - 1
    possible_starts.sort(key=lambda s: s.distance(goal))
    print(f"Found {len(possible_starts)} starting positions..")
    for s in possible_starts:
        node = star.find_path(s, goal)
        p = Hoshi.get_path(node)
        distance = len(p) - 1
        if distance > 0:
            print(s, distance)
        if distance < shortest_path and distance > 0:
            shortest_path = distance

    return shortest_path + 1


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r", encoding="utf8") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day12.txt'))}")
    print(f"Star2: {star2(read_input('./day12.txt'))}")
