from collections import deque

def interleave_queue(q: deque[int]) -> list[int]:
    # Your code here
    half = len(q) // 2
    first_half = []
    for _ in range(half):
        first_half.append(q.popleft())
    result = []
    for i in range(half):
        result.append(first_half[i])
        result.append(q.popleft())
    
    return result

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5, 6],
        [11, 12, 13, 14],
        [10, 20]
    ]
    
    for queue_list in test_cases:
        q = deque(queue_list)
        result = interleave_queue(q)
        print(f"{queue_list} -> {result}")