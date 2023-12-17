from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Elem:
    elem: str
    dirs: set[tuple[int, int]]

@dataclass
class Contraption:
    grid: list[list[Elem]]
    size: int

    @classmethod
    def parse(cls, data: str) -> Self:
        grid = []
        for line in data.splitlines():
            grid.append([Elem(e, set()) for e in [*line]])
        return cls(grid, len(grid[0]))

    def run(self, y: int, x: int, dy: int, dx: int) -> None:
        while y >= 0 and y < self.size and x >= 0 and x < self.size:
            e = self.grid[y][x]
            if (dy, dx) in e.dirs:
                return
            e.dirs.add((dy, dx))

            match self.grid[y][x].elem:
                case '/':
                    dx, dy = -dy, -dx
                case '\\':
                    dx, dy = dy, dx
                case '-':
                    if dx == 0:
                        self.run(y, x + 1, 0, 1)
                        self.run(y, x - 1, 0, -1)
                        return
                case '|':
                    if dy == 0:
                        self.run(y + 1, x, 1, 0)
                        self.run(y - 1, x, -1, 0)
                        return
            y += dy
            x += dx

    def score(self) -> int:
        total = 0
        for elems in self.grid:
            total += sum([len(elem.dirs) != 0 for elem in elems])
        return total

class Day16(BaseDay):
    c: Contraption

    def init(self) -> None:
        with open(self.input) as file:
            self.c = Contraption.parse(file.read())

    def part1(self) -> None:
        self.c.run(0, 0, 0, 1)
        print("day16 part1:", self.c.score())

    def part2(self) -> None:
        print("day16 part2:", 'TBD')
