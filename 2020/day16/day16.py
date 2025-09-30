import copy

inputfile = [i.rstrip() for i in open("input.txt", "r") if i.rstrip() != ""]

rules = []
my_ticket = 0
other_ticket = []

last_line_input = None
for line in inputfile:
    if line == "your ticket:":
        last_line_input = 1

    elif line == "nearby tickets:":
        last_line_input = 2

    else:
        if last_line_input == 1:
            my_ticket = copy.deepcopy(line)

        elif last_line_input == 2:
            other_ticket.append(line)
        else:
            rules.append(line)


# clean
invalid_numbers = []
valid_numbers = []
for row in rules:
    range1, range2 = row.split(":")[1].split(" or ")
    range1 = [int(i) for i in range1.split("-")]
    range2 = [int(i) for i in range2.split("-")]
    valid_numbers += range(range1[0], range1[1] + 1)
    valid_numbers += range(range2[0], range2[1] + 1)

for ticket in other_ticket:
    for number in ticket.split(","):
        if int(number) not in valid_numbers:
            invalid_numbers.append(int(number))

print(sum(invalid_numbers))
