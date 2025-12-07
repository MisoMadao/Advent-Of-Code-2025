with open('input.txt', 'r') as f:
    lines = [_.replace('\n', '') for _ in f.readlines()]
lines = [[_ for _ in line] for line in lines]
lines[1][lines[0].index('S')] = '|'


def solution_lists():

    total_split = 0
    for index_line, line in enumerate(lines):
        if index_line == 0:
            continue
        if index_line == len(lines) - 1:
            break
        line_split = 0
        for index_sym, symbol in enumerate(line):
            if symbol == '|':
                if lines[index_line + 1][index_sym] == '^':
                    total_split += 1
                    line_split += 1
                    lines[index_line + 1][index_sym - 1] = '|'
                    lines[index_line + 1][index_sym + 1] = '|'
                if lines[index_line + 1][index_sym] == '.':
                    lines[index_line + 1][index_sym] = '|'

    print(total_split)


def solution_indexes():

    beams = {lines[1].index('|')}
    n_split = 0

    for line in lines[2:]:
        new_beams = beams
        splitters = set([_ for _, v in enumerate(line) if v == '^'])
        for splitter in splitters:
            if splitter in beams:
                n_split += 1
                new_beams.update({splitter + 1, splitter - 1})
                new_beams.discard(splitter)
        beams = new_beams

    print(n_split)


solution_indexes()
solution_lists()
# 1609
