""" Implement GraphToGenome """

def read_data(file_name):
    with open(file_name, "r") as file:
        line = file.readline().strip().split(", (")

    length = len(line)
    line[0] = line[0].replace("(", "")
    graph = []
    for i in xrange(length):
        line[i] = line[i].replace(")", "")
        node1, node2 = line[i].split(",")
        graph.append(int(node1))
        graph.append(int(node2))

    return graph

def cycle_to_chrom(nodes):
    length = len(nodes)
    chrom = [0]*(length/2)
    for j in xrange(length/2):
        if nodes[2*j] < nodes[2*j+1]:
            chrom[j] = nodes[2*j+1]/2
        else:
            chrom[j] = -nodes[2*j]/2

    return chrom

def _get_pair_elem(start):
    if start % 2 == 0:
        return start-1
    else:
        return start+1

def graph_to_genom(graph):
    genom = []
    start = graph[0]
    st_index = 0
    end = _get_pair_elem(start)
    for i in xrange(len(graph)/2):
        if graph[2*i+1] == end:
            cycle = [end] + graph[st_index:2*i+2]
            genom.append(cycle_to_chrom(cycle))
            if 2*i+2 < len(graph):
                start = graph[2*i+2]
                st_index = 2*i+2
                end = _get_pair_elem(start)

    return genom

def form_answ(genom):
    answ = ""
    for j in xrange(len(genom)):
        for i in xrange(len(genom[j])):
            if genom[j][i] > 0:
                genom[j][i] = "+" + str(genom[j][i])
            else:
                genom[j][i] = str(genom[j][i])

        answ += "(" + " ".join(genom[j]) + ")"

    print answ

if __name__ == "__main__":
    data = read_data("in.txt")
    genom = graph_to_genom(data)
    form_answ(genom)

