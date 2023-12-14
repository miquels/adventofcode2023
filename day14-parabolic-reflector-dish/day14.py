from baseday import BaseDay
from dataclasses import dataclass

@dataclass
class Platform:
    grid: list[str]

    def tilt(self) -> int:
        load = 0
        max_y = len(self.grid)
        for x in range(len(self.grid[0])):
            next_free_y = 0
            for y in range (max_y):
                if self.grid[y][x] == 'O':
                    load += max_y - next_free_y
                    next_free_y += 1
                if self.grid[y][x] == '#':
                    next_free_y = y + 1
        return load
                  
class Day14(BaseDay):
    platform: Platform

    def init(self) -> None:
        with open(self.input) as file:
            data = file.read()
        self.platform = Platform(data.splitlines())

    def part1(self) -> None:
        print("day14 part1:", self.platform.tilt())

    def part2(self) -> None:
        print("day14 part2:", 'TBD')
