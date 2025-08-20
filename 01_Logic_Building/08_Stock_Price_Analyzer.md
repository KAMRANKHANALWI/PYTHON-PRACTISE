# Stock Price Analyzer

## Problem Background

You are developing a stock market analysis tool for a financial application. Traders and investors often need to monitor peak stock prices over specific time windows to make better trading decisions. Your task is to implement a feature that analyzes historical stock prices and identifies the maximum price within a moving window.

For instance, in a trading day, the application will take the last k minutes' stock prices as a sliding window and display the highest price during that period. This helps traders quickly spot trends and evaluate opportunities in real time.

## Problem Statement

You are developing a stock market analysis tool for a financial application. Traders and investors often need to monitor peak stock prices over specific time windows to make better trading decisions. Your task is to implement a feature that analyzes historical stock prices and identifies the maximum price within a moving window.

## Input Format

- **prices**: A list of integers representing stock prices at regular intervals.
- **k**: An integer representing the size of the sliding window (number of consecutive intervals).

## Output Format

- Return a list of integers where each element represents the maximum price in the respective sliding window.

## Example

**Input:**

```
prices = [10, 7, 12, 9, 8, 15]
k = 3
```

**Output:**

```
[12, 12, 12, 15]
```

**Explanation:**

- Window [10,7,12] -> max = 12
- Window [7,12,9] -> max = 12
- Window [12,9,8] -> max = 12
- Window [9,8,15] -> max = 15

## Constraints

- 1 ≤ prices.length ≤ 10^5
- 1 ≤ k ≤ prices.length
- 0 ≤ prices[i] ≤ 10^4

## Approach

1. Use a sliding window approach to examine each consecutive k elements
2. For each window, find the maximum value
3. Store the maximum in result array
4. Move window one position right and repeat
5. This achieves O(n\*k) time complexity
