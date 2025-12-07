fresh_ranges = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        if '-' in line:
            low, high = line.split('-')
            fresh_ranges.append(range(int(low), int(high) + 1))
        else:
            break

print(f'Original: {len(fresh_ranges)} ranges')
merged_ranges = []
processed_ranges = set()
fresh_ranges = sorted(fresh_ranges, key=lambda r: r[0])

def can_be_merged(r1, r2):
    if r2[0] in r1:
        if r2[-1] in r1:
            return True, r1
        else:
            return True, range(r1[0], r2[-1] + 1)
    else:
        return False, r1

for index, r1 in enumerate(fresh_ranges):
    if r1 not in processed_ranges:
        merged = r1
        if index + 1 < len(fresh_ranges):
            for r2 in fresh_ranges[index + 1:]:
                can_be, merged = can_be_merged(merged, r2)
                if not can_be:
                    # means r1 can't be merged, we save it and pass to the next one
                    merged_ranges.append(merged)
                    processed_ranges.add(r1)
                    break
                else:
                    # r1 was merged with r2, we use the merged range and test the next one
                    processed_ranges.update({r1, r2})  # make sure they don't get tested anymore by the first loop
            if can_be:
                merged_ranges.append(merged)
        else:
            merged_ranges.append(r1)


print(f'Merged ranges: {len(merged_ranges)} ranges')

fresh_ingredients = sum([len(r) for r in merged_ranges])

print(f'Fresh ingredients: {fresh_ingredients}')
# 350939902751909
