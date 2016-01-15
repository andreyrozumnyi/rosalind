""" Compute Distances Between Leaves """

import networkx as nx

def read_data(file_name):
    G = nx.DiGraph()
    gr_weight = {}
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            temp = line.split("->")
            i = int(temp[0])
            temp = temp[1].split(":")
            j = int(temp[0])
            w = int(temp[1])
            G.add_edge(i, j, weight = w)
            gr_weight[(i,j)] = w

    return G, gr_weight, n

def path_weight(weights, path):
    sum = 0
    if len(path) > 2:
        for i in xrange(len(path)-1):
            sum += weights[(path[i],path[i+1])]
    else:
        sum = weights[(path[0], path[1])]

    return sum

if __name__ == "__main__":
    graph, weights, n = read_data("in.txt")
    for i in xrange(n):
        for j in xrange(n):
            if i!=j:
                path = nx.shortest_path(graph, i, j)
                print path_weight(weights, path),
            else:
                print 0,
        print




