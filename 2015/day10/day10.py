import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readline()

string = puzzle_input
for _ in range(40):
    new_string = ""
    count = 0
    prev_number = string[0]
    for number in string:
        if number == prev_number:
            count += 1
        else:
            new_string = new_string + "{}{}".format(count, prev_number)
            prev_number = number
            count = 1
    new_string = new_string + "{}{}".format(count, prev_number)
    string = new_string
print(len(string))
