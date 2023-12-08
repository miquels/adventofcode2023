import math, re
from baseday import BaseDay
from dataclasses import dataclass
from typing import Callable, Self

@dataclass
class Node:
    name: str
    left: str
    right: str

    @classmethod
    def parse(cls, line: str) -> Self:
        matches = re.search(r'(\w+) = \((\w+), (\w+)\)', line)
        if matches is None:
            raise ValueError('failed to parse input line')
        return cls(*matches.groups())

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

    def count(self, node: Node, stop: Callable[[Node], bool]) -> int:
        steps = 0
        while True:
            for step in [*self.steps]:
                steps += 1
                node = self.nodes[node.left] if step == 'L' else self.nodes[node.right]
                if stop(node):
                    return steps

    def part1(self) -> None:
        steps = self.count(self.nodes['AAA'], lambda x: x.name == 'ZZZ')
        print('day08 part1:', steps)

    def part2(self) -> None:
        nodes = [node for name, node in self.nodes.items() if name.endswith('A')]
        cycles = [self.count(node, lambda x: x.name.endswith('Z')) for node in nodes]
        print('day08 part2:', math.lcm(*cycles))
