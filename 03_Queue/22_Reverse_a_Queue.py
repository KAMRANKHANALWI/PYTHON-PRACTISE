from collections import deque


def reverse_queue(q):
    # Your code here
    q = deque(q)
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q


if __name__ == "__main__":
    test_cases = [[10, 20, 30, 40, 50], [1, 2, 3], [5], []]

    for queue in test_cases:
        result = reverse_queue(queue.copy())  # copy to preserve original
        print(f"{queue} -> {list(result)}")
