import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [int(x.rstrip()) for x in puzzle_input]

count = 0
for line in range(len(puzzle_input) - 1):
    if puzzle_input[line] < puzzle_input[line + 1]:
        count += 1

print(count)
