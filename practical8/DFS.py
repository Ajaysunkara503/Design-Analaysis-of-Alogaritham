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

# DFS Function
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Starting vertex
while True:
    start = input("\nEnter the starting vertex: ")
    if start in graph:
        break
    else:
        print("Vertex not found! Please enter a valid vertex.")

print("\nDFS Traversal:")
visited = set()

# Call DFS
dfs(graph, start, visited)
print()