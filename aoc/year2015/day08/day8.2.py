def puzzle(puzzle_input: list[str]) -> int:
    total_length = 0
    total_string = 0


    for line in puzzle_input:
        total_length += len(line)
        index_pointer = 0
        special_count = 2
        while True:
            command = line[index_pointer]

            if command == '"':
                special_count += 1

            elif command == "\\":
                special_count += 1

            index_pointer += 1

            if index_pointer == len(line):
                break

        total_string += len(line) + special_count

    return total_string - total_length
