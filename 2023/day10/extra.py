def print_final(tuple_set: set[tuple[int, int]],
                grid_num: list[tuple[int, int, int]],
                grid_size: tuple[int, int]) -> None:

    fin_res: list[list[str]] = []
    for row in range(grid_size[0]):
        fin_res.append([])

        for col in range(grid_size[1]):
            fin_res[row].append("----")

            tup_test = (row, col)
            if tup_test in tuple_set:
                for x, y, val in grid_num:
                    if x == row and y == col:
                        fin_res[row][col] = "{0:0>4}".format(val)
                        break

    for row in fin_res:
        print(row)
