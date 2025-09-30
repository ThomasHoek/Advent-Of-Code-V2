# [Done] exited with code=0 in 0.052 seconds
import re

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


def check_info(year1: int, dict1: int, year2: int) -> bool:
    return year1 <= int(dict1) and year2 >= int(dict1)


total_correct = 0
for passport in new_input:
    correct = 0

    passport_dict = {}
    for line in passport:
        for word in line:
            key, value = word.split(":")
            passport_dict[key] = value

    if "byr" in passport_dict:
        if check_info(1920, passport_dict["byr"], 2002):
            correct += 1

    if "iyr" in passport_dict and correct == 1:
        if check_info(2010, passport_dict["iyr"], 2020):
            correct += 1

    if "eyr" in passport_dict and correct == 2:
        if check_info(2020, passport_dict["eyr"], 2030):
            correct += 1

    if "hgt" in passport_dict and correct == 3:
        var = passport_dict["hgt"]
        if "cm" in var:
            value1 = 150
            value2 = 193
            height2 = int(var[:-2])

        elif "in" in var:
            value1 = 59
            value2 = 76
            height2 = int(var[:-2])

        else:
            value1 = 0
            value2 = 0
            height2 = 9999

        if value1 <= height2 and value2 >= height2:
            correct += 1

    if "hcl" in passport_dict and correct == 4:
        var = passport_dict["hcl"]
        if var[0] == "#" and len(var) == 7 and re.match("[a-f0-9#]", var):
            correct += 1

    if "ecl" in passport_dict and correct == 5:
        var = passport_dict["ecl"]
        if var in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            correct += 1

    if "pid" in passport_dict and correct == 6:
        var = passport_dict["pid"]
        if re.match("[0-9]", var) and len(var) == 9:
            correct += 1

    # correct = correct + 1 if "cid"  in passport_dict else correct
    if correct == 7:
        total_correct += 1

print(total_correct)
