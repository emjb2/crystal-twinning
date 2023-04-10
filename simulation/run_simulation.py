from simulation.take_step import take_step
from initialise.make_lattice import make_lattice
import matplotlib.pyplot as plt
from general.find_layer_sums import find_layer_sums

def run_simulation(n, deltaMu, AA, AB, T, time):
    lattice = make_lattice(n)
    for k in range(time):
        lattice = take_step(n, lattice, deltaMu, T, AA, AB)
    wrong_place = 0
    for i in range(int((n**2)/2)):
        #wrong_count = [abs((n/2-1)-i%n) for x in lattice[i] if x != 0]
        #wrong_place += sum(wrong_count)
        wrong_place += sum([1 for x in lattice[i] if x == 1])
    for i in range(int((n**2)/2), n**2):
        #wrong_count2 = [abs((n/2)-i%n) for x in lattice[i] if x != 1]
        #wrong_place += sum(wrong_count2)
        wrong_place += sum([1 for x in lattice[i] if x == 0])
        #print("Total: "+str(sum([sum(x) for x in lattice])/sum([len(x) for x in lattice])))

    #sums = find_layer_sums(lattice)
    #plt.plot(list(range(len(sums))), sums, marker='.')
    #plt.ylabel("layer sum")
    #plt.xlabel("layer number, bottom up")
    #plt.show()

    return [wrong_place/sum([len(x) for x in lattice]), lattice, wrong_place]
