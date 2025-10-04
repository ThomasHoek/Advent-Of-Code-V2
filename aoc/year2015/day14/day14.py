import copy
import re



class rendeer:
    # Pre init everything
    rest = False
    total_dist = 0
    tick = 0
    rest_ticks = 0

    def __init__(self, speed: int, time_a: int, time_r: int):
        """__init__ set every variable

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

    def run(self, amount: int) -> int:
        """run Runs for amount of steps

        Calculates a predetermined amount of steps into the future

        Parameters
        ----------
        amount : int
            Total steps the simulation should run for

        Returns
        -------
        int
            Total distance travelled
        """
        for i in range(amount):
            self.step()
        return self.total_dist


def puzzle(puzzle_input: list[str]) -> int:
    all_dist = []
    for line in puzzle_input:
        reindeer = rendeer(*[int(i) for i in re.findall("\\d+", line)])
        all_dist.append(reindeer.run(2503))

    return max(all_dist)
