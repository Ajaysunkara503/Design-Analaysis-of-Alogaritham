# Practical 9
# Prim's Algorithm

# Function to display the adjacency matrix
def display_graph(graph):
    print("\nAdjacency Matrix:")
    for row in graph:
        for value in row:
            print(f"{value:<5}", end="")
        print()


# Function to find the Minimum Spanning Tree
def prim_mst(graph):
    vertices = len(graph)

    selected = [False] * vertices
    selected[0] = True

    edge_count = 0
    total_cost = 0

    print("\nMinimum Spanning Tree")
    print("Source\tDestination\tWeight")

    while edge_count < vertices - 1:

        minimum = float("inf")
        source = -1
        destination = -1

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            source = i
                            destination = j

        # Check if graph is disconnected
        if minimum == float("inf"):
            print("\nGraph is disconnected.")
            print("Minimum Spanning Tree cannot be formed.")
            return

        print(f"{source}\t{destination}\t\t{graph[source][destination]}")

        total_cost += graph[source][destination]
        selected[destination] = True
        edge_count += 1

    print("\nTotal Minimum Cost =", total_cost)


# Main program

vertices = int(input("Enter the number of vertices: "))

print("\nEnter the adjacency matrix.")
print("Enter 0 where there is no edge.\n")

graph = []

for i in range(vertices):

    row = list(map(int, input(f"Row {i + 1}: ").split()))

    while len(row) != vertices:
        print(f"Please enter exactly {vertices} values.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))

    graph.append(row)

display_graph(graph)

prim_mst(graph)