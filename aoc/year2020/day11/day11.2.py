# [Done] exited with code=0 in 0.089 seconds
import copy


def check_around(c_map, i_location, j_location):
    lst = []
    v_len_cmap = len(c_map) - 1
    h_len_cmap = len(c_map[0]) - 1

    def vertical(direction, i_vert):
        i_vert = i_vert + 1 if direction else i_vert - 1
        while c_map[i_vert][j_location] == ".":
            i_vert = i_vert + 1 if direction else i_vert - 1
            if i_vert < 0:
                return c_map[0][j_location]

            if i_vert > v_len_cmap:
                return c_map[v_len_cmap][j_location]

        return c_map[i_vert][j_location]

    def horizontal(direction, j_hor):
        j_hor = j_hor + 1 if direction else j_hor - 1
        while c_map[i_location][j_hor] == ".":
            j_hor = j_hor + 1 if direction else j_hor - 1

            if j_hor < 0:
                return c_map[i_location][0]

            if j_hor > h_len_cmap:
                return c_map[i_location][h_len_cmap]

        return c_map[i_location][j_hor]

    def check_diagonal(i, j):
        error = False
        if i < 0:
            i = 0
            error = True

        elif j < 0:
            j = 0
            error = True

        if i > v_len_cmap:
            i = v_len_cmap
            error = True

        if j > h_len_cmap:
            j = h_len_cmap
            error = True

        return [error, i, j]

    def diagonal(hor, vert, i_diag, j_diag):
        i_diag = i_diag + 1 if vert else i_diag - 1
        j_diag = j_diag + 1 if hor else j_diag - 1

        while c_map[i_diag][j_diag] == ".":
            i_diag = i_diag + 1 if vert else i_diag - 1
            j_diag = j_diag + 1 if hor else j_diag - 1

            check_lst = check_diagonal(i_diag, j_diag)

            if check_lst[0]:
                return c_map[check_lst[1]][check_lst[2]]

        return c_map[i_diag][j_diag]

    lst.append(diagonal(True, False, i_location, j_location))  # north east
    lst.append(vertical(True, i_location))  # north
    lst.append(diagonal(True, True, i_location, j_location))  # north west

    lst.append(horizontal(False, j_location))  # east
    lst.append(horizontal(True, j_location))  # west

    lst.append(diagonal(False, False, i_location, j_location))  # south east
    lst.append(vertical(False, i_location))  # south
    lst.append(diagonal(False, True, i_location, j_location))  # south east
    return lst


def puzzle(input_file) -> int:
    input_file = [row.rstrip() for row in input_file]
    input_empty = (len(input_file[0]) + 2) * ["."]
    input_file = [["."] + [letter for letter in row] + ["."] for row in input_file]
    input_file = [input_empty] + input_file + [input_empty]

    current_input = copy.deepcopy(input_file)


    counter = 0
    prev_input = []
    while prev_input != current_input:
        counter += 1
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
