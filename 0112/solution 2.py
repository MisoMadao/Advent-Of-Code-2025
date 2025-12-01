

def solution_math():
    """ wrong solution :/ """
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    v = 50
    pwd = 0

    for line in lines:
        # 3979 too low
        # 6195 too high
        direction = line[0]
        distance = int(line[1:])

        if direction == 'R':
            v += distance
            zero_clicks = int(v / 100)
            pwd += zero_clicks
            v = v % 100
        else:  # 'L'
            v -= distance
            zero_clicks = int(v / 100)
            pwd += zero_clicks
            if v != (v % 100):
                v = v % 100
                pwd += 1

    print(pwd)


def stupid_solution():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    v = 50
    pwd = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == 'R':
            for click in range(distance):
                v += 1
                if v == 100:
                    v = 0
                if v == 0:
                    pwd += 1
        else:  # 'L'
            for click in range(distance):
                v -= 1
                if v == -1:
                    v = 99
                if v == 0:
                    pwd += 1

    print(pwd)

stupid_solution()  # 6175

# solution_math()
