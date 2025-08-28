from collections import deque


def generate_binary_numbers(n):
    # Your code here
    result = []
    queue = deque()
    queue.append("1")
    for _ in range(n):
        curr = queue.popleft()
        result.append(curr)
        queue.append(curr + "0")
        queue.append(curr + "1")

    return result


if __name__ == "__main__":
    test_cases = [1, 3, 5, 8]

    for n in test_cases:
        result = generate_binary_numbers(n)
        print(f"n = {n}: {result}")
