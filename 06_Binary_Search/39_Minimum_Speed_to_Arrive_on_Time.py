import math

def min_speed_to_arrive(distances, hours):
    # Your code here
    def time_taken(v):
        total = 0
        for i in range(len(distances)):
            if i == len(distances) - 1:
                total += distances[i]/v
            else:
                total += math.ceil(distances[i]/v)
        return total
    
    low, high = 1, 10**7
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if time_taken(mid) <= hours:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

if __name__ == "__main__":
    test_cases = [
        ([1, 3, 2], 6.0),     # Expected: 1
        ([1, 1, 100000], 2.01),  # Expected: 10000000
        ([1, 1, 1], 1.9)      # Expected: -1
    ]
    
    for distances, hours in test_cases:
        result = min_speed_to_arrive(distances, hours)
        print(f"Distances: {distances}, hours={hours} -> {result}")