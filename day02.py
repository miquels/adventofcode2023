import sys
from baseday import BaseDay

class Game():
    number: int
    grabs: list[dict[str, int]]

    # INPUT: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    def __init__(self, game: str):
        [name, grablist] = game.strip().split(': ', 2)
        self.number = int(name.split(' ')[1])
        grabs = [grab.split(', ') for grab in grablist.split('; ')]
        self.grabs = [Game.grab(grab) for grab in grabs]

    # INPUT: ['3 blue', '4 red']
    @staticmethod
    def grab(grab: list[str]) -> dict[str, int]:
        balls = [ball.split(' ') for ball in grab]
        balls2 = [ (x[1], int(x[0])) for x in balls]
        return dict(balls2)

    def possible(self, red: int, green: int, blue: int) -> bool:
        for grab in self.grabs:
            if grab.get('red', 0) > red or grab.get('green', 0) > green or grab.get('blue', 0) > blue:
                return False
        return True

    def power(self) -> int:
        r = max([grab.get('red', 0) for grab in self.grabs])
        g = max([grab.get('green', 0) for grab in self.grabs])
        b = max([grab.get('blue', 0) for grab in self.grabs])
        return r * g * b

    def __str__(self):
        return f"Game {self.number}: {self.grabs}"

class Day02(BaseDay):
    input: str = 'day02-input.txt'

    def part1(self):
        total = 0
        with open(self.input) as f:
            for line in f:
                game = Game(line)
                if game.possible(12, 13, 14):
                    total += game.number
        print('day02 part1:', total)

    def part2(self):
        total = 0
        with open(self.input) as f:
            for line in f:
                game = Game(line)
                total += game.power()
        print('day02 part2:', total)

if __name__ == "__main__":
    day = Day02(sys.argv[1])
    day.run()
