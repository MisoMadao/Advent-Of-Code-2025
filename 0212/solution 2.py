with open('input.txt', 'r') as f:
    data = f.read()

ranges = [
    range(int(_.split('-')[0]), int(_.split('-')[1]) + 1)
    for _ in data.split(',')
]


def basic_solution():
    addition = 0

    def check_repeated(string: str, letters: int):
        # If we are at half of the string -> no repetition
        if letters > int(len(string) / 2):
            return False

        # If length of the string is not a multiple of the length of the substring to check -> no repetition
        if len(string) % letters == 0:
            # Check if substring is repeated
            lower_index = 0
            higher_index = letters
            repeated = False
            while higher_index < len(string):
                if string[lower_index:higher_index] == string[higher_index:higher_index+letters]:
                    lower_index = higher_index
                    higher_index += letters
                    repeated = True
                else:
                    # Substring is not repeated
                    repeated = False
                    break

            if repeated:
                return repeated

        return check_repeated(string, letters + 1)

    for rng in ranges:
        for num in rng:
            s_num = str(num)
            repeated_string = check_repeated(s_num, 1)
            if repeated_string:
                print(f'Found number {s_num}')
                addition += num

    return addition


addition = basic_solution()
# 50857215650
print(f'Final addition {addition}')
