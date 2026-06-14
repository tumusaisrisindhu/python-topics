def total_growth(prices):
    return prices[-1] - prices[0]


def highest_price(prices):
    return max(prices)


def lowest_price(prices):
    return min(prices)


def average_price(prices):
    return sum(prices) / len(prices)


def best_profit(prices):

    min_price = prices[0]
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit