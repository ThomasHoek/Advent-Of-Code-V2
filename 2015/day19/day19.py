import os
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]

rules = puzzle_input[:-2]
string = puzzle_input[-1]

comb_set = set()
for rule in rules:
    string2 = copy.deepcopy(string)

    substr, replace_str = rule.split(" => ")
    if string.count(substr) > 1:
        index = 0
        while string2.count(substr):
            string2 = copy.deepcopy(string)
            string2 = string2[index:]
            missing = string[:index]
            index += string2.find(substr) + len(substr)

            comb_set.add(missing + string2.replace(substr, replace_str, 1))

    else:
        comb_set.add(string2.replace(substr, replace_str))

comb_set.remove(string)   # remove itself
print(len(comb_set))
