with open("inputAOC6.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

lines_new = [line.strip().split() for line in lines]
cols = list(zip(*lines_new))

total = 0

for *nums, op in cols:
    total += eval(op.join(nums))

print(total)

