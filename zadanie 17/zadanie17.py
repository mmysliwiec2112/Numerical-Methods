import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def fxy(x, y) :
    return 100 * (x ** 4) - 200 * (x ** 2) * y + 100 * y ** 2 + x ** 2 - 2 * x + 1


# [df/dx, df/dy]
def gradient(gradient_arr, x, y) :
    gradient_arr[0] = - 2 + 2 * x + 400 * x ** 3 - 400 * x * y
    gradient_arr[1] = - 200 * x ** 2 + 200 * y


# [d^2f/dx^2, d^f/dxdy]
# [d^f/dxdy, d^2f/dy^2]
# jednak hesjan jest modyfikowany przez sama metode, aby zapewnic spadek w kolejnych krokach
# postac hesjanu z algorytmu:
# [(1 + lambda) * d^2f/dx^2, d^f/dxdy]
# [d^f/dxdy, (1 + lambda) * d^2f/dy^2]
def hessian(lambda_val, hessian_arr, x) :
    hessian_arr[0][0] = 2 + 1200 * x ** 2 - 400 * x
    hessian_arr[0][1] = hessian_arr[1][0] = (1 + lambda_val) * ((-400) * x)
    hessian_arr[1][1] = 200

# odwracanie hesjanu
def reverse_hessian(hessian_arr):
    return numpy.linalg.inv(hessian_arr)


def calculate_test_x_and_y(test_arr, hessian_arr, gradient_arr, x, y) :
    reverse_hessian_arr = reverse_hessian(hessian_arr)
    test_arr[0] = x - (reverse_hessian_arr[0][0] * gradient_arr[0] + reverse_hessian_arr[1][0] * gradient_arr[1])
    test_arr[1] = y - (reverse_hessian_arr[0][1] * gradient_arr[0] + reverse_hessian_arr[1][1] * gradient_arr[1])


def calculate_with_levenberg_marquardt(test_arr, x, y, lambda_val, hessian_arr, gradient_arr) :
    if fxy(test_arr[0], test_arr[1]) > fxy(x, y) :
        lambda_val *= 8
        hessian(lambda_val, hessian_arr, x)
    else :
        lambda_val /= 8
        x = test_arr[0]
        y = test_arr[1]
        ax.scatter(x, y, fxy(x, y))
        gradient(gradient_arr, x, y)
        calculate_test_x_and_y(test_arr, hessian_arr, gradient_arr, x, y)
        hessian(lambda_val, hessian_arr, x)
    return lambda_val, x, y


ax = plt.axes(projection="3d")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
hessian_arr = numpy.array([[0, 0], [0, 0]], float)
gradient_arr = numpy.array([0, 0], float)
test_arr = numpy.array([0, 0], float)
lambda_val = 2 ** (-10)
x1 = 5
y1 = 2
ax.scatter(x1, y1, fxy(x1, y1))
gradient(gradient_arr, x1, y1)
hessian(lambda_val, hessian_arr, x1)
calculate_test_x_and_y(test_arr, hessian_arr, gradient_arr, x1, y1)
for each in range(0, 3000) :
    lambda_val, x1, y1 = calculate_with_levenberg_marquardt(test_arr, x1, y1, lambda_val, hessian_arr, gradient_arr)
print("punkt pierwszy")
print(x1)
print(y1)
print(fxy(x1, y1))

x2 = 3
y2 = 3
ax.scatter(x2, y2, fxy(x2, y2))
gradient(gradient_arr, x2, y2)
hessian(lambda_val, hessian_arr, x2)
calculate_test_x_and_y(test_arr, hessian_arr, gradient_arr, x2, y2)
for each in range(0, 2000) :
    lambda_val, x2, y2 = calculate_with_levenberg_marquardt(test_arr, x2, y2, lambda_val, hessian_arr, gradient_arr)
print("punkt drugi")
print(x2)
print(y2)
print(fxy(x2, y2))

x3 = 2
y3 = 5
ax.scatter(x3, y3, fxy(x3, y3))
gradient(gradient_arr, x3, y3)
hessian(lambda_val, hessian_arr, x3)
calculate_test_x_and_y(test_arr, hessian_arr, gradient_arr, x3, y3)
for each in range(0, 1000) :
    lambda_val, x3, y3 = calculate_with_levenberg_marquardt(test_arr, x3, y3, lambda_val, hessian_arr, gradient_arr)
print("punkt trzeci")
print(x3)
print(y3)
print(fxy(x3, y3))
plt.show()
