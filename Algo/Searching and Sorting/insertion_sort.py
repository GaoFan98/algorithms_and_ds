def insertion_sort(arr):
    for i in range(1, len(arr)):
        # select first unsorted element
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        #     insert unsorted element to correct position
        arr[j + 1] = key

    return arr


arr = [10, 5, 13, 8, 2]
insertion_sort(arr)
print(arr)

"""
Big O: n^2
"""