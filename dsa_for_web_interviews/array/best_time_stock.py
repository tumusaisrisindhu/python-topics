def max_profit(prices):

    min_price = prices[0]
    profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = max(
            profit,
            price - min_price
        )

    return profit

prices = [7,1,5,3,6,4]

print(max_profit(prices))