from random import uniform, randint
from math import e
from general.neighbours import neighbours
k = 1.380649*(10**(-23))


def take_step(n, lattice, deltaMu, T, AA, AB):
    loc = randint(0, (n ** 2)-1)
    [no_AA, no_AB, current_type] = neighbours(n, loc, lattice)
    attach_prob = e ** (deltaMu)
    detach_prob = e ** ((6*AA-(no_AA*AA+no_AB*AB)))
    z1 = uniform(0,1) # decide which process, attachment or detachment
    if z1 < attach_prob/(attach_prob+detach_prob):
        z2 = uniform(0,1) # decide which attachment will occur, AA or AB
        if z2 < AA/(AA+AB):
            lattice[loc].append(current_type)
        else:
            lattice[loc].append((current_type-1)*(-1))
    elif z1 >= attach_prob/(attach_prob+detach_prob) and len(lattice[loc]) > 1:
        z3 = uniform(0,1)
        if z3 < (e ** ((6*AA-(no_AA*AA+no_AB*AB)))/(e ** ((6*AA-(AB))))):
            lattice[loc].pop()
    
    return lattice
