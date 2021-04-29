def shellSort(arr, n):
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2


arr = [9, 8, 6, 4, 1, 3, 7, 5,]
size = len(arr)
shellSort(arr, size)
print(arr)

"""
Big O: n^2
"""
