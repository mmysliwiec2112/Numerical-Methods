import math
import numpy

numpy.set_printoptions(precision=4)
filename = "data.txt"
with open(filename) as f :
    content = f.readlines()
content = [x.strip() for x in content]
x = numpy.array([])
y = numpy.array([])
for each in content :
    b = each.split("\t")
    temp1, temp2 = [float(e) for e in b]
    x = numpy.append(x, [temp1])
    y = numpy.append(y, [temp2])

n = len(x)
s = 2
# uzupelnianie macierzy A, ktora jest macierza zawierajaca fi(xi)
A = numpy.array([[0 for x in range(s + 1)] for y in range(n)], float)
for each in range(0, n) :
    for each2 in range(0, s + 1) :
        A[each][each2] = x[each] ** (s - each2)

# obliczam z rownania A^t * A * p = A^t * y wektor p, ktory zawiera wszystkie wartosci wspolczynnikow wielomianu
AtA = numpy.transpose(A) @ A
Aty = numpy.transpose(A) @ y
p = numpy.linalg.solve(AtA, Aty)
q = 0
sigma = 0
print(f'p: {p}')

# obliczanie sigmy - odchylenie standardowe
el_sum = 0
for each in range(0, n):
    el_sum = y[each]
    for each2 in range(0, s+1):
        el_sum -= p[each2] * (A[each][each2] ** (s - each2))
    sigma += el_sum ** 2
sigma /= n
print(f'sigma: {sigma}')

# obliczanie wartosci minimalizowanej formy kwadratowej
for each in range(0, n) :
    el_sum = 0
    for each2 in range(0, s + 1):
        el_sum += p[each2] * A[each][each2]
    el_sum -= y[each]
    q += el_sum ** 2

print(f'q: {q}')
aic = math.log(q) + (2 * s) / n
cp = sigma * numpy.linalg.inv(AtA)
print(f'aic: {aic}')
print(f'cp: \n{cp}')


