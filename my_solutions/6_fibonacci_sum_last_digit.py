
# 7 = 2 * 3 + 1
# Dividend = (Quotient × Divisor) + Remainder
# => F7 mod 2 = F1 mod 2 = 1.


def calc_fib(n):
	arr_nums = [0,1]

	if (n <= 1): return n
        
	for i in range(2,n+1):
		arr_nums.append((arr_nums[-1]+arr_nums[-2])%10)


	a = sum(arr_nums) %10

	return a 

n = int(input())
print(calc_fib(n))