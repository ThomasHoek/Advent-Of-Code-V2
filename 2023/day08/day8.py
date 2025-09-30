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


if __name__ == "__main__":
    import sys
    import os
    from io import TextIOWrapper
    from typing import TextIO

    try:
        final: bool = "final" in sys.argv
        file: bool = "file" in sys.argv
        clock: bool = "time" in sys.argv

    except IndexError:
        final = False
        file = False
        clock = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open("out.txt", "w")
        sys.stdout = f

    if clock:
        import time

        start: float = time.time()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 2

        puzzle_input: list[str] = open(f"{dir_path}/test2.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 6
        
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
