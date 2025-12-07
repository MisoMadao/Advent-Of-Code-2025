import re

data = []
max_length = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = [_ for _ in line.replace('\n', '')]
        if len(line) > max_length:
            max_length = len(line)
        data.append(line)

data = [line + ['' for _ in range(max_length - len(line))] for line in data]
operations = [_ for _ in data[-1] if _ not in ['', ' ']]
data = data[:-1]

max_lines = len(data)
numbers = []
num = ''
grand_total = 0
for x in range(max_length - 1, -1, -1):
    for y in range(max_lines):
        num += data[y][x]
    num = num.strip()
    if num:
        numbers.append(num)
        num = ''
    else:
        operation = operations.pop()
        operation = operation.join(numbers)
        grand_total += eval(operation)
        numbers = []
        num = ''

operation = operations.pop()
operation = operation.join(numbers)
grand_total += eval(operation)

print(grand_total)
