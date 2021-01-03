def calc_fib(frm,till):
	arr_nums = [0,1]

	if (till <= 1): return till
        
	for i in range(2,till+1):
		arr_nums.append((arr_nums[-1]+arr_nums[-2])%10)

	
	a = sum(arr_nums[frm:till+1]) %10

	return a 

if __name__ == '__main__':
    frm, till = map(int, input().split())
    print(calc_fib(frm, till))