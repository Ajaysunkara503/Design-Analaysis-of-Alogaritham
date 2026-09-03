import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]

start_time = time.time()

sorted_arr = selection_sort(arr)

end_time = time.time()

print("Sorted Array:", sorted_arr)
print("Execution Time:", end_time - start_time, "seconds")

# Complexity
print("Time Complexity (Best): O(n^2)")
print("Time Complexity (Average): O(n^2)")
print("Time Complexity (Worst): O(n^2)")
print("Space Complexity: O(1)")