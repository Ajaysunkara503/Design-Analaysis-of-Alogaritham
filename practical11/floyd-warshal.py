# Practical 11
# Floyd-Warshall Algorithm

# Function to display the distance matrix
def display_matrix(matrix):
    print("\nShortest Distance Matrix:")

    for row in matrix:
        for value in row:
            if value == INF:
                print("INF", end="\t")
            else:
                print(value, end="\t")
        print()


# Function to implement Floyd-Warshall Algorithm
def floyd_warshall(graph):

    vertices = len(graph)

    distance = []

    for row in graph:
        distance.append(row.copy())

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):

                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    display_matrix(distance)


# Main Program

INF = 99999

vertices = int(input("Enter the number of vertices: "))

print("\nEnter the adjacency matrix.")
print("Enter each row as space-separated values.")
print("Use 99999 where there is no direct edge.")
print("Example:")
print("0 5 99999 10\n")

graph = []

for i in range(vertices):

    row = list(map(int, input(f"Row {i + 1}: ").split()))

    while len(row) != vertices:
        print(f"Please enter exactly {vertices} values.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))

    graph.append(row)

floyd_warshall(graph)