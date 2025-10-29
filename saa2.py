# 1

def Sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sum = 0

    for j in range(cols):
        sum += matrix[0][j]
    for j in range(cols):
        sum += matrix[rows - 1][j]
    for i in range(1, rows - 1):
        sum += matrix[i][0] + matrix[i][cols - 1]   
    return sum

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(Sum(matrix))  # Output: 68

# 2

def Proccess (N):
    n = len(N)
    B = []

    dsum = sum(N[i][i] for i in range(n))
    B.append(dsum)

    for i in range(n):
        rsum = sum(N[i])
        B.append(rsum)

    count = 0
    for i in range(n):
        for j in range(n):
            if N[i][j] < i + j:
                count += 1
    B.append(count)
    return B

N = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Proccess(N))  # Output: [15, 6, 15, 24, 3]

# 3 

def Sum2(A):
    n = len(A)
    sum = sum(A[i][n - i - 1] for i in range(n))
    return sum

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Sum2(A))  # Output: 15

# 4

def simetric(M):
    n = len(M)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] < M[j][i]:
                pairs.append(((i, j, M[i][j]), (j, i, M[j][i])))
    return pairs

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(simetric(M))  # Output:   [((0, 1, 2), 
                                # (1, 0, 4)), 
                                # ((0, 2, 3), 
                                # (2, 0, 7)), 
                                # ((1, 2, 6), 
                                # (2, 1, 8))]