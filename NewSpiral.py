import numpy as np
matrix_data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix = np.array(matrix_data) if np is not None else matrix_data

def spiral_outward(mat):
    if np is not None and isinstance(mat, np.ndarray):
        mat = mat.tolist()

    if not mat or not mat[0]:
        return []

    n, m = len(mat), len(mat[0])

    for i in range(n):
        for j in range(m):
            v = mat[i][j]
            if v % 15 == 0:
                mat[i][j] = i + j
            elif v % 3 == 0:
                mat[i][j] = 0
            elif v % 5 == 0:
                mat[i][j] = 1

    r = (n - 1) // 2
    c = (m - 1) // 2

    res = [mat[r][c]]
    if n * m == 1:
        return res

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    step = 1
    dir_idx = 0

    while len(res) < n * m:
        for _ in range(2):
            dr, dc = dirs[dir_idx % 4]
            for _ in range(step):
                r += dr
                c += dc
                if 0 <= r < n and 0 <= c < m:
                    res.append(mat[r][c])
                    if len(res) == n * m:
                        return res
            dir_idx += 1
        step += 1

    return res



for row in matrix_data:
    print(row)


print(','.join(str(x) for x in spiral_outward(matrix)))