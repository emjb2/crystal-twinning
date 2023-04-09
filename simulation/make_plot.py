from simulation.run_simulation import run_simulation
from statistics import mean, stdev
import matplotlib.pyplot as plt

def make_plot(n, deltaMus, AA, AB, T, time, repeats):
    results = []
    errors = []
    for i in deltaMus:
        temp = []
        for p in range(repeats):
            temp.append(run_simulation(n, i, AA, AB, T, time))
            print(i, p)
        results.append(mean(temp))
        errors.append(stdev(temp))
    ymin = min(results)
    ymax = max(results)+max(errors)
    plt.errorbar(deltaMus, results, errors, marker='.')
    plt.title("Test")
    plt.xlabel('$\Delta$$\mu$ in multiples of $kT$')
    plt.ylabel('Strenght of A-B overlap')
    plt.xlim(0, deltaMus[-1])
    plt.ylim(ymin, 1.05*ymax)
    plt.legend()
    plt.show()
