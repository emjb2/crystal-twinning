from general.dirac_delta import dirac_delta
from random import randint

def neighbours(n, loc, lattice):
    current_height = len(lattice[loc])-1
    [top, bottom, left, right] = [list(range(n)), list(range(n**2 - n, n**2)), [i*n for i in range(n)], [i*n-1 for i in range(1,n)]]
    edge_locs = top + bottom + left + right
    corners = [0, n-1, n**2-1, n**2-n]
    top_half_locs = list(set(top+left[0:int(n/2)]+right[0:int(n/2)]))
    bottom_half_locs = list(set(bottom+left[int(n/2+1):]+right[int(n/2+1):]))
    if current_height >= 1:
        neighbours = [lattice[loc][-2]] #neighbour below
    else:
        neighbours = []
    current_type = lattice[loc][-1]
    if loc not in edge_locs:
    # order is right, left, down, up
        neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[(loc + n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
        neighbour_heights = [len(x) for x in neighbour_stacks]
        neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]
    elif loc in top_half_locs and loc not in corners:
        if loc in top:
            neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[(loc + n) % (n ** 2)], lattice[(loc + n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]    
        elif loc in left:
            neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1], lattice[(loc + n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            tall_stacks = [neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]    
        else:
            neighbour_stacks = [lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[(loc + n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]
    elif loc in bottom_half_locs and loc not in corners:
        if loc in bottom:
            neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[(loc - n) % (n ** 2)], 
            lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]    
        elif loc in left:
            neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[(loc + n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]    
        else:
            neighbour_stacks = [lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
            lattice[(loc + n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]
    elif loc in corners:
        if loc == 0:
            # order is right, left, down, up
            neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
                lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
                lattice[(loc + n) % (n ** 2)], lattice[(loc + n) % (n ** 2)],]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]
        elif loc == n-1:
            neighbour_stacks = [lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
                lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
                lattice[(loc + n) % (n ** 2)], lattice[(loc + n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]
        elif loc == n**2-1:
            neighbour_stacks = [lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
                lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1],
                lattice[(loc - n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]
        else:
            neighbour_stacks = [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1],
            lattice[(loc - n) % (n ** 2)], lattice[(loc - n) % (n ** 2)]]
            neighbour_heights = [len(x) for x in neighbour_stacks]
            neighbours += [neighbour_stacks[x][current_height] for x in range(4) if neighbour_heights[x] > current_height]

    [AA, AB] =  [[1 for i in neighbours if i == current_type], [1 for i in neighbours if i != current_type]]
    return [sum(AA), sum(AB), current_type]
