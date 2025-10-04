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
