from __future__ import annotations
from typing import Any
import itertools


def split_list(lst: list[Any], val: Any) -> list[list[Any]]:
    """From Github and modified. -T"""
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


letterdict: dict[str, int] = {"x": 0, "m": 1, "a": 2, "s": 3}


def workflow_solve(workflow_dict: dict[str, str], inp_str: str, numbers: list[int]):
    curr = workflow_dict[inp_str]
    for equation in curr.split(","):
        if ":" in equation:
            equation, final = equation.split(":")
            if ">" in equation:
                letter, number = equation.split(">")
                if numbers[letterdict[letter]] > int(number):
                    return final
            else:
                letter, number = equation.split("<")
                if numbers[letterdict[letter]] < int(number):
                    return final
        else:
            return equation

    raise NotImplementedError("Reached impossible")


def puzzle(puzzle_input: list[str]) -> int:
    workflow, ratings = split_list(puzzle_input, "")
    workflow_dict: dict[str, str] = {}
    for line in workflow:
        name, split_str = line[:-1].split(r"{")
        workflow_dict[name] = split_str

    ratings = [x[1:-1].split(",") for x in ratings]

    total = 0
    for rating in ratings:
        route = "in"
        while True:
            numbers = [int(x[2:]) for x in rating]
            route = workflow_solve(workflow_dict, route, numbers)
            if route == "A":
                total += sum(numbers)
                break
            elif route == "R":
                break

    return total


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
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 19114

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
