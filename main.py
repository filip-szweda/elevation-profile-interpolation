import pandas
from matplotlib import pyplot


def lagrange(step, data):
    points = data[::step]
    values = []
    for i, _ in reversed(list(enumerate(data))):
        value = 0
        for j, _ in enumerate(points):
            tmp = data[j][1]
            for k, _ in enumerate(points):
                if j != k:
                    tmp *= (data[i][0] - points[k][0]) / (points[j][0] - points[k][0])
            value += tmp
        values.append(value)
    return values


if __name__ == '__main__':
    data = pandas.read_csv('WielkiKanionKolorado.csv').values
    # steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    values = lagrange(10, data)
    font = {'family': 'Arial', 'size': 10}
    pyplot.rc('font', **font)
    pyplot.plot(range(len(data)), values)
    pyplot.xlabel('Matrix size')
    pyplot.ylabel('Execution time [s]')
    pyplot.title('Linear equations calculation methods execution times')
    pyplot.show()
