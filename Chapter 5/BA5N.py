""" Find a Topological Ordering of a DAG """


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


def topol_order(graph, start):
    global order
    global used
    used[start] = True
    graph[start].sort(reverse = True)
    for i in xrange(len(graph[start])):
        if used[graph[start][i]] == False:
            topol_order(graph, graph[start][i])

    order.append(start)


def get_verttexes(graph):
    vertexes = set()
    for item in graph:
        vertexes.add(item)
        for elem in graph[item]:
            vertexes.add(elem)

    return list(vertexes)


def write_to_file(file_name, order):
    string = ", ".join(str(i) for i in order)
    with open(file_name, 'w') as file:
        file.write(string)

if __name__ == "__main__":
    graph, vertexes = read_edges("in.txt")
    print graph
    order = []
    component = []
    used = {}
    for item in graph:
        used[item] = False

    vertexes.sort()
    for vert in vertexes:
        if not used[vert]:
            topol_order(graph, vert)

    write_to_file("out.txt", order[::-1])
    print order[::-1]