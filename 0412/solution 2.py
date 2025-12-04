import copy

with open('input.txt', 'r') as f:
    initial_diagram = [[item for item in line.replace('\n', '')] for line in f.readlines()]

max_line = len(initial_diagram) - 1
max_column = len(initial_diagram[0]) - 1
accessible_diagram = copy.deepcopy(initial_diagram)

def is_roll(x: str):
    return 1 if x == '@' else 0

def remove_rolls(diagram):
    removed_rolls = 0
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
                removed_rolls += 1
                accessible_diagram[line][column] = 'x'

    return removed_rolls, accessible_diagram

total_removed_rolls = 0
print('Initial state:')
for line in initial_diagram:
    print(''.join(line))

removed, new_diagram = remove_rolls(initial_diagram)
total_removed_rolls += removed
print(f'Removed {removed} rolls of paper:')
for line in new_diagram:
    print(''.join(line))

while removed != 0:
    removed, new_diagram = remove_rolls(new_diagram)
    total_removed_rolls += removed
    print(f'Removed {removed} rolls of paper:')
    for line in new_diagram:
        print(''.join(line))

print(f'Total removed rolls: {total_removed_rolls}')
