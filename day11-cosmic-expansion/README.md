## [Cosmic Expansion](https://adventofcode.com/2023/day/11)

Pretty simple.

Read grid into list of lists, get galaxy coordinates, then make a list of
empty rows (y coords) and empty columns (x coords). Adjust coordinates of
galaxies bij the number of empty rows/cols before them, multiplied by
either 2 or 1000000, then sum the manhattan distances of the unique coordinate
combinations.
