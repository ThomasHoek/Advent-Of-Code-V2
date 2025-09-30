# [Done] exited with code=0 in 0.198 seconds
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
    group_lst = []
    for person in group:
        person_set = set()
        for letter in person:
            person_set.add(letter)
        group_lst.append(person_set)

    total_length += len(set.intersection(*group_lst))
    # https://stackoverflow.com/a/17495274- > wildcard to iterate


print(total_length)
