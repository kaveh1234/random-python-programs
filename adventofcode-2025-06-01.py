from functools import reduce
import operator as opmod

with open("inputAOC6.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

number_rows = lines[:-1]
ops_row = lines[-1]

H = len(number_rows)
W = len(ops_row)

# (optional safety) pad rows if any are shorter
number_rows = [row.ljust(W) for row in number_rows]
ops_row = ops_row.ljust(W)

total = 0
cols = []  # columns collected for the current problem


def solve_problem(columns):
    if not columns:
        return 0

    # operator: last non-space char in bottom row across this problem
    oper = None
    for col in reversed(columns):
        if col[-1] != " ":
            oper = col[-1]
            break
    if oper not in {"+", "*"}:
        raise ValueError(f"Bad/missing operator: {oper!r}")

    # build numbers per row by reading across columns and removing spaces
    nums = []
    for r in range(H):
        s = "".join(col[r] for col in columns).replace(" ", "")
        if s:
            nums.append(int(s))

    if oper == "+":
        return sum(nums)
    else:
        return reduce(opmod.mul, nums, 1)


for c in range(W):
    blank_col = (ops_row[c] == " ") and all(row[c] == " " for row in number_rows)

    if blank_col:
        total += solve_problem(cols)
        cols = []
    else:
        # column = all number-row chars + op char at bottom
        cols.append([row[c] for row in number_rows] + [ops_row[c]])

# last problem
total += solve_problem(cols)

print(total)
