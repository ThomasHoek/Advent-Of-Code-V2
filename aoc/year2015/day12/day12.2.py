from typing import Any


def recursive_solve(func_input: Any) -> int:
    if type(func_input) is int:
        return func_input

    elif type(func_input) is list:
        return sum(recursive_solve(s) for s in func_input)

    elif type(func_input) is dict:
        if "red" in func_input.values():
            return 0
        else:
            return sum(recursive_solve(s) for s in func_input.values())
    return 0


def puzzle(puzzle_input: str) -> int:
    import json

    puzzle_json = json.loads(puzzle_input)
    return recursive_solve(puzzle_json)
