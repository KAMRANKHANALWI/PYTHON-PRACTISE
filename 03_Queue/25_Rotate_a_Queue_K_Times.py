from collections import deque


class QueueRotator:
    def __init__(self, arr: list[int]):
        self.q = deque(arr)

    def rotate(self, k: int) -> list[int]:
        # Handle empty queue
        if not self.q:
            return []
        k = k % len(self.q)
        first_part = []
        for i in range(k):
            first_part.append(self.q[i])
        second_part = []
        for i in range(k, len(self.q)):
            second_part.append(self.q[i])
        rotated = []
        for x in second_part:
            rotated.append(x)
        for x in first_part:
            rotated.append(x)
        return rotated


if __name__ == "__main__":
    test_cases = [
        ([10, 20, 30, 40, 50], 3),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3], 5),  # k > length
        ([], 3),  # empty queue
    ]

    for arr, k in test_cases:
        qr = QueueRotator(arr)
        result = qr.rotate(k)
        print(f"{arr} rotated {k} times -> {result}")
