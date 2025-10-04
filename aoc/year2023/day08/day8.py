from typing import Any
import re


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


def puzzle(puzzle_input: list[str]) -> Any:
    walk_path = puzzle_input[0]

    codes = puzzle_input[2:]

    code_dict: dict[str, Tree] = {}
    codes_tuple: list[list[str]] = [re.findall("[A-Z]+", x) for x in codes]
    # pre init
    for name, _, _ in codes_tuple:
        code_dict[name] = Tree(name)

    for name, left, right in codes_tuple:
        code_dict[name].set_left(code_dict[left])
        code_dict[name].set_right(code_dict[right])

    current: Tree = code_dict["AAA"]
    counter = 0
    while current.name != "ZZZ":
        move = walk_path[counter % len(walk_path)]
        counter += 1

        if move == "L":
            current = current.get_left()
        elif move == "R":
            current = current.get_right()

    return counter
