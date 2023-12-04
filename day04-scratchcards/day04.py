from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Card:
    winning: set[int]
    hand: list[int]

    def worth(self) -> int:
        matches = sum([number in self.winning for number in self.hand])
        return int(pow(2, matches - 1)) if matches > 0 else 0

    @classmethod
    def parse(cls, line: str) -> Self:
        [_, line] = line.split(': ')
        [w, h] = line.split(' | ')
        return cls(set(map(int, w.split())), list(map(int, h.split())))

class Game:
    cards: list[Card]

    def __init__(self, input: str) -> None:
        with open(input) as f:
            self.cards = [Card.parse(line) for line in f]

class Day04(BaseDay):
    def part1(self) -> None:
        game = Game(self.input)
        print('day04 part1', sum([card.worth() for card in game.cards]))

    def part2(self) -> None:
        print('day04 part2: TBD')
