from matplotlib import pyplot
import pandas

from methods.lagrange import lagrange
from methods.spline import spline


def plot_interpolation(name, knots_number, data_set_number, sample_data, real_values, interpolated_values):
    font = {'family': 'Arial', 'size': 10}
    pyplot.rc('font', **font)
    pyplot.plot(range(len(interpolated_values)), interpolated_values, label='Interpolated values', color='r')
    pyplot.plot(range(len(real_values)), real_values, label='Real values', color='b')
    pyplot.scatter(sample_data[0][0], sample_data[0][1], s=125, marker='.', label='Knots', color='g')
    for i, point in enumerate(sample_data):
        if i != 0:
            pyplot.scatter(point[0], point[1], s=125, marker='.', color='g')
    pyplot.xlabel('Point number')
    pyplot.ylabel('Height [m]')
    pyplot.title(name + ' interpolation compared to real values [' + str(knots_number) + ' knots]')
    pyplot.legend()
    pyplot.savefig('charts' + str(data_set_number + 1) + '/' + name + '-' + str(knots_number) + '-knots.png')
    pyplot.close()


if __name__ == '__main__':
    data_sets = ['data_sets/GlebiaChallengera.csv', 'data_sets/MountEverest.csv', 'data_sets/WielkiKanionKolorado.csv']
    for data_set_number, data_set in enumerate(data_sets):
        data = pandas.read_csv(data_set).values
        for i, value in enumerate(data):
            value[0] = i
        real_values = [value[1] for value in data]

        knots_numbers = [10, 30, 40, 70, 100]
        for knots_number in knots_numbers:
            lagrange_interpolated_values, sample_data = lagrange(data, knots_number)
            plot_interpolation('Lagrange', knots_number, data_set_number, sample_data, real_values,
                               lagrange_interpolated_values)

            spline_interpolated_values, sample_data = spline(data, knots_number)
            plot_interpolation('Spline', knots_number, data_set_number, sample_data, real_values,
                               spline_interpolated_values)
