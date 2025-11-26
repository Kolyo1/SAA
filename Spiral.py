import numpy as np
matrix_data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix = np.array(matrix_data) if np is not None else matrix_data


def spiral_order(mat):
    if np is not None and isinstance(mat, np.ndarray):
        mat = mat.tolist()

    if not mat or not mat[0]:
        return []

    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    res = []

    while left <= right and top <= bottom:
        
        for j in range(left, right + 1):
            res.append(mat[top][j])
        top += 1

        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(mat[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1

    return res



for row in matrix_data:
    print(row)

spiral = spiral_order(matrix)
print('\nSpiral order:')
print(','.join(str(x) for x in spiral))

minus = []
even = []
for x in spiral:
    if x < 0:
        minus.append(x)
    elif x % 2 == 0:
        even.append(x)

print(minus)
print(even)