import matplotlib.pylab as plt
import numpy as np
import seaborn as sns
from numpy.linalg import norm

"""
Onderstaande code is een aanpassing van de Udacity Course
"""


h = 1.0  # s
earthMass = 5.97e24  # kg
gConst = 6.67e-11  # N m2 / kg2


def acceleration(spaceshipPos):
    earthVector = - spaceshipPos
    return gConst * earthMass / norm(earthVector) ** 3 * earthVector


def ship_trajectory():
    num_steps = 13000
    x = np.zeros([num_steps + 1, 2])  # m
    v = np.zeros([num_steps + 1, 2])  # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step+1] = x[step] + h * v[step]
        v[step+1] = v[step] + h * acceleration(x[step])
    return x, v


def plot():
    x, v = ship_trajectory()

    sns.set(context="notebook")
    plt.plot(x[:, 0], x[:, 1])
    plt.scatter(0, 0)

    plt.axis('equal')
    plt.xlabel('Longitudinal position in m')
    plt.ylabel('Lateral position in m')

    plt.show()


if __name__ == "__main__":
    plot()
