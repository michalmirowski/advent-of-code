# https://adventofcode.com/2022/day/1

# read input
with open('input_files/input01.txt') as elf_input:
    elf_list = elf_input.read().splitlines()

print('Input list: ', elf_list)

# find top 3 max calories sum
new_sum = 0
top_list = []

for line in elf_list:
    if line == '':
        new_sum = 0
    else:
        new_sum += int(line)
        top_list.append(new_sum)
        top_list.sort(reverse=True)

print('Sorted top list:', top_list)
print('Max calories: ', top_list[0])
print('Top 3 in total: ', top_list[0] + top_list[1] + top_list[2])
