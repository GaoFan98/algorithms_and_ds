def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [num for num in arr[1:] if pivot <= num]
        greater = [num for num in arr[1:] if pivot > num]

        return quick_sort(less) + [pivot] + quick_sort(greater)


q = quick_sort([7, -9, 12, 8, 89])
print(q)
