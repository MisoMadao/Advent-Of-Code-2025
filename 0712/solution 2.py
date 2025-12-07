from colorama import Fore, Style

with open('input.txt', 'r') as f:
    lines = [_.replace('\n', '') for _ in f.readlines()]
lines = [[_ for _ in line] for line in lines]
lines[1][lines[0].index('S')] = '|'

counters = [0 for _ in range(len(lines[0]))]

beams = {lines[1].index('|')}

for line in lines[1:]:
    new_beams = beams
    splitters = set([_ for _, v in enumerate(line) if v == '^'])
    for splitter in splitters:
        if splitter in beams:
            to_sum = counters[splitter] if counters[splitter] else 1
            counters[splitter + 1] += to_sum
            counters[splitter - 1] += to_sum
            new_beams.update({splitter + 1, splitter - 1})
            new_beams.discard(splitter)
            counters[splitter] = 0
    beams = new_beams
    for _ in range(len(line)):
        if _ in splitters:
            print(Fore.BLUE + '^' + Style.RESET_ALL, end='   ')
        elif _ in beams:
            print(counters[_], end='   ')
        else:
            print('.', end='   ')
    print('\n')

timelines = sum(counters)
print(timelines)

# 12472142047197
