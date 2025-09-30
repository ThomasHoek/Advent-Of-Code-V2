# [Done] exited with code=0 in 0.305 seconds

import copy

input_file = open("input.txt", "r").readlines()
input_file = [int(word.rstrip()) for word in input_file]

number = 29221323

for i in range(len(input_file)):
    total_lst = [input_file[i]]
    i_counter = copy.deepcopy(i)

    while sum(total_lst) <= number:
        try:
            i_counter += 1
            total_lst.append(input_file[i_counter])

        except IndexError:
            break

        if sum(total_lst) == number:
            print(total_lst)
            print(min(total_lst) + max(total_lst))
