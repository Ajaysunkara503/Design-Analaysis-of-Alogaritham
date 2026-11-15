from collections import deque

# Input number of vertices
while True:
    try:
        n = int(input("Enter the number of vertices: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

# Create graph
graph = {}

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("\nBFS Traversal:")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Starting vertex
while True:
    start = input("\nEnter the starting vertex: ")
    if start in graph:
        break
    else:
        print("Vertex not found! Please enter a valid vertex.")

# Call BFS
bfs(graph, start)
print()