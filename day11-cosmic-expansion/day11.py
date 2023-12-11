from baseday import BaseDay
from dataclasses import dataclass
from itertools import combinations
from typing import Any, ClassVar, Iterator, Self

def transpose(array: list[list[bool]]) -> list[list[bool]]:
    a = list(zip(*array))
    return [list(x) for x in a]

def expansions(grid: list[list[bool]]) -> list[int]:
    return [y for y in range(0, len(grid)) if not any(grid[y])]

@dataclass
class Universe:
    stars: list[tuple[int, int]]

    @classmethod
    def parse(cls, input: str) -> Self:
        grid: list[list[bool]] = []
        stars = []
        with open(input) as f:
            for y, line in enumerate([line.strip() for line in f]):
                grid.append([c == '#' for c in [*line]])
                stars += [(y, x) for x in range(0, len(line)) if line[x] == '#']
        exp_y = expansions(grid)
        exp_x = expansions(transpose(grid))
        for i in range(0, len(stars)):
            star = stars[i]
            dy = sum([star[0] > y for y in exp_y])
            dx = sum([star[1] > x for x in exp_x])
            stars[i] = (star[0] + dy, star[1] + dx)
        return cls(stars)

class Day11(BaseDay):
    universe: Universe

    def init(self) -> None:
        self.universe = Universe.parse(self.input)

    def part1(self) -> None:
        sets = combinations(self.universe.stars, 2)
        total = 0
        for s0, s1 in sets:
            total += abs(s0[0] - s1[0]) + abs(s0[1] - s1[1])
        print("day11 part1:", total)

    def part2(self) -> None:
        print("day11 part2:", 'TBD')
