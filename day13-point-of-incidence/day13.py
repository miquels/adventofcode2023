from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Pattern:
    grid: list[str]

    def reflection(self, smudges: int) -> int:
        for y in range(0, len(self.grid) - 1):
            if self.reflects(y) == smudges:
                return y + 1
        return 0

    def reflects(self, y: int) -> int:
        diff = 0
        y1, y2 = y, y + 1
        while y1 >= 0 and y2 < len(self.grid):
            diff += sum([self.grid[y1][x] != self.grid[y2][x] for x in range(0, len(self.grid[0]))])
            if diff > 1:
                break
            y1 -= 1
            y2 += 1
        return diff

    def transpose(self) -> 'Pattern':
        grid = []
        for x in range(0, len(self.grid[0])):
            grid.append("".join([self.grid[y][x] for y in range(len(self.grid) -1, -1, -1)]))
        return Pattern(grid)

    def score(self, smudges: int) -> int:
        total = self.transpose().reflection(smudges)
        total += 100 * self.reflection(smudges)
        return total

class Day13(BaseDay):
    patterns: list[Pattern]

    def init(self) -> None:
        with open(self.input) as file:
            data = file.read()
        grids = data.strip("\n").split("\n\n")
        self.patterns = [Pattern(grid.split("\n")) for grid in grids]

    def part1(self) -> None:
        print("day13 part1:", sum([p.score(0) for p in self.patterns]))

    def part2(self) -> None:
        print("day13 part1:", sum([p.score(1) for p in self.patterns]))
