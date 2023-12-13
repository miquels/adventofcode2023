from baseday import BaseDay
from dataclasses import dataclass

@dataclass
class Pattern:
    grid: list[str]

    def reflection(self, smudges: int) -> int:
        for y in range(len(self.grid) - 1):
            if self.reflects(y) == smudges:
                return y + 1
        return 0

    def reflects(self, y: int) -> int:
        diff = 0
        for y1, y2 in zip(self.grid[y::-1], self.grid[y+1:]):
            diff += sum([x1 != x2 for x1, x2 in zip(y1, y2)])
            if diff > 1:
                break
        return diff

    def transpose(self) -> 'Pattern':
        return Pattern(["".join(x) for x in [*zip(*self.grid)]])

    def score(self, smudges: int) -> int:
        return self.transpose().reflection(smudges) + 100 * self.reflection(smudges)

class Day13(BaseDay):
    patterns: list[Pattern]

    def init(self) -> None:
        with open(self.input) as file:
            data = file.read()
        self.patterns = [Pattern(grid.splitlines()) for grid in data.split("\n\n")]

    def part1(self) -> None:
        print("day13 part1:", sum([p.score(0) for p in self.patterns]))

    def part2(self) -> None:
        print("day13 part1:", sum([p.score(1) for p in self.patterns]))
