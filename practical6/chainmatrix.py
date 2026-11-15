# Implementation of Matrix Chain Multiplication using Dynamic Programming

import time

def matrix_chain_order(p):
    n = len(p) - 1

    # DP table for minimum multiplication cost
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Table to store optimal split positions
    split = [[0 for _ in range(n)] for _ in range(n)]

    # Compute minimum cost
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        p[i] * p[k + 1] * p[j + 1])

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


def print_parenthesis(split, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_parenthesis(split, i, split[i][j])
        print_parenthesis(split, split[i][j] + 1, j)
        print(")", end="")


# Main Program

n = int(input("Enter the number of matrices: "))

print("\nEnter the dimensions:")

dimensions = []

for i in range(n + 1):
    dimensions.append(int(input(f"Dimension {i + 1}: ")))

start_time = time.perf_counter()

dp, split = matrix_chain_order(dimensions)

end_time = time.perf_counter()

print("\nRESULT")
print("Minimum number of multiplications:", dp[0][n - 1])

print("Optimal Parenthesization: ", end="")
print_parenthesis(split, 0, n - 1)
print()

print("\nExecution Time: {:.8f} seconds".format(end_time - start_time))