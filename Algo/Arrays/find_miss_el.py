# def finder(l1, l2):
#     num_dict = {}
#
#     for num in l1:
#         if num not in num_dict:
#             num_dict[num] = 1
#         else:
#             num_dict[num] += 1
#
#     for num in l2:
#         if num not in num_dict:
#             num_dict[num] = 1
#         else:
#             num_dict[num] -= 1
#
#     for num in num_dict:
#         if num_dict[num] > 0:
#             return num
#
#
# out = finder([5, 5, 7, 7], [5, 7, 7])
# print(out)


# faster solution
def finder_bitwise(l1, l2):
    result = 0

    for num in l1 + l2:
        result ^= num

    return result


out = finder_bitwise([5, 5, 7, 7], [5, 7, 7])
print(out)
