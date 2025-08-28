from collections import Counter
import heapq

def topKFrequent(nums, k):
    # TODO: Implement this function
    freq_map = Counter(nums)
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    result = sorted(heap, key=lambda x: -x[0])
    return [num for freq, num in result]

if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([1, 2], 2),
        ([4, 1, -1, 2, -1, 2, 3], 2)
    ]
    
    for nums, k in test_cases:
        result = topKFrequent(nums, k)
        print(f"{nums}, k={k} -> {result}")