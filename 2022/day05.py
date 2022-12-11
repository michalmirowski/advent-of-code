# https://adventofcode.com/2022/day/5
import copy

# read input
with open('input_files/input05.txt') as f:
    text = f.read().splitlines()
    start_stacks = text[0:8]
    moves = text[10:]

# workaround for a shorter first line - fill it in with characters
stacks_fixed = []
for line in start_stacks:
    if len(line) < len(max(start_stacks)):
        line = line + '*' * (len(max(start_stacks)) - len(line))
    stacks_fixed.append(line)

# transpose a list
stacks_transposed = []
temp = []

for i in range(1, len(max(stacks_fixed)), 4):  # iterate through columns; every 4 character might be a crate name
    temp = [element[i] for element in stacks_fixed if element[i] not in (' ', '*')]  # iterate through list items
    temp.reverse()
    stacks_transposed.append(temp)

print('Transposed stacks:', stacks_transposed)

# create a list for result of each part
final_stacks_01 = copy.deepcopy(stacks_transposed)
final_stacks_02 = copy.deepcopy(stacks_transposed)

# final solution
for move in moves:
    move = move.replace("from", ",").replace("move", "").replace("to", ",").replace(" ", "")
    move = list(map(int, move.split(",")))
    quantity = move[0]  # quantity of elements moved per one input line
    fr = move[1] - 1  # index of original stack (move from)
    to = move[2] - 1  # index of target stack (move to)

    # part one - crates are moved one by one
    for i in range(quantity):
        element_moved_01 = final_stacks_01[fr].pop()  # remove last element from original stack
        final_stacks_01[to].append(element_moved_01)  # add last element from original stack to target

    # part two - crates are moved together for each input line
    elements_moved_02 = final_stacks_02[fr][-quantity:]  # all items moved per one input line
    final_stacks_02[to] += elements_moved_02
    del final_stacks_02[fr][-quantity:]

# read last elements
top_crate_01 = ''.join([stack[-1] for stack in final_stacks_01])
top_crate_02 = ''.join([stack[-1] for stack in final_stacks_02])

print('Stacks after the rearrangement procedure completes:', '\nPART ONE: ', final_stacks_01, '\nPART TWO: ',
      final_stacks_02)
print('Crates that ended up on top of each stack:', '\nPART ONE: ', top_crate_01, '\nPART TWO: ', top_crate_02)
