# https://adventofcode.com/2022/day/4

import string

# create dictionary for priorities
letters = string.ascii_letters
priority_dict = {letters[i]: i + 1 for i in range(len(letters))}

# read input
with open('input_files/input03.txt') as puzzle_input:
    lines = puzzle_input.read().splitlines()

# part one
priority = 0

for line in lines:
    division = len(line) // 2
    first_comp = [line[i] for i in range(division)]
    second_comp = [line[-1 - i] for i in range(division)]
    common = set(first_comp).intersection(second_comp)
    priority += priority_dict[list(common)[0]]
print('Total priority:', priority)

# part two
priority_badge = 0

for i in range(0, len(lines), 3):
    group = lines[i:i + 3]
    common = set(group[0]).intersection(group[1], group[2])
    priority_badge += priority_dict[list(common)[0]]
print('Total priority of badge items:', priority_badge)
