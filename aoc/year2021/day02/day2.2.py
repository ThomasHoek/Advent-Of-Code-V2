def puzzle(puzzle_input):
    h_pos = 0
    depth = 0
    aim = 0

    for line in puzzle_input:
        if "forward" in line:
            com, val = line.split(" ")
            h_pos += int(val)
            depth += int(val) * aim
        else:
            com, val = line.split(" ")
            if com == "up":
                aim -= int(val)
            else:
                aim += int(val)

    return h_pos * depth
