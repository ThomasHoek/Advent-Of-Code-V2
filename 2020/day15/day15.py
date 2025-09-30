import copy

inputfile = [i.rstrip().split(",") for i in open("input.txt", "r")][0]

last = 0
mem_dict = {}
times_dict = {}
counter = 0
for i in inputfile[:-1]:
    counter += 1
    mem_dict[int(i)] = counter
    times_dict[int(i)] = 1

last = int(inputfile[-1])


while counter != 2020:
    counter += 1
    if last not in mem_dict:
        mem_dict[last] = counter
        last = 0

    else:
        org = copy.deepcopy(mem_dict[last])
        mem_dict[last] = counter
        last = counter - org

for value in mem_dict:
    if mem_dict[value] == 2020:
        print(value)
