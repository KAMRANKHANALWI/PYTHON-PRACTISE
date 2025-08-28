import heapq
import math

def k_closest(points, k):
    # Your code here
    heap = []
    for x, y in points:
        d2 = x*x + y*y
        heapq.heappush(heap, (-d2, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    heap.sort(key=lambda t: t[0], reverse=True)   
    return [[x, y] for _, x, y in heap]

if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        ([[1, 1], [1, 1], [1, 1]], 2),
        ([[0, 1], [1, 0]], 2)
    ]
    
    for points, k in test_cases:
        result = k_closest(points, k)
        print(f"{points}, k={k} -> {result}")