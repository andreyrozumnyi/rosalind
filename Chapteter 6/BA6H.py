""" Implement ColoredEdges """

def read_data(file_name):
    with open(file_name, 'r') as file:
        line = file.readline().strip().split(")")

    length = len(line)
    for i in xrange(length-1):
        line[i] = line[i].replace("(", "").split()

    return line[:length-1]

def chrom_to_cycle(chromosoms):
    length = len(chromosoms)
    nodes = [0]*(2*length)
    for j in xrange(length):
        i = int(chromosoms[j])
        if i > 0:
            nodes[2*j] = 2*i-1
            nodes[2*j+1] = 2*i
        else:
            nodes[2*j] = -2*i
            nodes[2*j+1] = -2*i-1

    return nodes

def colored_edges(genom):
    edges = []
    for i in xrange(len(genom)):
        nodes = chrom_to_cycle(genom[i])
        nodes.append(nodes[0])
        for j in xrange(len(genom[i])):
            edges.append((nodes[2*j+1], nodes[2*j+2]))

    print ', '.join(str(x) for x in edges)


if __name__ == "__main__":
    data = read_data("in.txt")
    colored_edges(data)