from baseday import BaseDay
from dataclasses import dataclass
from itertools import repeat
from typing import Self

@dataclass
class Position:
    y: int
    x: int

    def north(self) -> 'Position':
        return Position(self.y - 1, self.x)

    def south(self) -> 'Position':
        return Position(self.y + 1, self.x)

    def east(self) -> 'Position':
        return Position(self.y, self.x - 1)

    def west(self) -> 'Position':
        return Position(self.y, self.x + 1)

@dataclass
class Pipe:
    type: str

    def can_north(self) -> bool:
        return self.type in '|LJ'

    def can_south(self) -> bool:
        return self.type in '|7F'

    def can_east(self) -> bool:
        return self.type in '-J7'

    def can_west(self) -> bool:
        return self.type in '-LF'

@dataclass
class Maze:
    grid: list[list[Pipe]]
    start: Position
    pos: Position
    prevpos: Position

    def at(self, pos: Position) -> Pipe:
        return self.grid[pos.y][pos.x]

    def north(self) -> Pipe:
        return self.at(self.pos.north())

    def south(self) -> Pipe:
        return self.at(self.pos.south())

    def east(self) -> Pipe:
        return self.at(self.pos.east())

    def west(self) -> Pipe:
        return self.at(self.pos.west())

    def step(self) -> None:
        pipe = self.at(self.pos)
        nxt = self.pos
        if pipe.can_north() and self.pos.north() != self.prevpos:
            nxt = self.pos.north()
        if pipe.can_south() and self.pos.south() != self.prevpos:
            nxt = self.pos.south()
        if pipe.can_east() and self.pos.east() != self.prevpos:
            nxt = self.pos.east()
        if pipe.can_west() and self.pos.west() != self.prevpos:
            nxt = self.pos.west()
        self.prevpos = self.pos
        self.pos = nxt

    @classmethod
    def parse(cls, input: str) -> Self:
        grid = []
        with open(input) as f:
            for line in f:
                grid.append([Pipe(c) for c in line.strip()])
                grid[-1].append(Pipe('.'))
        grid.append(list(repeat(Pipe('.'), len(grid[0]) + 1)))

        max_y = len(grid) - 1
        max_x = len(grid[0]) - 1
        start = Position(0, 0)
        for y in range(0, max_y):
            for x in range(0, max_x):
                if grid[y][x].type == 'S':
                    start = Position(y, x)
                    break
        maze = cls(grid, start, start, Position(-1, -1))

        p = '.'
        if maze.north().can_south() and maze.south().can_north():
            p = '|'
        if maze.north().can_south() and maze.east().can_west():
            p = 'J'
        if maze.north().can_south() and maze.west().can_east():
            p = 'L'
        if maze.south().can_north() and maze.east().can_west():
            p = '7'
        if maze.south().can_north() and maze.west().can_east():
            p = 'F'
        if maze.east().can_west() and maze.west().can_east():
            p = '-'
        maze.at(start).type = p

        return maze

class Day10(BaseDay):
    maze: Maze

    def init(self) -> None:
        self.maze = Maze.parse(self.input)

    def part1(self) -> None:
        steps = 0
        while True:
            self.maze.step()
            steps += 1
            if self.maze.pos == self.maze.start:
                break
        print("day10 part1:", int(steps / 2))

    def part2(self) -> None:
        print("day10 part2:", 'TBD')
