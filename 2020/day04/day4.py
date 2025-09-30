# [Done] exited with code=0 in 0.069 seconds
input_file = open("input.txt", "r").readlines()

new_input = [[]]
counter = 0
for line in input_file:
    if line == "\n":
        counter += 1
        new_input.append([])
    else:
        new_input[counter].append(line.rstrip())


new_input = [[word.split(" ") for word in lst] for lst in new_input]

total_correct = 0
for passport in new_input:
    correct = 0

    passport_dict = {}
    for line in passport:
        for word in line:
            key, value = word.split(":")
            passport_dict[key] = value

    correct = correct + 1 if "byr" in passport_dict else correct
    correct = correct + 1 if "iyr" in passport_dict else correct
    correct = correct + 1 if "eyr" in passport_dict else correct
    correct = correct + 1 if "hgt" in passport_dict else correct
    correct = correct + 1 if "hcl" in passport_dict else correct
    correct = correct + 1 if "ecl" in passport_dict else correct
    correct = correct + 1 if "pid" in passport_dict else correct
    # correct = correct + 1 if "cid"  in passport_dict else correct
    if correct == 7:
        total_correct += 1

print(total_correct)
