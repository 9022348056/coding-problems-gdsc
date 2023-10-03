def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage
arr = [3, 6, 1, 8, 2, 4, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 8]
