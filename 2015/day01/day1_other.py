# This is an inspired solution for a language like c++ which does not have a .
# .count() function.

import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: str = open(f"{dir_path}/../input.txt", "r").readline()
print(len(puzzle_input.replace(")", "")) - len(puzzle_input.replace("(", "")))
