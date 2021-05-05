import numpy
# przyblizenia rozwiazan
x = numpy.zeros(128, float)
matrixSize = len(x)
# algorytm Gaussa-Seidela

# zmienne dla algorytmu
iteration = 1
prevX = 1
# deklaracje macierzy uzywanych w algorytmie, nie potrzebne dla znanej macierzy
# U = numpy.zeros(128, float)
# U = numpy.atleast_2d(U)
# U = U * numpy.transpose(U)
# D = numpy.zeros(128, float)
# D = numpy.atleast_2d(D)
# D = D * numpy.transpose(D)
# L = numpy.zeros(128, float)
# L = numpy.atleast_2d(L)
# L = L * numpy.transpose(L)
e = numpy.ones(matrixSize, float)
X = numpy.zeros(128, float)
# dzielę A na L + D + U, gdzie:
# L - dwie dolne przekątne
# D - główna przekątna
# U - dwie górne przekątne
# liczenie iteracji będzie odbywać się poprzez podstawienie do wzoru x^n+1 = D^-1 * b - D^-1 * L * x^n+1 - D^n-1 * U * x^n

# D^-1 * b
for row in range(0, matrixSize) :
    e[row] *= 0.25

# przybliżenia x
while iteration < 11:
    for row in range(0, matrixSize) :
        X[row] = e[row]
        for column in range(0, row) :
            if column == row - 4 or column == row - 1 :
                X[row] -= 0.25 * X[column]  # D^-1 * Lx^n+1 - Jedyne wartosci L jakie mają tu znaczenie to 1 * 1/4 - 1/4
        for column in range(row + 1, matrixSize) :
            if column == row + 1 or column == row + 4 :
                X[row] -= 0.25 * X[column]  # D^-1 * U * x - podobnie jak w przypadku macierzy L, jedynie licza sie elementy = 1, ktore sa na przekatnych ograniczonych ifem
        prevX = X[0]
    iteration += 1

print(f'iteracja: {iteration - 1}')
print(X)
