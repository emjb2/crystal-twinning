from random import uniform, randint
from math import e
from general.neighbours import neighbours
k = 1.380649*(10**(-23))


def take_step(n, lattice, deltaMu, T, AA, AB):
    initial_sum = sum([len(x) for x in lattice])
    loc = randint(0, (n ** 2)-1)
    [no_AA, no_AB, current_type] = neighbours(n, loc, lattice)
    attach_prob = e ** (deltaMu)
    detach_prob = e ** ((6*AA-(no_AA*AA+no_AB*AB)))
    z1 = uniform(0,1) # decide which process, attachment or detachment
    if z1 < attach_prob/(attach_prob+detach_prob):
        suggested_lattice = lattice.copy()
        suggested_lattice[loc] = suggested_lattice[loc] + [0]
        [if_0_no_00, if_0_no_01, new_type_0] = neighbours(n, loc, suggested_lattice)
        [if_1_no_11, if_1_no_01] = [if_0_no_01, if_0_no_00]
        z2 = uniform(0,1) # decide which attachment will occur, AA or AB
        if z2 < (if_0_no_00*AA+if_0_no_01*AB)/(if_0_no_00*AA+if_0_no_01*AB+if_1_no_11*AA+if_1_no_01*AB):
            lattice[loc] = lattice[loc] + [0]

        else:
            lattice[loc] = lattice[loc] + [1]

    elif z1 >= attach_prob/(attach_prob+detach_prob) and len(lattice[loc]) > 1:
        #z3 = uniform(0,1)
        #if z3 < (e ** ((6*AA-(no_AA*AA+no_AB*AB)))/(e ** ((6*AA-(AB))))):
        lattice[loc] = lattice[loc][0:-1]

    #print("Change: "+str(sum([len(x) for x in lattice])-initial_sum))

    return lattice
