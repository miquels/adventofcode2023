from baseday import BaseDay
from dataclasses import dataclass
from typing import Iterator, Self

@dataclass
class Row:
    springs: str
    ops: list[int]

    @classmethod
    def parse(cls, line: str) -> Self:
        s, o = line.split()
        ops = list(map(int, o.split(',')))
        return cls(s, ops)

    def permutations(self) -> Iterator[str]:
        sp = self.springs
        qs = [x for x in range(0, len(sp)) if sp[x] == '?']
        ba = bytearray(sp, 'ascii')
        for n in range(0, 2 ** len(qs)):
            for i, d in enumerate([*bin(n)[2:].zfill(len(qs))]):
                ba[qs[i]] = ord('#') if d == '1' else ord('.')
            yield ba.decode('ascii')

    def check_row(self, row: str) -> bool:
        return list(filter(int, (map(len, row.split('.'))))) == self.ops
    
class Day12(BaseDay):
    rows: list[Row]

    def init(self) -> None:
        self.rows = []
        with open(self.input) as f:
            self.rows = [Row.parse(line) for line in f]

    def part1(self) -> None:
        total = 0
        for row in self.rows:
            total += sum(row.check_row(r) for r in row.permutations())
        print("day12 part1:", total)

    def part2(self) -> None:
        print("day12 part2:", 'TBD')
