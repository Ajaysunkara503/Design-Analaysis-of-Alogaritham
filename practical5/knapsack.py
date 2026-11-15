# Implementation of 0/1 Knapsack Problem using Dynamic Programming

import time

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()

    return dp[n][capacity], selected


# Main Program

n = int(input("Enter number of items: "))

weights = []
values = []

print("\nEnter weight and value of each item:")

for i in range(n):
    wt = int(input(f"Weight of Item {i+1}: "))
    val = int(input(f"Value of Item {i+1}: "))
    weights.append(wt)
    values.append(val)

capacity = int(input("\nEnter knapsack capacity: "))

# Measure execution time
start_time = time.perf_counter()

max_profit, selected_items = knapsack(weights, values, capacity)

end_time = time.perf_counter()

# Output

print("\nRESULT")
print("Maximum Profit:", max_profit)

print("\nSelected Item Numbers:", selected_items)

print("\nSelected Item Details:")
total_weight = 0
total_value = 0

for i in selected_items:
    print(f"Item {i}: Weight = {weights[i-1]}, Value = {values[i-1]}")
    total_weight += weights[i-1]
    total_value += values[i-1]

print("\nTotal Weight:", total_weight)
print("Total Value :", total_value)

print("\nExecution Time: {:.8f} seconds".format(end_time - start_time))