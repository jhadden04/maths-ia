# first method: 4(1 - 1/3 + 1/5 - 1/7....)
# general formula: arctan(1) = 1 - 1/3 + 1/5 - 1/7.... = pi/4
import matplotlib.pyplot as plt
import numpy as np
pi = []
total = 0
iter = 100
for i in range(0, iter):
    total += (1/((2*i + 1)*(-1)**i))
    pi.append(4*total)
x_axis = []
for i in range(iter):
    x_axis.append(i+1)

print(pi)

xpoints = np.array(x_axis)
ypoints = np.array(pi)

plt.plot(xpoints, ypoints)
plt.show()

