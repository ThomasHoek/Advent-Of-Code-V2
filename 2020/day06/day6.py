# [Done] exited with code=0 in 0.242 seconds
input_file = open("input.txt", "r").readlines()

new_input = [[]]
counter = 0
for line in input_file:
    if line == "\n":
        counter += 1
        new_input.append([])
    else:
        new_input[counter].append(line.rstrip())

total_length = 0
for group in new_input:
    group_set = set()
    for person in group:
        for letter in person:
            group_set.add(letter)
    total_length += len(group_set)

print(total_length)
