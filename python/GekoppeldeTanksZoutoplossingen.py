import matplotlib.pylab as plt
import numpy as np


def tanks(ts=120, liters=100, inL=6, uitL=4, uitR=3, inR=1, cL=0.2, cR=0.1):
    assert inL + inR == uitL + uitR, "Geen evenwicht! Meer in/uit dan in/uit"
    
    tank1 = np.zeros(ts + 1)
    tank2 = np.zeros(ts + 1)
    
    tank1[0] = 0  # Startconcentratie in kg/l
    tank2[0] = 20 / liters  # Startconcentratie in kg/l

    for step in range(ts):
        tank1[step + 1] = tank1[step] + (inL * cL / liters) + (inR * tank2[step] / liters) - (uitL / liters * tank1[step]) - (uitR / liters * tank1[step])
        tank2[step + 1] = tank2[step] + (uitR / liters * tank1[step]) - (inR * tank2[step] / liters) - (2 / liters * tank2[step])

    return tank1, tank2, np.arange(ts + 1)


def plotMe(ts=120, liters=100, inL=6, uitL=4, uitR=3, inR=1, cL=0.2, cR=0.1):
    tank1, tank2, tsArr = tanks(ts=ts, liters=liters, inL=inL, uitL=uitL, uitR=uitR, inR=inR, cL=cL, cR=cR)
    plt.plot(tsArr, tank1, label="Tank 1")
    plt.plot(tsArr, tank2, label="Tank 2")

    plt.xlim(0, ts)
    plt.ylim(bottom=0)
    plt.title(f"Concentratie in kg/L in tank van {liters} liters")
    plt.xlabel("Aantal stappen")
    plt.ylabel("Concentratie in kg/L")
    plt.legend()
    plt.tight_layout()


plotMe(200, 100)

plt.show()
