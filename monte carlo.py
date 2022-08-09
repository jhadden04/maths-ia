import random
iteration = 1000
circle = 0
square = 0

for i in range(iteration ** 2):
    randx = random.uniform(-1, 1)
    randy = random.uniform(-1, 1)

    origin_distance = randx ** 2 + randy ** 2
    if origin_distance <= 1:
        circle += 1
    square += 1
    pi = 4 * (circle / square)

print(pi)
