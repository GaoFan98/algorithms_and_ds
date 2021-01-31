# list = [1, 4, 3, 4, 5]
#
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# modulus comparison keyword parameter
# print(max(-2, -65, 32, 11, key=abs))

# Integer related point and character on the integer point
# print(ord('~'))
# print(chr(65))

# return the whole value of division and it's reminder 5//3 = (1,2)
# print(divmod(5, 3))

# returns hashed version
# print(hash('secret'))

# returns unique id version
# print(id('secret'))

# age = int(input("Enter age: "))
# heart_rate = 206.9 - (0.67 * age)
# target = 0.65 * heart_rate
# print('Fat-burning heart rate is', target)

# import math
#
#
# def sqrt(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('x must be numeric')
#     elif x < 0:
#         raise ValueError('x cannot be negative')
#
#     return math.sqrt(x)
#     or without math
#     return x ** 0.5
#
#
# out = sqrt(4)
# print(out)

# def zero_div(x, y):
#     try:
#         ratio = x / y
#     except ZeroDivisionError:
#         return "You cannot divide by 0"
#
#     return ratio
#
#
# out = zero_div(2, 123)
# print(out)

# age = -1
# while age <= 0:
#     try:
#         age = int(input('Enter your age: '))
#         if age <= 0:
#             print('Age must be positive number')
#
#     except ValueError:
#         print('Invalid age specification')
#
#     except EOFError:
#         print('Unexpected error reading input')

# usage of next()
# data = [1,2,3,4,5,6]
# # it is wrong to do
# # print(next(data))
# # instead create list_iterator object first and then use next()
# i = iter(data)
# print(next(i))
#
# def factors(n):
#     for k in range(1, n + 1):
#         if n % k == 0:
#             yield k
#
#
# out = factors(10)
# print(out)

# def fibo():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         future = a + b
#         a = b
#         b = future
#
#
# print(fibo())

# Iterator
# class SequenceIterator:
#     def __init__(self, sequence):
#         self._seq = sequence
#         self._number = -1
#
#     def __next__(self):
#         self._number += 1
#
#         if self._number < len(self._seq):
#             return self._seq[self._number]
#         else:
#             return StopIteration()
#
#     def __iter__(self):
#         return self

# Range
# class Range:
#     def __init__(self, start, stop=None, step=1):
#         if step == 0:
#             raise ValueError('step cannot be 0')
#
#         if stop is None:
#             start, stop = 0, start
#
#         self._length = max(0, (stop - start + step - 1) // step)
#         self._start = start
#         self._step = step
#
#     def __len__(self):
#         return self._length
#
#     def __getitem__(self, item):
#         if item < 0:
#             item += len(self)
#
#         if not 0 <= item < self._length:
#             raise IndexError('index out of range')
#
#         return self._start + item * self._step
#
#
# test = Range(start=2, stop=10, step=2)
# print(test[2])
