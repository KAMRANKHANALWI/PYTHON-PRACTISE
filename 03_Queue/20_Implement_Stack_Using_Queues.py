from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Your code here
        # Step 1: enqueue into q2
        self.q2.append(x)
        # Step 2: move all elements from q1 -> q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # Your code here
        if not self.q1:
            return None
        return self.q1.popleft()

    def top(self):
        # Your code here
        if not self.q1:
            return None
        return self.q1[0]

    def isEmpty(self):
        # Your code here
        return len(self.q1) == 0

    def size(self):
        # Your code here
        return len(self.q1)


if __name__ == "__main__":
    # Test the StackUsingQueues
    stack = StackUsingQueues()

    # Test operations
    operations = [
        ("push", 1),
        ("push", 2),
        ("top", None),
        ("pop", None),
        ("size", None),
    ]

    results = []
    for op, val in operations:
        if op == "push":
            stack.push(val)
            results.append(None)
        elif op == "pop":
            results.append(stack.pop())
        elif op == "top":
            results.append(stack.top())
        elif op == "isEmpty":
            results.append(stack.isEmpty())
        elif op == "size":
            results.append(stack.size())

    print(f"Results: {results}")
