import copy


def puzzle(puzzle_input: list[str]) -> int:
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

    comb_set.remove(string)
    return len(comb_set)
