def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def puzzle(puzzle_input: str) -> int:
    totalsum = 0
    int_start = None
    for index, val in enumerate(puzzle_input):
        # start of number
        if isInt(val) and int_start is None:
            int_start = index

        # end of number
        elif not isInt(val) and int_start:
            number = int(puzzle_input[int_start:index])
            if puzzle_input[int_start - 1] == "-":
                totalsum -= number
            else:
                totalsum += number

            int_start = None
    return totalsum
