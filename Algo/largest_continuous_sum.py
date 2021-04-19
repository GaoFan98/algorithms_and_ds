# Kaden's algorithm
def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_current = max_global = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


out = large_cont_sum([-2, -3, 4, -1, -2, 1, 5, -3])
print(out)
