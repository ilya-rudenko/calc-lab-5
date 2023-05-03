from utils import read_file, draw_plot
from methods import make_delta_table, print_delta_table, gauss, lagrange

x, y = read_file()

if len(x) != len(y) or len(x) % 2 == 0:
    print("Error with dots")

else:

    print_delta_table(make_delta_table(y))

    gauss_x, gauss_y = gauss(x, y)

    lagrange_x, lagrange_y = lagrange(x, y)

    draw_plot(x, y, gauss_x, gauss_y, lagrange_x, lagrange_y , plot_original=False, plot_gauss=True, plot_lagrange=True)