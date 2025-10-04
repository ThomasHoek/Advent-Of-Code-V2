from typing import Any
import re
from math import gcd


class Tree:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_left(self, left: "Tree") -> None:
        self.left: Tree = left

    def set_right(self, right: "Tree") -> None:
        self.right: Tree = right

    def get_left(self) -> "Tree":
        return self.left

    def get_right(self) -> "Tree":
        return self.right

    def __repr__(self) -> str:
        return f"{self.name} = ({self.left.name}, {self.right.name})"


def floyd(tree_network: list[Tree], walk_path: str) -> list[int]:
    def move(animal: tuple[Tree, int]) -> tuple[Tree, int]:
        a_move = walk_path[animal[1] % len(walk_path)]

        if a_move == "L":
            new = animal[0].get_left()
        elif a_move == "R":
            new = animal[0].get_right()
        else:
            raise NotImplementedError("impossible")
        return (new, animal[1] + 1)

    cycle_lst: list[int] = []
    for begin in tree_network:
        tortoise: tuple[Tree, int] = (begin, 0)
        hare: tuple[Tree, int] = (begin, 0)

        tortoise = move(tortoise)
        hare = move(move(hare))

        # iterate until in cycle
        while tortoise[0] != hare[0]:
            tortoise = move(tortoise)
            hare = move(move(hare))

        # set tort still and make hare move.
        hare_num = hare[1]
        hare = move(hare)
        while tortoise[0] != hare[0]:
            hare = move(hare)
        hare_fin = hare[1]

        cycle_lst.append(hare_fin - hare_num)
    return cycle_lst


def end_check(inp: list[Tree]) -> bool:
    for tree in inp:
        if tree.name[-1] != "Z":
            return False
    return True


def puzzle(puzzle_input: list[str]) -> Any:
    walk_path = puzzle_input[0]

    codes = puzzle_input[2:]

    code_dict: dict[str, Tree] = {}
    codes_tuple: list[list[str]] = [re.findall("[1-9A-Z]+", x) for x in codes]

    # pre init
    for name, _, _ in codes_tuple:
        code_dict[name] = Tree(name)

    for name, left, right in codes_tuple:
        code_dict[name].set_left(code_dict[left])
        code_dict[name].set_right(code_dict[right])

    current: list[Tree] = [code_dict[x[0]] for x in codes_tuple if x[0][-1] == "A"]

    cycles: list[int] = floyd(current, walk_path)
    cycles.append(len(walk_path))

    # least common multiple
    lcm = 1
    for i in cycles:
        lcm = lcm * i // gcd(lcm, i)
    return lcm
