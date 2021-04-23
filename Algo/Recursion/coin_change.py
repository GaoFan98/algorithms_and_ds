# recursive version
def coin_change(target, coins):
    min_coins = target

    if target in coins:
        return 1

    else:
        # for every coin value that is <= target
        for coin in [c for c in coins if c <= target]:
            num_coins = 1 + coin_change(target - coin, coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


out = coin_change(10, [1, 5, 10])
print(out)


# dynamical programming
def get_change(given_coin, coins):
    if given_coin == 0:
        return 0

    table = [0] + [given_coin + 1 for i in range(given_coin)]
    # print(table)

    for index in range(0, given_coin + 1):
        for coin in coins:
            if index >= coin:
                table[index] = min(table[index], table[index - coin] + 1)

    return table[index]


out = get_change(10, [1, 5, 10])
print(out)
