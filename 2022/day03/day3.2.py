import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]
bin_size = 3
puzzle_input = [puzzle_input[i:i+bin_size]
                for i in range(0, len(puzzle_input), bin_size)]

total = 0
for line1, line2, line3 in puzzle_input:
    letter = list(set(line1).intersection(
                  set(line2).intersection(
                      set(line3))))[0]

    if letter.isupper():
        total += (ord(letter) - 64) + 26
    else:
        total += (ord(letter) - 97) + 1


print(total)