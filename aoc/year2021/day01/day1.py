def puzzle(puzzle_input):
    puzzle_input = [int(i) for i in puzzle_input]
    count = 0
    for line in range(0, len(puzzle_input) - 1):
        if puzzle_input[line] < puzzle_input[line + 1]:
            count += 1

    return count
