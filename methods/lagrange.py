def lagrange(original_data, knots_number):
    step = int(round(len(original_data) / knots_number * 2) / 2)
    data = original_data[::step]
    values = []
    for i in range(int(data[len(data) - 1][0] + 1)):
        value = 0
        for j, _ in enumerate(data):
            tmp = data[j][1]
            for k, _ in enumerate(data):
                if j != k:
                    tmp *= (original_data[i][0] - data[k][0]) / (data[j][0] - data[k][0])
            value += tmp
        values.append(value)
    return values, data
