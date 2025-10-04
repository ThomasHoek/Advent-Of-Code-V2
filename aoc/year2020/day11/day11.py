# [Done] exited with code=0 in 0.089 seconds
import copy



def check_around(c_map, i_location, j_location):
    lst = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            lst.append(c_map[i_location + i][j_location + j])

    return lst


def puzzle(input_file) -> int:        
    input_file = [row.rstrip() for row in input_file]
    input_empty = (len(input_file[0]) + 2) * ["."]
    input_file = [["."] + [letter for letter in row] + ["."] for row in input_file]
    input_file = [input_empty] + input_file + [input_empty]

    current_input = copy.deepcopy(input_file)

    prev_input = []
    while prev_input != current_input:
        prev_input = copy.deepcopy(current_input)

        for i in range(len(prev_input)):
            for j in range(len(prev_input[0])):
                char = prev_input[i][j]

                if char == "L":
                    output_lst = check_around(prev_input, i, j)
                    if "#" not in output_lst:
                        current_input[i][j] = "#"

                elif char == "#":
                    output_lst = check_around(prev_input, i, j)
                    if output_lst.count("#") >= 5:
                        current_input[i][j] = "L"

    total_count = 0
    for row in current_input:
        total_count += row.count("#")

    return total_count
