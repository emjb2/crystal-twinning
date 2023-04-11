from random import uniform, randint
from math import e
from general.neighbours import neighbours
from general.migration_options import migration_options
from statistics import mean
from random import choices
k = 1.380649*(10**(-23))


def take_step(n, lattice, deltaMu, T, AA, AB):
    initial_sum = sum([len(x) for x in lattice])
    loc = randint(0, (n ** 2)-1)
    [no_AA, no_AB, current_type] = neighbours(n, loc, lattice)
    attach_prob = e ** (deltaMu)
    detach_prob = e ** ((6*AA-(no_AA*AA+no_AB*AB)))
    migration_prob = e ** (6*AA-(no_AA*AA+no_AB*AB)+AA/2)
    z1 = uniform(0,1) # decide which process, attachment or detachment
    if z1 < attach_prob/(attach_prob+detach_prob+migration_prob):
        suggested_lattice = lattice.copy()
        suggested_lattice[loc] = suggested_lattice[loc] + [0]
        [if_0_no_00, if_0_no_01, new_type_0] = neighbours(n, loc, suggested_lattice)
        [if_1_no_11, if_1_no_01] = [if_0_no_01, if_0_no_00]
        z2 = uniform(0,1) # decide which attachment will occur, AA or AB
        if z2 < (if_0_no_00*AA+if_0_no_01*AB)/(if_0_no_00*AA+if_0_no_01*AB+if_1_no_11*AA+if_1_no_01*AB):
            lattice[loc] = lattice[loc] + [0]
        else:
            lattice[loc] = lattice[loc] + [1]
    elif attach_prob/(attach_prob+detach_prob+migration_prob)  <= z1 <= (attach_prob+detach_prob)/(attach_prob+detach_prob+migration_prob) and len(lattice[loc]) > 1:
        #z3 = uniform(0,1)
        #if z3 < (e ** ((6*AA-(no_AA*AA+no_AB*AB)))/(e ** ((6*AA-(AB))))):
        lattice[loc] = lattice[loc][0:-1]

    else:
        if len(lattice[loc]) > 1:
            [AAs, ABs, current_type] = neighbours(n, loc, lattice)
            current_energy = AAs*AA+ABs*AB
            [options, option_energies, needs_extra] = migration_options(n, loc, lattice, AA, AB)
            if needs_extra == 1:
                if len(options) > 0:
                    option_energies = option_energies + [mean(options)]
                else:
                    option_energies = option_energies + [1.5*AA+1.5*AB]
                options = options + ["out"]
            elif needs_extra == 2:
                if len(options) > 0:
                    x = mean(option_energies)
                else:
                    x = 1.5*AA+1.5*AB
                option_energies = option_energies + [x, x]
                options = options + ["out", "out"]
            if len(options) > 0:
                if option_energies == [0.0]:
                    print(options, needs_extra)
                    option_energies = [1]
                move = choices(range(len(options)), option_energies, k=1)[0]
                z3 = uniform(0, 1)
                if z3 < option_energies[move]/(option_energies[move]+current_energy):
                    if type(options[move]) == int:
                        lattice[options[move]] = lattice[options[move]] + [current_type]
                        lattice[loc] = lattice[loc][:-1]
                    else:
                        lattice[loc] = lattice[loc][:-1]


    #print("Change: "+str(sum([len(x) for x in lattice])-initial_sum))

    return lattice
