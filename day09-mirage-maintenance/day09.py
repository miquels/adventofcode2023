from baseday import BaseDay
from itertools import pairwise

class Day09(BaseDay):
    lines: list[list[int]]

    def init(self) -> None:
        with open(self.input) as f:
            self.lines = [list(map(int, line.split())) for line in f]

    def part1(self) -> None:
        total = 0
        for nums in self.lines:
            while True:
                total += nums[-1]
                nums = [n[1] - n[0] for n in pairwise(nums)]
                if sum(nums) == 0:
                    break
        print("day09 part1:", total)

    def part2(self) -> None:
        print("day09 part2:", 'TBD')
