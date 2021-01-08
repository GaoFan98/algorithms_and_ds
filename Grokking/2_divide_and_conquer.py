# Sum up all the nums in array with loop
def sum_nums(arr):
    total = 0

    for num in arr:
        total += num

    return total


out = sum_nums([18, 2, 8, 0, 32])


# Divide and conquer method to sum up all the nums in array
def d_n_q(arr):
    if arr == []:
        return 0

    return arr[0] + d_n_q(arr[1:])


new_out = d_n_q([18, 2, 8, 0, 32])


# count number of int in list

def int_count(arr):
    if arr == []:
        return 0

    return 1 + int_count(arr[1:])


new_o = int_count([18, 2, 8, 0, 32])


# max num in array

def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    return arr[0] if arr[0] > max(arr[1:]) else max(arr[1:])


max_num = max_num([18, 2, 8, 0, 32])
