import time
 
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

arr = [38, 27, 43, 3, 9, 82, 10]


start = time.time()

sorted_arr = merge_sort(arr)

end = time.time()

print("Sorted array:", sorted_arr)
print("Execution time:", end - start, "seconds")

# Complexities
print("Best Time Complexity: O(n log n)")
print("Average Time Complexity: O(n log n)")
print("Worst Time Complexity: O(n log n)")
print("Space Complexity: O(n)")