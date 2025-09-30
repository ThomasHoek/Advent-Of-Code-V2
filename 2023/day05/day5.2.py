from typing import Any
import itertools
import re
from functools import partial


def chunks(lst: list[Any]):
    """Yield successive n-sized chunks from lst. From Github and modified -T"""
    for i in range(0, len(lst), 2):
        yield tuple([lst[i], lst[i] + lst[i + 1]])


def split_list(lst: list[Any], val: Any) -> list[list[Any]]:
    """From Github and modified. -T"""
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


def list_to_tuple(lst: list[Any]) -> list[tuple[int, int, int]]:
    tuple_lst: list[tuple[int, int, int]] = []

    for x in lst:
        numbers: list[int] = re.findall(r"[0-9]+", x)
        if numbers != []:
            tuple_lst.append((int(numbers[0]),
                              int(numbers[1]),
                              int(numbers[2])))

    tuple_lst = sorted(tuple_lst, key=lambda tup: tup[1])
    return tuple_lst


def range_to_solution(
    boundaries: list[tuple[int, int, int]], number_inp: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    def add_destination(x: int) -> int:
        return destination - source + x

    new_numbers: list[tuple[int, int]] = []
    num_iter = 0

    # iterate while numbers available
    while num_iter < len(number_inp):
        lower_num, upper_num = number_inp[num_iter]

        # var to keep track if already changed
        change = True
        for destination, source, add in boundaries:
            if not change:
                continue

            # calc limit
            source_limit: int = source + add - 1

            # bool comparisons of limits
            lower_inner: bool = lower_num >= source and lower_num <= source_limit
            higher_inner: bool = upper_num >= source and upper_num <= source_limit
            inner: bool = lower_inner and higher_inner
            outer: bool = lower_num < source and upper_num > source_limit

            # match based on the bools
            match (outer, inner, lower_inner, higher_inner):
                case (True, _, _, _):
                    # outer -> source 5-10 | numbers  1 - 15
                    change = False
                    new_lower = add_destination(source)
                    new_top = add_destination(source_limit)

                    # unchecked
                    number_inp.append((lower_num, source - 1))
                    # middle
                    new_numbers.append((new_lower, new_top))
                    # unchecked
                    number_inp.append((new_top + 1, upper_num))

                case (False, True, True, True):
                    change = False

                    # pure inner -> source 5-10 | numbers  5-7
                    new_lower = add_destination(lower_num)
                    new_top = add_destination(upper_num)
                    new_numbers.append((new_lower, new_top))

                case (False, False, True, False):
                    change = False

                    # left side in, right out -> source 5-10  | numbers 7 - 15
                    new_lower = add_destination(lower_num)
                    new_top = add_destination(source_limit)

                    new_numbers.append((new_lower, new_top))
                    number_inp.append((source_limit + 1, upper_num))

                case (False, False, False, True):
                    change = False

                    # right side in, left out -> source 5-10 | numbers  1 - 7
                    new_lower = add_destination(source)
                    new_top = add_destination(upper_num)

                    number_inp.append((lower_num, source - 1))
                    new_numbers.append((new_lower, new_top))

                case _:
                    # if all False
                    pass

        if change:
            # if it never changed, add pure.
            new_numbers.append((lower_num, upper_num))

        num_iter += 1

    return new_numbers


def puzzle(puzzle_input: list[str]) -> Any:
    section_lst: list[list[Any]] = split_list(puzzle_input, "")

    seeds: list[int] = [int(x) for x in re.findall(r"[0-9]+", section_lst[0][0])]

    seeds_chunk: list[tuple[int, int]] = [x for x in chunks(seeds)]

    s2s = partial(range_to_solution, list_to_tuple(section_lst[1]))
    s2f = partial(range_to_solution, list_to_tuple(section_lst[2]))
    f2w = partial(range_to_solution, list_to_tuple(section_lst[3]))
    w2l = partial(range_to_solution, list_to_tuple(section_lst[4]))
    l2t = partial(range_to_solution, list_to_tuple(section_lst[5]))
    t2h = partial(range_to_solution, list_to_tuple(section_lst[6]))
    h2l = partial(range_to_solution, list_to_tuple(section_lst[7]))

    ans_tuple_lst: list[tuple[int, int]] = h2l(t2h(l2t(w2l(f2w(s2f(s2s(seeds_chunk)))))))
    first_ans: list[int] = [i[0] for i in ans_tuple_lst]
    return min(first_ans)


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
        import cProfile, pstats, io
        from pstats import SortKey

        pr = cProfile.Profile()
        pr.enable()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        # puzzle(puzzle_input_r)
        assert puzzle(puzzle_input_r) == 46

    if clock:
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
