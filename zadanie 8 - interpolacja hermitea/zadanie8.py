import numpy
import matplotlib.pyplot
import math


# funkcja zwracajaca wartosc funkcji w punkcie x
def fx(x) :
    return 1 / (1 + (5 * (x ** 2)))


def lagrange_interpolation(arr_x, arr_y, x) :
    value_in_x = 0
    for iterator in range(0, data_size) :
        upper_part = 1
        lower_part = 1
        for each in range(0, data_size) :
            if each != iterator :
                upper_part *= (x - arr_x[each])
                lower_part *= (arr_x[iterator] - arr_x[each])
        l_for_index = upper_part / lower_part
        value_in_x += arr_y[iterator] * l_for_index
    return value_in_x


numpy.printoptions(precision=4)
data_size = 65
data = numpy.zeros(data_size)
values = numpy.zeros(data_size)
x = numpy.linspace(-1, 1, num=data_size)
# uzupelnianie tabeli wartosciami x-a
for each in range(0, 32) :
    data[each] = -1 + each / 32
for each in range(0, 33) :
    data[each + 32] = 1 - (32 - each) / 32
# uzupelnianie tabeli wartosci funkcji i jej pochodnej dla x-a
for each in range(0, 65) :
    values[each] = fx(data[each])

# pokazanie punktow i przypisanym im przez funkcje oraz pochodna funkcji wartosci
matplotlib.pyplot.plot(data, values, 'ro')
matplotlib.pyplot.plot(data, lagrange_interpolation(data, values, x))
matplotlib.pyplot.show()
