from general.find_neighbours import find_neighbours
from general.neighbours import neighbours

def migration_options(n, loc, lattice, AA, AB):
    corners = [0, n**2-1, n**2-n, n-1]
    edge_not_corner = [x for x in list(set(list(range(n)) + list(range(n**2 - n, n**2)) + [i*n for i in range(n)] + [i*n-1 for i in range(1,n)])) if x not in corners]
    needs_extra = 0
    if loc in corners:
        needs_extra += 2
    elif loc in edge_not_corner:
        needs_extra += 1
    neighbour_stacks_possible = find_neighbours(n, loc)
    neighbour_stacks = [x for x in neighbour_stacks_possible if len(lattice[x]) <= len(lattice[loc])]
    current_type = lattice[loc][-1]
    neighbour_bonds = []
    neighbour_energies = []
    for i in neighbour_stacks:
        suggested_lattice = lattice.copy()
        suggested_lattice[loc] = suggested_lattice[loc][:-1]
        suggested_lattice[i] = suggested_lattice[i] + [current_type]
        neighbour_bonds.append(neighbours(n, i, lattice))
        neighbour_energies.append(neighbour_bonds[-1][0]*AA+neighbour_bonds[-1][1]*AB)
    
    return [neighbour_stacks, neighbour_energies, needs_extra]



