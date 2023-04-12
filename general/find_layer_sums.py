

def find_layer_sums(lattice):
    min_height = max([len(x) for x in lattice])
    print(min_height)
    layer = []
    for i in range(min_height):
        temp = []
        count = 0
        for x in lattice:
            if len(x) > i:
                count += 1
                temp = temp + [x[i]]
        layer = layer + [sum(temp)/count]
    
    return layer
            