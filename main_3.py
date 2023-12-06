import numpy as np
from matplotlib import pyplot as plt

x = 12.1
a_values = np.arange(-5, 12, 1.75)
f_values = []

for a in a_values:
    f = np.exp(a*x) - 3.45 * a
    f_values.append(f)

f_max = max(f_values)
f_min = min(f_values)
f_avg = np.mean(f_values)
f_len = len(f_values)

plt.plot(a_values, f_values)

line_avg = [f_avg] * len(a_values)
plt.plot(a_values, line_avg)

plt.xlabel("a")
plt.ylabel("f")

plt.show()
