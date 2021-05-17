def amazon_stock(prices):
    min_stock_price = prices[0]
    max_profit = 0

    for price in prices:
        min_stock_price = min(min_stock_price, price)  # 3
        comparison_profit = price - min_stock_price  # 7
        max_profit = max(max_profit, comparison_profit)  # 7

    return max_profit


out = amazon_stock([12, 11, 15, 3, 10])
print(out)
