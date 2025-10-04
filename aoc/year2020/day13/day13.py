def puzzle(input_file) -> int:
    depart_time = input_file[0]
    busses = input_file[1].replace("x,", "")
    busses = busses.replace(",,", ",").split(",")

    times_dict = {}

    for bus in busses:
        times_dict[bus] = 0
        while times_dict[bus] < int(depart_time):
            times_dict[bus] += int(bus)

    totalList = [int(bus) * (times_dict[bus] - int(depart_time)) for bus in busses]
    return min(totalList)