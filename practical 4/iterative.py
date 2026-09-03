import time

def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


n = int(input("Enter a number: "))

# Iterative Method
start = time.perf_counter()
iter_result = factorial_iterative(n)
end = time.perf_counter()

iter_time = end - start

print("\nIterative Method")
print("Factorial =", iter_result)
print("Execution Time =", iter_time, "seconds")
print("Time Complexity = O(n)")
print("Space Complexity = O(1)")

# Recursive Method
start = time.perf_counter()
rec_result = factorial_recursive(n)
end = time.perf_counter()

rec_time = end - start

print("\nRecursive Method")
print("Factorial =", rec_result)
print("Execution Time =", rec_time, "seconds")
print("Time Complexity = O(n)")
print("Space Complexity = O(n)")