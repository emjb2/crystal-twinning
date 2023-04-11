from simulation.make_plot_deltamu import make_plot_deltamu
from simulation.run_simulation import run_simulation
from simulation.make_plot_ratio import make_plot_ratio

if __name__ == "__main__":
    # note that we found that as of a supersaturation of 5 we don't have changes in
    # wrong placements anymore, with tiny errorbars, so we'll stick with 5.
    #make_plot_deltamu(30, [0,5,10], 1, 0.1, 290, 50000, 7)
    #x = run_simulation(30, 7, 1, 0.1, 290, 50000)
    #print(x[1], x[2])
    make_plot_ratio(30, 5, 1, 0, 1, 0.05, 290, 50000, 5)
    #run_simulation(30, 5, 1, 0.000001, 290, 10000)
