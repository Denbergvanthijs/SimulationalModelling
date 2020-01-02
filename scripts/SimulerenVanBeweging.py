import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


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


def plot(t, x, v):
    sns.set(context="notebook")
    
    axes_height = plt.subplot(211)
    sns.lineplot(t, x)
    axes_velocity = plt.subplot(212)
    sns.lineplot(t, v)
    
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    
    axes_height.set_xlim(left=0)
    axes_velocity.set_xlim(left=0)

    plt.show()


if __name__ == '__main__':
    t, x, v = forward_euler()
    plot(t, x, v)
