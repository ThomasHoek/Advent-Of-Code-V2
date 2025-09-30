from typing import Any
from dataclasses import dataclass
import re


class patern_class:
    """Class for keeping track of patterns and numbers."""

    def __init__(self, number: int, org_pattern: str) -> None:
        self.number: int = number
        self.org_pattern: str = org_pattern
        self.split = "|" in org_pattern
        if self.split:
            left, right = org_pattern.split(" | ")
            self.left = [left]
            self.right = [right]
            
        else:
            self.matched_patterns: list[str] = [org_pattern]

    done: bool = False

    def match_pattern_re(self, re_pattern):
        if self.split:
            for patt in self.left:
                if re_pattern.findall(patt):
                    return False
            for patt in self.right:
                if re_pattern.findall(patt):
                    return False
            return True

        else:
            for patt in self.matched_patterns:
                if re_pattern.findall(patt):
                    return  False
            return True


    def __repr__(self) -> str:
        if self.split:
            out_str = ''.join(self.left) + " | " + ''.join(self.right)
        else:
            out_str = ''.join(self.matched_patterns)
        return f"num: {self.number}, patt: {out_str}"


def reduce_pattern(pattern_lst: list[patern_class]) -> list[str]:
    re_filter = re.compile(r"(\d)")
    no_num_lst: list[int] = []

    while True:
        # FIND
        for i in pattern_lst:
            print(i)
            if i.done:
                continue
            else:
                if i.match_pattern_re(re_filter):
                    no_num_lst.append(i.number)
        if no_num_lst == [0]:
            break

        # REPLACE
        for num in no_num_lst:
            print(pattern_lst[num])

            for replace_patt in pattern_lst:
                print(replace_patt)
                if replace_patt.split:
                    for patt in self.left:
                        

                    for patt in self.right:
                else:
                    if num in replace_patt.matched_patterns:
                        print("normal")
                    
        break
    return ["test"]


def puzzle(puzzle_input: Any) -> Any:
    print(puzzle_input)
    pattern_str: list[str] = []
    matches: list[str] = []

    empty_mask = False
    for x in puzzle_input:
        if x == "":
            empty_mask = True
        else:
            (pattern_str, matches)[empty_mask].append(x)

    pattern_match: list[patern_class] = []
    for single_pattern in pattern_str:
        p_num, p_str = single_pattern.split(": ")
        pattern_match.append(patern_class(int(p_num), p_str.replace('"', "")))

    reduce_pattern(pattern_match)


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
        puzzle_input_r: list[int] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[int] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 2

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
