import matplotlib.pylab as plt
import numpy as np


def tanks(ts, liters, inL=6, uitL=4, uitR=3, uitR2=2, inR=1, cL=0.2, cR=0.1, kgL=0, kgR=20):
    assert inL + inR == uitL + uitR, "Geen evenwicht! Meer in/uit dan in/uit"

    tank1 = np.zeros(ts + 1)
    tank2 = np.zeros(ts + 1)

    tank1[0] = kgL / liters  # Startconcentratie in kg/l
    tank2[0] = kgR / liters  # Startconcentratie in kg/l

    for step in range(ts):
        tank1[step + 1] = tank1[step] + (inL * cL / liters) + (inR * tank2[step] / liters) - (uitL / liters * tank1[step]) - (uitR / liters * tank1[step])
        tank2[step + 1] = tank2[step] + (uitR / liters * tank1[step]) - (inR * tank2[step] / liters) - (uitR2 / liters * tank2[step])

    return tank1, tank2, np.arange(ts + 1)


def plotMe(ts, liters, **kwargs):
    tank1, tank2, tsArr = tanks(ts, liters, **kwargs)
    plt.plot(tsArr, tank1, label=f"Tank 1; Eindconc: {tank1[-1]:.2f}")
    plt.plot(tsArr, tank2, label=f"Tank 2; Eindconc: {tank2[-1]:.2f}")

    plt.xlim(0, ts)
    plt.ylim(bottom=0)
    plt.title(f"Concentratie in kg/L in twee tanks van {liters} liters")
    plt.xlabel("Aantal stappen")
    plt.ylabel("Concentratie in kg/L")
    plt.legend(loc="lower right")
    plt.tight_layout()


plotMe(250, 100)
plt.show()
