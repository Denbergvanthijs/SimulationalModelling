import math

import numpy as np
from numpy.linalg import norm
import matplotlib.pylab as plt

"""
Onderstaande code is een aanpassing van de Udacity Course
Gebruik zowel forward Euler-integratie als Heun-integratie om de vergelijking u' (t) = u(t) (met beginconditie u(0) = 1) op te lossen. 
Maak plots van de twee benaderingen tussen t = 0 en t = 1  en laat het verschil in nauwkeurigheid van de twee methoden zien. 

Varieer het aantal stappen n tussen t = 0 en t = 1. Laat voor n = 5,10,20 en 100 zien wat de benadering is van u(1) = e.
"""


def heun(steps=100):
    u = np.zeros([steps + 1])
    e = np.zeros([steps + 1])

    h = 1/steps
    t = list(np.arange(0, 1+h, step=h))

    u[0] = 1
    e[0] = math.e ** 0

    for step in range(steps):
        u[step + 1] = u[step] + h * u[step]  # Euler
        u[step + 1] = u[step] + h * ((u[step] + u[step + 1])/2)  # Heun
        e[step + 1] = math.e ** t[step]  # e^t

    return t, u, e


fig, axes = plt.subplots()

xs = [5, 10, 20, 100]  # Gevraagd aantal steps volgens opdracht
for x in xs:
    t, u, e = heun(steps=x)
    plt.plot(t, u, label=f"n = {x}\nu(1) = {u[-1]:.3f}")

plt.plot(t, e, color='black', label=f"u(t) = e^t\nu(1) = {math.e:0.3f}")
plt.axhline(y=math.e, color='black', linestyle='--')
plt.xlim(0, 1)
plt.ylim(1, 3)
plt.title("Hogere Orde Benadering: Heun\n Naarmate de stepsize kleiner wordt, nadert de lijn e^t")
plt.xlabel("t (per 1)/n\nwaarbij n = aantal steps")
plt.ylabel("u(t) voor n-aantal steps")
plt.legend()
plt.tight_layout()
plt.show()
