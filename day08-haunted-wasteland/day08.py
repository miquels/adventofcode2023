import re
from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Node:
    name: str
    left: str
    right: str

    @classmethod
    def parse(cls, line: str) -> Self:
        name, left, right = re.search(r'(\w+) = \((\w+), (\w+)\)', line).groups()
        return cls(name, left, right)

class Day08(BaseDay):
    steps: str
    nodes: dict[str, Node]

    def init(self) -> None:
        with open(self.input) as f:
            self.steps = next(f).strip()
            next(f)
            self.nodes = {}
            for line in f:
                node = Node.parse(line)
                self.nodes[node.name] = node

    def part1(self) -> None:
        node = self.nodes['AAA']
        done = False
        steps = 0
        while not done:
            for step in [*self.steps]:
                steps += 1
                if step == 'L':
                    node = self.nodes[node.left]
                else:
                    node = self.nodes[node.right]
                if node.name == 'ZZZ':
                    done = True
                    break
        print('day08 part1:', steps)

    def part2(self) -> None:
        print('day08 part2:', 'TBD')
