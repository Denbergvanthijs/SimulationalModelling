import numpy as np
import matplotlib.pylab as plt

"""
Onderstaande code is een aanpassing van de Udacity Course 'Differential Equations in action'
"""


def backward_euler(pop, eStart, iStart, rStart, h=0.5, transm_coeff=5e-9, lat_time=1, infec_time=5, end_time=60):
    """Verplichtte input: Start populatie en de startpopulaties van e, i en r"""
    steps = int(end_time / h)
    times = h * np.arange(steps + 1)

    s = np.zeros(steps + 1)
    e = np.zeros(steps + 1)
    i = np.zeros(steps + 1)
    r = np.zeros(steps + 1)

    s[0] = pop - rStart - iStart
    e[0] = eStart
    i[0] = iStart
    r[0] = rStart

    for step in range(steps):
        p = ((1 + h / infec_time) / (h * transm_coeff) + i[step]) / (h / lat_time) - (s[step] + e[step]) / (1 + h / lat_time)
        q = -((1 + h / infec_time) / (h * transm_coeff) * e[step] + (s[step] + e[step]) * i[step]) / ((1 + h / lat_time) * (h / lat_time))

        e[step + 1] = -0.5 * p + (0.25 * p ** 2 - q) ** 0.5
        i[step + 1] = (i[step] + h / lat_time * e[step + 1]) / (1 + h / infec_time)
        s[step + 1] = s[step] / (1 + h * transm_coeff * i[step + 1])
        r[step + 1] = r[step] + h / infec_time * i[step + 1]

    return s, e, i, r, times


def plot_me(pop, e, i, r, h=0.5, transm_coeff=5e-9, lat_time=1, infec_time=5, end_time=60):
    """Verplichtte input: Start populatie en de startpopulaties van e, i en r"""
    sArr, eArr, iArr, rArr, x = backward_euler(pop, e, i, r, h=h, transm_coeff=transm_coeff, lat_time=lat_time, infec_time=infec_time, end_time=end_time)

    plt.plot(x, sArr, label="S")
    plt.plot(x, eArr, label="E")
    plt.plot(x, iArr, label="I")
    plt.plot(x, rArr, label="R")

    plt.title("SEIR-model met correctie voor stiffness")
    plt.xlabel('Tijd in dagen')
    plt.ylabel('Aantal personen')
    plt.xlim(0, end_time)
    plt.ylim(0, pop)
    # plt.yscale("log")
    plt.legend()
    plt.show()


# plot_me(1e8, 0, 1e5, 1e6, end_time=120)  # Standaard waardes van Udacity
# Studentnummer: 1740697
# Totale populatie:                 97 mil.
# Gem. contacten per dag:           6
# Kans op infectie per contact:     4

populatie = 9.7e7
coeff = 0.04 / populatie * 6
infec_time = 5
herd = populatie - ((1/infec_time) / coeff)

print(f"Transmissie coëfficiënt: {coeff:0.2e}")
print(f"Herd Immunity: {herd:_.0f} mensen of {(herd / populatie)*100:.2f}% van de populatie")

plot_me(populatie, 0, 1e5, 1e6, transm_coeff=coeff, lat_time=2, end_time=300, h=1)
