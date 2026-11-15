# Practical 10
# Kruskal's Algorithm

# Function to find the parent of a vertex
def find(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find(parent, parent[vertex])


# Function to perform union of two sets
def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    parent[root_u] = root_v


# Function to implement Kruskal's Algorithm
def kruskal(vertices, edges):

    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(vertices)]

    total_cost = 0

    print("\nMinimum Spanning Tree")
    print("Source\tDestination\tWeight")

    for u, v, weight in edges:

        if find(parent, u) != find(parent, v):

            union(parent, u, v)

            print(f"{u}\t{v}\t\t{weight}")

            total_cost += weight

    print("\nTotal Minimum Cost =", total_cost)


# Main Program

vertices = int(input("Enter the number of vertices: "))
edge_count = int(input("Enter the number of edges: "))

print("\nEnter each edge as space-separated values.")
print("Format: Source Destination Weight")
print("Example:")
print("0 1 2\n")

edges = []

for i in range(edge_count):

    edge = list(map(int, input(f"Edge {i + 1}: ").split()))

    while len(edge) != 3:
        print("Please enter exactly 3 values.")
        edge = list(map(int, input(f"Edge {i + 1}: ").split()))

    edges.append(edge)

kruskal(vertices, edges)