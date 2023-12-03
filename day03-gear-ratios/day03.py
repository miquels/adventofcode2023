from dataclasses import dataclass
import itertools
import re

from baseday import BaseDay

@dataclass 
class Number:
    value: int
    x: tuple[int, int]
    y: int

@dataclass 
class Symbol:
    value: str
    x: int
    y: int

class Game:
    numbers: list[list[Number]]
    symbols: list[Symbol]

    def __init__(self, input):
        self.numbers  = []
        self.symbols  = []
        y = 0
        with open(input) as f:
            for line in f:
                (nums, syms) = self.parse(line.strip(), y)
                self.numbers.append(nums)
                self.symbols.extend(syms)
                y += 1

    def parse(self, line: str, y: int) -> tuple[list[Number], list[Symbol]]:
        nums: list[Number] = []
        syms: list[Symbol] = []
        n = re.finditer(r"([0-9]+)", line)
        if n is not None:
            nums.extend(map(lambda x: Number(int(x.group(1)), x.span(), y), n))
        s = re.finditer(r"([^0-9.])", line)
        if s is not None:
            syms.extend(map(lambda x: Symbol(x.group(1), x.span()[0], y), s))
        return (nums, syms)

    def overlap_y(self, symbol: Symbol, offset: int, remove: bool) -> list[Number]:
        rnums = []
        numbers = self.numbers[symbol.y + offset]
        i = 0
        while i < len(numbers):
            n = numbers[i]
            if symbol.x >= n.x[0] - 1 and symbol.x <= n.x[1]:
                if remove:
                    rnums.append(numbers.pop(i))
                else:
                    rnums.append(numbers[i])
                    i += 1
            else:
                i += 1
        return rnums

    def overlap(self, symbol: Symbol, remove: bool = False)-> list[Number]:
        rnums = []
        if symbol.y > 0:
            rnums.extend(self.overlap_y(symbol, -1, remove))
        rnums.extend(self.overlap_y(symbol, 0, remove))
        if symbol.y < len(self.numbers) - 1:
            rnums.extend(self.overlap_y(symbol, 1, remove))
        return rnums

    def part_numbers(self) -> list[Number]:
        rnums = []
        for symbol in self.symbols:
            rnums.extend(self.overlap(symbol, True))
        return rnums

    def gear_parts(self) -> list[tuple[Number, Number]]:
        rnums = []
        stars = filter(lambda x: x.value == '*', self.symbols)
        for symbol in stars:
            nums = self.overlap(symbol, False)
            if len(nums) == 2:
                rnums.append((nums[0], nums[1]))
        return rnums

class Day03(BaseDay):
    def part1(self):
        game = Game(self.input)
        parts = game.part_numbers()
        print('day03 part1:', sum(map(lambda x: x.value, parts)))

    def part2(self):
        game = Game(self.input)
        parts = game.gear_parts()
        print('day03 part2:', sum(map(lambda x: x[0].value * x[1].value, parts)))
