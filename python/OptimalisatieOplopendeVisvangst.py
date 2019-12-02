import matplotlib.pylab as plt
import numpy


def total_harvest(maximum_growth_rate=0.5, carrying_capacity=2e6, maximum_harvest_rate=0.8 * 2.5e5, end_time=10, h=0.1):
    num_steps = int(end_time / h)

    fish = numpy.zeros(num_steps + 1)  # tons
    fish[0] = 2e5

    results = []

    for ramp_start in numpy.arange(0., 10.01, 0.5):  # 10.01 to prevent issues with roundoff errors
        for ramp_end in numpy.arange(ramp_start, 10.01, 0.5):  # 10.01 to prevent issues with roundoff errors
            total_harvest = 0
            is_extinct = False
            for step in range(num_steps):
                time = h * step  # years
                harvest_factor = 0.0

                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)

                harvest_rate = harvest_factor * maximum_harvest_rate

                if is_extinct:
                    current_harvest = 0.
                    fish_next_step = 0.
                else:
                    current_harvest = h * harvest_rate
                    fish_next_step = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)

                    if fish_next_step <= 0.:
                        is_extinct = True
                        current_harvest = fish[step]
                        fish_next_step = 0.

                fish[step + 1] = fish_next_step
                total_harvest += current_harvest

            results.append([ramp_start, ramp_end, total_harvest])
    return results


results = total_harvest()


def plot_me():
    print([(r[0], r[1], r[2]) for r in results if r[2] == max([r[2] for r in results])])

    plt.scatter([r[0] for r in results], [r[1] for r in results], [5e-11 * r[2] ** 2. for r in results], edgecolor='none')
    plt.xlabel('Ramp start in years')
    plt.ylabel('Ramp end in years')
    plt.show()


plot_me()
