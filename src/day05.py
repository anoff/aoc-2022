from typing import TypedDict


Move = TypedDict("Move", {"from": int, "to": int, "count": int})


def star1(text: list[str]) -> str:
    crates, moves = parse_input(text)
    for mv in moves:
        for i in range(0, mv["count"]):
            f = mv["from"] - 1  # compensate for 0-offset
            t = mv["to"] - 1
            crates[t].insert(0, crates[f].pop(0))

    tops = "".join([c[0] for c in crates])
    return tops


def star2(text: list[str]) -> int:
    pass


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r") as f:
        return [line.replace("\n", "") for line in f.readlines()]


def parse_input(text: list[str]) -> tuple[list[list[str]], list[Move]]:
    """Parse input into list of crates and list of Moves."""
    crates_str, moves_str = "\n".join(text).split("\n\n")
    moves = [
        Move(
            {
                "to": int(m.split(" ")[5]),
                "count": int(m.split(" ")[1]),
                "from": int(m.split(" ")[3]),
            }
        )
        for m in moves_str.split("\n")
        if len(m) > 0
    ]
    crates: list[list[str]] = list()
    crates_lst = crates_str.split("\n")
    crates_count = len(crates_lst[-1].split("  "))
    for n in range(0, crates_count):
        crates.append(list())
    for row in crates_lst[0:-1]:
        for ix in range(0, crates_count):
            pos = 1 + (ix * 4)
            if row[pos].strip() != "":
                crates[ix].append(row[pos])
    print(crates)
    return (crates, moves)


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day05.txt'))}")
    print(f"Star2: {star2(read_input('./day05.txt'))}")
