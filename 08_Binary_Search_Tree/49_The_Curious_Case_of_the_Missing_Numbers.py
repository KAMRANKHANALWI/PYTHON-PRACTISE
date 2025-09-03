from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def solve(root, L, R, K):
    # Enter Your Code Here
    vals = inorder(root)
    present = [x for x in vals if L <= x <= R]
    present_set = set(present)
    count = 0
    for num in range(L, R+1):
        if num not in present_set:
            count += 1
            if count == K:
                return num
    return -1

# Don't change any code outside the solve function
def build_tree(values):
    if not values or values[0] == -1:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        curr = queue.popleft()
        
        if i < len(values) and values[i] != -1:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1
        
        if i < len(values) and values[i] != -1:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1
    
    return root

if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # BST with values [5, 2, 7, -1, -1, -1, 10]
    # Contains: {2, 5, 7, 10}
    # Range [1, 10]: Missing {1, 3, 4, 6, 8, 9}
    # 3rd missing = 4
    test_values = [5, 2, 7, -1, -1, -1, 10]
    root = build_tree(test_values)
    result = solve(root, 1, 10, 3)
    print(result)  # Should print 4
    
    print("\nTest 2:")
    # Empty BST case
    root2 = build_tree([])
    result2 = solve(root2, 1, 5, 2)
    print(result2)  # Should print 2 (1st missing = 1, 2nd missing = 2)
    
    print("\nTest 3:")
    # No missing numbers case
    test_values3 = [3, 2, 4, 1, -1, -1, 5]
    root3 = build_tree(test_values3)
    result3 = solve(root3, 1, 5, 1)
    print(result3)  # Should print -1 (no missing numbers)
    
    # Uncomment below for interactive testing
    # N = int(input())
    # input_values = list(map(int, input().split()))
    # L, R, K = map(int, input().split())
    # root = build_tree(input_values)
    # print(solve(root, L, R, K), end="")