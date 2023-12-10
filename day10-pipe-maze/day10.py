from baseday import BaseDay
from dataclasses import dataclass
from itertools import count, repeat
from typing import Any, ClassVar, Self

@dataclass
class Position:
    y: int
    x: int
    dirs: ClassVar[Any] = { 'N': (-1, 0), 'S': (1, 0), 'E': (0, -1), 'W': (0, 1) }

    def to(self, dir: str) -> 'Position':
        d = self.dirs[dir]
        return Position(self.y + d[0], self.x + d[1])

@dataclass
class Element:
    type: str
    dirs: ClassVar[Any] = { 'N': '|LJ', 'S': '|7F', 'E': '-J7', 'W': '-LF' }

    def can(self, dir: str) -> bool:
        return self.type in self.dirs[dir]

@dataclass
class Maze:
    grid: list[list[Element]]
    start: Position
    pos: Position
    prevpos: Position

    def at(self, pos: Position) -> Element:
        return self.grid[pos.y][pos.x]

    def to(self, dir: str) -> Element:
        return self.at(self.pos.to(dir))

    def step(self) -> None:
        elem = self.at(self.pos)
        nxt = self.pos
        for dir in ['N', 'S', 'E', 'W']:
            if elem.can(dir) and (nxt := self.pos.to(dir)) != self.prevpos:
                break
        self.prevpos = self.pos
        self.pos = nxt

    @classmethod
    def parse(cls, input: str) -> Self:
        grid = []
        start: Position
        with open(input) as f:
            for y, line in enumerate(f):
                grid.append([Element(c) for c in line.strip()])
                grid[-1].append(Element('.'))
                if (x := line.find('S')) >= 0:
                    start = Position(y, x)
        grid.append(list(repeat(Element('.'), len(grid[0]) + 1)))
        return cls(grid, start, start, Position(-1, -1))

    def run(self) -> int:
        for d1, d2 in [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]:
            if (e := self.to(d1)) and e.can(d2):
                self.pos = self.pos.to(d1)
        for steps in count(2):
            self.step()
            if self.pos == self.start:
                break
        return steps

class Day10(BaseDay):
    maze: Maze

    def init(self) -> None:
        self.maze = Maze.parse(self.input)

    def part1(self) -> None:
        val = self.maze.run()
        print("day10 part1:", val // 2)

    def part2(self) -> None:
        print("day10 part2:", 'TBD')
