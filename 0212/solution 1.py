with open('input.txt', 'r') as f:
    data = f.read()

ranges = [
    range(int(_.split('-')[0]), int(_.split('-')[1]) + 1)
    for _ in data.split(',')
]

addition = 0

for rng in ranges:
    for num in rng:
        s_num = str(num)
        if len(s_num) % 2 == 0:
            if s_num[:(int(len(s_num)/2))] == s_num[int(len(s_num)/2):]:
                print(f'Found number {s_num}')
                addition += num

print(f'Final addition {addition}')
