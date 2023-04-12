from math import floor

def pos_to_coords(n, loc):
    y_coord_not = floor(loc/n)
    x_coord = loc%n
    return [(y_coord_not-n+1)*(-1), x_coord]