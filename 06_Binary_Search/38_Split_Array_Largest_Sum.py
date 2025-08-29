def split_array(nums, m):
    # Your code here
    def can_split(nums, m, target):
        count = 1
        curr_sum = 0
        for num in nums:
            if curr_sum + num > target:
                count += 1
                curr_sum = num
                if count > m:
                    return False
            else:
                curr_sum += num
        return True
    
    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if can_split(nums, m, mid):
            high = mid
        else:
            low = mid + 1
    
    return low

if __name__ == "__main__":
    test_cases = [
        ([7, 2, 5, 10, 8], 3),    # Expected: 14
        ([1, 2, 3, 4, 5], 2),     # Expected: 9
        ([1, 4, 4], 3),           # Expected: 4
        ([1, 1, 2], 2)            # Expected: 2
    ]
    
    for nums, m in test_cases:
        result = split_array(nums, m)
        print(f"Array: {nums}, m={m} -> {result}")