from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solve(root, L, R):
    def collect_in_range(node):
        if not node:
            return []
        result = []
        if node.val > L:
            result += collect_in_range(node.left)
        if L <= node.val <= R:
            result.append(node.val)
        if node.val < R:
            result += collect_in_range(node.right)
        return result

    def sum_range(a, b):
        if a > b:
            return 0
        return (b * (b + 1)) // 2 - ((a - 1) * a) // 2

    nodes = collect_in_range(root)
    present_sum = sum(nodes)
    full_sum = sum_range(L, R)
    return full_sum - present_sum

def buildTree(values):
    if not values or values[0] == -1:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] != -1:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != -1:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # BST with values [5, 2, 7, -1, -1, -1, 10]
    # Contains: {2, 5, 7, 10}
    # Range [1, 10]: Sum should be 55, present sum = 2+5+7+10 = 24
    # Missing sum = 55 - 24 = 31
    test_values = [5, 2, 7, -1, -1, -1, 10]
    root = buildTree(test_values)
    result = solve(root, 1, 10)
    print(result)  # Should print 31
    
    print("\nTest 2:")
    # Complete BST in range
    test_values2 = [3, 2, 4, 1, -1, -1, 5]
    root2 = buildTree(test_values2)
    result2 = solve(root2, 1, 5)
    print(result2)  # Should print 0 (no missing numbers)
    
    print("\nTest 3:")
    # Empty BST
    root3 = buildTree([])
    result3 = solve(root3, 1, 5)
    print(result3)  # Should print 15 (1+2+3+4+5)
    
    # Uncomment below for interactive testing
    # N = int(input())
    # values = list(map(int, input().split()))
    # L, R = map(int, input().split())
    # root = buildTree(values)
    # print(solve(root, L, R), end='')