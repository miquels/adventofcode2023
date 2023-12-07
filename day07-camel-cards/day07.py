from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

cardmap = {
        '5': 7, '41': 6, '32': 5, '311': 4, '221': 3, '2111': 2, '11111': 1,
}

strengthmap = {
        'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'j', 'T': 'i', '9': 'h',
        '8': 'g', '7': 'f', '6': 'e', '5': 'd', '4': 'c', '3': 'b', '2': 'a',
}

@dataclass
class Hand:
    cards: str
    type: int
    strength: str
    bid: int

    @classmethod
    def parse(cls, line: str) -> Self:
        cards, bid = line.split()
        n = [ 49 ]
        s = sorted(cards)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n[-1] += 1
            else:
                n.append(49)
        type = cardmap["".join(map(chr, sorted(n, reverse = True)))]
        strength = "".join(map(lambda x: strengthmap[x], [*cards]))
        return cls(cards, type, strength, int(bid))

    def __lt__(self, other: Self) -> bool:
        if self.type < other.type:
            return True
        if self.type == other.type:
            return bool(self.strength < other.strength)
        return False

class Day07(BaseDay):
    hands: list[Hand]

    def init(self) -> None:
        self.hands = []
        with open(self.input) as f:
            for line in f:
                self.hands.append(Hand.parse(line))

    def part1(self) -> None:
        total = 0
        for i, hand in enumerate(sorted(self.hands)):
            total += (i + 1) * hand.bid
        print('day07 part1:', total)

    def part2(self) -> None:
        print('day07 part2:', 'TBD')
