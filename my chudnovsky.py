# very much limited by floating points etc

import math
from decimal import *
import matplotlib.pyplot as plt
import numpy as np
getcontext().prec = 100
pi = []
iter = 20
sqrt = 100.0249968757810059447921878763577780015950243686963146571355115696509678538643042923111879484
for i in range(1,iter):
    total = 0
    for q in range(i):
        total += (math.factorial(6*q)*(545141034*q + 13591409))/(math.factorial(3*q)*(math.factorial(q)**3)*(-2623537412640768000)**q)
    total = (426880*sqrt)/total
    total = "{0:.40f}".format(total)

    pi.append(total)
print(pi)
iterations = []
for i in range(1,iter):
    iterations.append(i)

x_pi = np.array([0, iter])
y_pi = np.array([math.pi, math.pi])

xpoints = np.array(iterations)
ypoints = np.array(pi)

plt.plot(x_pi, y_pi, label="pi")
plt.plot(xpoints, ypoints, label="leibniz approximation")
leg = plt.legend(loc='upper center')
plt.show()

#https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/ uselessness of generating digits of pi
