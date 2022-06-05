import numpy


def spline(original_data, step):
    data = original_data[::step]
    n = len(data) - 1
    coefficients_number = 4
    equations_number = n * coefficients_number
    matrix = numpy.array([[0.0 for x in range(equations_number)] for y in range(equations_number)])
    b = numpy.array([0.0 for x in range(equations_number)])

    for j in range(n):
        h = data[j + 1][0] - data[j][0]

        matrix[coefficients_number * j][coefficients_number * j] = 1
        b[coefficients_number * j] = data[j][1]

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

    coefficients = numpy.linalg.solve(matrix, b)

    values = []
    for i in range(len(original_data) - 1):
        for j in range(len(data) - 1):
            value = 0
            if data[j][0] <= i <= data[j + 1][0]:
                for k in range(coefficients_number):
                    h = i - data[j][0]
                    value += coefficients[coefficients_number * j + k] * h ** k
                break
        values.append(value)
    return values
