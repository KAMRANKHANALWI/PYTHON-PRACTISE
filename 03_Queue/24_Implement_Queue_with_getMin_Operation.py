from collections import deque

class MinQueue:
    def __init__(self):
        self.q = deque()
        self.min_q = deque()
    
    def enqueue(self, x: int) -> None:
        # Your code here
        self.q.append(x)
        # Maintain min_q in increasing order
        while self.min_q and self.min_q[-1] > x:
            self.min_q.pop()
        self.min_q.append(x)
    
    def dequeue(self) -> int:
        # Your code here
        if not self.q:
            return -1
        val = self.q.popleft()
        # Cascade delete from min_q if needed
        if self.min_q and val == self.min_q[0]:
            self.min_q.popleft()
        
        return val
    
    def peek(self) -> int:
        # Your code here
        return self.q[0]
    
    def getMin(self) -> int:
        # Your code here
        if not self.min_q:
            return -1
        return self.min_q[0]
    
    def isEmpty(self) -> bool:
        # Your code here
        return len(self.q) == 0
    
    def size(self) -> int:
        # Your code here
        return len(self.q)

if __name__ == "__main__":
    # Test the MinQueue
    queue = MinQueue()
    
    # Test operations
    operations = [
        ("enqueue", 3),
        ("enqueue", 1),
        ("enqueue", 5),
        ("getMin", None),
        ("dequeue", None),
        ("getMin", None),
        ("peek", None)
    ]
    
    results = []
    for op, val in operations:
        if op == "enqueue":
            queue.enqueue(val)
            results.append(None)
        elif op == "dequeue":
            results.append(queue.dequeue())
        elif op == "peek":
            results.append(queue.peek())
        elif op == "getMin":
            results.append(queue.getMin())
        elif op == "isEmpty":
            results.append(queue.isEmpty())
        elif op == "size":
            results.append(queue.size())
    
    print(f"Results: {results}")