from itertools import permutations

from aoc.modules.text_parser import parse

REGEX_STR = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."


def puzzle(puzzle_input: list[str]) -> int:
    all_names: set[str] = set()
    name_dict: dict[tuple[str, str], int] = {}

    # Create a stange matrix in the dict.
    for line in puzzle_input:
        person1, win_lose, amount_str, person2 = parse(REGEX_STR, line)
        amount = int(amount_str)
        if win_lose == "lose":
            amount = -amount

        all_names.add(person1)
        name_dict[(person1, person2)] = amount

    for name in all_names:
        name_dict[("me", name)] = 0
        name_dict[(name, "me")] = 0
    all_names.add("me")

    max_happy = 0
    # every possible combination, brute force
    for combination in list(permutations(all_names)):
        combination = list(combination)
        combination.append(combination[0])
        set_happiness = 0
        for name_index in range(len(combination) - 1):
            set_happiness += name_dict[(combination[name_index], combination[name_index + 1])]

        # because I am lazy, reverse of list.
        combination_2 = combination[::-1]
        for name_index in range(len(combination_2) - 1):
            set_happiness += name_dict[(combination_2[name_index], combination_2[name_index + 1])]

        if set_happiness > max_happy:
            max_happy = set_happiness

    return max_happy
