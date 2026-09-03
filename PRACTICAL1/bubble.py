import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

start = time.time()

bubble_sort(arr)


end = time.time()

print("Sorted array:", arr)
print("Execution time:", end - start, "seconds")

# Complexities
print("Best Time Complexity: O(n)")
print("Average Time Complexity: O(n^2)")
print("Worst Time Complexity: O(n^2)")
print("Space Complexity: O(1)")