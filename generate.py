import numpy as np
from generate_func import F

x = np.linspace(-4, 4, 13)

y = F(x)

f = open("file.txt", "w")

for i in range(len(x)):
    f.write(f"{x[i]}, {y[i]}\n")

f.close()
