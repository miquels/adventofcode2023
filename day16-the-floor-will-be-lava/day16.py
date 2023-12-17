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

    def run(self, y: int, x: int, dy: int, dx: int) -> int:
        for elems in self.grid:
            for elem in elems:
                elem.dirs.clear()
        self.subrun(y, x, dy, dx)
        total = 0
        for elems in self.grid:
            total += sum([len(elem.dirs) != 0 for elem in elems])
        return total

    def subrun(self, y: int, x: int, dy: int, dx: int) -> None:
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
                        self.subrun(y, x + 1, 0, 1)
                        self.subrun(y, x - 1, 0, -1)
                        return
                case '|':
                    if dy == 0:
                        self.subrun(y + 1, x, 1, 0)
                        self.subrun(y - 1, x, -1, 0)
                        return
            y += dy
            x += dx

class Day16(BaseDay):
    c: Contraption

    def init(self) -> None:
        with open(self.input) as file:
            self.c = Contraption.parse(file.read())

    def part1(self) -> None:
        self.c.run(0, 0, 0, 1)
        print("day16 part1:", self.c.run(0, 0, 0, 1))

    def part2(self) -> None:
        scores = []
        for y in range(self.c.size):
            scores.append(self.c.run(y, 0, 0, 1))
            scores.append(self.c.run(y, self.c.size -1, 0, -1))
        for x in range(self.c.size):
            scores.append(self.c.run(0, x, 1, 0))
            scores.append(self.c.run(self.c.size -1, x, -1, 0))
        print("day16 part2:", max(scores))
