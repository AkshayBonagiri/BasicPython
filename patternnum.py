rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print(rows - i + 1, end='')
    print()  # Move to the next line after printing all characters for the current row
