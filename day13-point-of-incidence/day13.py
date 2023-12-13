from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Pattern:
    grid: list[str]

    def reflection(self) -> int:
        for y in range(0, len(self.grid) - 1):
            if self.reflects(y):
                return y + 1
        return 0

    def reflects(self, y: int) -> bool:
        y1 = y
        y2 = y1 + 1
        while y1 >= 0 and y2 < len(self.grid):
            if self.grid[y1] != self.grid[y2]:
                return False
            y1 -= 1
            y2 += 1
        return True

    def transpose(self) -> 'Pattern':
        grid = []
        for x in range(0, len(self.grid[0])):
            grid.append("".join([self.grid[y][x] for y in range(len(self.grid) -1, -1, -1)]))
        return Pattern(grid)

    def score(self) -> int:
        total = self.transpose().reflection()
        total += 100 * self.reflection()
        return total

class Day13(BaseDay):
    patterns: list[Pattern]

    def init(self) -> None:
        with open(self.input) as file:
            data = file.read()
        grids = data.strip("\n").split("\n\n")
        self.patterns = [Pattern(grid.split("\n")) for grid in grids]

    def part1(self) -> None:
        print("day13 part1:", sum([p.score() for p in self.patterns]))

    def part2(self) -> None:
        print("day13 part2:", 'TBD')
