from baseday import BaseDay
from dataclasses import dataclass
from math import floor, ceil, sqrt
from functools import reduce

def quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    n = sqrt(b*b - 4*a*c)
    s1 = (-b - n) / 2*a
    s2 = (-b + n) / 2*a
    return s1, s2

@dataclass
class Race:
    time:   int
    distance: int

    def wins(self) -> int:
        s1, s2 = quadratic(-1, self.time, -self.distance)
        return ceil(max(s1, s2)) - floor(min(s1, s2)) - 1

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
