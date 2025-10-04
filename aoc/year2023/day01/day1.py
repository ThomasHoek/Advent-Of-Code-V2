import re


def puzzle(puzzle_input: list[str]) -> int:
    total = 0
    re_filter = re.compile(r"\d")
    for code in puzzle_input:
        number_lst = re_filter.findall(code)
        total += int(number_lst[0] + number_lst[-1])
    return total
