import math
import copy


def puzzle(inputfile: list) -> int:
    """Run Conway 4D for 6 cycles. inputfile is list[str] of lines (".#.." style).
    Returns the total active cubes as int.
    """
    inputfile2 = []
    counter = 0
    for i in inputfile:
        inputfile2.append([])
        for j in i:
            inputfile2[counter].append(int(j.replace(".", "0").replace("#", "1")))
        counter += 1

    total_add = 25
    dim2_grid = []
    empty_dim2_grid = []
    for i in range(math.ceil((total_add - len(inputfile2)) / 2)):
        dim2_grid.append([int(i) for i in ["0"] * total_add])

    for i in range(len(inputfile2)):
        var = (total_add - len(inputfile[i])) / 2
        before = [int(i) for i in ["0"] * math.ceil(var)]
        after = [int(i) for i in ["0"] * math.floor(var)]
        dim2_grid.append(before + inputfile2[i] + after)

    for i in range(math.ceil((total_add - len(inputfile2)) / 2)):
        dim2_grid.append([int(i) for i in ["0"] * total_add])

    for i in range(total_add):
        empty_dim2_grid.append([int(i) for i in ["0"] * total_add])


    dim3_grid = []
    empty_dim3_grid = []

    for i in range(total_add):
        if i == math.ceil((total_add - len(inputfile2)) / 2):
            dim3_grid.append(dim2_grid)
        else:
            dim3_grid.append(empty_dim2_grid)


    for i in range(total_add):
        empty_dim3_grid.append(empty_dim2_grid)


    grid = []
    for i in range(total_add):
        if i == math.ceil((total_add - len(inputfile2)) / 2):
            grid.append(dim3_grid)
        else:
            grid.append(empty_dim3_grid)

    inputfile2 = []
    dim2_grid = []
    empty_dim2_grid = []
    dim3_grid = []
    empty_dim3_grid = []


    def get_surrounding(layer, x, y, z, w):
        sur_lst = []
        for wsur in [w - 1, w, w + 1]:
            for zsur in [z - 1, z, z + 1]:
                for ysur in [y - 1, y, y + 1]:
                    for xsur in [x - 1, x, x + 1]:
                        if not (wsur == w and zsur == z and ysur == y and xsur == x):
                            if wsur < 0 or zsur < 0 or ysur < 0 or xsur < 0:
                                sur_lst.append(0)
                            else:
                                try:
                                    sur_lst.append(grid[wsur][zsur][ysur][xsur])
                                except IndexError:
                                    sur_lst.append(0)
        return sum(sur_lst)


    for _ in range(6):
        new_grid = []
        for w in range(len(grid)):
            new_grid.append([])
            for z in range(len(grid[w])):
                new_grid[w].append([])
                for y in range(len(grid[w][z])):
                    new_grid[w][z].append([])
                    for x in range(len(grid[w][z][y])):
                        new_grid[w][z][y].append([])
                        total_sur = get_surrounding(grid, w=w, x=x, y=y, z=z)
                        if grid[w][z][y][x] and (total_sur == 2 or total_sur == 3):
                            new_grid[w][z][y][x] = 1

                        elif grid[w][z][y][x]:
                            new_grid[w][z][y][x] = 0

                        elif total_sur == 3:
                            new_grid[w][z][y][x] = 1

                        else:
                            new_grid[w][z][y][x] = 0
        grid = copy.deepcopy(new_grid)


    total = 0
    for w in new_grid:
        for z in w:
            for y in z:
                for x in y:
                    total += x
