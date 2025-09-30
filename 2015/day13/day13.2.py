from itertools import permutations
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()

puzzle_input = [x.rstrip() for x in puzzle_input]
all_names = set()
name_dict = {}

# Create a stange matrix in the dict.
for line in puzzle_input:
    person1, other = line.split(" would ")
    amount, person2 = other[:-1].split(" happiness units by sitting next to ")
    amount = (int(amount[5:]) * -1) if "lose" in amount else int(amount[5:])
    all_names.add(person1)
    name_dict[(person1, person2)] = int(amount)

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
        set_happiness += name_dict[(combination[name_index],
                                    combination[name_index + 1])]

    # because I am lazy, reverse of list.
    combination_2 = combination[::-1]
    for name_index in range(len(combination_2) - 1):
        set_happiness += name_dict[(combination_2[name_index],
                                    combination_2[name_index + 1])]

    if set_happiness > max_happy:
        max_happy = set_happiness

print(max_happy)
