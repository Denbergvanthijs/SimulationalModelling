import numpy as np
from numpy.linalg import norm
import matplotlib.pylab as plt

"""
Onderstaande code is een aanpassing van de Udacity Course
Gebruik zowel forward Euler-integratie als Heun-integratie om de vergelijking u' (t) = u(t) (met beginconditie u(0) = 1) op te lossen. 
Maak plots van de twee benaderingen tussen t = 0 en t = 1  en laat het verschil in nauwkeurigheid van de twee methoden zien. 

Varieer het aantal stappen n tussen t = 0 en t = 1. Laat voor n = 5,10,20 en 100 zien wat de benadering is van u(1) = e.
"""


def functie(steps=100):
    u = np.zeros([steps + 1])
    v = np.zeros([steps + 1])

    h = 1/steps

    u[0] = 1

    for step in range(steps):
        u[step+1] = u[step] + h * v[step]
        v[step+1] = v[step] + h * u[step]
    return u, v


fig, axes = plt.subplots()

xs = [5, 10, 20, 100]
for x in xs:
    u, v = functie(steps=x)
    plt.plot(u, v)

plt.show()
