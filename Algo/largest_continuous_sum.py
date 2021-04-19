# Kaden's algorithm
def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_arr = curr_max = 0

    for num in range(1, len(arr)):
        curr_max = max(arr[num], curr_max + arr[num])
        max_arr = max(max_arr, curr_max)

    return max_arr


out = large_cont_sum([-2, -3, 4, -1, -2, 1, 5, -3])
print(out)
