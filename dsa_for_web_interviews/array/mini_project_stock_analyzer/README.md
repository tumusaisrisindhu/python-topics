# Stock Price Analyzer

A simple Python project that analyzes stock prices using array concepts.

## Features

- Find highest stock price
- Find lowest stock price
- Calculate average price
- Calculate total growth
- Find maximum profit from one buy and one sell

## Project Structure

```text
mini_project_stock_analyzer/
│
├── app.py
├── stock_data.py
├── analyzer.py
└── README.md
```

## How to Run

```bash
python app.py
```

## Sample Data

```python
prices = [100, 105, 103, 120, 115, 125, 130]
```

## Sample Output

```text
===== STOCK ANALYZER =====

Prices: [100, 105, 103, 120, 115, 125, 130]

Highest Price : 130
Lowest Price  : 100
Average Price : 114.00
Total Growth  : 30
Best Profit   : 30
```

## DSA Concepts Used

- Array Traversal → Visit all prices one by one.
- Min/Max Search → Find highest and lowest price.
- Best Time to Buy & Sell Stock → Find maximum profit.
- Time Complexity → O(n)

## What I Learned

- Working with arrays
- Looping through data
- Finding min, max, and average values
- Solving a common interview problem (Best Time to Buy and Sell Stock)
- Organizing code into multiple Python files
