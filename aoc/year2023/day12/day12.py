from itertools import groupby


def find_groups(inp_str: str) -> list[int]:
    # cut everything after ?
    if "?" in inp_str:
        inp_str = inp_str.split("?")[0]
    return [len(list(g)) for k, g in groupby(inp_str) if k == "#"]


def recursive_make(inp_str: str, org_pattern: list[int]) -> int:
    total = 0
    if "?" not in inp_str:
        return 0

    for i in "#.":
        replace_str = inp_str.replace("?", i, 1)
        replace_groups = find_groups(replace_str)

        if replace_groups == org_pattern and "?" not in replace_str:
            total += 1
        else:
            same_pattern = True
            if len(replace_groups) <= len(org_pattern):
                for j in range(len(replace_groups)):
                    if replace_groups[j] > org_pattern[j]:
                        same_pattern = False
            else:
                same_pattern = False

            if same_pattern:
                total += recursive_make(replace_str, org_pattern)

    # print(total)
    return total


def puzzle(puzzle_input: list[str]) -> int:
    # go from left to right recursively
    # every new recursive iter, most left replace
    # check if groups still match every iter
    # if group is wrong, stop and go up.

    puzzle_total = 0
    for row in puzzle_input:
        raw_str, combos = row.split(" ")
        int_patterns: list[int] = [int(x) for x in combos.split(",")]
        puzzle_total += recursive_make(raw_str, int_patterns)
    return puzzle_total
