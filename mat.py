import math

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

n = len(matrix)
m = len(matrix[0]) if matrix else 0
L = min(n, m)
secondary = [matrix[i][m - 1 - i] for i in range(L)]


k = 4

vals = [x for x in secondary if x % k == 0]

if not vals:
    print(0)
else:
    g = abs(vals[0])
    for x in vals[1:]:
        g = math.gcd(g, abs(x))
    print(g)