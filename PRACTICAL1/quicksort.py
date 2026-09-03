import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]      
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]

start = time.time()

sorted_arr = quick_sort(arr)

end = time.time()

print("Sorted array:", sorted_arr)
print("Execution time:", end - start, "seconds")

# Complexities
print("Best Time Complexity: O(n log n)")
print("Average Time Complexity: O(n log n)")
print("Worst Time Complexity: O(n^2)")
print("Space Complexity: O(log n)")