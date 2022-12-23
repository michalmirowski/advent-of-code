# https://adventofcode.com/2022/day/7

from collections import defaultdict
import re

with open("input_files/input07.txt", "r") as f:
    lines = f.read().splitlines()

cwd = []
sizes = defaultdict(int)

for line in lines:
    if line.startswith("$ cd"):  # if cd, update current directory
        special, cd, dir_name = line.split(' ')  # split $, cd and directory name
        if dir_name == "..":  # if 'cd ..', go back to previous working directory
            cwd = cwd[:-1]
        else:
            cwd.append(dir_name)
    elif line.startswith("$ cd"):  # if ls, then do nothing
        continue
    elif line[0].isdigit():  # if file size, add to current working directory size
        size = re.sub(r'[^0-9]', '', line)  # leave only numbers
        for i in range(1, len(cwd) + 1):
            sizes['/'.join(cwd[0:i])] += int(size)

# part one
print('PART ONE:', sum(filter(lambda x: x < 100000, sizes.values())))

# part two - list comprehension
print('PART TWO:', min([sizes[key] for key in sizes.keys() if (70000000 - sizes['/']) + sizes[key] > 30000000]))

# part two - lambda
print('PART TWO ALTERNATIVE SOLUTION:', min(filter(lambda x: (70000000 - sizes['/']) + x > 30000000, sizes.values())))
