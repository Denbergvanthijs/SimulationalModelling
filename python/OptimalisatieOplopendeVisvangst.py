import matplotlib.pylab as plt
import numpy as np


def total_harvest(max_growth_rate=0.5, carrying_cap=2e6, MSY=0.8, end_time=10, t=0.1, vangst_start=0):
    max_harv_rate = MSY * 2.5e5
    ts = int(end_time / t)

    fish = np.zeros(ts + 1)
    fish[0] = 2e5
    results = []

    for ramp_start in np.arange(0, end_time+0.01, 0.5):
        for ramp_end in np.arange(ramp_start, end_time+0.01, 0.5):
            total_harvest = 0
            is_extinct = False

            for step in range(ts):
                time = step * t  # years
                harvest_factor = 0.0

                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)

                if ramp_start < vangst_start:
                    harvest_factor = 0.0

                harvest_rate = harvest_factor * max_harv_rate

                if is_extinct:
                    current_harvest = 0
                    fish_next_step = 0
                else:
                    current_harvest = t * harvest_rate
                    fish_next_step = fish[step] + t * (max_growth_rate * (1. - fish[step] / carrying_cap) * fish[step] - harvest_rate)

                    if fish_next_step <= 0:
                        current_harvest = fish[step]
                        is_extinct = True
                        fish_next_step = 0

                fish[step + 1] = fish_next_step
                total_harvest += current_harvest

            results.append([ramp_start, ramp_end, total_harvest])
    return results


def plot_me(**kwargs):
    results = total_harvest(**kwargs)

    print([(r[0], r[1], r[2]) for r in results if r[2] == max([r[2] for r in results])])  # Max harvest
    plt.scatter([r[0] for r in results], [r[1] for r in results], [5e-11 * r[2] ** 2. for r in results], edgecolor='none')
    plt.xlabel('Ramp start in years')
    plt.ylabel('Ramp end in years')
    plt.show()


plot_me(MSY=0.7, vangst_start=2)
