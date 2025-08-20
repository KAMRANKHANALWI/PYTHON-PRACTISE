import json


def max_traffic_flow(traffic_flow, k):
    # Your code here
    # Step 1: sum of first k elements
    window_sum = sum(traffic_flow[:k])
    max_sum = window_sum
    # Step 2: slide the window
    for i in range(k, len(traffic_flow)):
        window_sum = window_sum - traffic_flow[i - k] + traffic_flow[i]
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == "__main__":
    traffic_flow, k = [10, 20, 30, 40, 50], 3
    result = max_traffic_flow(traffic_flow, k)
    print(result)
