from typing import Any
import re


def puzzle(puzzle_input: Any) -> Any:
    total = 0

    re_filter = re.compile(r"([\d| ]+) \| ([\d| ]+)")

    for line in puzzle_input:
        tuple_groups = re_filter.search(line).groups()
        win_num, self_num = (
            set([int(x) for x in re.split(r"\s+", xs) if x]) for xs in tuple_groups
        )

        amount = len(win_num.intersection(self_num))
        if amount != 0:
            total += 2 ** (amount - 1)

    return total
