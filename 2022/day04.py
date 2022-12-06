# https://adventofcode.com/2022/day/4

# read input
with open('input_files/input04.txt') as puzzle_input:
    lines = puzzle_input.read().splitlines()

# solution part one and two
fully_contain_counter = 0
overlap_counter = 0

# retrieve lists by min/max values
for line in lines:
    first_elf, second_elf = line.split(',')
    first_elf_start, first_elf_end = first_elf.split('-')
    second_elf_start, second_elf_end = second_elf.split('-')

    first_elf_list = [i for i in range(int(first_elf_start), int(first_elf_end)+1)]
    second_elf_list = [i for i in range(int(second_elf_start), int(second_elf_end)+1)]

    common = set(first_elf_list).intersection(second_elf_list)
    # condition part one
    if len(common) > 0 and (len(common) == len(first_elf_list) or len(common) == len(second_elf_list)):
        fully_contain_counter += 1
    # condition part two
    if len(common) > 0:
        overlap_counter += 1


print("Number of pairs where one range fully contains the other:", fully_contain_counter)

print("Number of pairs where ranges overlap:", overlap_counter)
