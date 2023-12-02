class BaseDay():
    input: str
    example: bool

    def __init__(self, input: str | None = None, example: bool = False):
        dir, name = self.__module__.split('.')
        if input is None:
            if example:
                input = dir + '/' + name + '-example.txt'
            else:
                input = dir + '/' + name + '-input.txt'
        self.input = input

    def part1(self) -> None:
        raise NotImplementedError()

    def part2(self) -> None:
        raise NotImplementedError()

    def run(self, part: int | None = None) -> None:
        if part is None or part == 1:
            self.part1()
        if part is None or part == 2:
            self.part2()
