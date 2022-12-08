from __future__ import annotations
from typing import TypeAlias

Trees: TypeAlias = list[list[int]]
TreeView: TypeAlias = list[list[bool]]


def check_visibility(trees: Trees, direction: tuple[int, int]) -> TreeView:
    """Check the visibilit of each tree from a direction.

    Args:
        trees: 2d map of tree heights
        direction: x,y position to view on the map
            1,0 means look to the right (view map from the left side)

    Returns:
        list of a bool map"""
    n_rows = len(trees)
    n_cols = len(trees[0])

    visible: TreeView = []
    for n in range(0, n_rows):
        visible.append([True] * n_cols)
    if direction == (1, 0):  # from left ->
        for y in range(0, n_rows):
            max_h = -1
            for x in range(0, n_cols):
                height = trees[y][x]
                if height > max_h:
                    max_h = height
                    if height == 9 and x < n_cols - 1:
                        visible[y][x + 1 :] = [False] * (n_rows - x + 1)
                else:
                    visible[y][x] = False
    elif direction == (0, 1):  # from top V
        for x in range(0, n_cols):
            max_h = -1
            for y in range(0, n_rows):
                height = trees[y][x]
                if height > max_h:
                    max_h = height
                    if height == 9:
                        for ny in range(y + 1, n_rows):
                            visible[ny][x] = False
                        continue
                else:
                    visible[y][x] = False
    elif direction == (-1, 0):  # from right <-
        for y in range(0, n_rows):
            max_h = -1
            for x in range(n_cols - 1, -1, -1):
                height = trees[y][x]
                if height > max_h:
                    max_h = height
                    if height == 9:
                        visible[y][0:x] = [False] * x
                        continue
                else:
                    visible[y][x] = False
    elif direction == (0, -1):  # from bottom ^
        for x in range(0, n_cols):
            max_h = -1
            for y in range(n_rows - 1, -1, -1):
                height = trees[y][x]
                if height > max_h:
                    max_h = height
                    if height == 9:
                        for ny in range(y - 1, -1, -1):
                            visible[ny][x] = False
                        continue
                else:
                    visible[y][x] = False
    return visible


def star1(lines: list[str]) -> int:
    """Part1."""
    trees = parse_input(lines)
    v1 = check_visibility(trees, (1, 0))
    v2 = check_visibility(trees, (0, 1))
    v3 = check_visibility(trees, (0, -1))
    v4 = check_visibility(trees, (-1, 0))
    total = v1
    total_trees = 0
    for y, _ in enumerate(total):
        for x, _ in enumerate(total[0]):
            total[y][x] = v1[y][x] | v2[y][x] | v3[y][x] | v4[y][x]
            if total[y][x]:
                total_trees += 1
    return total_trees


def scenic_score(trees: Trees, x0: int, y0: int) -> int:
    """Calculate the product of view distance in each direction."""
    trees_left, trees_right, trees_top, trees_bottom = [0, 0, 0, 0]
    n_rows = len(trees)
    n_cols = len(trees[0])
    # look right ->
    start_h = trees[y0][x0]
    for x in range(x0 + 1, n_cols):
        height = trees[y0][x]
        trees_right += 1
        if height >= start_h:
            break
    # look left <-
    for x in range(x0 - 1, -1, -1):
        height = trees[y0][x]
        trees_left += 1
        if height >= start_h:
            break
    # look down V
    for y in range(y0 + 1, n_rows):
        height = trees[y][x0]
        trees_bottom += 1
        if height >= start_h:
            break
    # look up ^
    for y in range(y0 - 1, -1, -1):
        height = trees[y][x0]
        trees_top += 1
        if height >= start_h:
            break
    score = trees_left * trees_right * trees_top * trees_bottom
    return score


def star2(lines: list[str]) -> int:
    """Part2."""
    trees = parse_input(lines)
    max_score = 0
    for y, _ in enumerate(trees):
        for x, _ in enumerate(trees[0]):
            score = scenic_score(trees, x, y)
            if score > max_score:
                print(x, y)
                max_score = score
    return max_score


def parse_input(text: list[str]) -> Trees:
    """Convert text to int map."""
    trees = []
    for line in text:
        trees.append([int(c) for c in line])
    return trees


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r", encoding="utf8") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day08.txt'))}")
    print(f"Star2: {star2(read_input('./day08.txt'))}")
