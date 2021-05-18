def largest_product_3_int(list):
    if len(list) < 3:
        return 'Not enough integers for triplets'

    else:
        list.sort()
        return max(list[0] * list[1] * list[len(list) - 1],
                   list[len(list) - 1] * list[len(list) - 2] * list[len(list) - 3])


out = largest_product_3_int([2, 1, 3, 5, 1])
print(out)
