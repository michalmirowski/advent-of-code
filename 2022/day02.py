# https://adventofcode.com/2022/day/2

# first column - opponent play
# A - Rock, B = Paper, C - Scissors

# points rules
# Rock = 1, Paper = 2, Scissors = 3
# Lost = 0, Draw = 3, Win = 6

# read input
with open('input_files/input02.txt') as puzzle_input:
    lines = puzzle_input.read().splitlines()

# part one

# second column - response
# X = Rock, Y - Paper, Z - Scissors

wins = ['A Y', 'B Z', 'C X']
draws = ['A X', 'B Y', 'C Z']
loses = ['A Z', 'B X', 'C Y']


def part_one():
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    points = 0
    for line in lines:
        my_play = line[2]
        points += (line in wins) * 6
        points += (line in draws) * 3
        points += shape_score[my_play]

    print('Total score according to the first strategy: ', points)


# part two

# second column is now expected result
# X = Lost, Y - Draw, Z - Win
win_matrix = {'A': 'B', 'B': 'C', 'C': 'A'}
loss_matrix = {'A': 'C', 'B': 'A', 'C': 'B'}


def part_two():
    shape_score = {'A': 1, 'B': 2, 'C': 3}
    my_play = ''
    points = 0
    for line in lines:
        op_play = line[0]
        result = line[2]
        if result == 'Y':  # draw
            points += 3
            my_play = op_play
        elif result == 'Z':  # win
            points += 6
            my_play = win_matrix[op_play]
        elif result == 'X':  # loss
            my_play = loss_matrix[op_play]
        points += shape_score[my_play]

    print('Total score according to the second strategy: ', points)


part_one()
part_two()
