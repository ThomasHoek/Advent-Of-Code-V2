class boat:
    def __init__(self):
        self.direction = "E"
        self.xcoord = 0
        self.ycoord = 0

    def forward(self, f_input, amount):
        if f_input == "N":
            self.ycoord += amount

        elif f_input == "E":
            self.xcoord += amount

        elif f_input == "S":
            self.ycoord -= amount

        elif f_input == "W":
            self.xcoord -= amount

        return (self.xcoord, self.ycoord)

    def change_direction(self, new_direction, amount):
        direction_cycle = ["N", "E", "S", "W"]
        amount = (amount // 90) % 4
        if new_direction == "L":
            self.direction = direction_cycle[
                (direction_cycle.index(self.direction) - amount) % 4
            ]

        elif new_direction == "R":
            self.direction = direction_cycle[
                (direction_cycle.index(self.direction) + amount) % 4
            ]

        return (self.xcoord, self.ycoord)

    def f_direction(self, amount):
        self.forward(self.direction, amount)
        return (self.xcoord, self.ycoord)

    def output(self):
        return (
            self.xcoord,
            self.ycoord,
            self.direction,
            abs(self.xcoord) + abs(self.ycoord),
        )


def puzzle(input_file) -> int:
    santa = boat()
    for line in input_file:
        command, amount = line[0], int(line[1:])
        if command in ["N", "E", "S", "W"]:
            santa.forward(command, amount)

        elif command in ["L", "R"]:
            santa.change_direction(command, amount)

        elif command in ["F"]:
            santa.f_direction(amount)

    return santa.output()
