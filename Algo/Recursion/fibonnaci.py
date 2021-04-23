# def fib_iter(n):
#     a, b = 0, 1
#
#     for i in range(n):
#         a, b = b, a + b
#
#     return a
#
# out = fib_iter(5)
# print(out)

# def fibonacci_recrusion(n):
#     if n <= 1:
#         return n
#
#     return fibonacci_recrusion(n - 1) + fibonacci_recrusion(n - 2)
#
#
# out = fibonacci_recrusion(5)
# print(out)

# def good_fibonacci(n):
#     if (n <= 1):
#         return (n, 0)
#
#     else:
#         (a, b) = good_fibonacci(n - 1)
#         return (a + b, a)
#
#
# out = good_fibonacci(5)
# print(out)

# n = 10
# cache = [None] * (n + 1)
#
#
# def fib_dynamic(n):
#     if n <= 1:
#         return n
#
#     if cache[n] != None:
#         return cache[n]
#
#     cache[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)
#
#     return cache[n]
#
#
# out = fib_dynamic(5)
# print(out)
