from __future__ import annotations
from math import floor
from typing import Callable, TypeAlias

MonkeyID: TypeAlias = int
WorryLevel: TypeAlias = int


class Monkey:
    """One of the monkey in the group."""

    items: list[int]
    test_fn: Callable[[WorryLevel], MonkeyID]
    op_fn: Callable[[WorryLevel], WorryLevel]
    monkey_id: int
    n_throw: int
    mod: int

    def __init__(
        self,
        monkey_id: int,
        mod: int,
        test_fn: Callable[[WorryLevel], MonkeyID],
        op_fn: Callable[[WorryLevel], WorryLevel],
    ):
        """Create new monkey.

        Args:
            monkey_id: monkey id
            mod: the monkeys unique modulo operator
            test_fn: function that gets called with current item value
                returns the monkey that will receive the item
            op_fn: change of worry level for item, gets item value passed
                returns the new level
        """
        self.items = []
        self.monkey_id = monkey_id
        self.test_fn = test_fn
        self.op_fn = op_fn
        self.n_throw = 0
        self.mod = mod

    def add_item(self, value: WorryLevel) -> None:
        """Add a new item to the monkeys stack."""
        self.items.append(value)

    def throw(self) -> tuple[MonkeyID, WorryLevel]:
        """Initate throwing the next item in the monkeys stack.

        Returns:
            tuple of monkey ID that receives the item and the new value of the item."""
        item = self.items.pop(0)
        new_value = self.calc_new_value(item)
        target_monkey = self.test_fn(new_value)
        self.n_throw += 1
        return (target_monkey, new_value)

    def throw2(self) -> tuple[MonkeyID, WorryLevel]:
        """Star2: Initate throwing the next item in the monkeys stack.

        Returns:
            tuple of monkey ID that receives the item and the new value of the item."""
        item = self.items.pop(0)
        new_value = self.op_fn(item)
        target_monkey = self.test_fn(new_value)
        self.n_throw += 1
        # print(f"{self.monkey_id} -> {target_monkey}: {new_value}\t({item})")
        return (target_monkey, new_value)

    def calc_new_value(self, value: WorryLevel) -> WorryLevel:
        """Determine the value (worry level) for an item.

        Including operation and relief phase (/3)."""
        return floor(self.op_fn(value) / 3)


def star1(lines: list[str]) -> int:
    """Part1."""
    rounds = 20
    monkeys = parse_input(lines)
    for _ in range(rounds):
        for active_monkey in monkeys:
            while len(active_monkey.items) > 0:
                target_monkey, value = active_monkey.throw()
                monkeys[target_monkey].add_item(value)

    top_throwers = sorted(monkeys, key=lambda m: m.n_throw, reverse=True)

    return top_throwers[0].n_throw * top_throwers[1].n_throw


def star2(lines: list[str]) -> str:
    """Part2."""
    rounds = 10000
    monkeys = parse_input(lines)
    # prev_throws = [0] * len(monkeys)
    for r in range(rounds):
        for active_monkey in monkeys:
            while len(active_monkey.items) > 0:
                target_monkey, value = active_monkey.throw2()
                monkeys[target_monkey].add_item(value % monkeys[target_monkey].mod)
        # print(f"== After round: {r} ==")
        # for ix, m in enumerate(monkeys):
        #     print(f"{m.monkey_id}; {m.n_throw} (+{m.n_throw - prev_throws[ix]})")
        #     prev_throws[ix] = m.n_throw

    top_throwers = sorted(monkeys, key=lambda m: m.n_throw, reverse=True)
    print(top_throwers[0].n_throw, top_throwers[1].n_throw)
    return top_throwers[0].n_throw * top_throwers[1].n_throw


def parse_input(text: list[str]) -> list[Monkey]:
    """Convert text into list of operation codes."""
    monkeys = []
    for lines in "\n".join(text).split("\n\n"):
        batch = lines.split("\n")
        monkey_id = int(batch[0].split(" ")[1][0:-1])
        items = [int(x) for x in batch[1].split(" items: ")[1].split(", ")]
        mod = int(batch[3].split("divisible by ")[1])
        true_target = int(batch[4].split(" to monkey ")[1])
        false_target = int(batch[5].split(" to monkey ")[1])

        def get_test_fn(
            mod: int, true_target: int, false_target: int
        ) -> Callable[[WorryLevel], MonkeyID]:
            def test_fn(value: WorryLevel) -> MonkeyID:
                if value % mod == 0:
                    return true_target
                return false_target

            return test_fn

        op_operand = batch[2].split("old ")[1].split(" ")[0]
        assert op_operand in ["*", "+"]
        op_value = batch[2].split("old ")[1].split(" ")[1]

        def get_op_fn(
            op_value: str, op_operand: str
        ) -> Callable[[WorryLevel], WorryLevel]:
            def op_fn(value: WorryLevel) -> WorryLevel:
                other_val = 0
                if op_value == "old":
                    other_val = value
                else:
                    other_val = int(op_value)

                if op_operand == "*":
                    return value * other_val
                return value + other_val

            return op_fn

        m = Monkey(
            monkey_id,
            mod,
            get_test_fn(mod, true_target, false_target),
            get_op_fn(op_value, op_operand),
        )
        for i in items:
            m.add_item(i)
        monkeys.append(m)
    return monkeys


def read_input(filepath: str) -> list[str]:
    """Read input."""
    with open(filepath, "r", encoding="utf8") as f:
        return [line.replace("\n", "") for line in f.readlines()]


if __name__ == "__main__":
    print(f"Star1: {star1(read_input('./day11.txt'))}")
    print(f"Star2: {star2(read_input('./day11.txt'))}")
