def get_change(given_coin):
    coins = [1,5,10]

    if given_coin == 0:
    	return 0

    table = [0] + [given_coin+1 for i in range(given_coin)]  
    
    for index in range(0, given_coin+1):
    	for coin in coins:
    		if index >= coin:
    			table[index] = min(table[index],table[index-coin]+1)

    return table[index]	

given_coin = int(input())
print(get_change(given_coin))
