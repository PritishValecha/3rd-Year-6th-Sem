def create_graph():
    noOfNodes = int(input("Enter number of nodes : "))
    graph = {}
    for i in range(noOfNodes):
        node = input("Enter name of the node : ")
        neighbours = []
        noOfNeighbours = int(input("Enter number of neighbours : "))
        for j in range(noOfNeighbours):
            neighbour = input("Enter neighbour : ")
            neighbours.append(neighbour)
        graph[node] = neighbours
    print(graph)
    return graph

def bfs(graph, s):
    visited = []
    queue = [s]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        print(node, end=" ")
        neighbours = graph[node]
        for i in neighbours:
            if (i not in visited):
                queue.append(i)

def dfs(graph, s):
    visited = []
    queue = [s]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        print(node, end=" ")
        neighbours = graph[node]
        if(neighbours[0] not in visited):
            queue.append(neighbours[0])
        if(len(queue)==0):
            for i in list(graph.keys()):
                if i not in visited:
                    queue.append(i)

def main():
    g = create_graph()
    start = input("Enter start node : ")
    bfs(g, start)
    print()
    dfs(g, start)

main()