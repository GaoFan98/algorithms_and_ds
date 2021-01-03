# Recursive way
# def calc_fib(n):
# 	if n <= 1:
# 		return n

# 	return calc_fib(n-1)+calc_fib(n-2)

# n = int(input())
# print(calc_fib(n))

# Faster way of fibonacci
def calc_fib(n):
	arr_nums = [0,1]

	if (n <= 1):
		return n
        
	for i in range(2,n+1):
		arr_nums.append(arr_nums[-1]+arr_nums[-2])

	return arr_nums[-1]


n = int(input())
print(calc_fib(n))