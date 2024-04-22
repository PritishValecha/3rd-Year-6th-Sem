def create_graph():
    no_of_nodes = int(input("Enter the number of nodes : "))
    graph = []
    for i in range(no_of_nodes):
        list = []
        print("For",i,"th row : \n")
        for j in range(no_of_nodes):
            n = int(input("Enter the weight of edge "))
            list.append(n)
        graph.append(list)
    for i in range(no_of_nodes):
        print(graph[i], end="\n")
    return graph

def prims(graph):
    visited = []
    for i in range(len(graph)):
        visited.append(False)
    visited[0] = True
    for i in range(len(graph)-1):
        min = 9999
        for j in range(len(graph)):
            if(visited[j]==True):
                for k in range(len(graph)):
                    if((visited[k]!=True) and (graph[j][k]<min) and (graph[j][k]!=0)):
                        min = graph[j][k]
                        v1 = j
                        v2 = k
        print("Edge found ",v1," - ",v2," : ",graph[v1][v2],"\n")
        visited[v2] = True
                
def main():
    # g = create_graph()
    g = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]
    prims(g)

main()