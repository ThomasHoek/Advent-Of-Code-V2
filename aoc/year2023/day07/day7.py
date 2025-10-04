from typing import Any
from collections import Counter


def to_hex_code(inp_str: str):
    c_dict: dict[str, int] = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    #                 5K, 4K, FH,  3K,  2P, 1P, HC
    #                  0,  1,   2,  3,   4,  5,  6
    rank: list[int] = [0, 0, 0, 0, 0, 0, 0]
    inp_lst = list(inp_str)

    count_inp = Counter(inp_lst)

    # set bool vars
    if len(count_inp) == 1:  # 5k
        rank[0] = 1
    elif len(count_inp) == 2:  # 4k | FH
        top_2 = count_inp.most_common(2)
        if top_2[0][1] == 4:  # 4K
            rank[1] = 1

        elif top_2[0][1] == 3:  # FH
            rank[2] = 1
        else:
            assert NotImplementedError("impossible")

    elif len(count_inp) == 3:  # 3k | 2P
        top_3 = count_inp.most_common(3)
        if top_3[0][1] == 3:  # 3K
            rank[3] = 1

        elif top_3[0][1] == 2 and top_3[1][1] == 2:  # 2P
            rank[4] = 1
        else:
            assert NotImplementedError("impossible")

    elif len(count_inp) == 4:  # 1P
        top_2 = count_inp.most_common(2)
        rank[5] = 1

    elif len(count_inp) == 5:  # HC
        rank[6] = 1

    else:
        assert NotImplementedError("impossible")

    for inp in inp_lst:
        rank.append(c_dict[inp])

    final_code = 0
    for counter, cycle_code in enumerate(iterable=rank, start=1):
        final_code = final_code + (cycle_code * (16 ** (len(rank) - counter)))

    return final_code


def puzzle(puzzle_input: list[str]) -> Any:
    split_input: list[list[str]] = [x.split(" ") for x in puzzle_input]

    final: list[tuple[int, int]] = []
    for code, score in split_input:
        final.append((to_hex_code(code), int(score)))

    final.sort(key=lambda x: x[0])

    total = 0
    for counter, score in enumerate(final, start=1):
        total += counter * score[1]

    return total
