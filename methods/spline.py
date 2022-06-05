import numpy


def spline(original_data, knots_number):
    step = int(round(len(original_data) / knots_number * 2) / 2)
    data = original_data[::step]
    n = len(data) - 1
    coefficients_number = 4
    equations_number = n * coefficients_number
    A = numpy.array([[0.0 for _ in range(equations_number)] for _ in range(equations_number)])
    b = numpy.array([0.0 for _ in range(equations_number)])

    for i in range(n):
        h = data[i + 1][0] - data[i][0]

        A[coefficients_number * i][coefficients_number * i] = 1
        b[coefficients_number * i] = data[i][1]

        for j in range(coefficients_number):
            A[coefficients_number * i + 1][coefficients_number * i + j] = h ** j
            b[coefficients_number * i + 1] = data[i + 1][1]

        if i > 0:
            for j in range(coefficients_number):
                if j == 0:
                    A[coefficients_number * (i - 1) + 2][j + coefficients_number * (i - 1)] = j
                else:
                    A[coefficients_number * (i - 1) + 2][j + coefficients_number * (i - 1)] = j * h ** (j - 1)
            A[coefficients_number * (i - 1) + 2][1 + coefficients_number * i] = -1

        if i > 0:
            A[coefficients_number * (i - 1) + 3][coefficients_number * (i - 1) + 2] = 2
            A[coefficients_number * (i - 1) + 3][coefficients_number * (i - 1) + 3] = 6 * h
            A[coefficients_number * (i - 1) + 3][coefficients_number * i + 2] = -2

        if i == n - 2:
            A[equations_number - 2][2] = 2
        if i == n - 1:
            A[equations_number - 1][-2] = 2
            A[equations_number - 1][-1] = 6 * h

    coefficients = numpy.linalg.solve(A, b)

    values = []
    for i in range(int(data[len(data) - 1][0] + 1)):
        for j in range(len(data) - 1):
            value = 0
            if data[j][0] <= i <= data[j + 1][0]:
                for k in range(coefficients_number):
                    h = i - data[j][0]
                    value += coefficients[coefficients_number * j + k] * h ** k
                break
        values.append(value)
    return values, data
