import re, sys
from baseday import BaseDay

class Day01(BaseDay):

    def part1(self):
        total = 0
        with open(self.input) as f:
            for line in f:
                digits = [c for c in line if c.isdigit()]
                total += int(digits[0] + digits[-1])
        print("day1 part1: ", total)

    def part2(self):
        digitmap = {
            'zero': 0 ,'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        }
        digits = '|'.join(digitmap.keys())
        total = 0
        with open(self.input) as f:
            for line in f:
                first = digitmap[re.search(f"^.*?({digits}).*", line).group(1)]
                last = digitmap[re.search(f"^.*({digits})", line).group(1)]
                total += first * 10 + last
        print("day1 part2: ", total)
