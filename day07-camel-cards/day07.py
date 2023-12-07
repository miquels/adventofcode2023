from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

cardmap = {
        '5': 7, '41': 6, '32': 5, '311': 4, '221': 3, '2111': 2, '11111': 1,
}

strengthmap1 = {
        'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'j', 'T': 'i', '9': 'h', '8': 'g',
        '7': 'f', '6': 'e', '5': 'd', '4': 'c', '3': 'b', '2': 'a',
}

strengthmap2 = {
        'A': 'm', 'K': 'l', 'Q': 'k', 'T': 'j', '9': 'i', '8': 'h',
        '7': 'g', '6': 'f', '5': 'e', '4': 'd', '3': 'c', '2': 'b', 'J': 'a',
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
        return cls(cards, 0, '', int(bid))

    def __lt__(self, other: Self) -> bool:
        if self.type < other.type:
            return True
        if self.type == other.type:
            return bool(self.strength < other.strength)
        return False

    def apply_part1_rules(self) -> None:
        n = [ 49 ]
        s = sorted(self.cards)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n[-1] += 1
            else:
                n.append(49)
        self.type = cardmap["".join(map(chr, sorted(n, reverse = True)))]
        self.strength = "".join(map(lambda x: strengthmap1[x], [*self.cards]))

    def apply_part2_rules(self) -> None:
        n = [ 49 ]
        s = sorted([card for card in self.cards if card != 'J'])
        jokers = len(self.cards) - len(s)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n[-1] += 1
            else:
                n.append(49)
        n = sorted(n, reverse = True)
        for i in range(0, len(n)):
            if jokers > 0:
                add = min(jokers, 53 - n[i])
                n[i] += add
                jokers -= add
        self.type = cardmap["".join(map(chr, n))]
        self.strength = "".join(map(lambda x: strengthmap2[x], [*self.cards]))

class Day07(BaseDay):
    hands: list[Hand]

    def init(self) -> None:
        self.hands = []
        with open(self.input) as f:
            for line in f:
                self.hands.append(Hand.parse(line))

    def part1(self) -> None:
        total = 0
        for hand in self.hands:
            hand.apply_part1_rules()
        for i, hand in enumerate(sorted(self.hands)):
            total += (i + 1) * hand.bid
        print('day07 part1:', total)

    def part2(self) -> None:
        total = 0
        for hand in self.hands:
            hand.apply_part2_rules()
        for i, hand in enumerate(sorted(self.hands)):
            total += (i + 1) * hand.bid
        print('day07 part2:', total)
