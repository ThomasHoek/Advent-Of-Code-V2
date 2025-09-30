import os
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = json.loads(open(f"{dir_path}/input.txt", "r").read())


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


print(recursive_solve(puzzle_input))
