inputfile = [i.rstrip() for i in open("input2.txt", "r")]

split_index = inputfile.index("")
rules = inputfile[:split_index]
inputs = inputfile[split_index + 1:]


def remove_lst(the_list, val):
    return [value for value in the_list if value != val]


rules_dict = {}
for rule in rules:
    rules_dict[int(rule.split(":")[0])] = remove_lst(
        remove_lst(list(rule.split(":")[1] + " "), " "), '"'
    )


multiple_lst = []
single_lst = []


def find_no_num(edit_rules):
    single_lst = []
    for i in edit_rules.keys():
        num_lst = []
        for j in edit_rules[i]:
            for k in j.strip().split(" "):
                num_lst.append(k.isdigit())

        if sum(num_lst) == 0:
            single_lst.append(i)

    return single_lst


def change(dict_rules, single_lst):
    for i in dict_rules.keys():
        if i not in single_lst:
            awnser = dict_rules[i]
            for single in single_lst:

                if "|" not in dict_rules[single]:
                    if len(dict_rules[single]) == 1:
                        awnser = [
                            x.replace(str(single), dict_rules[single][0])
                            for x in awnser
                        ]
                    else:
                        print(awnser, dict_rules[single])

                elif "|" in dict_rules[single]:
                    print(awnser, dict_rules[single])

                # else:

            dict_rules[i] = awnser

    for i in single_lst:
        del dict_rules[i]

    return dict_rules


for i in range(2):
    single_lst = find_no_num(rules_dict)
    rules_dict = change(rules_dict, single_lst)
    print(rules_dict)
