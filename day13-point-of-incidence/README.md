# [--- Day 13: Point of Incidence ---](https://adventofcode.com/2023/day/13)

## Part 1.

We get a bunch of matrixes filled with '#' and '.' characters. In the
matrix, we need to find a line between rows or columns where the two
sides of the line are mirror images of each other. If one side is smaller
than the other, ignore the larger part of the other side.

Strategy:

- compare row 0-1. same -> done
- compare row 1-2, then 0-3. same -> done
- compare row 2-3, then 1-4, then 0-5. same -> done

... etc until the last row minus one.

To compare columns, just transpose the matrix and do the same thing.

Comments on some of the code:

```
for y1, y2 in zip(self.grid[y::-1], self.grid[y+1:]):
```

This creates two lists, one of the rows above 'y', and one of the rows 'below'.
The first one, of the rows below, also runs in reverse. So for y = 2, we
get rows 2,1,0 and 3,4,5. Zip them together and that's rows
(2,3) (1,4) (0, 5). This is what we need, see above at 'Strategy'.

```
diff += sum([x1 != x2 for x1, x2 in zip(y1, y2)])
```
This compares every element in the two rows. We use the fact that Python
automatically casts booleans to small integers, 1 and 0. The result is the
number of differences encountered between the two rows (0 if they're the same).
And we need that for part 2.


## Part 2.

We need to find the same mirror image, but one image has a smudge on it
and is a '#' instead of a '.' or vice versa.

We can follow the same strategy as in part1, but now we count the number
of mismatches we encounter. If a total set of comparisions differs by
one character, we know that there was one smudge.
