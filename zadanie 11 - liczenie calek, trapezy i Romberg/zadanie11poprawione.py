import numpy
import math
import matplotlib.pyplot
import scipy.integrate


# funkcja zwracajaca wartosc zadanej funkcji dla danego punktu x
def fx(x) :
    a = math.pi * ((1 + (x ** (1 / 2))) / (1 + (x ** 2)))
    return numpy.sin(a) * (math.e ** (-x))


# funkcja liczaca wartosc calki na podstawie metody trapezow, uzywana w pierwszej kolumnie metody Romberga
def trapezoidal_integral(i, a, b) :
    amount_of_steps = 2 ** i
    dx = (b - a) / amount_of_steps  # obliczanie dlugosci kroku dla podanej ilosci krokow
    sum_of_elements = 0.0
    for each in range(0, amount_of_steps) :
        if each != 0 or each != amount_of_steps - 1 :
            sum_of_elements += dx * fx(a + each * dx)  # poczatek przedzialu calkowania to 0- nie ma go w wywolaniu funkcji
    sum_of_elements += dx * (fx(a) + fx(amount_of_steps - 1)) / 2
    return sum_of_elements


# funckja liczaca kolejne wyrazenia do metody Romberga: Ank = 1/4^m-1 * (4^m * an-1,k - An-1,k)
def romberg_integral(romberg_array, i, m) :
    return (((4 ** m) * romberg_array[m - 1][i]) - romberg_array[m - 1][i - 1]) / (4 ** m - 1)


# dane
epsilon = 10
x = numpy.linspace(0, 18, num=epsilon)
matplotlib.pyplot.plot(x, fx(x))

# wyliczam x, dla ktorego e ^ -x osiagnie wymagana dokladnosc
end = 0
while math.e ** (-end) > 10 ** (-7) :
    end += 1
x = numpy.linspace(0, end, num=epsilon)
# dla e ^ -17 osiagamy juz granice, powyzej ktorej wartosci mozemy juz zaniedbac i przyrownac do 0
# z tego, wynika, ze przedzial w ktorym chcemy policzyc calke to przedzial (0,18)

# wyliczam kolejne zbiory punktow, z ktorych metoda trapezow wyliczam calke, dopoki kolejne przyblizenia nie osiana zadanej dokladnosci
# zaczynam od przedzialow o dlugosci (xn - x0)/n = 1
previous_result = 0
current_result = 1
iteration = 0
while iteration < 40 and abs(current_result - previous_result) > 10 ** (-7) :
    previous_result = current_result
    epsilon += epsilon
    x = numpy.linspace(0, end, num=epsilon)
    current_result = trapezoidal_integral(iteration, 0, end)
    iteration += 1
print(f' wymagana ilosc iteracji to: {iteration}')

# resetuje ilosc podzialow
epsilon = 11
k = 10
x = numpy.linspace(0, 18, num=(2 ** k))
romberg = numpy.atleast_2d(numpy.zeros(k))
romberg = romberg * numpy.transpose(romberg)
iteration = 0
romberg[0][0] = trapezoidal_integral(0, 0, end)
romberg[1][0] = trapezoidal_integral(1, 0, end)

# podstawiam do kolejnych wyrazow w tablicy Romberga wyrazenia liczone przez funkcje do momentu osiagniecia granicznej liczby iteracji lub osiagniecia wymaganej dokladnosci
while iteration == 0 or iteration == 1 or (iteration < k and abs(
        romberg[iteration - 2][k - iteration + 1] - romberg[iteration - 1][k - iteration]) > 10 ** (-7)) :
    for each in range(0, k - iteration) :
        if each == 0 and iteration != 0 or iteration != 1 :
            romberg[iteration][each] = trapezoidal_integral(each, 0, end)
        elif romberg[iteration][each] - romberg[iteration - 1][each] < 10 ** (-7) :
            romberg[iteration][each] = romberg_integral(romberg, iteration, each)
    iteration += 1

# wyswietlanie wynikow
print(f' wynik metody trapezów {current_result}')
result = scipy.integrate.quad(fx, 0, 18)
print(f' kontrolny {result[0]}')
print(f' kontrolny Romberg {scipy.integrate.romberg(fx, 0, 18)}')
print(f' wymagana ilosc iteracji dla metody Romberga to: {iteration}')
print(f' wynik metody Romberga {romberg[k - iteration][iteration - 1]}')
