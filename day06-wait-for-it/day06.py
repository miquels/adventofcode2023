from baseday import BaseDay
from dataclasses import dataclass
from functools import reduce

@dataclass
class Race:
    time:   int
    distance: int

    def wins(self) -> int:
        count = 0
        for t in range(1, self.time):
            dist = (self.time - t) * t;
            count += dist > self.distance
        return count

class Day06(BaseDay):
    races1: list[Race]
    race2: Race

    def init(self) -> None:
        self.races1 = []
        with open(self.input) as f:
            lines = [x.split()[1:] for x in f]
            for n in range(0, len(lines[0])):
                self.races1.append(Race(int(lines[0][n]), int(lines[1][n])))
            self.race2 = Race(int("".join(lines[0])), int("".join(lines[1])))

    def part1(self) -> None:
        score = reduce(lambda x, y: x*y, [race.wins() for race in self.races1])
        print('day06 part1:', score)

    def part2(self) -> None:
        print('day06 part2:', self.race2.wins())
