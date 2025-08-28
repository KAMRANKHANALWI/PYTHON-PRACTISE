import heapq

def kthSmallest(matrix, k):
    # Your code here
    n = len(matrix)
    heap = []
    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))
    count = 0
    while heap:
        val, r, c = heapq.heappop(heap)
        count += 1
        if count == k:
            return val
        
        # If there's a next element in the row, push it
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

if __name__ == "__main__":
    test_cases = [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),
        ([[1, 2], [1, 3]], 2),
        ([[1, 2], [1, 3]], 3),
        ([[-5]], 1)
    ]
    
    for matrix, k in test_cases:
        result = kthSmallest(matrix, k)
        print(f"Matrix: {matrix}, k={k} -> {result}")