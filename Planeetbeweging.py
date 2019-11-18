import numpy as np
import math
import matplotlib.pyplot as plt


def planeet(steps=360, planet=(5, 0), otherVec=(0, 0)):
    x = np.zeros(steps)
    y = np.zeros(steps)

    x[0] = planet[0]
    y[0] = planet[1]

    for step in range(steps - 1):
        x[step + 1] = math.tan(1/steps) + x[step]
        y[step + 1] = math.tan(1/steps) + y[step]

    return x, y


x, y = planeet()

plt.plot(x, y)
plt.show()
