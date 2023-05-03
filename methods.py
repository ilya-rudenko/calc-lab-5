import numpy as np


def make_delta_table(y):
    n = len(y)

    table = {}

    for i in range(n):
        table[i] = {}

    center = n // 2

    for i in range(n):
        table[0][i - center] = y[i]

    for i in range(1, n):
        for j in range(0, n - i):
            # print(j-center)
            table[i][j - center] = table[i - 1][j - center + 1] - table[i - 1][j - center]
            pass
    # print(table)

    return table


def print_delta_table(table):
    for i in table:
        for j in table[i]:
            print(round(table[i][j], 7), end=" ")
        print()
        # print(table[i])


def make_t_arr(n, method):
    if n == 0:
        return []

    if n % 2 == 1:
        center = (n - 1) // 2
        arr = []

        for i in range(-center, center + 1):
            arr.append(i)
        return arr

    center = n // 2

    if method == "second":
        arr = []

        for i in range(-center, center):
            arr.append(i)
        return arr
    else:
        arr = []

        for i in range(-center + 1, center + 1):
            arr.append(i)
        return arr


def gauss(x, y):
    n = len(x)
    center = x[n // 2]

    table = make_delta_table(y)

    X = np.linspace(x[0], x[-1], 50)
    Y = np.linspace(0, 0, 50)

    fact = {0: 1}
    for i in range(1, n):
        fact[i] = fact[i - 1] * i

    # print(fact)
    # print_delta_table(table)

    new_n = (n - 1) // 2

    for i in range(len(X)):
        xi = X[i]
        t = (xi - center) / (x[1] - x[0])
        if xi == center:
            Y[i] = y[i]
        elif xi > center:
            p = 0
            ind = 0
            c = 0

            for k in range(new_n * 2 + 1):
                numerator = 1

                for t_ind in make_t_arr(k, method="first"):
                    numerator *= t - t_ind

                numerator = numerator * table[k][ind] / fact[k]

                p += numerator

                c += 1

                if c == 2:
                    ind -= 1
                    c = 0

            Y[i] = p

        else:
            p = 0
            ind = 0
            c = 1

            for k in range(new_n * 2 + 1):
                numerator = 1

                for t_ind in make_t_arr(k, method="second"):
                    numerator *= t - t_ind

                numerator = numerator * table[k][ind] / fact[k]

                p += numerator

                c += 1

                if c == 2:
                    ind -= 1
                    c = 0

            Y[i] = p

    return X, Y


def lagrange(x, y):
    n = len(x)

    X = np.linspace(x[0], x[-1], 50)
    Y = np.linspace(0, 0, 50)

    for i in range(len(X)):
        xi = X[i]

        sum = 0

        for index in range(n):
            num = 1
            den = 1

            for k in range(n):
                if k == index:
                    continue

                num *= xi - x[k]
                den *= x[index] - x[k]

            p = num / den

            sum += p*y[index]

        Y[i] = sum

    return X, Y

