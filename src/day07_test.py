# flake8: noqa
from .day07 import star1, star2, build_tree

TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split(
    "\n"
)


def test_build_tree():
    root = build_tree(TEST_INPUT)
    assert len(root.dirs) == 2
    assert len(root.files) == 2


def test_star1():
    assert star1(TEST_INPUT) == 95437


def test_star2():
    pass
