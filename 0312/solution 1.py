with open('input.txt', 'r') as f:
    data = f.readlines()

pwd = 0

for line in data:
    line = line.replace('\n', '')
    digit_line = [int(_) for _ in line]
    first_digit = max(digit_line[:-1])  # avoid searching in last position
    digit_index = digit_line.index(first_digit)
    second_digit = max(digit_line[digit_index+1:])
    max_joltage = int(f'{first_digit}{second_digit}')
    print(f'max jolts {max_joltage} for line {line}')
    pwd += max_joltage

print(f'PWD {pwd}')
# 17031
