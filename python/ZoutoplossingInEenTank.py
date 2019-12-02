import matplotlib.pylab as plt
import numpy as np


def tank(ts=120, liters=1000, litersIn=6, litersUit=6, concGroei=0.1):
    c = 0
    conc = [c:= c + (litersIn * concGroei / liters) - (litersUit / liters * c) for _ in range(ts + 1)]
    return conc, np.arange(ts + 1)


def plotMe(ts, liters, litersIn, litersUit, concGroei):
    conc, tsArr = tank(ts=ts, liters=liters, litersIn=litersIn, litersUit=litersUit, concGroei=concGroei)
    plt.plot(tsArr, conc, label=f"In={litersIn} Uit={litersUit} Groei={concGroei}")

    plt.xlim(0, ts)
    plt.ylim(bottom=0)
    plt.title(f"Concentratie in kg/L in tank van {liters} liters")
    plt.xlabel("Aantal stappen")
    plt.ylabel("Concentratie in kg/L")
    plt.legend()
    plt.tight_layout()


plotMe(1200, 1000, 6, 5, 0.1)
plotMe(1200, 1000, 6, 6, 0.1)

plt.show()
