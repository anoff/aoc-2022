def hand_score(sign: str) -> int:
    if sign == "X":
        return 1
    elif sign == "Y":
        return 2
    elif sign == "Z":
        return 3
    return 0


def round_score(sign1: str, sign2: str) -> int:
    if sign1 == "A":
        if sign2 == "Y":
            return 6
        elif sign2 == "Z":
            return 0
        else:
            return 3
    elif sign1 == "B":
        if sign2 == "X":
            return 0
        elif sign2 == "Z":
            return 6
        else:
            return 3
    elif sign1 == "C":
        if sign2 == "X":
            return 6
        elif sign2 == "Y":
            return 0
        else:
            return 3
    return 0


def is_win(sign1: str, sign2: str) -> bool:
    return round_score(sign1, sign2) == 6


def get_hand(sign1: str, result: str) -> str:
    if sign1 == "A":
        if result == "Y":
            return "X"
        elif result == "Z":
            return "Y"
        else:
            return "Z"
    elif sign1 == "B":
        if result == "X":
            return "X"
        elif result == "Z":
            return "Z"
        else:
            return "Y"
    elif sign1 == "C":
        if result == "X":
            return "Y"
        elif result == "Y":
            return "Z"
        else:
            return "X"
    return "-"


def star1(text: list[str]) -> int:
    score = 0
    for line in text:
        sign1, sign2 = line.strip().split(" ")
        score += round_score(sign1, sign2) + hand_score(sign2)
    return score


def star2(text: list[str]) -> int:
    score = 0
    for line in text:
        sign1, result = line.strip().split(" ")
        sign2 = get_hand(sign1, result)
        score += round_score(sign1, sign2) + hand_score(sign2)
    return score


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('day02.txt'))}")
    print(f"Star2: {star2(read_input('day02.txt'))}")
