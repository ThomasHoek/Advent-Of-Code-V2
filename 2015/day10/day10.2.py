def puzzle(puzzle_input: str) -> int:
    string = puzzle_input
    for _ in range(50):
        new_string = ""
        count = 0
        prev_number = string[0]
        for number in string:
            if number == prev_number:
                count += 1
            else:
                new_string = new_string + "{}{}".format(count, prev_number)
                prev_number = number
                count = 1
        new_string = new_string + "{}{}".format(count, prev_number)
        string = new_string
    return len(string)
