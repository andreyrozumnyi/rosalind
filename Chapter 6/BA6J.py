""" Implement 2-BreakOnGenomeGraph """

def read_data(file_name):
    with open(file_name, 'r') as file:
        edges = file.readline().strip().split("), (")
        breaks = file.readline().strip().split(",")

    edges_len = len(edges)
    edges[0] = edges[0].replace("(", "")
    edges[edges_len-1] = edges[edges_len-1].replace(")", "")
    for i in xrange(edges_len):
        node1, node2 = edges[i].split(",")
        edges[i] = (int(node1), (int(node2)))

    for i in xrange(len(breaks)):
        breaks[i] = int(breaks[i])

    return edges, breaks

def two_break_on_gen_gr(edges, breaks):
    i = breaks[0]
    i_ = breaks[1]
    j = breaks[2]
    j_ = breaks[3]
    for k in xrange(len(edges)):
        if edges[k] == (i, i_):
            edges[k] = (j_, i_)
        elif edges[k] == (i_, i):
            edges[k] = (i_, j_)
        elif edges[k] == (j, j_):
            edges[k] = (j, i)
        elif edges[k] == (j_, j):
            edges[k] = (i, j)

    print edges

if __name__ == "__main__":
    edges, breaks = read_data("in.txt")
    two_break_on_gen_gr(edges, breaks)