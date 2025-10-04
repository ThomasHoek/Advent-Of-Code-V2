def puzzle(inputfile: list) -> int:
    """Run Conway 3D for 6 cycles. inputfile is list[str] of lines (".#.." style).
    Returns the total active cubes as int.
    """
    # parse
    inputfile2 = []
    counter = 0
    for i in inputfile:
        inputfile2.append([])
        for j in i:
            inputfile2[counter].append(int(j.replace(".", "0").replace("#", "1")))
        counter += 1

    inputfile = inputfile2

    def new_create_outer(layer):
        outer = (len(layer) + 2) * [0]
        return [outer] * len(outer)

    def create_outer(layer):
        outer = [[0] * (len(layer) + 2)]
        layer2 = []
        for row in layer:
            layer2.append([0] + row + [0])

        return outer + layer2 + outer

    def get_surrounding(layer, x, y, z):
        sur_lst = []
        for zsur in [z - 1, z, z + 1]:
            for ysur in [y - 1, y, y + 1]:
                for xsur in [x - 1, x, x + 1]:
                    if not (zsur == z and ysur == y and xsur == x):
                        if zsur < 0 or ysur < 0 or xsur < 0:
                            sur_lst.append(0)
                        else:
                            try:
                                sur_lst.append(grid[zsur][ysur][xsur])
                            except IndexError:
                                sur_lst.append(0)
        return sum(sur_lst)

    # init
    first = [new_create_outer(inputfile)]
    middle = [create_outer(inputfile)]
    last = [new_create_outer(inputfile)]
    grid = first + middle + last

    for _ in range(6):
        new_grid = []
        for z in range(len(grid)):
            new_grid.append([])
            for y in range(len(grid[z])):
                new_grid[z].append([])
                for x in range(len(grid[z][y])):
                    new_grid[z][y].append([])
                    total_sur = get_surrounding(grid, x=x, y=y, z=z)
                    if grid[z][y][x] and (total_sur == 2 or total_sur == 3):
                        new_grid[z][y][x] = 1

                    elif grid[z][y][x]:
                        new_grid[z][y][x] = 0

                    elif total_sur == 3:
                        new_grid[z][y][x] = 1

                    else:
                        new_grid[z][y][x] = 0

        first = [new_create_outer(new_grid[0])]
        middle = [create_outer(i) for i in new_grid]
        last = [new_create_outer(new_grid[-1])]
        grid = first + middle + last

    total = 0
    for z in new_grid:
        for y in z:
            for x in y:
                total += x

    return total
