from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def BFS(self, start):
        visited = [False] * self.V
        q = deque()

        visited[start] = True
        q.append(start)

        while q:
            v = q.popleft()
            print(v, end=" ")

            for u in self.adj[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)


g = Graph(5)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)

print("BFS Traversal:", end=" ")
g.BFS(0)
