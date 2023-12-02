class BaseDay():
    input: str

    def __init__(self, input: str | None = None):
        if input is None:
            input = self.__class__.__name__.lower() + '-input.txt'
        self.input = input

    def part1(self) -> None:
        raise NotImplementedError()

    def part2(self) -> None:
        raise NotImplementedError()

    def run(self) -> None:
        self.part1()
        self.part2()
