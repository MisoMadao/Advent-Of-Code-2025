import re

with open('input.txt', 'r') as f:
    data = f.readlines()


data = [re.sub(pattern=r'\s+', repl=' ', string=_.strip()).split(' ') for _ in data]

new_data = []
for x, line in enumerate(data):
    for y, val in enumerate(line):
        if y not in range(len(new_data)):
            new_data.insert(y, [])
        new_data[y].insert(x, val)

grand_total = 0
for operation_list in new_data:
    operation = operation_list[-1].join(operation_list[:-1])
    grand_total += eval(operation)

print(grand_total)
