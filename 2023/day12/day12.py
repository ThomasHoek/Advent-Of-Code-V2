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
            print(replace_str, org_pattern)
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
        print(raw_str)
        int_patterns: list[int] = [int(x) for x in combos.split(",")]
        puzzle_total += recursive_make(raw_str, int_patterns)
        print()
    return puzzle_total


if __name__ == "__main__":
    import sys
    import os
    from io import TextIOWrapper
    from typing import TextIO

    try:
        final: bool = "final" in sys.argv
        file: bool = "file" in sys.argv
        clock: bool = "time" in sys.argv

    except IndexError:
        final = False
        file = False
        clock = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open("out.txt", "w")
        sys.stdout = f

    if clock:
        import time

        start: float = time.time()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 21

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore


# That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data;
# there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. [Return to Day 12]