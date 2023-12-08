import re
from baseday import BaseDay
from dataclasses import dataclass
from typing import Self

@dataclass
class Node:
    name: str
    left: str
    right: str
    final: bool

    @classmethod
    def parse(cls, line: str) -> Self:
        name, left, right = re.search(r'(\w+) = \((\w+), (\w+)\)', line).groups()
        return cls(name, left, right, name.endswith('Z'))

    def step(self, step: str, nodes: dict[str, 'Node']) -> 'Node':
        if step == 'L':
            return nodes[self.left]
        else:
            return nodes[self.right]

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
                node = node.step(step, self.nodes)
                if node.name == 'ZZZ':
                    done = True
                    break
        print('day08 part1:', steps)

    def part2(self) -> None:
        nodes = [node for name, node in self.nodes.items() if name.endswith('A')]
        numnodes = len(nodes)
        done = False
        steps = 0
        while not done:
            for step in [*self.steps]:
                steps += 1
                final = 0
                for i in range(0, numnodes):
                    nodes[i] = nodes[i].step(step, self.nodes)
                    final += nodes[i].final
                if final == numnodes:
                    done = True
                    break
        print('day08 part2:', steps)
