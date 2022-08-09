# first method: 4(1 - 1/3 + 1/5 - 1/7....)
# general formula: arctan(1) = 1 - 1/3 + 1/5 - 1/7.... = pi/4
import matplotlib.pyplot as plt
import numpy as np
import math

print(math.pi)
pi = []
total = 0
iter = 100
for i in range(0, iter):
    total += (1 / ((2 * i + 1) * (-1) ** i))
    pi.append(4 * total)
x_axis = []
for i in range(iter):
    x_axis.append(i + 1)

print(pi)

xpoints = np.array(x_axis)
ypoints = np.array(pi)

x_pi = np.array([0, iter])
y_pi = np.array([math.pi, math.pi])

plt.plot(xpoints, ypoints, label="leibniz approximation")
plt.plot(x_pi, y_pi, label="pi")

plt.show()

