with open('input.txt', 'r') as f:
    lines = f.readlines()

v = 50
pwd = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])

    while distance >= 100:
        distance -= 100

    if direction == 'R':
        v += distance
    else:  # 'l'
        v -= distance

    if v > 99:
        v = v - 100
    if v < 0:
        v = 100 + v

    if v == 0:
        pwd += 1

print(pwd)  # 1102
