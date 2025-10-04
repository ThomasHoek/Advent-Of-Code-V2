import copy
import re



class rendeer:
    rest = False
    total_dist = 0
    tick = 0
    rest_ticks = 0
    points = 0

    def __init__(self, speed: int, time_a: int, time_r: int):
        """__init__ settings every variable

        Reindeer olympics, every rendeir has their own attributs which get set.

        Parameters
        ----------
        speed : int
            Speed of the reindeer in km/s
        time_a : int
            Time for long the reindeir is active
        time_r : int
            Time how long the reindeir rests
        """
        self.speed = speed
        self.time_active = time_a
        self.time_rest = time_r
        self.active_ticks = time_a

    def step(self):
        """step Single Step of the race

        Adds distance if the deer is active, otherwise lets the deer rest.
        """
        self.tick += 1
        if self.rest:
            self.rest_ticks -= 1
            if self.rest_ticks == 0:
                self.rest = False
                self.active_ticks = copy.deepcopy(self.time_active)

        else:
            self.total_dist += self.speed
            self.active_ticks -= 1
            if self.active_ticks == 0:
                self.rest = True
                self.rest_ticks = copy.deepcopy(self.time_rest)

    def get_dist(self) -> int:
        """get_dist get distance variable

        Returns the distance

        Returns
        -------
        int
            Distance travelled up to so far
        """
        return self.total_dist

    def give_point(self):
        """give_point Adds one point to the reindeer

        Adds a point to the reindeer if this command is called
        """
        self.points += 1

    def get_points(self) -> int:
        """get_points Get points

        Get the points the reindeer has aquired up to this far

        Returns
        -------
        int
            Points in the lead
        """
        return self.points

def puzzle(puzzle_input: list[str]) -> int:
    all_rendeir = []
    for line in puzzle_input:
        all_rendeir.append(rendeer(*[int(i) for i in re.findall("\\d+", line)]))

    for i in range(2503):
        distance = []
        for reindeer in all_rendeir:
            reindeer.step()
            distance.append(reindeer.get_dist())

        m = max(distance)
        max_index_lst = [i for i, j in enumerate(distance) if j == m]
        for index in max_index_lst:
            all_rendeir[index].give_point()

    point_lst = []
    for reindeer in all_rendeir:
        point_lst.append(reindeer.get_points())
    return max(point_lst)
