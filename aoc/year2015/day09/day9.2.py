import re
from itertools import permutations

from aoc.modules.text_parser import parse

PARSE_PATTERN: re.Pattern[str] = re.compile(r"(\w+) to (\w+) = (\d+)")


def puzzle(puzzle_input: list[str]) -> int:
    all_places: set[str] = set()
    city_dict: dict[tuple[str, str], int] = {}

    # Create a stange matrix in the dict.
    for line in puzzle_input:
        place1, place2, distance_str = parse(PARSE_PATTERN, line)
        distance = int(distance_str)

        all_places.add(place1)
        all_places.add(place2)
        city_dict[(place1, place2)] = distance
        city_dict[(place2, place1)] = distance

    max_distance = 0

    # every possible combination, brute force
    for combination in permutations(all_places):
        local_distance = 0
        for city_index in range(len(combination) - 1):
            local_distance += city_dict[(combination[city_index], combination[city_index + 1])]

        if local_distance > max_distance:
            max_distance = local_distance

    return int(max_distance)
