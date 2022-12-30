# https://adventofcode.com/2022/day/8
# based on https://github.com/mebeim/aoc/tree/master/2022#day-8---treetop-tree-house walktrough

with open("input_files/input08.txt", "r") as f:
    grid = f.read().splitlines()

y, x = len(grid), len(grid[0])  # height and width of the grid
visible = y * 2 + x * 2 - 4  # minus 4 because they would be duplicated
east, west, north, south = 0, 0, 0, 0  # tree counters in each direction
best = 0

for r in range(1, y - 1):  # iterate through rows except first and last
    row = grid[r]

    for c in range(1, x - 1):  # iterate through columns except first and last
        tree = row[c]
        visible_from_east = True
        visible_from_west = True
        visible_from_north = True
        visible_from_south = True

        for east in range(c + 1, x):  # going right from the tree to the right border
            if tree <= row[east]:
                visible_from_east = False
                break
        for west in range(c - 1, -1, -1):  # going left from the tree to the left border
            if tree <= row[west]:
                visible_from_west = False
                break
        for south in range(r + 1, y):  # going down from the tree to the bottom
            if tree <= grid[south][c]:
                visible_from_south = False
                break
        for north in range(r - 1, -1, -1):  # going up from the tree to the upper border
            if tree <= grid[north][c]:
                visible_from_north = False
                break

        # PART ONE
        if visible_from_east or visible_from_west or visible_from_north or visible_from_south:
            visible += 1

        # PART TWO
        score = (east - c) * (c - west) * (south - r) * (r - north)

        if score > best:
            best = score

print('PART ONE: Number of visible trees =', visible)
print('PART TWO: Highest scenic score =', best)
