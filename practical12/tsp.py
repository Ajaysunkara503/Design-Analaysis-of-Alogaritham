# Practical 12
# Travelling Salesman Problem

from itertools import permutations


# Function to find the minimum cost path
def travelling_salesman(graph):

    vertices = len(graph)

    cities = []

    for i in range(1, vertices):
        cities.append(i)

    minimum_cost = float("inf")
    best_path = ()

    for path in permutations(cities):

        current_city = 0
        current_cost = 0

        for city in path:
            current_cost += graph[current_city][city]
            current_city = city

        current_cost += graph[current_city][0]

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_path = (0,) + path + (0,)

    print("\nMinimum Cost =", minimum_cost)

    print("Best Path =", end=" ")

    for city in best_path:
        print(city, end=" ")


# Main Program

vertices = int(input("Enter the number of cities: "))

print("\nEnter the cost matrix.")
print("Enter each row as space-separated values.")
print("Example:")
print("0 10 15 20\n")

graph = []

for i in range(vertices):

    row = list(map(int, input(f"Row {i + 1}: ").split()))

    while len(row) != vertices:
        print(f"Please enter exactly {vertices} values.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))

    graph.append(row)

travelling_salesman(graph)