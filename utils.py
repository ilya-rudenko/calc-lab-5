import numpy as np
import matplotlib.pyplot as plt
from generate_func import F


def read_file():
    x = []
    y = []

    f = open("file.txt", "r")

    for line in f:
        xi, yi = [float(i) for i in line.split(",")]
        x.append(xi)
        y.append(yi)

    f.close()

    z = zip(x, y)
    zs = sorted(z, key=lambda tup: tup[0])
    x = [x[0] for x in zs]
    y = [x[1] for x in zs]

    return x, y


def draw_plot(orig_x, orig_y, gauss_x, gauss_y, lagrange_x, lagrange_y, plot_original=False, plot_gauss=True, plot_lagrange=True):
    plt.axvline(x=0, c="black")
    plt.axhline(y=0, c="black")

    if plot_gauss:
        plt.plot(gauss_x, gauss_y, color="g")
    if plot_lagrange:
        plt.plot(lagrange_x, lagrange_y, color="r")

    s = [64 for i in range(len(orig_x))]

    plt.scatter(orig_x, orig_y, color="b", s=s)

    if plot_original:
        X = np.linspace(orig_x[0] - 2, orig_x[-1] + 2, 100)
        Y = F(X)

        plt.plot(X, Y, color="b")

    plt.show()
