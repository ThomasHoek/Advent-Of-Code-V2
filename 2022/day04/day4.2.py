import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]

counter = 0
for first, second in [x.split(",") for x in puzzle_input]:
    first_min, first_max = [int(x) for x in first.split("-")]
    second_min, second_max = [int(x) for x in second.split("-")]

    if (first_min <= second_min) and (first_max >= second_min):
        counter += 1

    elif (first_min <= second_max) and (first_max >= second_max):
        counter += 1

    elif (second_min <= first_min) and (second_max >= first_min):
        counter += 1

    elif (second_min <= first_max) and (second_max >= first_max):
        counter += 1


print(counter)
