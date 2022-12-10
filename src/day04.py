def star1(text: list[str]) -> int:
    count = 0
    for g in text:
        # get start/end positions
        e1, e2 = g.split(",")
        e1_1, e1_2 = [int(c) for c in e1.split("-")]
        e2_1, e2_2 = [int(c) for c in e2.split("-")]
        if (e1_1 <= e2_1 and e1_2 >= e2_2) or (e2_1 <= e1_1 and e2_2 >= e1_2):
            count += 1
    return count


def star2(text: list[str]) -> int:
    count = 0
    for g in text:
        # get start/end positions
        e1, e2 = g.split(",")
        e1_1, e1_2 = [int(c) for c in e1.split("-")]
        e2_1, e2_2 = [int(c) for c in e2.split("-")]
        s1 = set(range(e1_1, e1_2 + 1))
        s2 = set(range(e2_1, e2_2 + 1))
        if len(list(s1.intersection(s2))) > 0:
            count += 1
    return count


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('day04.txt'))}")
    print(f"Star2: {star2(read_input('day04.txt'))}")
