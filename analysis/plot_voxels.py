import numpy as np
import matplotlib.pyplot as plt
from general.pos_to_coords import pos_to_coords
from math import floor

def plot_voxels(n, lattice):
    coordinates = np.zeros((n, n, max([len(x) for x in lattice])))
    colours = np.zeros((n, n, max([len(x) for x in lattice]), 4))
    for x in range(len(lattice)):
        for i in range(len(lattice[x])):
            [[y_coord, x_coord], z_coord] = [pos_to_coords(n, x), i]
            coordinates[x_coord, y_coord, z_coord] = 1
            if lattice[x][i] == 1:
                colours[x_coord, y_coord, z_coord, 0] = 1
                colours[x_coord, y_coord, z_coord, 1] = 0
                colours[x_coord, y_coord, z_coord, 2] = 0
                colours[x_coord, y_coord, z_coord, 3] = 0.6
            else:
                colours[x_coord, y_coord, z_coord, 0] = 0
                colours[x_coord, y_coord, z_coord, 1] = 0
                colours[x_coord, y_coord, z_coord, 2] = 1
                colours[x_coord, y_coord, z_coord, 3] = 0.6

    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(coordinates, facecolors = colours)
    ax.set_box_aspect([1, 1, max([len(x) for x in lattice])/n])    
    ax.set_ylim3d(0, n)
    ax.set_xlim3d(0, n)
    ax.set_zlim3d(0, max([len(x) for x in lattice]))
    plt.show()
    
    
