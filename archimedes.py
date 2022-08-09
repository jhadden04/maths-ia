import math
import matplotlib.pyplot as plt
import numpy as np
upper_pi = []
lower_pi = []
difference = []
average = []
iteration = []
iter = 100
for i in range(3,iter):
    inner_circumference = i*(math.sqrt(2-2*math.cos(2*math.pi/i)))
    outer_circumference = 2 * i * math.tan(2 * math.pi / (2 * i))
    lower_pi.append(inner_circumference/2)
    upper_pi.append(outer_circumference/2)
    difference.append(outer_circumference/2 - inner_circumference/2)
    average.append((outer_circumference/2 + inner_circumference/2)/2)
    iteration.append(i)


print(upper_pi)
print(lower_pi)
print(difference)
print(average)

upper_y = np.array(upper_pi)
upper_x = np.array(iteration)

lower_y = np.array(lower_pi)
lower_x = np.array(iteration)

x_pi = np.array([0, iter])
y_pi = np.array([math.pi, math.pi])

plt.plot(upper_x, upper_y, label="upper bound of pi")
plt.plot(lower_x, lower_y, label="lower bound of pi")
plt.plot(x_pi, y_pi, 'b-',label='pi')
plt.xlabel("Number of Sides")
leg = plt.legend(loc='upper center')


plt.show()
