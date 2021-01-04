

def max_pairwise_product(numbers):
	if len(numbers)==1:
		return numbers[0]

	index = 0

	for i in range(len(numbers)):
		if numbers[i]>numbers[index]:
			numbers[index],numbers[i] = numbers[i],numbers[index]

			index+=1

	return numbers[0]*numbers[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
