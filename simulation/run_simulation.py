from simulation.take_step import take_step
from initialise.make_lattice import make_lattice

def run_simulation(n, deltaMu, AA, AB, T, time):
    lattice = make_lattice(n)
    initial_lattice = lattice
    for k in range(time):
        lattice = take_step(n, lattice, deltaMu, T, AA, AB)
    wrong_place = 0
    for i in range((n**2)/2):
        wrong_count = [abs((n/2-1)-i%n) for x in lattice[i] if x != 0]
        wrong_place += sum(wrong_count)
    for i in range((n**2)/2, n**2):
        wrong_count2 = [abs((n/2-1)-i%n) for x in lattice[i] if x != 0]
        wrong_place += sum(wrong_count2)
    return wrong_count/sum([len(x) for x in lattice])

