from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list) # defaultdict(list) adds an empty list to all the adjList elements

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def bfs(self, start):
        queue = deque()
        visited = [False] * (max(self.adjList.keys()) + 1)

        visited[start] = True
        queue.append(start)

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.adjList[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

graph = Graph()

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)

graph.bfs(1)

# print(graph.adjList[5])