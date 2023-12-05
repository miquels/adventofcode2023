from baseday import BaseDay
from dataclasses import dataclass
from typing import Iterator, Self

@dataclass
class MapLine:
    dst_start: int
    src_start: int
    len: int

@dataclass
class Map:
    maplines: list[MapLine]

    @classmethod
    def parse(cls, input: Iterator[str]) -> Self:
        next(input)
        maplines = []
        for line in input:
            if line == "\n":
                break
            numbers = list(map(int, line.split()))
            maplines.append(MapLine(numbers[0], numbers[1], numbers[2]))
        return cls(maplines)

    def map(self, number: int) -> int:
        for line in self.maplines:
            if number >= line.src_start and number < line.src_start + line.len:
                return line.dst_start + (number - line.src_start)
        return number

class Game:
    seeds: list[int]
    maps: list[Map]

    def __init__(self, input: Iterator[str]):
        line = next(input)
        self.seeds = list(map(int, line.split()[1:]))
        next(input)
        self.maps = []
        for _ in range(0, 7):
            self.maps.append(Map.parse(input))

    def map_seed(self, seed: int) -> int:
        for map in self.maps:
            seed = map.map(seed)
        return seed

class Day05(BaseDay):
    game: Game

    def init(self) -> None:
        with open(self.input) as f:
            self.game = Game(f)

    def part1(self) -> None:
        locations = [self.game.map_seed(seed) for seed in self.game.seeds]
        print('day05 part1:', min(locations))

    def part2(self) -> None:
        print('day05 part2: TBD')
