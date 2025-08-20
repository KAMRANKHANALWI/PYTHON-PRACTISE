def max_in_rolling_window(prices, k):
    # you need to write the code here
    result = []
    for i in range(len(prices) - k + 1):
        window = prices[i : i + k]
        result.append(max(window))
    return result


if __name__ == "__main__":
    prices = [10, 7, 12, 9, 8, 15]
    k = 3
    result = max_in_rolling_window(prices, k)
    print(result)
