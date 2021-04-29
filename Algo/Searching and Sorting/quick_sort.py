def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [num for num in arr[1:] if num <= pivot]
        greater = [num for num in arr[1:] if num > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


q = quick_sort([7, -9, 12, 8, 89])
print(q)

"""
Big O: nlog(n)
"""
