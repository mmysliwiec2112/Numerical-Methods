import numpy


def getValA(col, row) :
    if col == row + 1 or col + 1 == row or col + 4 == row or col == row + 4 :
        return 1.0
    elif col == row :
        return 4.0
    else :
        return 0.0


prevX = 0
numpy.printoptions(precision=4)
X = numpy.zeros(128, float)
matrixSize = len(X)

R = numpy.ones(matrixSize, float)
RRt = 0
P = numpy.ones(matrixSize, float)
alpha = 0
alpha_times_P = numpy.zeros(matrixSize, float)
beta = 0
beta_times_P = numpy.zeros(matrixSize, float)
e = numpy.ones(matrixSize, float)
PA = numpy.zeros(matrixSize, float)
PAP = 0

# ustawiam poczatkowe wyniki na 1
# for each in range(0, matrixSize) :
#     R[each] = P[each] = e[each]
for each in range(0, matrixSize) :
    RRt += R[each] ** 2

# przygotowuje zmienne pod pierwsza iteracje
iteration = 1
R_norm = 0
for each in range(0, matrixSize) :
    R_norm += R[each] ** 2
R_norm = R_norm ** 0.5

while R_norm > 0.001 and iteration < 25 :

    print(f'iteracja: {iteration}')
    # tworzenie wektora p * A
    for each in range(0, matrixSize) :
        for each2 in range(0, matrixSize) :
            if getValA(each, each2) != 0:
                PA[each] += P[each2] * getValA(each, each2)
        PAP += P[each] * PA[each]

    # alpha  = r * r^t / p * Ap
    alpha = RRt / PAP
    for each in range(0, matrixSize) :
        alpha_times_P[each] = alpha * P[each]

    # beta = r * r^t
    beta = RRt

    # r = r - alpha * Ap
    for each in range(0, matrixSize) :
        R[each] = R[each] - alpha * PA[each]

    # liczenie nowego r * r^t
    RRt = 0
    for each in range(0, matrixSize) :
        RRt += R[each] ** 2

    beta = RRt / beta

    # wyliczanie p = r + beta*p
    for each in range(0, matrixSize) :
        beta_times_P[each] = beta * P[each]
        P[each] = R[each] + beta_times_P[each]

    # liczenie kolejnej iteracji rozwiazan
    # x = x + alpha * p
    for each in range(0, matrixSize) :
        X[each] = X[each] + alpha_times_P[each]

    # inkrementacja iteracji
    iteration += 1

    for each in range(0, matrixSize) :
        PA[each] = 0
    PAP = 0

    R_norm = 0
    for each in range(0, matrixSize) :
        R_norm += R[each] ** 2
    R_norm = R_norm ** 0.5
    # numpy.linalg.norm(R)
print(numpy.array(X))
