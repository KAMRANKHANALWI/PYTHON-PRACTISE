def find_kth_missing(arr, k):
    # Your code here
    n = len(arr)
    left, right = 0, n - 1
    def missing(i):
        # how many positives are missing before arr[i]
        return arr[i] - (i + 1)
    # find first index with missing(i) >= k
    while left <= right:
        mid = (left + right) // 2
        if missing(mid) < k:
            left = mid + 1
        else:
            right = mid - 1
    
    # left is the count of array elements <= the answer
    return k + left

if __name__ == "__main__":
    test_cases = [
        ([2, 3, 4, 7, 11], 5),  # Expected: 9
        ([1, 2, 3, 4], 2),      # Expected: 6
        ([2], 1),               # Expected: 1
        ([1, 3, 5], 3)          # Expected: 6
    ]
    
    for arr, k in test_cases:
        result = find_kth_missing(arr, k)
        print(f"Array: {arr}, k={k} -> {result}")