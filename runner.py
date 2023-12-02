
import day01, day02

days = [ day01.Day01, day02.Day02 ]

for day in days:
    instance = day()
    instance.run()
