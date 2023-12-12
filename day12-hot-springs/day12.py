from baseday import BaseDay
from dataclasses import dataclass
from typing import Iterator, Self
import re

@dataclass
class Row:
    springs: str
    ops: list[int]
    pat: re.Pattern[str] = re.compile('')
    count: int = 0

    @classmethod
    def parse(cls, line: str) -> Self:
        s, o = line.split()
        ops = list(map(int, o.split(',')))
        return cls(s, ops)

    def unfold(self) -> None:
        self.springs = "?".join([self.springs] * 5)
        self.ops = self.ops * 5

    def compile(self) -> None:
        pats = []
        for o in self.ops:
            pats.append(f"[?#]{{{o}}}")
        pat = r"[.?]*" + "[.?]+".join(pats) + r"[.?]*$"
        self.pat = re.compile(pat)

    def recurse(self, sub: str) -> None:
        if not self.pat.match(sub):
            return
        if sub.find('?') < 0:
            self.count += 1
            return
        self.recurse(sub.replace('?', '.', 1))
        self.recurse(sub.replace('?', '#', 1))
    
class Day12(BaseDay):

    def solve(self, unfold: bool) -> int:
        rows = [Row.parse(line) for line in open(self.input)]
        total = 0
        for row in rows:
            if unfold:
                row.unfold()
            row.compile()
            row.recurse(row.springs)
        return sum([r.count for r in rows])

    def part1(self) -> None:
        print("day12 part1:", self.solve(False))

    def part2(self) -> None:
        print("day12 part2:", self.solve(True))
