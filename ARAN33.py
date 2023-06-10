import numpy as np


def gauss_seidel(A, b, tolerance):
    n = len(A)
    x = [0.0 for i in range(n)]
    x[0] = b[0] / A[0][0]
    counter =0
    condition = True
    e = (1 / 2) * (1 / pow(10, tolerance))
    while condition:
        maxold = max(x)
        for i in range(n):
            suma = 0
            if i == 0:
                suma = suma + x[i + 1] * A[i][i + 1]
            elif i == n - 1:
                suma = suma + x[i - 1] * A[i][i - 1]
            else:
                suma = suma + x[i - 1] * A[i][i - 1] + x[i - 1] * A[i][i - 1]
            x[i] = (b[i] - suma) / A[i][i]

        ei = abs(max(x) - maxold)
        print("Error:",ei)
        condition = ei > e
        counter+=1

    print("After", counter, "iterations")

    for k in range(n):
        x[k] = round(x[k], tolerance)
    print("Error sufficiently small.")
    return x


def main():
    n=10

    A = [[0.0] * n for i in range(n)]

    for i in range(n):
        A[i][i] = 5
        A[i][i - 1] = -2
        if i < n - 1:
            A[i][i + 1] = -2
    A[0][n - 1] = 0
    print(A)

    b = [0.0 for i in range(n)]
    for i in range(n):
        if i == 0 or i == n - 1:
            b[i] = 3
        else:
            b[i] = 1
    print(b)

    x = gauss_seidel(A, b, 4)
    print("x:",x)

    input("Give any input to continue to n=10000")
    print("Calculating...")
    SystemExit()
    n = 10000
    A = [[0.0] * n for i in range(n)]

    for i in range(n):
        A[i][i] = 5
        A[i][i - 1] = -2
        if i < n - 1:
            A[i][i + 1] = -2
    A[0][n - 1] = 0

    b = [0.0 for i in range(n)]
    for i in range(n):
        if i == 0 or i == n - 1:
            b[i] = 3
        else:
            b[i] = 1

    x = gauss_seidel(A, b, 4)
    print("x:",x)


main()
