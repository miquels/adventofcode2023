from baseday import BaseDay
from dataclasses import dataclass
from typing import Self
import hashlib

@dataclass
class Platform:
    grid: list[bytearray]
    size: int
    orientation: str = 'N'

    @classmethod
    def parse(cls, data: str) -> Self:
        grid = [bytearray(x, 'ascii') for x in data.splitlines()]
        return cls(grid, len(grid[0]))

    def mapxy(self, y: int, x: int) -> tuple[int, int]:
        match self.orientation:
            case 'N':
                return y, x
            case 'E':
                return x, y
            case 'W':
                return x, self.size - y - 1
            case 'S':
                return self.size - y - 1, x
        return 0, 0

    def get(self, y: int, x) -> str:
        y, x = self.mapxy(y, x)
        return chr(self.grid[y][x])

    def set(self, y: int, x: int, val: str) -> None:
        y, x = self.mapxy(y, x)
        self.grid[y][x] = ord(val)

    def tilt(self, orientation: str = 'N') -> None:
        self.orientation = orientation
        for x in range(self.size):
            next_free_y = 0
            for y in range (self.size):
                if self.get(y, x) == 'O':
                    if next_free_y != y:
                        self.set(y, x, '.')
                        self.set(next_free_y, x, 'O')
                    next_free_y += 1
                if self.get(y, x) == '#':
                    next_free_y = y + 1

    def load(self) -> tuple[int, 'hashlib._Hash']:
        load = 0
        hash = hashlib.new('sha256')
        for y in range(self.size):
            hash.update(self.grid[y])
            for x in range(self.size):
                if self.grid[y][x] == ord('O'):
                    load += self.size - y
        return load, hash.digest()

class Day14(BaseDay):
    platform: Platform

    def part1(self) -> None:
        with open(self.input) as file:
            self.platform = Platform.parse(file.read())
        self.platform.tilt()
        print("day14 part1:", self.platform.load()[0])

    def part2(self) -> None:
        with open(self.input) as file:
            self.platform = Platform.parse(file.read())
        cycles = {}
        count = 0
        searching = True
        while count < 1000000000:
            # This is weird, puzzle says NWSE, but that doesn't work.
            for dir in 'N', 'E', 'S', 'W':
                self.platform.tilt(dir)
            count += 1
            load, digest = self.platform.load()
            if searching:
                if digest in cycles:
                    cycle = count - cycles[digest]
                    count %= cycle
                    count += (1000000000 // cycle) * cycle
                    searching = False
                cycles[digest] = count
        print("day14 part2:", load)
