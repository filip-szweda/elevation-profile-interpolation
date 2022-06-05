from matplotlib import pyplot
import numpy as np
import pandas


def lagrange(data):
    values = []
    for i, _ in reversed(list(enumerate(data))):
        value = 0
        for j, _ in enumerate(data):
            tmp = data[j][1]
            for k, _ in enumerate(data):
                if j != k:
                    tmp *= (data[i][0] - data[k][0]) / (data[j][0] - data[k][0])
            value += tmp
        values.append(value)
    return values

def spline_calc(x, coefficients_number, coefficients, data):
    for i in range(len(data)-1):
        result = 0
        if data[i][0] <= x <= data[i+1][0]:
            for j in range(coefficients_number):
                h = x - data[i][0]
                result += coefficients[4 * i + j] * h**j
            break
    return result

def spline(datax):
    data = [(1, 6), (3, -2), (5, 4)]
    n = len(data) - 1
    equations_number = n * 4
    coefficients_number = 4
    matrix = np.array([[0 for x in range(equations_number)] for y in range(equations_number)])
    b = np.array([0 for x in range(equations_number)])

    for j in range(0, n):
        h = data[j + 1][0] - data[j][0]

        matrix[coefficients_number * j][coefficients_number * j] = 1
        b[4 * j] = data[j][1]

        for i in range(coefficients_number):
            matrix[coefficients_number * j + 1][coefficients_number * j + i] = h ** i
            b[coefficients_number * j + 1] = data[j + 1][1]

        if j > 0:
            for i in range(coefficients_number):
                if i == 0:
                    matrix[coefficients_number * (j - 1) + 2][i + coefficients_number * (j - 1)] = i
                else:
                    matrix[coefficients_number * (j - 1) + 2][i + coefficients_number * (j - 1)] = i * h ** (
                            i - 1)
            matrix[coefficients_number * (j - 1) + 2][1 + coefficients_number * j] = -1

        if j > 0:
            matrix[coefficients_number * (j - 1) + 3][coefficients_number * (j - 1) + 2] = 2
            matrix[coefficients_number * (j - 1) + 3][coefficients_number * (j - 1) + 3] = 6 * h
            matrix[coefficients_number * (j - 1) + 3][coefficients_number * j + 2] = -2

        if j == n - 2:
            matrix[equations_number - 2][2] = 2
        if j == n - 1:
            matrix[equations_number - 1][-2] = 2
            matrix[equations_number - 1][-1] = 6 * h

    results = np.linalg.solve(matrix, b)
    values = []
    for i in range(0, data[-1][0] + 1):
        value = spline_calc(i, 4, results, data)
        values.append(value)
    return values

if __name__ == '__main__':
    data = pandas.read_csv('WielkiKanionKolorado.csv').values

    # steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # values = lagrange(data[::10])
    # font = {'family': 'Arial', 'size': 10}
    # pyplot.rc('font', **font)
    # pyplot.plot(range(len(data)), values)
    # pyplot.xlabel('x')
    # pyplot.ylabel('y')
    # pyplot.title('Lagrange interpolation')
    # pyplot.show()

    values = spline(data[::10])
    font = {'family': 'Arial', 'size': 10}
    pyplot.rc('font', **font)
    pyplot.plot(range(len(values)), values)
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.title('Spline interpolation')
    pyplot.show()
    test = ""