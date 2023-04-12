import numpy as np
import matplotlib.pyplot as plt
from general.pos_to_coords import pos_to_coords
from math import floor

def plot_voxels(n, lattice):
    #limit = int(floor((max([len(x) for x in lattice])-min([len(x) for x in lattice]))/2+min([len(x) for x in lattice])))
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

            #yd = (x_coord<x<x_coord+1) & (y_coord<y<y_coord+1) & (i<z<i+1)
            #cube_list = cube_list + [[(x_coord<x<x_coord+1) & (y_coord<y<y_coord+1) & (i<z<i+1)]]
            #if lattice[x][i] == 1:
            #    cube_colours = cube_colours + ['red']
            #else:
            #    cube_colours = cube_colours + ['blue']

    #colors = np.empty(cubes.shape, dtype=object)
    #for x in range(len(cube_list)):
    #    colors[cube_list[x][0]] = cube_colours[x]
    #ax = plt.figure().add_subplot(projection = '3d')
    #ax.voxels(cubes, facecolors = colors, edgecolor = 'k')
    #plt.show()
    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(coordinates, facecolors = colours)
    ax.set_box_aspect([1, 1, max([len(x) for x in lattice])/n])    
    ax.set_ylim3d(0, n)
    ax.set_xlim3d(0, n)
    ax.set_zlim3d(0, max([len(x) for x in lattice]))
    plt.show()
    
    
