# read input
with open('input_files/input06.txt') as puzzle_input:
    data = puzzle_input.read()


# part one and two solution
def find_marker_in_datastream(datastream, unique_len):
    marker = []
    counter = 0
    for i in range(len(datastream)):
        marker += datastream[i]
        counter += 1
        if len(marker) == unique_len:
            if len(marker) == len(set(marker)):  # check if all elements in list are unique
                break
            del marker[0]
    print('When marker has', unique_len, 'unique characters,then first marker is after', counter,
          'characters and it is:', marker)


find_marker_in_datastream(data, 4)
find_marker_in_datastream(data, 14)
