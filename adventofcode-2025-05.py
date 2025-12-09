# im proud of dis one
with open('inputAOC5.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

blank_index = lines.index('')

range_lines = lines[:blank_index]

# parse ranges
parsed_ranges = []
for r in range_lines:
    start, end = r.split('-')
    parsed_ranges.append((int(start), int(end)))

# sort ranges by start
parsed_ranges.sort()

# merge ranges
merged = []
cur_start, cur_end = parsed_ranges[0]

for start, end in parsed_ranges[1:]:
    if start <= cur_end + 1:
        # overlap -> extend the current range
        cur_end = max(cur_end, end)
    else:
        # no overlap -> close current and start new
        merged.append((cur_start, cur_end))
        cur_start, cur_end = start, end

# append last range
merged.append((cur_start, cur_end))

# count total fresh IDs
total = sum(end - start + 1 for start, end in merged)
print(total)
