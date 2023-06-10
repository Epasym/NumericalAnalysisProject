import random
import math
from copy import deepcopy


def generate_G(A, q):
    n = len(A)
    G = [[[0.0] for j in range(n)] for i in range(n)]

    for j in range(n):
        nj = 0
        for i in range(n):
            nj = nj + A[j][i]
        for i in range(n):
            G[i][j] = (q / n) + ((A[j][i] * (1 - q)) / nj)

    return G


def mult(A, b):
    n = len(A)
    n0 = len(A[0])
    m = len(b)
    Ab = [0 for i in range(n)]

    if n0 != m:
        print("Incorrect dimensions!")
        exit(1)

    for i in range(n):
        for j in range(n0):
            Ab[i] = Ab[i] + A[i][j] * b[j]

    return Ab


def mult_matrix(A, B):
    n = len(A)
    n0 = len(A[0])
    m = len(B)
    m0 = len(B[0])
    AB = [[[0.0] for j in range(m0)] for i in range(n)]

    if n0 != m:
        print("Incorrect dimensions!")
        exit(1)

    for k in range(n):
        for i in range(m0):
            for j in range(m):
                AB[i][k] = AB[i][k] + A[i][j] * B[j][k]

    return AB


def power_method(A):
    n = len(A)
    L = []
    x0 = [[0.0] for i in range(n)]
    xp = [[0.0] for i in range(n)]
    ei = [[0.0] for i in range(n)]
    k = 0

    while True:

        if k == 0:
            jr = random.randint(0, n - 1)
            for i in range(n):
                x0[i] = A[i][jr]
            xp = mult(A, x0)
        else:
            xp = mult(A, x0)

        for i in range(n):
            if xp[i] != 0:
                d = xp[i]
                break

        for i in range(n):
            ei[i] = xp[i] / d

        L.append(d)
        x0 = deepcopy(ei)

        if k != 0 and abs(L[k] - L[k - 1]) < math.pow(10, -6) / 2:
            return ei

        k = k + 1


def normalize(b):
    n = len(b)
    suma = 0

    for i in range(n):
        suma = suma + b[i]

    for i in range(n):
        b[i] = b[i] / suma

    return b


def main():
    A = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

    print("A1:\n")
    q = 0.15
    G = generate_G(A, q)

    ei = power_method(G)

    p = normalize(ei)
    print("p:", p)

    print("\nA2:")
    print("Changes: A[3,3], A[3,4], A[3,5] = 1, A[1,9] = 0\n")
    A[2][2] = 1
    A[2][3] = 1
    A[2][4] = 1
    A[0][8] = 0
    G = generate_G(A, q)

    ei = power_method(G)

    p = normalize(ei)
    oldp = p
    print("p:", p)

    # -------------------------------------------------

    print("\n q = 0.02\n")
    q = 0.02
    G = generate_G(A, q)

    ei = power_method(G)

    p = normalize(ei)
    print("p:", p)

    print("\n q = 0.6\n")
    q = 0.6
    G = generate_G(A, q)

    ei = power_method(G)

    p = normalize(ei)
    print("p:", p)

    # -------------------------------------------------

    print("\nA3:")
    print("Changes: A[8,11], A[12,11] = 3\n")
    q = 0.15
    A[7][10] = 3
    A[11][10] = 3
    G = generate_G(A, q)

    ei = power_method(G)

    p = normalize(ei)
    print("p:", p)
    print("Old p of page 10 and 11:", oldp[9], oldp[10])
    print("New p of page 10 and 11:", p[9], p[10])

    # -------------------------------------------------

    print("\nA4:")
    for i in range(len(A)):
        del(A[i][9])
    del (A[9])

    print("Changes: page 10 has been deleted\n")

    G = generate_G(A, q)

    ei = power_method(G)

    p = normalize(ei)
    print("p:", p)

    return 0


main()
