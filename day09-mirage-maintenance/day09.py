from baseday import BaseDay
from functools import reduce
from itertools import pairwise

def calc(numbers: list[int], index: int) -> list[int]:
    nums = [ numbers ]
    while True:
        nums.append([n[1] - n[0] for n in pairwise(nums[-1])])
        if sum(nums[-1]) == 0:
            return [num[index] for num in nums]

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
