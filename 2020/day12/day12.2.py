input_file = [row.rstrip() for row in open("input.txt", "r").readlines()]


class boat:
    def __init__(self):
        self.direction = "E"
        self.way_xcoord = 10
        self.way_ycoord = 1

        self.xcoord = 0
        self.ycoord = 0

    def way_forward(self, f_input, amount):
        if f_input == "N":
            self.way_ycoord += amount

        elif f_input == "E":
            self.way_xcoord += amount

        elif f_input == "S":
            self.way_ycoord -= amount

        elif f_input == "W":
            self.way_xcoord -= amount

    def rotate_waypoint(self, new_direction):

        dir_lst = [self.way_xcoord, self.way_ycoord]
        neg_dir_lst = [self.way_xcoord * (-1), self.way_ycoord * (-1)]
        total_dir = dir_lst + neg_dir_lst + dir_lst + neg_dir_lst + dir_lst

        new_dir = total_dir[4 + new_direction: 6 + new_direction]
        self.way_xcoord, self.way_ycoord = new_dir[0], new_dir[1]

    def change_direction(self, new_direction, amount):
        direction_cycle = ["N", "E", "S", "W"]
        amount = (amount // 90) % 4

        if new_direction == "L":
            new_dir = (direction_cycle.index(self.direction) - amount) % 4
            self.direction = direction_cycle[new_dir]
            self.rotate_waypoint(amount * (-1))

        elif new_direction == "R":
            new_dir = (direction_cycle.index(self.direction) + amount) % 4
            self.direction = direction_cycle[new_dir]
            self.rotate_waypoint(amount)

        return (self.xcoord, self.ycoord)

    def f_direction(self, amount):
        self.xcoord += self.way_xcoord * amount
        self.ycoord += self.way_ycoord * amount

    def output(self):
        return (
            self.xcoord,
            self.ycoord,
            self.direction,
            abs(self.xcoord) + abs(self.ycoord),
        )


santa = boat()

for line in input_file:
    command, amount = line[0], int(line[1:])
    if command in ["N", "E", "S", "W"]:
        santa.way_forward(command, amount)

    elif command in ["L", "R"]:
        santa.change_direction(command, amount)

    elif command in ["F"]:
        santa.f_direction(amount)

print(santa.output())
