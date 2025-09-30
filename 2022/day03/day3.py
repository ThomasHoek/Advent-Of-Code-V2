import os
from math import floor
dir_path = os.path.dirname(os.path.realpath(__file__))
# puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]

total = 0
for line in puzzle_input:

    letter = list(set(line[:floor(len(line)/2)]).intersection(
                  set(line[floor(len(line)/2):])))[0]

    if letter.isupper():
        total += (ord(letter) - 64) + 26
    else:
        total += (ord(letter) - 97) + 1

print(total)
