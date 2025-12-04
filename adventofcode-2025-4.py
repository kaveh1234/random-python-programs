with open('inputAOC4.txt', 'r', encoding='utf8') as f:
    lines = f.read().splitlines()
    
grid = []

for line in lines:
    grid.append(list(line))

total_removed = 0

while True:
    to_remove = []

    # 1. scan grid to find accessible @
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                voisin_count = 0
                for test_row in range(row-1, row+2):
                    for test_col in range(col-1, col+2):
                        if 0 <= test_row < len(grid) and 0 <= test_col < len(grid[row]):
                            if grid[test_row][test_col] == '@':
                                if test_row == row and test_col == col:
                                    continue
                                voisin_count += 1
                if voisin_count < 4:
                    to_remove.append((row, col))
                
                            

    # 2. stop if nothing else can be removed
    if not to_remove:
        break

    # 3. remove all of them at once
    for (r, c) in to_remove:
        grid[r][c] = '.'

    # 4. track how many we removed this round
    total_removed += len(to_remove)

# print total_removed
print(total_removed)
