from baseday import BaseDay
from collections import OrderedDict
from dataclasses import dataclass
from functools import reduce

def hash(s: str) -> int:
    return reduce(lambda a, b: (17 * (a + b)) % 256, bytes(s, 'ascii'), 0)

class Day15(BaseDay):
    initseq: list[str] = []

    def init(self) -> None:
        with open(self.input) as file:
            for line in file:
                self.initseq += [word for word in line.strip().split(',')]

    def part1(self) -> None:
        print("day15 part1:", sum([hash(s) for s in self.initseq]))

    def part2(self) -> None:
        boxes: list[OrderedDict] = [OrderedDict() for _ in range(256)]
        for step in self.initseq:
            if step.endswith('-'):
                label, _ = step.split('-')
                h = hash(label)
                if label in boxes[h]:
                    boxes[h].pop(label)
            else:
                label, focal = step.split('=')
                boxes[hash(label)][label] = focal
        total = 0
        for boxno, box in enumerate(boxes):
            for slot, focal in enumerate(box.values(), 1):
                total += (boxno + 1) * slot * int(focal)
        print("day15 part2:", total)

