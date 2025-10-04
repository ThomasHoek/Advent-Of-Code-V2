memory: dict[str, int] = {}


# add memoization
def recursive_make(inp_str: str, pattern: list[int]) -> int:
    global memory

    mem_inp = inp_str + "_".join(map(str, pattern))

    total = 0
    if inp_str == "":
        if pattern == []:
            return 1
        else:
            return 0

    elif mem_inp in memory:
        return memory[mem_inp]

    else:
        firstchar = inp_str[0]

        if firstchar == ".":
            subtotal: int = recursive_make(inp_str[1:], pattern)
            total += subtotal

        elif firstchar == "?":
            for i in ".#":
                subtotal = recursive_make(i + inp_str[1:], pattern)
                total += subtotal
        else:  # has to be a "#"
            if pattern == []:
                return 0

            group_size = pattern[0]
            if len(inp_str) == group_size:
                if "." not in inp_str[:group_size]:
                    subtotal = recursive_make(inp_str[group_size + 1 :], pattern[1:])
                    total += subtotal

            elif len(inp_str) > group_size:
                if "." not in inp_str[:group_size] and inp_str[group_size] in ".?":
                    subtotal = recursive_make(inp_str[group_size + 1 :], pattern[1:])
                    total += subtotal
            else:
                return 0

    memory[mem_inp] = total
    return total


def puzzle(puzzle_input: list[str]) -> int:
    puzzle_total = 0
    for row in puzzle_input:
        global memory
        memory = {}

        raw_str, combos = row.split(" ")
        long_str = (
            raw_str + "?" + raw_str + "?" + raw_str + "?" + raw_str + "?" + raw_str
        )
        long_combos = combos + "," + combos + "," + combos + "," + combos + "," + combos
        long_int_patterns: list[int] = [int(x) for x in long_combos.split(",")]
        sub_total = recursive_make(long_str, long_int_patterns)

        puzzle_total += sub_total

    return puzzle_total

