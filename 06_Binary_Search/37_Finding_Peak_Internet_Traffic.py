def find_peak_traffic(arr):
    # Your code here
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            # peak is on the right side
            low = mid + 1
        else:
            # peak is at mid or on the left side
            high = mid 
        
    return low # low == high at the end

if __name__ == "__main__":
    test_cases = [
        [1, 3, 5, 7, 6, 4, 2],    # Expected: 3
        [10, 20, 30, 40, 50],     # Expected: 4  
        [50, 40, 30, 20, 10],     # Expected: 0
        [1, 2, 1],                # Expected: 1
        [5]                       # Expected: 0
    ]
    
    for arr in test_cases:
        result = find_peak_traffic(arr)
        print(f"Array: {arr} -> Peak at index {result} (value: {arr[result]})")