from dataclasses import dataclass
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

    def __init__(self, input: str) -> None:
        self.numbers  = []
        self.symbols  = []
        with open(input) as f:
            for (y, line) in enumerate(f):
                (nums, syms) = self.parse(line.strip(), y)
                self.numbers.append(nums)
                self.symbols.extend(syms)

    def parse(self, line: str, y: int) -> tuple[list[Number], list[Symbol]]:
        n = re.finditer(r"([0-9]+)", line)
        s = re.finditer(r"([^0-9.])", line)
        nums = list(map(lambda x: Number(int(x.group(1)), x.span(), y), n))
        syms = list(map(lambda x: Symbol(x.group(1), x.span()[0], y), s))
        return (nums, syms)

    def overlap_y(self, symbol: Symbol, offset: int) -> list[Number]:
        if symbol.y + offset < 0 or symbol.y + offset >= len(self.numbers):
            return []
        predicate = lambda n: symbol.x >= n.x[0] - 1 and symbol.x <= n.x[1]
        return list(filter(predicate, self.numbers[symbol.y + offset]))

    def overlap(self, symbol: Symbol)-> list[Number]:
        rnums = []
        rnums.extend(self.overlap_y(symbol, -1))
        rnums.extend(self.overlap_y(symbol, 0))
        rnums.extend(self.overlap_y(symbol, 1))
        return rnums

    def part_numbers(self) -> list[Number]:
        rnums = []
        for symbol in self.symbols:
            rnums.extend(self.overlap(symbol))
        return rnums

    def gear_parts(self) -> list[tuple[Number, Number]]:
        rnums = []
        stars = filter(lambda x: x.value == '*', self.symbols)
        for symbol in stars:
            nums = self.overlap(symbol)
            if len(nums) == 2:
                rnums.append((nums[0], nums[1]))
        return rnums

class Day03(BaseDay):
    def part1(self) -> None:
        game = Game(self.input)
        parts = game.part_numbers()
        print('day03 part1:', sum(map(lambda x: x.value, parts)))

    def part2(self) -> None:
        game = Game(self.input)
        parts = game.gear_parts()
        print('day03 part2:', sum(map(lambda x: x[0].value * x[1].value, parts)))
