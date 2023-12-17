from baseday import BaseDay
from dataclasses import dataclass
from functools import reduce

def hash(s: str) -> int:
    return reduce(lambda a, b: (17 * (a + b)) % 256, bytes(s, 'ascii'), 0)

class Day15(BaseDay):
    initseq: list[str] = []

    def init(self) -> None:
        with open(self.input) as file:
            for line in file:
                self.initseq += [word for word in line.strip().split(',')]

    def part1(self) -> None:
        print("day15 part1:", sum([hash(s) for s in self.initseq]))

    def part2(self) -> None:
        print("day15 part2:", 'TBD')
