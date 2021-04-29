def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


our_list = [19, 13, 6, 2, 18, 8]
bubble_sort(our_list)
print(our_list)

"""
Big O: n^2
"""