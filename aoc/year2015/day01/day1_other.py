# This is an inspired solution for a language like c++ which does not have a .
# .count() function.


def puzzle(puzzle_input: str):
    return len(puzzle_input.replace(")", "")) - len(puzzle_input.replace("(", ""))
