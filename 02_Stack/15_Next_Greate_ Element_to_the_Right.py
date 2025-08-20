# Please implement this function only
def nextGreaterElement(arr):
    # Your code here
    n = len(arr)
    result = [-1] * n
    stack = []
    # Traverse from right to left
    for i in range(n-1, -1, -1):
        # Pop equal or smaller element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        # If stack not empty → top is next greater
        if stack:
            result[i] = stack[-1]
        # Push current element
        stack.append(arr[i]) 
        
    return result

if __name__ == "__main__":
    test_cases = [
        [4, 5, 2, 25],
        [1, 3, 2, 4],
        [13, 7, 6, 12],
        []
    ]
    
    for arr in test_cases:
        result = nextGreaterElement(arr)
        print(f"{arr} -> {result}")