import scipy.linalg
import numpy


def thomas(a, b, c, d) :
    matrixSize = len(d)
    X = numpy.zeros(matrixSize, float)
    beta = numpy.zeros(matrixSize - 1, float)
    gamma = numpy.zeros(matrixSize, float)

    beta[0] = c[0] / b[0]
    gamma[0] = d[0] / b[0]

    for each in range(1, matrixSize - 1) :
        beta[each] = c[each] / (b[each] - a[each - 1] * beta[each - 1])
    for each in range(1, matrixSize) :
        gamma[each] = (d[each] - a[each] * gamma[each - 1]) / (b[each] - a[each] * beta[each - 1])
    X[matrixSize - 1] = gamma[matrixSize - 1]
    for each in range(matrixSize - 1, 0, -1) :
        X[each - 1] = gamma[each - 1] - beta[each - 1] * X[each]
    return X


numpy.set_printoptions(precision=4)

A = ([4, 1, 0, 0, 0, 0, 0],
     [1, 4, 1, 0, 0, 0, 0],
     [0, 1, 4, 1, 0, 0, 0],
     [0, 0, 1, 4, 1, 0, 0],
     [0, 0, 0, 1, 4, 1, 0],
     [0, 0, 0, 0, 1, 4, 1],
     [0, 0, 0, 0, 0, 1, 4])

Ap = [0, 1, 1, 1, 1, 1, 1]
Bp = [4, 4, 4, 4, 4, 4, 4]
Cp = [1, 1, 1, 1, 1, 1, 0]
D = [1, 2, 3, 4, 5, 6, 7]

X = thomas(Ap, Bp, Cp, D)
print(f'Wynik działania algorytmu: {X}')
print(f'Wynik kontrolny:           {numpy.linalg.solve(A, D)}')
