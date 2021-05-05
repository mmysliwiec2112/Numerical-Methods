import numpy
import math


def givens_tridiagonal_rotation(A, result, el_col, el_row) :
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
    return g @ A, g @ result


numpy.set_printoptions(precision=4)
# reprezentacja zadanej macierzy
A = numpy.array([[19 / 12, 13 / 12, 5 / 6, 5 / 6, 13 / 12, -17 / 12],
                 [13 / 12, 13 / 12, 5 / 6, 5 / 6, -11 / 12, 13 / 12],
                 [5 / 6, 5 / 6, 5 / 6, -1 / 6, 5 / 6, 5 / 6],
                 [5 / 6, 5 / 6, -1 / 6, 5 / 6, 5 / 6, 5 / 6],
                 [13 / 12, -11 / 12, 5 / 6, 5 / 6, 13 / 12, 13 / 12],
                 [-17 / 12, 13 / 12, 5 / 6, 5 / 6, 13 / 12, 19 / 12]], float)

matrixSize = len(A)
iterationNumber = 0
e = numpy.ones(matrixSize, float)
x = numpy.ones_like(numpy.zeros(matrixSize, float))
# funkcja biegnąca po całej macierzy, która tworzy kolejne transformacje Householdera dla macierzy A tak, aby zostawiać elementy tylko na trzech diagonalach
# robi to poprzez wyliczenie alfy i r, ktore potem podkladane sa do obliczania kolejnych komorek wektora v, ktory pomnozony przez siebie transponowanego daje macierz przeksztalenia P
# po pomnozeniu macierzy A przez P z macierzy A usuwane sa wszystkie elementy z danej kolumny poza elementem na trzech przekatnych
for column in range(0, matrixSize - 2) :

    # wyliczanie alfy ze wzoru, numpy.linalg.norm to funkcja liczaca norme aktualnie przegladanej kolumny macierzy A
    alpha = -1 * numpy.sign(A[column + 1][column]) * numpy.linalg.norm(A[column])
    # print(f'alpha: {alpha}')
    # wyliczanie r ze wzoru
    r = math.sqrt(1 / 2 * (alpha ** 2 - A[column + 1][column] * alpha))
    v = numpy.zeros(matrixSize, float)

    # wyliczanie wektora v
    for index in range(column, matrixSize) :
        if column == index :
            # dla elementu ktorego indeks jest rowny indeksowi przegladanej kolumny wpisywane jest zero,
            v[index] = 0
        elif column + 1 == index :
            # do kolejnego wpisywany jest specjalny wyraz,
            v[index] = (A[column + 1][column] - alpha) / (2 * r)
            # natomiast pozostale obliczane sa odddzielnym wzorem
        else :
            v[index] = A[index][column] / (2 * r)

    iterationNumber += 1
    vt = numpy.atleast_2d(v)
    vt = vt.transpose()
    # print(f'vt: \n{vt}')
    # wyliczanie macierzy P, ktora jest macierza transformacji usuwajacej elementy z kolumny macierzy A
    P = numpy.identity(matrixSize, float)
    V = 2 * v * vt
    # print(f'macierzV: {V}')
    P = P - V
    # print(f'Macierz P: \n {P}')
    # finalne wyliczanie macierzy A
    A = P @ A @ P
    x = P @ x
    print(f'Macierz A po {iterationNumber} iteracji: \n{A}')

# po sprowadzeniu do macierzy trojdiagonalnej wykonuje obroty Givensa, aby zostawic tylko wartosci na przekatnej macierzy lub powyzej tej przekatnej
# oraz licze zmiane przy obratach givensa dla rozwiazania rownania

for each in range(0, matrixSize - 1) :
    A, x = givens_tridiagonal_rotation(A, x, each, each + 1)

eigenvalues = numpy.zeros(matrixSize)
for row in range(matrixSize - 1, 0, -1) :
    if row != matrixSize - 1:
        eigenvalues[row] = A[row+1][row] / A[row][row]
    else:
        eigenvalues[row] = A[row][row]
print(A)
print(f'wartosci algortymu przeprowadzonego na macierzy: {eigenvalues}')
