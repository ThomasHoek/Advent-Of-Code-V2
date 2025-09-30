import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [int(x.rstrip()) for x in puzzle_input] + [0, 0]

count = 0
prev = None
for line in range(len(puzzle_input) - 2):
    a = puzzle_input[line]
    b = puzzle_input[line + 1]
    c = puzzle_input[line + 2]

    if prev is not None and (a + b + c) > prev:
        count += 1

    prev = a + b + c


print(count)
