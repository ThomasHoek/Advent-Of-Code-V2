from itertools import permutations

def puzzle(puzzle_input: list[str]) -> int:
    all_places = set()
    city_dict = {}

    # Create a stange matrix in the dict.
    for line in puzzle_input:
        place1, other = line.split(" to ")
        place2, distance = other.split(" = ")
        all_places.add(place1)
        all_places.add(place2)
        city_dict[(place1, place2)] = int(distance)
        city_dict[(place2, place1)] = int(distance)

    min_distance = float("inf")

    # every possible combination, brute force
    for combination in permutations(all_places):
        local_distance = 0
        for city_index in range(len(combination) - 1):
            local_distance += city_dict[
                (combination[city_index], combination[city_index + 1])
            ]

        if local_distance < min_distance:
            min_distance = local_distance

    return min_distance
