inputfile = open("input.txt", "r")
depart_time = inputfile.readline()
busses = inputfile.readline().rstrip().replace("x,", "")
busses = busses.replace(",,", ",").split(",")

times_dict = {}

for bus in busses:
    times_dict[bus] = 0

    while times_dict[bus] < int(depart_time):
        times_dict[bus] += int(bus)

    print(bus, times_dict[bus] - int(depart_time))
