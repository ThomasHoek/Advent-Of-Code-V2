from typing import Any
import re
from collections import defaultdict


def puzzle(puzzle_input: Any) -> Any:
    counter_dict = defaultdict(int=1)
    counter_dict[1] = 1
    counter_dict.default_factory = lambda: 1

    re_filter = re.compile(r"([\d| ]+) \| ([\d| ]+)")

    for number, line in enumerate(puzzle_input, start=1):
        tuple_groups = re_filter.search(line).groups()
        win_num, self_num = (
            set([int(x) for x in re.split(r"\s+", xs) if x]) for xs in tuple_groups
        )

        amount = len(win_num.intersection(self_num))
        if amount != 0:
            for i in range(number + 1, number + amount + 1):
                counter_dict[i] += 1 * counter_dict[number]
        else:
            # create if not already exist
            counter_dict[number]

    return sum(counter_dict.values()) - 1

