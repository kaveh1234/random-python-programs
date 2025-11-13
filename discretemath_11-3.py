
count = 0
for i in range(1, 1001):
    c = round(i**(1/3))
    s = int(i**(1/2))

    is_square = (s*s == i)
    is_cube = (c*c*c == i)

    if not is_square and not is_cube:
        count += 1

print(count)
