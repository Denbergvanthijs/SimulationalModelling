import numpy as np
import matplotlib.pyplot as plt

"""
Onderstaande code is een aanpassing van de Udacity Course
"""


def forward_euler(h=0.1, g=9.81, friction=0.1, steps=50):
    t = np.zeros(steps+1)
    x = np.zeros(steps+1)
    v = np.zeros(steps+1)

    for step in range(steps):
        t[step + 1] = h * (step + 1)
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] - h * g
    return t, x, v


def plot_me(t, x, v):
    axes_height = plt.subplot(211)
    plt.plot(t, x)
    axes_velocity = plt.subplot(212)
    plt.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')

    plt.show()


t, x, v = forward_euler()
plot_me(t, x, v)
