fresh_ranges = []
available_ingredients = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        if '-' in line:
            low, high = line.split('-')
            fresh_ranges.append(range(int(low), int(high) + 1))
        else:
            if line:
                available_ingredients.append(int(line))

fresh_ingredients = 0
for ingredient in available_ingredients:
    if any([ingredient in r for r in fresh_ranges]):
        fresh_ingredients += 1

print(f'Fresh ingredients: {fresh_ingredients}')
# 511
