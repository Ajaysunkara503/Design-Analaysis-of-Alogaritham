import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = [64, 25, 12, 22, 11]
start_time = time.time()

sorted_arr = insertion_sort(arr)

end_time = time.time()

print("Sorted Array:", sorted_arr)
print("Execution Time:", end_time - start_time, "seconds")

# Complexity
print("Time Complexity (Best): O(n)")
print("Time Complexity (Average): O(n^2)")
print("Time Complexity (Worst): O(n^2)")
print("Space Complexity: O(1)")