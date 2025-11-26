matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for row in matrix:
    print(row)

for row in matrix:
    avg = sum(row) / len(row)
    for j in range(len(row)):
        if row[j] > avg:
            row[j] = 0

for row in matrix:
    print(row)