from baseday import BaseDay
from functools import reduce
from itertools import pairwise

def calc(numbers: list[int], index: int) -> list[int]:
    res = []
    while sum(numbers) != 0:
        res.append(numbers[index])
        numbers = [n[1] - n[0] for n in pairwise(numbers)]
    return res

class Day09(BaseDay):
    lines: list[list[int]]

    def init(self) -> None:
        with open(self.input) as f:
            self.lines = [list(map(int, line.split())) for line in f]

    def part1(self) -> None:
        total = sum(sum(calc(line, -1)) for line in self.lines)
        print("day09 part1:", total)

    def part2(self) -> None:
        total = sum(reduce(lambda x, y: y - x, calc(line, 0)[::-1]) for line in self.lines)
        print("day09 part2:", total)
