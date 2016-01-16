import networkx as nx

def read_edges(fileName):
    graph = dict()
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            node1, node_list = line.strip().split("->")
            node_list = node_list.strip().split(",")
            node1 = int(node1)
            for node2 in node_list:
                if node1 in graph:
                    graph[node1].append(int(node2))
                else:
                    graph[node1] = [int(node2)]

    vertexes = get_verttexes(graph)
    for vertex in vertexes:
        if vertex not in graph:
            graph[vertex] = []

    return graph, vertexes

def get_verttexes(graph):
    vertexes = set()
    for item in graph:
        vertexes.add(item)
        for elem in graph[item]:
            vertexes.add(elem)

    return list(vertexes)

if __name__ == "__main__":
    graph, vertexes = read_edges("in.txt")
    G=nx.DiGraph()
    for vert in vertexes:
        G.add_node(vert)

    for node in graph:
        for neighb in graph[node]:
            G.add_edge(node, neighb)

    ts = nx.topological_sort(G)
    ts = [str(node) for node in ts]
    print ", ".join(ts)
