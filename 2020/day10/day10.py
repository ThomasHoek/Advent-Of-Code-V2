# [Done] exited with code=0 in 0.089 seconds
input_file = open("input.txt", "r").readlines()
input_file = [int(word.rstrip()) for word in input_file]
input_file.sort()

my_dict = {3: 1, 1: 1}

for i in range(len(input_file) - 1):
    diff = input_file[i + 1] - input_file[i]

    if diff in my_dict:
        my_dict[diff] += 1
    else:
        my_dict[diff] = 1

print(my_dict)
print(my_dict[1] * my_dict[3])
