from baseday import BaseDay
from dataclasses import dataclass
from itertools import count, repeat
from typing import Any, ClassVar, Iterator, Self

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
    loop: bool = False
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
        # Find the next possible position that doesn't go back.
        elem = self.at(self.pos)
        nxt = self.pos
        for dir in ['N', 'S', 'E', 'W']:
            if elem.can(dir) and (nxt := self.pos.to(dir)) != self.prevpos:
                break
        self.prevpos = self.pos
        self.pos = nxt

    @classmethod
    def parse(cls, input: str) -> Self:
        # Create grid with an extra column on the right and row at the bottom.
        grid = []
        start: Position
        with open(input) as f:
            for y, line in enumerate(f):
                grid.append([Element(c) for c in [*line.strip(), '.']])
                if (x := line.find('S')) >= 0:
                    start = Position(y, x)
        grid.append(list(repeat(Element('.'), len(grid[0]))))
        return cls(grid, start, start, start)

    def set_start_elem(self) -> None:
        # Calculate the start pipe element.
        for s in '-', '|', 'F', 'L', 'J', '7':
            e = Element(s)
            m = 0
            for d1, d2 in [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]:
                if e.can(d1) and (n := self.to(d1)) and n.can(d2):
                    m += 1
            if m == 2:
                self.at(self.start).type = e.type
                break

    def follow_loop(self) -> int:
        for steps in count(1):
            self.at(self.pos).loop = True
            self.step()
            if self.pos == self.start:
                break
        return steps

    def enclosed(self) -> int:
        count = 0
        inside = False
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[0])):
                elem = self.grid[y][x]
                if elem.loop and elem.type in '|JL':
                    inside = not inside
                if inside and not self.grid[y][x].loop:
                    count += 1
        return count

class Day10(BaseDay):
    maze: Maze

    def init(self) -> None:
        self.maze = Maze.parse(self.input)
        self.maze.set_start_elem()

    def part1(self) -> None:
        val = self.maze.follow_loop()
        print("day10 part1:", val // 2)

    def part2(self) -> None:
        print("day10 part2:", self.maze.enclosed())
