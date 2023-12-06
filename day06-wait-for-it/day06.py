from baseday import BaseDay
from dataclasses import dataclass
from typing import Iterable

@dataclass
class Race:
    time:   int
    distance: int

class Day06(BaseDay):
    races: list[Race]

    def init(self) -> None:
        self.races = []
        with open(self.input) as f:
            lines = [x.split()[1:] for x in f]
            for n in range(0, len(lines[0])):
                self.races.append(Race(lines[0][n], lines[1][n]))
        print('races:', self.races)

    def part1(self) -> None:
        print('day06 part1:', 'TBD')

    def part2(self) -> None:
        print('day06 part2:', 'TBD')
