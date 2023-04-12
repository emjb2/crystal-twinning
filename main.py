from simulation.make_plot_deltamu import make_plot_deltamu
from simulation.run_simulation import run_simulation
from simulation.make_plot_ratio import make_plot_ratio
from simulation.make_plot_timesteps import make_plot_timesteps
from analysis.plot_voxels import plot_voxels

if __name__ == "__main__":
    #make_plot_deltamu(30, [0,5,10], 1, 0.1, 290, 50000, 7)
    #x = run_simulation(30, 7, 1, 0.1, 290, 50000)
    make_plot_ratio(30, 1, [1], 0, 0.1, 0.005, 290, 10000, 3)
    #run_simulation(30, 4, 0.5, 0.05, 290, 20000)
