import matplotlib.pyplot as plt
from simulation.run_simulation import run_simulation
from statistics import mean, stdev
from general.find_layer_sums import find_layer_sums

def make_plot_ratio(n, deltaMu, AA, ratio_start, ratio_end, ratio_step, T, time, repeats):
    results = []
    errors = []
    ratios = [((x*ratio_step)+ratio_start) for x in range(int(((ratio_end-ratio_start)/ratio_step)+1))]
    ABs = [AA*x for x in ratios]
    for i in ABs:
        temp = []
        for p in range(repeats):
            x = run_simulation(n, deltaMu, AA, i, T, time)
            temp.append(x[0])
            print(i, p)
        results.append(mean(temp))
        errors.append(stdev(temp))
    ymin = min(results)
    ymax = max(results)+max(errors)
    plt.errorbar(ratios, results, errors, marker='.')
    plt.title(r"Strength of A-A is "+str(AA)+r"/(kT)")
    plt.xlabel('Ratio of A-A strength to A-B strength')
    plt.ylabel('Strength of A-B overlap')
    plt.xlim(0, ratios[-1])
    plt.ylim(ymin, 1.05*ymax)
    plt.legend()

    plt.show()

