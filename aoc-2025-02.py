def is_invalid_id(n):
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths (must divide evenly into total length)
    for pattern_len in range(1, length):
        if length % pattern_len == 0:
            repeats = length // pattern_len
            if repeats >= 2:
                pattern = s[:pattern_len]
                if pattern * repeats == s:
                    return True
    return False

with open('inputAOC2.txt', 'r', encoding='utf8') as f:
    data = f.read().strip()

ranges = data.split(',')
total = 0

for r in ranges:
    start, end = map(int, r.split('-'))
    for id_num in range(start, end + 1):
        if is_invalid_id(id_num):
            total += id_num

print(total)
