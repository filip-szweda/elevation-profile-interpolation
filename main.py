from matplotlib import pyplot
import pandas

from methods.lagrange import lagrange
from methods.spline import spline


def plot_interpolation(name, knots_number, real_values, interpolated_values):
    font = {'family': 'Arial', 'size': 10}
    pyplot.rc('font', **font)
    pyplot.plot(range(len(interpolated_values)), interpolated_values, label='Interpolated values')
    pyplot.plot(range(len(real_values)), real_values, label='Real values')
    pyplot.xlabel('Point')
    pyplot.ylabel('Height [m]')
    pyplot.title(name + ' interpolation values in comparison to real values [' + str(knots_number) + ' knots]')
    pyplot.legend()
    pyplot.savefig('charts/' + name + '-' + str(knots_number) + '.png')
    pyplot.close()


if __name__ == '__main__':
    data = pandas.read_csv('WielkiKanionKolorado.csv').values
    for i, value in enumerate(data):
        value[0] = i
    real_values = [value[1] for value in data]

    knots_numbers = [10, 40, 70, 100]
    for knots_number in knots_numbers:
        lagrange_interpolated_values = lagrange(data, knots_number)
        plot_interpolation('Lagrange', knots_number, real_values, lagrange_interpolated_values)

        spline_interpolated_values = spline(data, knots_number)
        plot_interpolation('Spline', knots_number, real_values, spline_interpolated_values)
