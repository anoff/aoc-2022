from __future__ import annotations
from typing import Union
from os import path


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Dir:
    dirs: list[Dir]
    files: list[File]
    path: str
    name: str
    parent: Union[Dir, None]

    def __init__(self, name: str, parent: Dir):
        self.name = name
        self.files = list()
        self.dirs = list()
        if parent:
            self.parent = parent
            self.path = path.join(parent.path, name)
        else:
            self.path = "/"
            self.parent = None

    def add(self, item: Union[Dir, File]) -> Dir:
        if isinstance(item, File):
            self.files.append(item)
        elif isinstance(item, Dir):
            self.dirs.append(item)
        return self

    def get_size(self) -> int:
        """Calculate the size of this folder (and all subfolders)."""
        files = sum([f.size for f in self.files])
        dirs = sum([d.get_size() for d in self.dirs])
        return files + dirs

    def get_subdir(self, name: str) -> Dir:
        """Get instance of a previously added sub directory."""
        for d in self.dirs:
            if d.name == name:
                return d
        raise ValueError(f"Directory could not be found. name={name}")

    def get_subdirs(self) -> list[Dir]:
        """Get all sub directories (recursively)."""
        dirs = self.dirs
        for d in dirs:
            dirs += d.get_subdirs()
        return dirs


def build_tree(lines: list[str]) -> Dir:
    root = Dir("/", None)
    curdir = root
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "ls":
                pass
            elif parts[1] == "cd":
                target = parts[2]
                if target == "..":
                    assert isinstance(curdir.parent, Dir)
                    curdir = curdir.parent
                elif target == "/":
                    curdir = root
                else:
                    curdir = curdir.get_subdir(target)
        elif parts[0] == "dir":
            name = parts[1]
            curdir.add(Dir(name, parent=curdir))
        else:  # should be a file
            name = parts[1]
            size = int(parts[0])
            curdir.add(File(name, size))
    return root

def star1(lines: list[str]) -> int:
    root = build_tree(lines)
    dirs = root.get_subdirs()
    total = 0
    for d in dirs:
        size = d.get_size()
        if size <= 100000:
            total += size
    return total


def star2(text: str) -> int:
    pass


def read_input(filepath: str) -> str:
    """Read input."""
    with open(filepath, "r") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day07.txt'))}")
    print(f"Star2: {star2(read_input('./day07.txt'))}")
