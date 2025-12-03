with open('input.txt', 'r') as f:
    data = f.readlines()

pwd = 0

for line in data:
    line = line.replace('\n', '')
    digit_line = [int(_) for _ in line]
    first_digit = max(digit_line[:-11])  # need at least 11 digits after the first one
    digit_position = digit_line[:-11].index(first_digit)
    used_positions = range(digit_position + 1)
    max_joltage = str(first_digit)
    for i in range(11):  # find the next 11 digits
        next_digit = max(digit_line[digit_position + 1:-10 + i] if i < 10 else digit_line[digit_position + 1:])
        digit_position = [digit_index for digit_index, v in enumerate(digit_line) if v == next_digit and digit_index not in used_positions][0]
        used_positions = range(digit_position + 1)
        max_joltage += str(next_digit)

    print(f'max jolts {max_joltage} for line {line}')
    pwd += int(max_joltage)

print(f'PWD {pwd}')
# 168575096286051
