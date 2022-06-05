from matplotlib import pyplot
import pandas

from methods.lagrange import lagrange
from methods.spline import spline


def plot_interpolation(name, step, real_values, interpolated_values):
    font = {'family': 'Arial', 'size': 10}
    pyplot.rc('font', **font)
    pyplot.plot(range(len(interpolated_values)), interpolated_values, label='Interpolated values')
    pyplot.plot(range(len(real_values)), real_values, label='Real values')
    pyplot.xlabel('Point')
    pyplot.ylabel('Height [m]')
    pyplot.title(name + ' interpolation values in comparison to real values')
    pyplot.legend()
    pyplot.savefig(name + '-' + str(step) + '.png')
    pyplot.close()


if __name__ == '__main__':
    data = pandas.read_csv('WielkiKanionKolorado.csv').values
    for i, value in enumerate(data):
        value[0] = i

    # knots_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    real_values = [value[1] for value in data]
    for step in steps:
        # lagrange_interpolated_values = lagrange(data, step)
        # plot_interpolation('Lagrange', step, real_values, lagrange_interpolated_values)

        spline_interpolated_values = spline(data, step)
        plot_interpolation('Spline', step, real_values, spline_interpolated_values)
