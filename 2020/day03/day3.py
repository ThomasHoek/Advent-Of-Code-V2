# [Done] exited with code=0 in 0.038 seconds
input_file = open("input.txt", "r").readlines()

total = {".": 0, "#": 0}
counter = 0
for i in range(len(input_file)):
    total[input_file[i][counter]] = total[input_file[i][counter]] + 1
    counter = (counter + 3) % len(input_file[i].rstrip())


print(total)