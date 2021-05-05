import matplotlib.pyplot
import numpy
import  scipy.interpolate


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


def pol(x):
    suma = 0
    for each in range (0, len(values)):
        suma += values[each] * (x ** (len(values) - each - 1))
    return suma


x_data = numpy.array([0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.9375000])
y_data = numpy.array([0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307])
data_size = 8
matplotlib.pyplot.plot([0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.9375000],
                       [0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307])
matplotlib.pyplot.plot([0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.9375000],
                       [0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307], 'ro')

x = numpy.linspace(-1, 1)
y = numpy.zeros(50)


A = numpy.atleast_2d(numpy.ones(data_size))
At = numpy.transpose(A)
A = A * At
for row in range(0, data_size):
    temp = x_data[row]
    for col in range(0, data_size):
        A[row][col] = temp ** (data_size - col - 1)
numpy.set_printoptions(precision=3)
values = numpy.linalg.solve(A, y_data)
control = scipy.interpolate.lagrange(x_data, y_data)
print(f'wartosci wspolczynnikow wielomianu: \n{values}')
print(f'kontrolne obliczenia: \n{control}')
matplotlib.pyplot.plot(x, lagrange_interpolation(x_data, y_data, x), '-r')
matplotlib.pyplot.plot(x, pol(x), '-g')
matplotlib.pyplot.show()
