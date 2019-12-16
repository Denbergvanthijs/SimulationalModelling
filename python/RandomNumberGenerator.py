import random
import time

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# from psutil import virtual_memory


def remove_trailing(number: int):
    """
    Verwijderd de trailing 0 van integers
    https://stackoverflow.com/questions/52908011/better-way-to-remove-trailing-zeros-from-an-integer
    """
    while number % 10 == 0:
        number //= 10
    return number


def generate_seed():
    tijd = time.time()
    seed = round(tijd - int(tijd), 18)  # 0.xxxxxx..., afronden ter voorkomen OverflowError
    seed = int(seed * 10 ** (len(str(seed)) - 2))  # Alle getallen achter de komma, verplaatsen naar voren. str(seed) levert ook '0.' op. Dus -2 voor compensatie
    return seed


def generator(samples=1_000, seed=generate_seed()):
    """
    Normalisatie = (x - min) / (max - min)
    Waarbij: min = 0
             max = aantal cijfers achter de komma

    Stel: 4 cijfers achter de komma
    Dan:  max = 9999
    """
    lijstInt = np.zeros(samples, dtype='int64')
    lijstInt[0] = seed
    print(f"Seed: {seed}, {len(str(seed))}")

    for step in range(samples - 1):
        lijstInt[step + 1] = remove_trailing(int(str(lijstInt[step] ** 2)[-8:]))  # trailing 0 verwijderen, kwadraad van xxx0 zal xx00 opleveren wat uiteindelijk fouten oplevert

    lijstFloat = [(x - int("1" + "0" * (len(str(x))-1))) / (int("9" * len(str(x))) - int("1" + "0" * (len(str(x))-1))) for x in lijstInt]  # Normalisatie
    return lijstFloat


def plot_me(samples=1_000):
    generated_vals = generator(samples=samples)
    uniques = len(set(generated_vals))

    baseline = []
    for _ in range(samples):
        baseline.append(random.uniform(0, 1))

    sns.set()
    _, ax = plt.subplots()

    sns.distplot(baseline, bins=10, label=f"Baseline, {len(set(baseline)):_.0f} unieke waardes", kde=False, ax=ax)
    sns.distplot(generated_vals, bins=10, label=f"Eigen generator, {uniques:_.0f} unieke waardes", kde=False, ax=ax)
    ax.axhline(samples//10, label="Verwachtte waarde voor iedere kolom")

    # plt.xlim(0, 1)
    # plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.ylim(bottom=0)
    plt.title(f"Histogram voor {samples:_.0f} waardes tussen 0 en 1")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    plot_me(samples=10_000)
    # print([(n:=generate_seed(), len(str(n))) for _ in range(10)])
