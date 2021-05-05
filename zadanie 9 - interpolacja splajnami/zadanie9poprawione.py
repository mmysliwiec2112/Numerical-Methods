import numpy
import matplotlib.pyplot


# funkcja zwracajaca wartosc funkcji w punkcie x
def fx(x) :
    return 1 / (1 + (5 * (x ** 2)))


# funkcja zwracajaca wartosc pochodnej funkcji fx w zadanym punkcie x
def fx_derivative(x) :
    return -10 * x / ((1 + 5 * (x ** 2)) ** 2)


# obliczanie wartosci drugiej pochodnej algorytmem Thomasa
def calculate_second_derivative_values(fun_a, fun_b, fun_c, fun_d, arr_x) :
    h = arr_x[1] - arr_x[0] # blad byl tu - zamiast odleglosci miedzy x-ami bralem roznice pomiedzy ich wartosciami
    matrix_size = len(fun_d)
    for each in range(0, matrix_size) :
        fun_d[each] = fun_d[each] * 6 / (h ** 2)

    X = numpy.zeros(matrix_size, float)
    beta = numpy.zeros(matrix_size, float)
    gamma = numpy.zeros(matrix_size, float)

    beta[0] = -fun_c[0] / fun_b[0]
    gamma[0] = fun_d[0] / fun_b[0]

    for each in range(1, matrix_size) :
        beta[each] = -fun_c[each] / (fun_b[each] + fun_a[each - 1] * beta[each - 1])
    for each in range(1, matrix_size) :
        gamma[each] = (fun_d[each] - fun_a[each] * gamma[each - 1]) / (fun_b[each] + fun_a[each] * beta[each - 1])
    X[matrix_size - 1] = gamma[matrix_size - 1]
    for each in range(matrix_size - 1, 0, -1) :
        X[each - 1] = gamma[each - 1] - beta[each - 1] * X[each]
    return X



# funkcja tworząca splajny kubiczne
def cubic_spline_interpolation(arr_x, arr_y, arr_sec_der_y, idx, x) :
    a = (arr_x[idx + 1] - x) / (arr_x[idx + 1] - arr_x[idx])
    b = (x - arr_x[idx]) / (arr_x[idx + 1] - arr_x[idx])
    c = 1 / 6 * (a ** 3 - a) * ((arr_x[idx + 1] - arr_x[idx]) ** 2)
    d = 1 / 6 * (b ** 3 - b) * ((arr_x[idx + 1] - arr_x[idx]) ** 2)
    return a * arr_y[idx] + b * arr_y[idx + 1] + c * arr_sec_der_y[idx] + d * arr_sec_der_y[idx + 1]


# dane
data_size = 65
data = numpy.zeros(data_size)
values = numpy.zeros(data_size)
derivative_values = numpy.zeros(data_size)

# uzupelnianie tabeli wartosciami x-a
for each in range(0, 32) :
    data[each] = -1 + each / 32
for each in range(0, 33) :
    data[each + 32] = 1 - (32 - each) / 32

# uzupelnianie tabeli wartosci funkcji i jej pochodnej dla x-a
for each in range(0, 65) :
    values[each] = fx(data[each])
    derivative_values[each] = fx_derivative(data[each])

# tworzenie wartosci macierzy potrzebnej przy wyliczaniu wartosci drugiej pochodnej poprzez algorytm Thomasa
a = numpy.zeros(data_size)
b = numpy.zeros(data_size)
c = numpy.zeros(data_size)
d = numpy.zeros(data_size)
for each in range(0, data_size) :
    if each == 0 :
        b[each] = 4
        a[each] = 0
    elif each == data_size - 1 :
        b[each] = 4
        c[each] = 0
    else :
        a[each] = 1
        b[each] = 4
        c[each] = 1
for each in range(0, data_size) :
    if each == 0 or each == data_size - 1 :
        d[each] = 0
    else :
        d[each] = values[each - 1] - 2 * values[each] + values[each + 1]

# licze wartosci drugiej pochodnej
second_derivative_values = calculate_second_derivative_values(a, b, c, d, data)


# tworze na wykresie punkty w miejscach zadanych przez dane
matplotlib.pyplot.plot(data, values, 'ro')

# idac po kolei po wszystkich wezlach lacze kolejne pary wezlow splajnami tworzonymi przez funkcje
for each in range(0, data_size - 1) :
    x = numpy.linspace(data[each], data[each + 1], num=100)
    matplotlib.pyplot.plot(x, cubic_spline_interpolation(data, values, second_derivative_values, each, x))
matplotlib.pyplot.show()
