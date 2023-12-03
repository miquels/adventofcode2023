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
    symbols: list[list[Symbol]]

    def __init__(self, input):
        self.numbers  = []
        self.symbols  = []
        y = 0
        with open(input) as f:
            for line in f:
                (nums, syms) = self.parse(line.strip(), y)
                self.numbers.append(nums)
                self.symbols.append(syms)
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

    def overlap_y(self, symbol: Symbol, offset: int) -> list[Number]:
        rnums = []
        numbers = self.numbers[symbol.y + offset]
        i = 0
        while i < len(numbers):
            n = numbers[i]
            if symbol.x >= n.x[0] - 1 and symbol.x <= n.x[1]:
                rnums.append(numbers.pop(i))
            else:
                i += 1
        return rnums

    def overlap(self, symbol: Symbol)-> list[Number]:
        rnums = []
        if symbol.y > 0:
            rnums.extend(self.overlap_y(symbol, -1))
        rnums.extend(self.overlap_y(symbol, 0))
        if symbol.y < len(self.numbers) - 1:
            rnums.extend(self.overlap_y(symbol, 1))
        return rnums

    def part_numbers(self) -> list[Number]:
        rnums = []
        for symbol in itertools.chain.from_iterable(self.symbols):
            rnums.extend(self.overlap(symbol))
        return rnums

class Day03(BaseDay):
    def part1(self):
        game = Game(self.input)
        parts = game.part_numbers()
        print('day03 part1:', sum(map(lambda x: x.value, parts)))

    def part2(self):
        print('day03 part2: TBD')
