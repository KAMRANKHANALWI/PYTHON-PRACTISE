class MinStack:
    def __init__(self):
        # Your code here
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        # Your code here
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
    
    def pop(self) -> int:
        # Your code here
        if not self.stack:
            return -1
        self.min_stack.pop()
        return self.stack.pop()
    
    def top(self) -> int:
        # Your code here
        if not self.stack:
            return -1
        return self.stack[-1]
    
    def getMin(self) -> int:
        # Your code here
        if not self.min_stack:
            return -1
        return self.min_stack[-1]

if __name__ == "__main__":
    # Test the MinStack
    stack = MinStack()
    
    # Test operations
    operations = [
        ("push", 5),
        ("push", 2), 
        ("push", 4),
        ("getMin", None),
        ("pop", None),
        ("getMin", None),
        ("top", None)
    ]
    
    results = []
    for op, val in operations:
        if op == "push":
            stack.push(val)
            results.append(-1)
        elif op == "pop":
            results.append(stack.pop())
        elif op == "top":
            results.append(stack.top())
        elif op == "getMin":
            results.append(stack.getMin())
    
    print(f"Results: {results}")