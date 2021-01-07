# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	"""
	Input:
	3 50   => number of items/ capacity of bag
	60 20  => value/weight of item
	100 50 => value/weight of item
	120 30 => value/weight of item

	Output:
	180.0000
	max number of fractions in bag
	in this case we take 1st and 3rd item cause it is the max(value/weight)
	"""
	max_capacity = capacity[1]
	item_num = capacity[0]

	K = [[0 for x in range(max_capacity + 1)] for x in range(item_num + 1)]

	for item in range(item_num+1):
		for capacity in range(max_capacity+1):
			if item == 0 or capacity == 0:
				K[item][capacity] = 0
			elif weights[item-1] <= capacity:
				K[item][capacity] = max(values[item-1] + K[item-1][capacity-weights[item-1]],  K[item-1][capacity]) 

	return K[item_num][max_capacity]


opt_value = get_optimal_value(capacity=[3,50],weights=[20,50,30],values=[60,100,120])
print(opt_value)
