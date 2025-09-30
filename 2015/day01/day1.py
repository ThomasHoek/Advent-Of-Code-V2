#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height

import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: str = open(f"{dir_path}/../input.txt", "r").readline()
up: int = puzzle_input.count("(")
down: int = puzzle_input.count(")")
print(up - down)
