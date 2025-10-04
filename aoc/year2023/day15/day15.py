def puzzle(puzzle_input: str) -> int:
    total = 0
    for i in puzzle_input[0].split(","):
        sub_total = 0
        for char in list(i):
            sub_total += ord(char)
            sub_total *= 17
            sub_total = sub_total % 256
        # print(sub_total)
        total += sub_total
    return total
