def puzzle(puzzle_input):
    puzzle_input = [int(i) for i in puzzle_input]

    count = 0
    prev = None
    for line in range(len(puzzle_input) - 2):
        a = puzzle_input[line]
        b = puzzle_input[line + 1]
        c = puzzle_input[line + 2]

        if prev is not None and (a + b + c) > prev:
            count += 1

        prev = a + b + c

    return count
