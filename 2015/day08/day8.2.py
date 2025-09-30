import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]

total_length = 0
total_string = 0


for line in puzzle_input:
    total_length += len(line)
    index_pointer = 0
    special_count = 2
    while True:
        command = line[index_pointer]

        if command == "\"":
            special_count += 1

        elif command == "\\":
            special_count += 1

        index_pointer += 1

        if index_pointer == len(line):
            break

    total_string += len(line) + special_count

print(total_string - total_length)
