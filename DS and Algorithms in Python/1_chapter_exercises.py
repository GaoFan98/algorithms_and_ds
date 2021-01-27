# --------R-1.1-----------
# def is_multiple(n, m):
#     if m == 0:
#         return False
#
#     return n % m == 0
#
#
# print(is_multiple(10, 5))  # True
# print(is_multiple(10, 3))  # False

# --------R-1.2-----------
# def is_even(k: int):
#     list_of_even = [0, 2, 4, 6, 8]
#     if int(str(k)[-1:]) in list_of_even:
#         return "EVEN"
#     return "ODD"
#
#
# print(is_even(-14))

# --------R-1.3-----------
# def min_max(data):
#     if len(data) == 0:
#         return False
#
#     min_num = max_num = data[0]
#     for i in data:
#         if i > max_num:
#             max_num = i
#         elif i < min_num:
#             min_num = i
#
#     return (min_num, max_num)
#
#
# print(min_max([75, 1, 4, -5, 60]))

# --------R-1.4 and R-1.5-----------
# def square_sum(n: int):
#     return sum(x * x for x in range(1, n))
#
#
# print(square_sum(10))

# --------R-1.6 and R-1.7-----------
# def odd_square_num(n):
#     return sum(x * x for x in range(1, n) if x % 2 == 1)
#
#
# print(odd_square_num(10))

# --------R-1.8-----------
# s = "Hello"
# n = len(s)
# s[k] for -n <= k < 0

# --------R-1.9-----------
# print(list(range(50, 81, 10)))

# --------R-1.10-----------
# print(list(range(8, -9, -2)))

# --------R-1.11-----------
# print([2 ** x for x in range(9)])

# --------R-1.12-----------
# import random
#
#
# # print(random.choice([1, 3, 4]))
# # print(random.randrange(1, 4))
#
# def rand_choice(data):
#     # print(data[len(data)-1])
#     return random.randrange(data[0], data[len(data) - 1])
#
#
# print(rand_choice([1, 4, 6, 8]))

# --------C-1.13-----------

