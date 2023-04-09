from general.dirac_delta import dirac_delta
from random import randint

def neighbours(n, loc, lattice):
    current_height = len(lattice[loc])-1
    [top, bottom, left, right] = [list(range(n)), list(range(n**2 - n, n**2)), [i*n for i in range(n)], [i*n-1 for i in range(1,n)]]
    edge_locs = top + bottom + left + right
    top_half_locs = list(set(top+left[0:int(n/2)]+right[0:int(n/2)]))
    bottom_half_locs = list(set(bottom+left[int(n/2+1):]+right[int(n/2+1):]))
    if current_height > 1:
        neighbours = [lattice[loc][-2]] #neighbour below
    else:
        neighbours = []
    current_type = lattice[loc][-1]
    if loc not in edge_locs:
    # order is right, left, down, up
        neighbours += [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1][current_height],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1][current_height],
            lattice[(loc + n) % (n ** 2)][current_height], lattice[(loc - n) % (n ** 2)][current_height]]
    elif loc in top_half_locs:
        if loc in top:
            neighbours += [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1][current_height],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1][current_height],
            lattice[(loc + n) % (n ** 2)][current_height], lattice[randint(0, (n**2)/2)][current_height]]
        elif loc in left:
            neighbours += [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1][current_height],
            lattice[randint(0, (n**2)/2)][current_height],
            lattice[(loc + n) % (n ** 2)][current_height], lattice[(loc - n) % (n ** 2)][current_height]]
        else:
            neighbours += [lattice[randint(0, (n**2)/2)][current_height],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1][current_height],
            lattice[(loc + n) % (n ** 2)][current_height], lattice[(loc - n) % (n ** 2)][current_height]]
    elif loc in bottom_half_locs:
        if loc in bottom:
            neighbours += [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1][current_height],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1][current_height],
            lattice[randint((n**2)/2, n**2)][current_height], lattice[(loc - n) % (n ** 2)][current_height]]
        elif loc in left:
            neighbours += [lattice[loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1][current_height],
            lattice[randint((n**2)/2, n**2)][current_height],
            lattice[(loc + n) % (n ** 2)][current_height], lattice[(loc - n) % (n ** 2)][current_height]]
        else:
            neighbours += [lattice[randint((n**2)/2, n**2)][current_height],
            lattice[loc + ((dirac_delta(0, loc % n)) * n) - 1][current_height],
            lattice[(loc + n) % (n ** 2)][current_height], lattice[(loc - n) % (n ** 2)][current_height]]
    [AA, AB] =  [[1 for i in neighbours if i == current_type], [1 for i in neighbours if i != current_type]]
    return [sum(AA), sum(AB), current_type]
