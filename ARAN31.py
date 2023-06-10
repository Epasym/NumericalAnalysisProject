import numpy as np


def forw_subst(L, b):
    n = len(L)
    d = [0.0 for i in range(n)]
    for i in range(n):
        lproduct = 0
        for j in range(i):
            if i != j:
                lproduct += L[i][j] * d[j]
        d[i] = b[i] - lproduct

    return d


def back_subst(U, d):
    n = len(U)
    x = [0.0 for i in range(n)]
    for i in range(n-1, -1, -1):
        uproduct = 0
        for j in range(i):
            if i != j:
                uproduct += U[i][j] * x[j]
        x[i] = d[i] - uproduct

    return x


def lu_decomp(A):
    U = A
    n = len(U)
    factor = [[0.0] * n for j in range(n)]

    for k in range(n):
        for i in range(k+1, n):
            factor[k][i] = U[i][k] / U[k][k]
            for j in range(k, n):
                U[i][j] = U[i][j] - factor[k][i] * U[k][j]

    L = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            L[i][j] = factor[j][i]
            if i == j:
                L[i][i] = 1

    return U, L


def solve(A, b):

    U, L = lu_decomp(A)
    print("U:", U)
    print("L:", L)

    print("Solving Ld=b for d:")
    d = forw_subst(L, b)
    print("d:", d)

    print("Solving Ux=d for x:")
    x = back_subst(U,d)
    print("x:", x)

    return x


print("\nExample:\n")
A = [[1.0, 1.0, -1.0], [6.0, 2.0, 2.0], [-3.0, 4.0, 1.0]]
b = [3.0, 2.0, 1.0]
print("Solve Ax=b...")
print("A:", A)
print("b:", b)
print("\nSolution:\n")
solve(A, b)
