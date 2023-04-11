from simulation.make_plot_deltamu import make_plot_deltamu
from simulation.run_simulation import run_simulation
from simulation.make_plot_ratio import make_plot_ratio
from simulation.make_plot_timesteps import make_plot_timesteps

if __name__ == "__main__":
    # note that we found that as of a supersaturation of 5 we don't have changes in
    # wrong placements anymore, with tiny errorbars, so we'll stick with 5.
    #make_plot_deltamu(30, [0,5,10], 1, 0.1, 290, 50000, 7)
    #x = run_simulation(30, 7, 1, 0.1, 290, 50000)
    #print(x[1], x[2])
    #make_plot_ratio(30, 5, [1, 2, 3, 4], 0, 0.5, 0.05, 290, 100000, 3)
    run_simulation(30, 5, 1, 0.000001, 290, 10000)
    # this is timestep calibration 1: make_plot_timesteps(30, 5, 2, 0, 0.5, 0.05, 290, [1000, 10000, 50000, 100000, 500000], 1)
