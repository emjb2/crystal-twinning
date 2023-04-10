

def find_layer_sums(lattice):
    max_height = max([len(x) for x in lattice])
    layer = []
    for i in range(max_height):
        temp = []
        count = 0
        for x in lattice:
            if len(x) > i:
                count += 1
                temp.append(x[i])
        layer.append(sum(temp)/count)
    
    return layer
            