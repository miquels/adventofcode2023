from baseday import BaseDay
from dataclasses import dataclass
from typing import Self
import re

@dataclass
class Row:
    springs: str
    groups: list[int]

    @classmethod
    def parse(cls, line: str) -> Self:
        s, o = line.split()
        groups = list(map(int, o.split(',')))
        return cls(s, groups)

CACHE: dict[tuple[str, tuple[int, ...]], int] = {}

def munch(springs: str, groups: tuple[int, ...]) -> int:
    xt = (springs, groups)
    if xt not in CACHE:
        CACHE[xt] = do_munch(springs, groups)
    return CACHE[xt]

def do_munch(springs: str, groups: tuple[int, ...]) -> int:
    res = 0
    springs = springs.lstrip('.')
    if len(groups) == 0:
        # Trailing '.' and '?' are fine.
        res += re.match(r"[.?]*$", springs) is not None
        return res
    # Match '[#?]' of length 'groups[0]' followed by '.', '?', or EOL
    match = re.match(f"[#?]{{{groups[0]}}}(?:[?.]|$)", springs) is not None
    if match:
        # Skip the group that we matched and try the rest.
        res += munch(springs[groups[0]+1:], groups[1:])
    if springs[0:1] == '?':
        # This '?' could be a '.', so skip over it and try to match.
        res += munch(springs[1:], groups)
    return res

class Day12(BaseDay):
    rows: list[Row]

    def init(self) -> None:
        with open(self.input) as f:
            self.rows = [Row.parse(line) for line in f]

    def solve(self, unfold: int) -> int:
        total = 0
        for i, row in enumerate(self.rows):
            springs = "?".join([row.springs] * unfold)
            groups = row.groups * unfold
            total += munch(springs, tuple(groups))
        return total

    def part1(self) -> None:
        print("day12 part1:", self.solve(1))

    def part2(self) -> None:
        print("day12 part2:", self.solve(5))
