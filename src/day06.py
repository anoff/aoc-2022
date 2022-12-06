def find_end_of_marker(text: str, marker_len: int) -> int:
    for n in range(marker_len, len(text)):
        chars = text[n - marker_len : n]
        assert len(chars) == marker_len
        s = set(list(chars))
        n_unique_chars = len(s)
        if n_unique_chars == marker_len:
            return n
    return -1


def star1(text: str) -> int:
    return find_end_of_marker(text, 4)


def star2(text: str) -> int:
    return find_end_of_marker(text, 14)


def read_input(filepath: str) -> str:
    """Read input."""
    with open(filepath, "r") as f:
        return [line.replace("\n", "") for line in f.readlines()][0]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day06.txt'))}")
    print(f"Star2: {star2(read_input('./day06.txt'))}")
