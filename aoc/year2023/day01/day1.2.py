import re


def puzzle(puzzle_input: list[str]) -> int:
    str2num: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    total = 0
    re_filter = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    for code in puzzle_input:
        number_lst = re_filter.findall(code)
        left = number_lst[0] if number_lst[0].isdigit() else str2num[number_lst[0]]
        right = number_lst[-1] if number_lst[-1].isdigit() else str2num[number_lst[-1]]
        total += int(left + right)
    return total