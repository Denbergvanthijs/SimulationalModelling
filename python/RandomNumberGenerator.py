import random
import time

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def remove_trailing(number: int):
    """
    Verwijderd de trailing 0 van integers
    https://stackoverflow.com/questions/52908011/better-way-to-remove-trailing-zeros-from-an-integer
    """
    while number % 10 == 0 and number != 0:
        number //= 10
    return number


def generate_seed():
    """Genereerd een willekeurig getal met behulp van de tijd"""
    tijd = time.time()
    seed = round(tijd - int(tijd), 18)  # 0.xxxxxx..., afronden ter voorkomen OverflowError
    seed = int(seed * 10 ** (len(str(seed)) - 2))  # Alle getallen achter de komma, verplaatsen naar voren. str(seed) levert ook '0.' op. Dus -2 voor compensatie
    return seed


def generator(samples=1_000, seed=generate_seed()):
    """Normalisatie = (x - min) / (max - min)
    Gebruiker kan eigen samplesize en seed meegeven
    """
    numbersInt = np.zeros(samples, dtype='int64')
    numbersInt[0] = seed
    print(f"Seed: {seed}, {len(str(seed))}")

    for step in range(samples - 1):
        numbersInt[step + 1] = remove_trailing(int(str(numbersInt[step] ** 2)[-8:]))  # trailing 0 verwijderen, kwadraad van xxx0 zal xx00 opleveren wat uiteindelijk fouten oplevert

    numbersFloat = np.zeros(samples, dtype='float')
    for i, step in enumerate(numbersInt):
        ondergr = int("1" + "0" * (len(str(step)) - 1))
        bovengr = int("9" * len(str(step)))

        numbersFloat[i] = (step - ondergr) / (bovengr - ondergr)

    return numbersFloat


def plot_me(samples=1_000, seed=generate_seed()):
    """
    Plot de eigen generator en een baseline.
    De baseline is de ingebouwde random.uniform() generator.
    """
    generated_vals = generator(samples=samples, seed=seed)
    uniques = len(set(generated_vals))

    baseline = []
    for _ in range(samples):
        baseline.append(random.uniform(0, 1))

    sns.set()
    _, ax = plt.subplots()

    sns.distplot(baseline, bins=10, label=f"Baseline, {len(set(baseline)):_.0f} unieke waardes", kde=False, ax=ax)
    sns.distplot(generated_vals, bins=10, label=f"Eigen generator, {uniques:_.0f} unieke waardes", kde=False, ax=ax)
    ax.axhline(samples//10, label=f"Verwacht, +-{samples//10:_.0f} waardes per kolom", color="black")

    plt.xlim(0, 1)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.ylim(bottom=0)
    plt.title(f"Histogram voor {samples:_.0f} waardes tussen 0 en 1")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    plot_me(samples=10_000)
    # print([(n:=generate_seed(), len(str(n))) for _ in range(10)])
