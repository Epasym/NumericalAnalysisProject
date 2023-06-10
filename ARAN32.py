from math import sqrt


def is_square(A):
    for row in A:
        if not len(row) == len(A):
            return False
    return True


def cholesky_decomposition(A):
    # A must be nxn, positive, and symmetrical
    n = len(A)
    if not is_square(A):
        return "A is not square"
    else:
        for i in range(n):
            for j in range(i, n):
                if A[i][j] != A[j][i]:
                    return "A is not symmetrical"

    L = [[0.0] * n for i in range(n)]

    L[0][0] = round(sqrt(A[0][0]), 5)

    try:
        for k in range(1, n):
            for i in range(k + 1):
                s = 0
                if k != i:
                    for j in range(i):
                        s += L[i][j] * L[k][j]
                    L[k][i] = round((A[k][i] - s) / L[i][i], 5)
                else:
                    for j in range(k):
                        s += L[k][j] ** 2
                    L[k][k] = round(sqrt(A[k][k] - s), 5)
    except Exception as e:
        print(type(e))
        return "Something went wrong"

    return L


print("\nExample:")
A = [[6, 15, 55], [15, 55, 225], [55, 225, 979]]
print("\nMatrix A:")
print(A)
print("-------------------------")
print("Cholesky decomposition:")
print(cholesky_decomposition(A))
