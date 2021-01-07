
# Sum((F(i))**2) = (Fn)*(Fn+1)
# Sum(F(5)**2) = F(5)*F(6) 

def calc_fib(n):
	arr_nums = [0,1]

	if (n <= 1):
		return n
        
	for i in range(2,n+2):
		arr_nums.append(arr_nums[-1]+arr_nums[-2])


	return (arr_nums[-1]*arr_nums[-2])%10


n = int(input())
print(calc_fib(n))