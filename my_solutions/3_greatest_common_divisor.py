# [10,4] => 2
# [16 ,12] => 4
# [36,8]

# slow 
# def gcd(a, b):
# 	best = 1

# 	for num in range(2,min(a,b)+1):
# 		# num => 2,3,4
# 		if a%num == 0 and b%num == 0:
# 			best = num

# 	return best


# recursion Euclidian algorithm with reminder

# a / b = c (rem)
# b / rem = c (rem)
# b / rem = c (rem)
# till b / rem = c (rem == 0)

# 88 / 14 = 6 (4)
# 14 / 4 = 3 (2)
# 4 / 2 = 2

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))