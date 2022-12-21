# read input
with open('input_files/input06.txt') as puzzle_input:
    data = puzzle_input.read()

marker = []
counter = 0
marker_len = 14  # 4 to get answer for part one, 14 for part two

# part one and two solution
for i in range(len(data)):
    marker += data[i]
    counter += 1
    if len(marker) == marker_len:
        if len(marker) == len(set(marker)):  # check if all elements in list are unique
            break
        del marker[0]
print('First marker after', counter, 'characters and it is:', marker)
