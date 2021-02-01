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

# Inheritance example
# class CreditCard:
#     def __init__(self, customer, bank, account_id, credit_limit):
#         self._customer = customer
#         self._bank = bank
#         self._account = account_id
#         self._limit = credit_limit
#         self._balance = 0
#
#     def get_customer(self):
#         return self._customer
#
#     def get_bank(self):
#         return self._bank
#
#     def get_account(self):
#         return self._account
#
#     def get_limit(self):
#         return self._limit
#
#     def get_balance(self):
#         return self._balance
#
#     def charge(self, price):
#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price
#             return True
#
#     def make_payment(self, amount):
#         self._balance -= amount
#
#
# class PredatoryCreditCard(CreditCard):
#     def __init__(self, customer, bank, account_id, credit_limit, annual_percent):
#         """
#         super().__init__ inherit params from parent class
#         """
#         super().__init__(customer, bank, account_id, credit_limit)
#         self._year_per = annual_percent
#
#     def charge(self, price):
#         success = super().charge(price)
#
#         if not success:
#             self._balance += 5
#
#         return success
#
#     def process_month(self):
#         if self._balance > 0:
#             monthly_fee = pow(1 + self._year_per, 1 / 12)
#             self._balance *= monthly_fee

# more example on inheritance
# class Progression:
#     def __init__(self, start):
#         self._current = start
#
#     def _advance(self):
#         self._current += 1
#
#     def __next__(self):
#         if self._current is None:
#             raise StopIteration
#         else:
#             answer = self._current
#             self._advance()
#             return answer
#
#     def __iter__(self):
#         return self
#
#     def print_progression(self, n):
#         print(" ".join(str(next(self)) for _ in range(n)))
#
#
# class ArithmeticProgression(Progression):
#     def __init__(self, increment=1, start=0):
#         super().__init__(start)
#         self._increment = increment
#
#     def _advance(self):
#         self._current += self._increment
#
#
# class GeometricProgression(Progression):
#     def __init__(self, base=1, start=1):
#         super().__init__(start)
#         self._base = base
#
#     def _advance(self):
#         self._current *= self._base
#
#
# class FibonacciProgression(Progression):
#     def __init__(self, first=1, second=1):
#         super().__init__(first)
#         self._prev = second - first
#
#     def _advance(self):
#         self._prev, self._current = self._current, self._prev + self._current
#
#
# print("Default progression")
# Progression(1).print_progression(10)
#
# print("Arithmetic progression")
# ArithmeticProgression(5).print_progression(10)
#
# print("Arithmetic progression")
# GeometricProgression(5).print_progression(10)
#
# print("Fibonacci progression with first number 41 and second number 123")
# FibonacciProgression(41, 123).print_progression(10)
