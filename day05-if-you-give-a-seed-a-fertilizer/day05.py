from baseday import BaseDay
from dataclasses import dataclass
from itertools import batched
from typing import Iterator, Self

@dataclass
class MapLine:
    start: int
    end: int
    offset: int

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
            dst_start, src_start, length = list(map(int, line.split()))
            maplines.append(MapLine(src_start, src_start + length, dst_start - src_start))
        return cls(maplines)

    def map(self, number: int) -> int:
        for line in self.maplines:
            if number >= line.start and number < line.end:
                return number + line.offset
        return number

class Almanac:
    seednums: list[int]
    maps: list[Map]

    def __init__(self, input: Iterator[str]):
        line = next(input)
        self.seednums = list(map(int, line.split()[1:]))
        next(input)
        self.maps = []
        for _ in range(0, 7):
            self.maps.append(Map.parse(input))

    def map_seed(self, seed: int) -> int:
        for map in self.maps:
            seed = map.map(seed)
        return seed

class Day05(BaseDay):
    almanac: Almanac

    def init(self) -> None:
        with open(self.input) as f:
            self.almanac = Almanac(f)

    def part1(self) -> None:
        locations = [self.almanac.map_seed(seed) for seed in self.almanac.seednums]
        print('day05 part1:', min(locations))

    def part2(self) -> None:
        locations = []
        for start, length in batched(self.almanac.seednums, 2):
            loc = min(self.almanac.map_seed(seed) for seed in range(start, start + length))
            locations.append(loc)
        print('day05 part2:', min(locations))
