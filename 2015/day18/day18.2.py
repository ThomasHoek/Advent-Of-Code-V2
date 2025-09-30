import copy
# no numpy

class GameOfLife:
    matrix = []

    def __init__(self, inp_str):
        for line in inp_str:
            self.matrix.append([x for x in line])
        self.set_corners()

    def __repr__(self):
        return_str = ""
        for row in self.matrix:
            return_str += " ".join(row) + "\n"
        return return_str

    def inbounds(self, x, y):
        if x < 0 or y < 0:  # below 0
            return False
        if x > len(self.matrix) - 1 or y > len(self.matrix) - 1:  # above 100
            return False
        return True

    def sum_neighbours(self, x, y):
        total_sum = 0
        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if (
                    (row != x or col != y)
                    and self.inbounds(row, col)
                    and self.matrix[row][col] == "#"
                ):
                    total_sum += 1

        return total_sum

    def rules(self, current, new_sum):
        if current == ".":
            if new_sum in [3]:
                return "#"
            else:
                return "."
        else:
            if new_sum in [2, 3]:
                return "#"
            else:
                return "."

    def set_corners(self):
        end = len(self.matrix) - 1
        self.matrix[0][0] = "#"
        self.matrix[0][end] = "#"
        self.matrix[end][0] = "#"
        self.matrix[end][end] = "#"

    def step(self):
        self.copy_matrix = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.copy_matrix[i][j] = self.rules(
                    self.matrix[i][j], self.sum_neighbours(i, j)
                )
        self.matrix = copy.deepcopy(self.copy_matrix)
        self.set_corners()

    def awnser(self):
        total_sum = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "#":
                    total_sum += 1
        return total_sum


def puzzle(puzzle_input: list[str]) -> int:
    grid = GameOfLife(puzzle_input)
    for _ in range(100):
        grid.step()
    return grid.awnser()
