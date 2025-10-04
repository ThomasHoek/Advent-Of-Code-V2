import os


def puzzle(puzzle_input):
    puzzle_input = [x.rstrip("\n") for x in puzzle_input]

    crates = puzzle_input[: puzzle_input.index("") - 1]
    numbers = puzzle_input[puzzle_input.index("") - 1 : puzzle_input.index("")]
    moves = puzzle_input[puzzle_input.index("") + 1 :]

    amount = int(numbers[-1].split("   ")[-1])
    crate_lst = []
    for i in range(amount):
        crate_lst.append([])

    for crate_row in crates:
        for counter, crate in enumerate(
            [crate_row[x : x + 3] for x in range(0, len(crate_row), 4)]
        ):
            if crate == "   ":
                continue
            crate_lst[counter].insert(0, crate)


    for instruction in moves:
        amount, start, end = [
            int(x)
            for x in instruction.removeprefix("move ")
            .replace("from ", "")
            .replace(" to", "")
            .split(" ")
        ]

        for i in range(amount):
            crate = crate_lst[start - 1].pop(-1)
            crate_lst[end - 1].append(crate)

    return "".join([str(x[-1])[1] for x in crate_lst])
