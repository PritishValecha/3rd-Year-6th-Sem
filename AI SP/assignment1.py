def create_graph():
    no_of_nodes = int(input("Enter the number of nodes in the graph : "))
    node = []
    graph = {}
    for i in range(no_of_nodes):
        node_name = input("Enter name of the node : ")
        node.append(node_name)
        no_of_neighbours = int(input("Enter the number of neighbours of node "+node[i]+" : "))
        neighbours = []
        for i in range(no_of_neighbours):
            neighbours.append(input())
        graph[node_name] = neighbours
    return(graph)

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        visited.append(node)
        neighbours = graph[node]
        for i in neighbours:
            if i not in visited:
                queue.append(i)

def dfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        visited.append(node)
        neighbours = graph[node]
        if neighbours[0] not in visited:
            queue.append(neighbours[0])
        if(len(queue)==0):
            for i in list(graph.keys()):
                if i not in visited:
                    queue.append(i)


def main() :
    g = create_graph()
    s = input("Enter first node : ")
    bfs(g, s)
    print("\n")
    dfs(g, s)

main()