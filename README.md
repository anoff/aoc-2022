# Advent of Code 2022

> [adventofcode.com/2022](https://adventofcode.com/2022)

This will be the best advented code ever!
Trying to use test driven development and typed python.

Code auto-formatted with black

## Things I learned

### Python

- `set()`s are awesome to get unique elements from a list
- `set()`s also allow you to find intersections and overlaps
- need to tell VS Code to use `setup.cfg` for activated linters (see `.vscode/settings.json`)

### Programming approach

- TDD on top level is always worth it
- adding tests for smaller steps creates very modular code..maybe too many functions, seem to lack cohesion because all functions are only used one time
- beware of edge cases (day8: extreme values sitting on the edge of the map)
- just because you think that two implementations do the same thing, does not mean they do (test them both)
- using `dict()` or `list()` for instantiation is slower than using the literals `{}`, `[]`
- using `typing.Dict/List` was necessary pre Python 3.10 but now `dict/list/tuple[]` are preferred solutions without additional imports
