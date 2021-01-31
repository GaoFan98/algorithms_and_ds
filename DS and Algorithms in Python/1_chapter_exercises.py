# ################R-1.1################
# def is_multiple(n, m):
#     if m == 0:
#         return False
#
#     return n % m == 0
#
#
# print(is_multiple(10, 5))  # True
# print(is_multiple(10, 3))  # False

# ################R-1.2################
# def is_even(k: int):
#     list_of_even = [0, 2, 4, 6, 8]
#     if int(str(k)[-1:]) in list_of_even:
#         return "EVEN"
#     return "ODD"
#
#
# print(is_even(-14))

# ################R-1.3################
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

# ################R-1.4 and R-1.5################
# def square_sum(n: int):
#     return sum(x * x for x in range(1, n))
#
#
# print(square_sum(10))

# ################R-1.6 and R-1.7################
# def odd_square_num(n):
#     return sum(x * x for x in range(1, n) if x % 2 == 1)
#
#
# print(odd_square_num(10))

# ################R-1.8################
# s = "Hello"
# n = len(s)
# s[k] for -n <= k < 0

# ################R-1.9################
# print(list(range(50, 81, 10)))

# ################R-1.10################
# print(list(range(8, -9, -2)))

# ################R-1.11################
# print([2 ** x for x in range(9)])

# ################R-1.12################
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

# ################C-1.13################
# def order_reverse(data):
#     reverse = []
#
#     while len(data):
#         reverse.append(data.pop())
#
#     return reverse
#
#
# print(order_reverse([-2131, 2, 3, 4, 5]))

# ################C-1.14################
# def odd_product_pair(data):
#     """
#     2*2 = 4 even
#     3*4 = 12 even
#     3*3 = 9 odd
#     """
#     for first in data:
#         for second in data:
#             if first != second and (first * second) % 2 == 1:
#                 yield (first, second)
#
#
# for item in odd_product_pair([1, 2, 3, 4, 5]):
#     print(item)

# ################C-1.15################
# def diff_nums(data):
#     """
#     2*2 = 4 even
#     3*4 = 12 even
#     3*3 = 9 odd
#     """
#     unique_nums = set()
#
#     for num in data:
#         if num not in unique_nums:
#             unique_nums.add(num)
#             return True
#
#         else:
#             return False
#
#
# print(diff_nums([11, 2, 4, 3]))

# ################C-1.18################
# 0, 6 - 2 = 4, 12 - 6 = 6, 20 - 12 = 8, 30 - 20 = 10, 42 - 30 = 12
# a-b = b
# [0, 2, 6, 12, 20, 30, 42]

# ################C-1.19################
# print([chr(97 + char) for char in range(26)])

# ################C-1.20################
# import random
#
#
# #
# # mylist = ["apple", "banana", "cherry"]
# # random.shuffle(mylist)
# #
# # print(mylist)
#
# # print(random.randint(3, 9))
#
# def rand_int(data):
#     if len(data):
#         for el in range(len(data)):
#             shuffle = random.randint(0, len(data) - 1)
#             data[shuffle], data[el] = data[el], data[shuffle]
#     else:
#         return False
#
#     return data
#
#
# print(rand_int(["apple", "banana", "cherry", "melon"]))

# ################C-1.22################
# def dot_product(a, b):
#     if len(a) != len(b):
#         return False
#
#     c = []
#     [c.append(a * b) for a, b in zip(a, b)]
#
#     return c
#
#
# print(dot_product([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))

# ################C-1.24################
# def vowel_count(data):
#     vowels = {"a", "e", "i", "o", "u"}
#
#     count = 0
#     for l in data.lower():
#         if l in vowels:
#             count += 1
#
#     return count
#
#
# print(vowel_count('Hello World'))

# ################C-1.25################
# def remove_symbols(data):
#     sym = {'.', ',', '!', '?', ':', ';', "'"}
#
#     removed = "".join(el for el in data if el not in sym)
#
#     return removed
#
#
# print(remove_symbols("Let's try, Mike."))

# ################C-1.26################
# Copied from another repo cause do not want to waste my time for this task
# def arithmetic_check(a, b, c):
#     if a + b == c:
#         return 'Can be used for addition'
#     elif a - b == c:
#         return 'Can be used for subtraction'
#     elif a * b == c:
#         return 'Suitable for multiplication'
#     elif a / b == c:
#         return 'Suitable for division'
#     else:
#         return 'Not good for any of the big four'
#
#
# print(arithmetic_check(1, 2, 3))

# ################C-1.28################
# Copied from repo. do not want to waste time on this task
# def p_norm(v, p=2):
#     assert p != 0, 'You cannot use zero as a p-value'
#     sum = 0
#     for num in v:
#         sum += num ** p
#     return sum ** (1 / p)
#
#
# print(p_norm([4, 3]))

# ################P-1.29################
# def permutations(head, tail=''):
#     if len(head) == 0:
#         print(tail)
#     else:
#         for i in range(len(head)):
#             # print(head[:i])
#             # print(head[i + 1:])
#             # print(head[:i] + head[i + 1:])
#             # print(head[i])
#             # print(tail)
#             # print(head[:i] + head[i + 1:], tail + head[i])
#             permutations(head[i + 1:] + head[:i], head[i] + tail)
#
#
# print(permutations("catdog"))

# ################P-1.30################
# def divide_by_two(n):
#     count = 0
#
#     while n > 2:
#         n /= 2
#         count += 1
#
#     return count
#
#
# print(divide_by_two(99))

# ################P-1.31################
# def return_change(given, back):
#     money = [100, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
#
#     out = {}
#     c = given - back
#
#     for coin in range(len(money)):
#         if c // money[coin] != 0:
#             out[money[coin]] = int(c // money[coin])
#             c = c % money[coin]
#     print(out)
#
#     # out['100'] = c // money[0]
#     # c = c % money[0]
#     # out['20'] = c // money[1]
#     # c = c % money[1]
#     # out['10'] = c // money[2]
#     # c = c % money[2]
#     # out['5'] = c // money[3]
#     # c = c % money[3]
#     # out['2'] = c // money[4]
#     # c = c % money[4]
#     # out['1'] = c // money[5]
#     # c = c % money[5]
#     # out['0.25'] = c // money[6]
#     # c = c % money[6]
#     # out['0.10'] = c // money[7]
#     # c = c % money[7]
#     # out['0.05'] = c // money[8]
#     # c = c % money[8]
#     # out['0.01'] = c // money[9]
#     # c = c % money[9]
#     #
#     # print(out)
#
#
# print(return_change(1000.84, 575))

# ################P-1.34################
# copied from another repo
# import random
#
#
# def create_typo(message, char_range):
#     error_spot = random.randrange(0, len(message))
#     error_character = random.choice(char_range)
#     incorrect_message = list(message)
#     incorrect_message[error_spot] = chr(error_character)
#     return (''.join(incorrect_message))
#
#
# def spamalot(message, num_errors=8, num_lines=10):
#     # find all the character values for Aa-Zz
#     char_range = list(range(ord('A'), ord('Z') + 1)) + list(range(ord('a'), ord('z') + 1))
#
#     line_count = 0
#     error_lines = set()
#     while line_count < num_errors:
#         new_error_line = random.randrange(num_lines)
#         if new_error_line not in error_lines:
#             error_lines.add(new_error_line)
#             line_count += 1
#
#     for i in range(num_lines):
#         if i not in error_lines:
#             print(message)
#         else:
#             print(create_typo(message, char_range), '<- This is the typo')
#
#
# spamalot('I will never spam my friends again')

# ################P-1.35################
# import random
#
#
# def birthday(n_people):
#     birthday = [random.randrange(0, 365) for _ in range(n_people)]
#     unique_birth = set()
#
#     for b in birthday:
#         if b not in unique_birth:
#             unique_birth.add(b)
#
#     counter = 0
#     for trial in range(101):
#         if trial in unique_birth:
#             counter += 1
#
#
# print(birthday(23))

# ################P-1.36################
# Not interesting task
