def findSmallestNumber(arr):
    smallest = arr[0]
    index = 0

    for num in range(1, len(arr)):
        if arr[num] < smallest:
            smallest = arr[num]
            index = num

    return index


def selectionSort(arr):
    arr_num = []

    for num in range(len(arr)):
        smallest = findSmallestNumber(arr)
        arr_num.append(arr.pop(smallest))

    return arr_num


sel_sort = selectionSort([2, 90, 0, -1, 60])
print(sel_sort)
