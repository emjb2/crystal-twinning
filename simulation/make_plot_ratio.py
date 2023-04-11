import matplotlib.pyplot as plt
from simulation.run_simulation import run_simulation
from statistics import mean, stdev
from general.find_layer_sums import find_layer_sums

def make_plot_ratio(n, deltaMu, AAs, ratio_start, ratio_end, ratio_step, T, time, repeats):
    results = [[]] * len(AAs)
    errors = [[]] * len(AAs)
    ratios = [((x*ratio_step)+ratio_start) for x in range(int(((ratio_end-ratio_start)/ratio_step)+1))]
    def AB_list(AA):
        return [AA*x for x in ratios]
    for k in range(len(AAs)):
        ABs = AB_list(AAs[k])
        for i in ABs:
            temp = []
            for p in range(repeats):
                x = run_simulation(n, deltaMu, AAs[k], i, T, time)
                temp.append(x[0])
                #(i, p)
            results[k] = results[k] + [mean(temp)]
            errors[k] = errors[k] + [stdev(temp)]
            print("AA strength: "+str(AAs[k])+"   AB strength: "+str(i)+"  Repeat: "+str(p))
    ymin = min([min(x) for x in results])
    ymax = max([max(x) for x in results])+max([max(x) for x in errors])
    colours = ['midnightblue', 'lightskyblue', 'gold', 'mediumvioletred', 'forestgreen', 'black']
    for i in range(len(AAs)):
        plt.errorbar(ratios, results[i], errors[i], marker='.', color = colours[i], label=r"$E_{AA}$ bond strength: "+str(AAs[i])+"kT")
    plt.xlabel('Ratio of A-A strength to A-B strength')
    plt.ylabel('Proportio of type A molecules in final crystal')
    plt.xlim(0, ratios[-1])
    plt.ylim(ymin, 1.05*ymax)
    plt.legend()

    plt.show()

