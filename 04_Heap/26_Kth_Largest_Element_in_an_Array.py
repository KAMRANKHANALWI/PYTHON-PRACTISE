import heapq

def findKthLargest(nums, k):
    # TODO: Implement this function
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num) # push element into heap
        if len(min_heap) > k:
            heapq.heappop(min_heap) # pop smallest if size > k
    
    return min_heap[0]

if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([1], 1),
        ([1, 2], 1)
    ]
    
    for nums, k in test_cases:
        result = findKthLargest(nums, k)
        print(f"{nums}, k={k} -> {result}")