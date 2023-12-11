from baseday import BaseDay
from dataclasses import dataclass
from itertools import combinations
from typing import Self

def transpose(array: list[list[bool]]) -> list[list[bool]]:
    a = list(zip(*array))
    return [list(x) for x in a]

def expansions(grid: list[list[bool]]) -> list[int]:
    return [y for y in range(0, len(grid)) if not any(grid[y])]

@dataclass
class Universe:
    galaxies: list[tuple[int, int]]
    exp_y: list[int]
    exp_x: list[int]

    @classmethod
    def parse(cls, input: str) -> Self:
        grid: list[list[bool]] = []
        galaxies = []
        with open(input) as f:
            for y, line in enumerate([line.strip() for line in f]):
                grid.append([c == '#' for c in [*line]])
                galaxies += [(y, x) for x in range(0, len(line)) if line[x] == '#']
        exp_y = expansions(grid)
        exp_x = expansions(transpose(grid))
        return cls(galaxies, exp_y, exp_x)

    def calc(self, factor: int) -> int:
        galaxies = []
        for galaxy in self.galaxies:
            dy = sum([galaxy[0] > y for y in self.exp_y])
            dx = sum([galaxy[1] > x for x in self.exp_x])
            galaxies.append((galaxy[0] + factor * dy, galaxy[1] + factor * dx))
        sets = combinations(galaxies, 2)
        return sum(abs(g0[0] - g1[0]) + abs(g0[1] - g1[1]) for g0, g1 in sets)

class Day11(BaseDay):
    universe: Universe

    def init(self) -> None:
        self.universe = Universe.parse(self.input)

    def part1(self) -> None:
        print("day11 part1:", self.universe.calc(1))

    def part2(self) -> None:
        print("day11 part2:", self.universe.calc(999999))
