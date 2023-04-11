import matplotlib.pyplot as plt
from simulation.run_simulation import run_simulation
from statistics import mean, stdev
from general.find_layer_sums import find_layer_sums

def make_plot_timesteps(ns, deltaMu, AA, ratio_start, ratio_end, ratio_step, T, time, repeats):
    results = [[]] * len(ns)
#    errors = [[]] * len(ns)
    ratios = [((x*ratio_step)+ratio_start) for x in range(int(((ratio_end-ratio_start)/ratio_step)+1))]
    def AB_list(AA):
        return [AA*x for x in ratios]
    ABs = AB_list(AA)
    for k in range(len(ns)):
        for i in ABs:
            temp = []
            for p in range(repeats):
                x = run_simulation(ns[k], deltaMu, AA, i, T, time)
                temp.append(x[0])
            results[k] = results[k] + [mean(temp)]
#            errors[k] = errors[k] + [stdev(temp)]
            print("AA strength: "+str(AA)+"   AB strength: "+str(i)+"  Repeat: "+str(p))
    ymin = min([min(x) for x in results])
#    ymax = max([max(x) for x in results])+max([max(x) for x in errors])
    ymax = max([max(x) for x in results])*1.05
    colours = ['midnightblue', 'lightskyblue', 'gold', 'mediumvioletred', 'forestgreen', 'black']
    for i in range(len(ns)):
#        plt.errorbar(ratios, results[i], errors[i], marker='.', color = colours[i], label="Time steps: "+str(times[i]))
        plt.errorbar(ratios, results[i], marker='.', color = colours[i], label="Lattice size: "+str(ns[i])+" by "+str(ns[i]))    
    plt.xlabel('Ratio of A-A strength to A-B strength')
    plt.ylabel('Proportion of type A molecules in final crystal')
    plt.xlim(0, ratios[-1])
    plt.ylim(ymin, 1.05*ymax)
    plt.legend()

    plt.show()

