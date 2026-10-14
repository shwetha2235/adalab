
from typing import List

def strassen_multiply(
    A: List[List[int]],
    B: List[List[int]]
) -> List[List[int]]:

    if not A or not B:
        raise ValueError("Matrices cannot be empty")

    if any(len(row) != len(A[0]) for row in A):
        raise ValueError("Invalid matrix A")

    if any(len(row) != len(B[0]) for row in B):
        raise ValueError("Invalid matrix B")

    if len(A[0]) != len(B):
        raise ValueError("Matrix multiplication not possible")

    rows = len(A)
    cols = len(B[0])
    inner = len(B)

    size = max(rows, cols, inner)
    n = 1
    while n < size:
        n *= 2

    X = [[0] * n for _ in range(n)]
    Y = [[0] * n for _ in range(n)]

    for i in range(rows):
        for j in range(inner):
            X[i][j] = A[i][j]

    for i in range(inner):
        for j in range(cols):
            Y[i][j] = B[i][j]

    def multiply(X, Y):
        n = len(X)

        if n == 1:
            return [[X[0][0] * Y[0][0]]]

        mid = n // 2

        A11 = [row[:mid] for row in X[:mid]]
        A12 = [row[mid:] for row in X[:mid]]
        A21 = [row[:mid] for row in X[mid:]]
        A22 = [row[mid:] for row in X[mid:]]

        B11 = [row[:mid] for row in Y[:mid]]
        B12 = [row[mid:] for row in Y[:mid]]
        B21 = [row[:mid] for row in Y[mid:]]
        B22 = [row[mid:] for row in Y[mid:]]

        def add(P, Q):
            return [[P[i][j] + Q[i][j]
                     for j in range(mid)] for i in range(mid)]

        def sub(P, Q):
            return [[P[i][j] - Q[i][j]
                     for j in range(mid)] for i in range(mid)]

        M1 = multiply(add(A11, A22), add(B11, B22))
        M2 = multiply(add(A21, A22), B11)
        M3 = multiply(A11, sub(B12, B22))
        M4 = multiply(A22, sub(B21, B11))
        M5 = multiply(add(A11, A12), B22)
        M6 = multiply(sub(A21, A11), add(B11, B12))
        M7 = multiply(sub(A12, A22), add(B21, B22))

        C11 = add(sub(add(M1, M4), M5), M7)
        C12 = add(M3, M5)
        C21 = add(M2, M4)
        C22 = add(add(sub(M1, M2), M3), M6)

        result = [[0] * n for _ in range(n)]

        for i in range(mid):
            for j in range(mid):
                result[i][j] = C11[i][j]
                result[i][j + mid] = C12[i][j]
                result[i + mid][j] = C21[i][j]
                result[i + mid][j + mid] = C22[i][j]

        return result

    product = multiply(X, Y)

    return [row[:cols] for row in product[:rows]]


# Main program
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Product Matrix:")
for row in strassen_multiply(A, B):
    print(row)
