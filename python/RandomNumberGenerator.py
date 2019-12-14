import time
import random

import matplotlib.pyplot as plt
import seaborn as sns
from psutil import virtual_memory
import numpy as np


def generator(samples=1_000):
    """
    Random getal genereren door tijd, in ns achter de komma, te normaliseren tussen 0 en 1
    Cijfers achter de comma worden van rechts naar links gesliced voor betere willekeur

    Normalisatie = (x - min) / (max - min)
    Waarbij: min = 0
             max = aantal cijfers achter de komma

    Stel: 4 cijfers achter de komma
    Dan:  max = 9999
    """
    tijd = time.time()

    tijd_ns = str(tijd - int(tijd))  # 0.xxxxxx...
    startwaarde = int(float(tijd_ns[2:]))  # 0. strippen, getal 8 lang maken

    lijstInt = np.zeros(samples, dtype='int64')
    lijstInt[0] = startwaarde
    print(f"Startwaarde: {lijstInt[0]}")

    for step in range(samples - 1):
        lijstInt[step + 1] = str(lijstInt[step] ** 2)[-8:]

    lijstFloat = [x / int("9" * len(str(x))) for x in lijstInt]  # Normalisatie
    return lijstFloat


def plot_me(samples=1_000):
    generated_vals = generator(samples=samples)

    baseline = []
    for x in range(samples):
        baseline.append(random.uniform(0, 1))

    sns.set()
    sns.distplot(baseline, bins=10, label=f"Baseline, {len(set(baseline)):_.0f} unieke waardes", kde=False)
    sns.distplot(generated_vals, bins=10, label=f"Eigen generator, {len(set(generated_vals)):_.0f} unieke waardes", kde=False)

    plt.xlim(0, 1)
    plt.ylim(bottom=0)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.title(f"Histogram voor {samples:_.0f} waardes tussen 0 en 1")

    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    plot_me(samples=10000)
