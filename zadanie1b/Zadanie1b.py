import pprint

import numpy
import math
import scipy.linalg


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
        gamma[each] = (d[each] - a[each - 1] * gamma[each - 1]) / (b[each] - a[each - 1] * beta[each - 1])
    X[matrixSize - 1] = gamma[matrixSize - 1]
    for each in range(matrixSize - 1, 0, -1) :
        X[each - 1] = gamma[each - 1] - beta[each - 1] * X[each]
    return X


matrixSize = 7
numpy.set_printoptions(precision=4)
A = ([4, 1, 0, 0, 0, 0, 1],
     [1, 4, 1, 0, 0, 0, 0],
     [0, 1, 4, 1, 0, 0, 0],
     [0, 0, 1, 4, 1, 0, 0],
     [0, 0, 0, 1, 4, 1, 0],
     [0, 0, 0, 0, 1, 4, 1],
     [1, 0, 0, 0, 0, 1, 4])
B = ([1, 2, 3, 4, 5, 6, 7])

# z algorytmu Shermana-Morrisona wiemy, ze macierz zadana jest przeksztalceniem macierzy nazwanej prevA o wektor uv^t
# gdzie u = v ^ t = [1, 0, 0, 0, 0, 0, 0, 1]

u = numpy.array([1, 0, 0, 0, 0, 0, 1], float)
v = numpy.atleast_2d(u)
v = numpy.transpose(u)
# print(v)
prevA = numpy.array([[3, 1, 0, 0, 0, 0, 0],
                     [1, 3, 1, 0, 0, 0, 0],
                     [0, 1, 3, 1, 0, 0, 0],
                     [0, 0, 1, 3, 1, 0, 0],
                     [0, 0, 0, 1, 3, 1, 0],
                     [0, 0, 0, 0, 1, 3, 1],
                     [0, 0, 0, 0, 0, 1, 3]], float)

# po znalezieniu tego rozkładu wystarczy obliczyć trzy kroki:

# używam algorytmu Thomasa do podpunktu pierwszego i drugiego
Ap = numpy.array([0, 1, 1, 1, 1, 1, 1], float)
Bp = numpy.array([3, 3, 3, 3, 3, 3, 3], float)
Cp = numpy.array([1, 1, 1, 1, 1, 1, 0], float)
D = numpy.array([1, 2, 3, 4, 5, 6, 7], float)
# 1) A * z = b
z = thomas(Ap, Bp, Cp, D)

# 2) A * q = u
q = thomas(Ap, Bp, Cp, u)

# 3) w = z - (v^t)*z/(1+v^t*q)*q
# krok trzeci jest już prostym równaniem do obliczenia

v_times_z = numpy.multiply(v, z)
v_times_q = numpy.multiply(v, q)
vq_plus_1 = v_times_q + 1
vz_times_q = numpy.multiply(v_times_z, q)
vz_dividedby_1vtq_times_q = numpy.divide(vz_times_q, vq_plus_1)

w = numpy.subtract(z, vz_dividedby_1vtq_times_q)

print(f'rezultat:  {w}')
print(f'kontrolny: {numpy.linalg.solve(prevA,D)}')

