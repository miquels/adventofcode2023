from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Card:
    winning: set[int]
    have: list[int]
    instances: int

    def matches(self) -> int:
        return sum([number in self.winning for number in self.have])

    def worth(self) -> int:
        matches = self.matches()
        return int(pow(2, matches - 1)) if matches > 0 else 0

    @classmethod
    def parse(cls, line: str) -> Self:
        _, line = line.split(': ')
        w, h = line.split(' | ')
        return cls(set(map(int, w.split())), list(map(int, h.split())), 1)

class Day04(BaseDay):
    cards: list[Card]

    def init(self) -> None:
        with open(self.input) as f:
            self.cards = [Card.parse(line) for line in f]

    def part1(self) -> None:
        print('day04 part1', sum([card.worth() for card in self.cards]))

    def part2(self) -> None:
        for (i, card) in enumerate(self.cards):
            for c in self.cards[i + 1: i + 1 + card.matches()]:
                c.instances += card.instances
        print('day04 part2:', sum([card.instances for card in self.cards]))
