import re

inputfile = [i.rstrip() for i in open("input2.txt", "r")]

split_index = inputfile.index("")
rules = inputfile[:split_index]
inputs = inputfile[split_index + 1 :]

rules_dict = {}
for rule in rules:
    rules_dict[int(rule.split(":")[0])] = rule.split(":")[1] + " "

multiple_lst = []
single_lst = []


def find_no_num(edit_rules):
    single_lst = []
    for i in edit_rules.keys():
        num_lst = []
        for j in edit_rules[i].strip().split(" "):
            num_lst.append(j.isdigit())

        if sum(num_lst) == 0:
            single_lst.append(i)

    return single_lst


def change(dict_rules, single_lst):
    for i in dict_rules.keys():
        awnser = dict_rules[i]

        for single in single_lst:
            if "|" not in dict_rules[single]:
                awnser = re.sub(
                    r"\b%s\b" % str(single),
                    dict_rules[single].strip().replace('"', ""),
                    awnser,
                )
            else:
                awnser = re.sub(
                    r"\b%s\b" % str(single),
                    ",[ " + dict_rules[single].strip().replace('"', "") + " ],",
                    awnser,
                )

            print(list(awnser))
            dict_rules[i] = awnser

    for i in single_lst:
        del dict_rules[i]

    return dict_rules


while len(rules_dict) > 1:
    single_lst = find_no_num(rules_dict)
    rules_dict = change(rules_dict, single_lst)

comb_rules = rules_dict[0]
comb_rules = comb_rules.strip()
print(comb_rules)


# def change(dict_rules, single_lst):
# for i in dict_rules.keys():
#     awnser = dict_rules[i]

#     for single in single_lst:
#         if "|" not in dict_rules[single]:
#             awnser = re.sub(r"\b%s\b" % str(single) , dict_rules[single].strip().replace('"',''), awnser)
#         else:
#             awnser = re.sub(r"\b%s\b" % str(single) , ",[ " + dict_rules[single].strip().replace('"','') + " ]," , awnser)

#         print(list(awnser))
#         dict_rules[i] = awnser

# for i in single_lst:
#     del dict_rules[i]

# return dict_rules
# print(mix)
# aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb.
