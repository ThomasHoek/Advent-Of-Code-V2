def puzzle(puzzle_input):
    h_pos = 0
    depth = 0

    for line in puzzle_input:
        if "forward" in line:
            com, val = line.split(" ")
            h_pos += int(val)
        else:
            com, val = line.split(" ")
            if com == "up":
                depth -= int(val)
            else:
                depth += int(val)

    return h_pos * depth
