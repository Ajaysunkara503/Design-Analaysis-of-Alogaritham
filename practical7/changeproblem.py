# Practical 7
# Implementation of Making Change Problem using Dynamic Programming

import time

# Function to find minimum number of coins
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


# Main Program 

# User Input
coins = list(map(int, input("Enter coin denominations (space-separated): ").split()))
amount = int(input("Enter the amount: "))

# Measure Execution Time
start = time.perf_counter()
result = coin_change(coins, amount)
end = time.perf_counter()

execution_time = end - start

# Output
print("\nMAKING CHANGE USING DYNAMIC PROGRAMMING ")

print("Coin Denominations :", coins)
print("Amount             :", amount)

if result == -1:
    print("Result             : Change cannot be made.")
else:
    print("Minimum Coins      :", result)

print(f"Execution Time     : {execution_time:.10f} seconds")
print("Time Complexity    : O(n × m)")
print("Space Complexity   : O(m)")