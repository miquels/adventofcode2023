# Based on Cor's solution in PHP translated to python.

from baseday import BaseDay
from itertools import pairwise

# Use recursion.
def calc(numbers: list[int]) -> int:
    nums = [n[1] - n[0] for n in pairwise(numbers)]
    return numbers[-1] if sum(nums) == 0 else numbers[-1] + calc(nums)

class Day09(BaseDay):
    lines: list[list[int]]

    def init(self) -> None:
        with open(self.input) as f:
            self.lines = [list(map(int, line.split())) for line in f]

    def part1(self) -> None:
        print("day09 part1:", sum(calc(line) for line in self.lines))

    # Realization that part2 is part1 with the numbers reversed.
    def part2(self) -> None:
        print("day09 part2:", sum(calc(line[::-1]) for line in self.lines))
