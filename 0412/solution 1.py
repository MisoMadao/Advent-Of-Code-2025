import copy

with open('input.txt', 'r') as f:
    diagram = [[item for item in line.replace('\n', '')] for line in f.readlines()]

max_line = len(diagram) - 1
max_column = len(diagram[0]) - 1
accessible_tolls = 0
accessible_diagram = copy.deepcopy(diagram)

def is_roll(x: str):
    return 1 if x == '@' else 0

for line, v1 in enumerate(diagram):
    for column, v2 in enumerate(diagram[line]):
        if not is_roll(diagram[line][column]):
            continue
        adjacent_rolls = 0

        # left
        if column > 0:
            adjacent_rolls += is_roll(diagram[line][column - 1])
            # left up
            if line > 0:
                adjacent_rolls += is_roll(diagram[line - 1][column - 1])
            # left down
            if line < max_line:
                adjacent_rolls += is_roll(diagram[line + 1][column - 1])
        # up
        if line > 0:
            adjacent_rolls += is_roll(diagram[line - 1][column])
        # down
        if line < max_line:
            adjacent_rolls += is_roll(diagram[line + 1][column])
        # right
        if column < max_column:
            adjacent_rolls += is_roll(diagram[line][column + 1])
            # right up
            if line > 0:
                adjacent_rolls += is_roll(diagram[line - 1][column + 1])
            # right down
            if line < max_line:
                adjacent_rolls += is_roll(diagram[line + 1][column + 1])

        if adjacent_rolls < 4:
            accessible_tolls += 1
            accessible_diagram[line][column] = 'x'

print('Final Diagram')
for line in accessible_diagram:
    print(''.join(line))

print(f'Accessible rolls {accessible_tolls}')
# 1602
