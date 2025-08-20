def max_cash_in_window(cash, k):
    # you just need to implement this function
    # your code here
    # Step 1: initial window sum
    window_sum = sum(cash[:k])
    max_sum = window_sum
    # Step 2: slide the window
    for i in range(k, len(cash)):
        window_sum = window_sum - cash[i - k] + cash[i]
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == "__main__":
    cash = [10, 20, 30, 40, 50, 60]
    k = 3
    result = max_cash_in_window(cash, k)
    print(result)
