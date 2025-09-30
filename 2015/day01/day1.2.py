#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height

import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: str = open(f"{dir_path}/../input.txt", "r").readline()
pos: int = 0

count = 0
for count, next_floor in enumerate(puzzle_input, start=1):
    if next_floor == "(":
        pos += 1
    else:
        pos -= 1

    if pos == -1:
        break

print(count)
