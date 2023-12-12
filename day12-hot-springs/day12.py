from baseday import BaseDay
from dataclasses import dataclass
from typing import Iterator, Self
import re

@dataclass
class Row:
    springs: str
    re: re.Pattern
    count: int

    @classmethod
    def parse(cls, line: str) -> Self:
        s, o = line.split()
        ops = list(map(int, o.split(',')))
        pats = []
        for o in ops:
            pats.append(f"[?#]{{{o}}}")
        pat = r"[.?]*" + "[.?]+".join(pats) + r"[.?]*$"
        return cls(s, re.compile(pat), 0)

    def calc(self, sub: str) -> None:
        if not re.match(self.re, sub):
            return
        if sub.find('?') < 0:
            self.count += 1
            return
        self.calc(sub.replace('?', '.', 1))
        self.calc(sub.replace('?', '#', 1))
    
class Day12(BaseDay):
    rows: list[Row]

    def init(self) -> None:
        self.rows = []
        with open(self.input) as f:
            self.rows = [Row.parse(line) for line in f]

    def part1(self) -> None:
        total = 0
        for row in self.rows:
            row.calc(row.springs)
        print("day12 part1:", sum([r.count for r in self.rows]))

    def part2(self) -> None:
        print("day12 part2:", 'TBD')
