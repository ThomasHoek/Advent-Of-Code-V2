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

valid_tickets = []
for ticket in other_ticket:
    ticket_valid = True
    for number in ticket.split(","):
        if int(number) not in valid_numbers:
            invalid_numbers.append(int(number))
            ticket_valid = False

    if ticket_valid:
        valid_tickets.append(ticket)

bin_ticket_lst = []
ticket_lst = []

counter = 0
for row in my_ticket.split(","):
    bin_ticket_lst.append([])
    ticket_lst.append([])
    ticket_lst[counter].append(int(row))
    counter += 1

for ticket in valid_tickets:
    for number in range(len(ticket.split(","))):
        ticket_num = int(ticket.split(",")[number])
        ticket_lst[number].append(ticket_num)

counter = 0
for row in rules:

    valid_numbers = []
    range1, range2 = row.split(":")[1].split(" or ")
    range1 = [int(i) for i in range1.split("-")]
    range2 = [int(i) for i in range2.split("-")]
    valid_numbers += range(range1[0], range1[1] + 1)
    valid_numbers += range(range2[0], range2[1] + 1)

    for sublst in ticket_lst:
        sum_lst = sum([1 if i in valid_numbers else 0 for i in sublst])
        if sum_lst == len(sublst):
            bin_ticket_lst[counter].append(1)
        else:
            bin_ticket_lst[counter].append(0)
    counter += 1

departure_rules = bin_ticket_lst[0:6]
departure_rules2 = []
skip_num = []
bin_ticket_sort = copy.deepcopy(bin_ticket_lst)
bin_ticket_sort.sort()

for row in bin_ticket_sort:
    for i in range(len(row)):
        if row[i] == 1 and i not in skip_num:
            skip_num.append(i)
            if row in departure_rules:
                departure_rules2.append(i)


total = 1
for number in departure_rules2:
    total *= int(my_ticket.split(",")[number])
print(total)
