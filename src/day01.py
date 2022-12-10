def star_1() -> None:
    input = read_input("day01.txt")
    elves = [sum(e) for e in input]
    print(f"Max calories: {max(elves)}")


def star_2() -> None:
    input = read_input("day01.txt")
    elves = [sum(e) for e in input]
    top3 = sorted(elves, reverse=True)[0:3]
    print(f"Top3 calories: {sum(top3)}")


def read_input(filepath: str) -> list[list[int]]:
    """Read input and parse it."""
    text = list()
    entry: list[int]
    with open(filepath, "r") as f:
        entry = list()
        for line in f:
            if line == "\n":
                text.append(entry)
                entry = list()
            else:
                entry.append(int(line))
    if len(entry) > 0:
        text.append(entry)
    return text


if __name__ == "__main__":
    star_1()
    star_2()
