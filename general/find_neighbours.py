from general.dirac_delta import dirac_delta

def find_neighbours(n, loc):
    [top, bottom, left, right] = [list(range(n)), list(range(n**2 - n, n**2)), [i*n for i in range(n)], [i*n-1 for i in range(1,n)]]
    edge_locs = top + bottom + left + right
    if loc not in edge_locs:
        # order is right, left, down, up
        return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            loc + ((dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n ** 2), (loc - n) % (n ** 2)]
    elif loc in top and loc not in left and loc not in right:
        return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            loc + ((dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n ** 2)]
    elif loc in right and loc not in top and loc not in bottom:
        return [loc + ((dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n ** 2), (loc - n) % (n ** 2)]
    elif loc in bottom and loc not in left and loc not in right:
        return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            loc + ((dirac_delta(0, loc % n)) * n) - 1, (loc - n) % (n ** 2)]
    elif loc in left and loc not in top and loc not in bottom:
        return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            (loc + n) % (n ** 2), (loc - n) % (n ** 2)]
    elif loc in top and loc in right:
        return[loc + ((dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n ** 2)]
    elif loc in top and loc in left:
        return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            (loc + n) % (n ** 2)]
    elif loc in bottom and loc in right:
        return [loc + ((dirac_delta(0, loc % n)) * n) - 1, (loc - n) % (n ** 2)]
    elif loc in bottom and loc in left:
        return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1, (loc - n) % (n ** 2)]