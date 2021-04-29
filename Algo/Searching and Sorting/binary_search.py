def binary_search(num_list):
    search_num = max(num_list)

    low = 0
    high = len(num_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = num_list[mid]

        if guess == search_num:
            return mid

        if guess > search_num:
            high = mid - 1

        else:
            low = mid + 1

    return -1


res = binary_search([1, 4, 9, 14, 36, 49, 56, 78, 213, 439, 569, 772, 890, 918])
print(res)

"""
Big O: log(n)
"""
