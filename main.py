from matplotlib import pyplot
import pandas

from methods.lagrange import lagrange
from methods.spline import spline


def plot_interpolation(real_values, interpolated_values):
    font = {'family': 'Arial', 'size': 10}
    pyplot.rc('font', **font)
    pyplot.plot(range(len(interpolated_values)), interpolated_values, label='Interpolated values')
    pyplot.plot(range(len(real_values)), real_values, label='Real values')
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.title('Lorem ipsum')
    pyplot.legend()
    pyplot.show()


if __name__ == '__main__':
    data = pandas.read_csv('WielkiKanionKolorado.csv').values
    for i, value in enumerate(data):
        value[0] = i

    steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    real_values = [value[1] for value in data]

    lagrange_interpolated_values = lagrange(data, 10)
    plot_interpolation(real_values, lagrange_interpolated_values)

    spline_interpolated_values = spline(data, 10)
    plot_interpolation(real_values, spline_interpolated_values)
