with open('inputAOC3.txt', 'r', encoding='utf8') as f:
    lines = f.read().splitlines()

max_list = []    

for line in lines:
    keep = 12
    to_remove = len(line) - keep
    
    digits = list(line)
    
    removed = 0
    while removed < to_remove:
        found = False
        for i in range(len(digits) - 1):
            if digits[i] < digits[i+1]:
                digits.pop(i)
                removed += 1
                found = True
                break
        if not found:
            digits.pop()
            removed += 1
    max_val = int(''.join(digits))
    max_list.append(max_val)


print(sum(max_list))
