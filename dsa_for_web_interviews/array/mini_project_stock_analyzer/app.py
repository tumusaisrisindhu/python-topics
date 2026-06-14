from stock_data import prices
from analyzer import *

print("===== STOCK ANALYZER =====")

print(f"Prices: {prices}")

print(f"Highest Price : {highest_price(prices)}")
print(f"Lowest Price  : {lowest_price(prices)}")
print(f"Average Price : {average_price(prices):.2f}")
print(f"Total Growth  : {total_growth(prices)}")
print(f"Best Profit   : {best_profit(prices)}")