import copy


# work backwards. Going from e -> string is TOO big of a memory problem.
def new_result(rules, string):
    comb_set = set()
    for rule in rules:
        string2 = copy.deepcopy(string)

        substr, replace_str = rule.split(" => ")
        if string.count(replace_str) > 1:
            index = 0
            while string2.count(replace_str):
                string2 = copy.deepcopy(string)
                string2 = string2[index:]
                missing = string[:index]
                index += string2.find(replace_str) + len(substr)

                comb_set.add(missing + string2.replace(replace_str, substr, 1))
                # comb_set.add(missing + string2.replace(replace_str, substr))

        else:
            comb_set.add(string2.replace(replace_str, substr))

    comb_set = clean_set(comb_set)
    return comb_set


def clean_set(inp_set: set) -> set:
    lst = list(inp_set)
    copy_lst = copy.deepcopy(lst)
    for i in lst:
        if len(i) == 1:
            pass
        else:
            if "e" in i:
                copy_lst.remove(i)
    return set(copy_lst)


def puzzle(puzzle_input: list[str]) -> int:
    rules = puzzle_input[:-2]
    end = puzzle_input[-1]
    string = "e"

    counter = 0
    old_set = set()
    old_set.add(end)
    new_set = set()

    while string not in new_set:
        new_set = set()
        for set_str in old_set:
            new_set.update(new_result(rules, set_str))

        new_set = new_set.difference(old_set)  # remove itself

        new_set = list(new_set)
        new_set.sort()

        try:
            new_set = new_set[:2000]
        except IndexError:
            pass

        new_set = set(new_set)

        old_set = copy.deepcopy(new_set)

        counter += 1

    return counter
