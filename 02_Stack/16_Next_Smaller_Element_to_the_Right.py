# Please implement this function only
def nextSmallerElement(arr):
    # Your code here
    n = len(arr)
    result = [-1] * n
    stack = []
    # Scan form right to left
    for i in range(n-1, -1, -1):
        # Pop equal or larger elements
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        # If stack not empty → top is next smaller
        if stack:
            result[i] = stack[-1]
        # Push current element
        stack.append(arr[i])
    
    return result

if __name__ == "__main__":
    test_cases = [
        [4, 5, 2, 10, 8],
        [1, 3, 2, 4],
        [5, 4, 3, 2, 1],
        []
    ]
    
    for arr in test_cases:
        result = nextSmallerElement(arr)
        print(f"{arr} -> {result}")