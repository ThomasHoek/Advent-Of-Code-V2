
def recursive_solve(input):
    if type(input) == int:
        return input

    elif type(input) == list:
        return sum(recursive_solve(s) for s in input)

    elif type(input) == dict:
        if "red" in input.values():
            return 0
        else:
            return sum(recursive_solve(s) for s in input.values())
    return 0


def puzzle(puzzle_input: str) -> int:
    import json
    puzzle_json = json.loads(puzzle_input)
    return recursive_solve(puzzle_json)
