def get_duplicate_item(list1: str, list2: str) -> str:
    s1 = set(list1)
    s2 = set(list2)
    common = list(s1.intersection(s2))
    if len(common):
        return common[0]
    return ""


def split_string(text: str) -> tuple[str, str]:
    l = len(text)
    return (text[0 : l // 2], text[l // 2 :])


def get_score(item: str) -> int:
    """Calculate the item score."""
    n = ord(item[0]) - 96  # offset to "a"
    if n <= 0:
        return (
            n + 32 + 26
        )  # uppercase letters have smaller offset than lower case -> compensate for offset and add 26 priorities for lowercase
    else:
        return n


def star1(input) -> int:
    score = 0
    for rucksack in input:
        (list1, list2) = split_string(rucksack)
        duplicate = get_duplicate_item(list1, list2)
        score += get_score(duplicate)
    return score


def get_badge(rucksacks: list[str]) -> str:
    """Identify the common item (badge) that all rucksacks have in common.

    Args:
        rucksacks: should be a list of three strings

    Returns:
        common item (single character as string)
    """
    s1 = set(rucksacks[0])
    s2 = set(rucksacks[1])
    s3 = set(rucksacks[2])
    common = list(s1.intersection(s2).intersection(s3))
    if len(common):
        return common[0]
    return ""


def star2(input) -> int:
    # split into groups of 3
    groups = [input[i : i + 3] for i in range(0, len(input), 3)]
    scores = [get_score(get_badge(g)) for g in groups]
    return sum(scores)


def read_input(filepath: str) -> list[str]:
    """Read input."""
    input = list()
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('day03.txt'))}")
    print(f"Star2: {star2(read_input('day03.txt'))}")
