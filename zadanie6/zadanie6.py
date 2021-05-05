import numpy


def givens_tridiagonal_rotation(A, el_col, el_row) :
    xi = A[el_col][el_col]
    xj = A[el_col][el_row]
    # print(f'xi: {xi} oraz xj: {xj}')
    c = xi / (xi ** 2 + xj ** 2) ** 0.5
    s = xj / (xi ** 2 + xj ** 2) ** 0.5

    g = numpy.identity(matrixSize, float)

    g[el_col][el_row] = s
    g[el_row][el_col] = -s
    g[el_col][el_col] = g[el_row][el_row] = c
    # print(f'macierz G: \n{g}')
    return g @ A


numpy.printoptions(precision=4)
A = numpy.array([[2, -1, 0, 0, 1],
                 [-1, 2, 1, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 1, 2, -1],
                 [1, 0, 0, -1, 2]])
matrixSize = len(A)
eigenvalue = 0.38197
B = numpy.zeros(matrixSize, float)
I = numpy.identity(matrixSize)
eigenvalue_times_identity = eigenvalue * I
A = A - eigenvalue_times_identity
# wystarczy sfaktoryzować macierz i rozwiązać równanie liniowe (A - I * labda)x = 0, gdzie x to rozwiązanie
# usunięcie elementu A[0][5]
A = givens_tridiagonal_rotation(A, 0, matrixSize - 1)
for column in range(0, matrixSize -1):
    A = givens_tridiagonal_rotation(A, column, column + 1)
print(f'Macierz A po rotacji Givensa: \n{A}')
print(f'Kontrolne rozwiązanie \n{numpy.linalg.solve(A,B)}')
