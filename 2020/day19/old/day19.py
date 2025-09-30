inputfile = [i.rstrip() for i in open("input2.txt", "r")]

split_index = inputfile.index("")
rules = inputfile[:split_index]
inputs = inputfile[split_index + 1:]

rules_dict = {}
for rule in rules:
    rules_dict[int(rule.split(":")[0])] = rule.split(":")[1]


def split_or(rule_line):
    split_rule = []
    counter = 0
    for subrules2 in [i.split(" ") for i in rule_line.split("|")]:
        subrules2 = [x for x in subrules2 if x]
        for subrule3 in subrules2:
            split_rule.append([])
            var = rules_dict[int(subrule3)]
            if '"' in var:
                split_rule[counter].append(var.split('"')[-2])
            else:
                split_rule[counter].append(recursive_find(var))
        counter += 1

    return [i for i in split_rule if i != []]


def recursive_find(rule):
    awnser_rule = []
    for subrule in rule.split(" "):
        if subrule != "":
            if "|" in subrule:
                return split_or(rule)
            else:
                awnser = rules_dict[int(subrule)]
                if '"' in awnser:
                    awnser_rule.append(awnser.split('"')[-2])
                else:
                    awnser_rule.append(recursive_find(awnser))

    return awnser_rule


rule_zero = recursive_find(rules_dict[0])


def remove_doubles(lst):
    return list(set(lst))


def flatten_lst(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list


# def solve_lst(lst,check):
#     for i in check:


# print(rule_zero)
# mix = solve_lst(rule_zero, inputs)
# print(mix)
# aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb.
