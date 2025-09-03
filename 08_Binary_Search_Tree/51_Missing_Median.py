from collections import deque
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)

def solve(root, L, R):
    # Complete the function
    # Step 1: Collect BST values
    vals = []
    inorder(root, vals)
    
    # Step 2: Filter values in [L, R]
    present = [x for x in vals if L <= x <= R]
    present_set = set(present)
    
    # Step 3: Collect missing numbers
    missing = [num for num in range(L, R+1) if num not in present_set]
    
    if not missing:
        return -1
    
    n = len(missing)
    mid = n // 2
    
    if n % 2 == 1:
        return missing[mid]  # odd case
    else:
        return min(missing[mid-1], missing[mid])  # even case → smaller of two middle

# Don't touch the below code
def buildTree(input):
    if not input or input[0] == -1:
        return None
    root = TreeNode(input[0])
    q = deque([root])
    i = 1
    while q and i < len(input):
        curr = q.popleft()
        if i < len(input) and input[i] != -1:
            curr.left = TreeNode(input[i])
            q.append(curr.left)
        i += 1
        if i < len(input) and input[i] != -1:
            curr.right = TreeNode(input[i])
            q.append(curr.right)
        i += 1
    return root

def main():
    input = sys.stdin.read().splitlines()
    M = int(input[0])
    nodeValues = list(map(int, input[1].split()))
    L, R = map(int, input[2].split())
    root = buildTree(nodeValues)
    print(solve(root, L, R), end="")

if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # BST with values [5, 2, 7, -1, -1, -1, 10]
    # Contains: {2, 5, 7, 10}
    # Range [1, 10]: Missing {1, 3, 4, 6, 8, 9}
    # Count = 6 (even), middle elements are missing[2]=4 and missing[3]=6
    # Return smaller: 4
    test_values = [5, 2, 7, -1, -1, -1, 10]
    root = buildTree(test_values)
    result = solve(root, 1, 10)
    print(result)  # Should print 4
    
    print("\nTest 2:")
    # Odd number of missing elements
    test_values2 = [4, 2, 6, 1, 3, 5, 7]
    root2 = buildTree(test_values2)
    result2 = solve(root2, 1, 9)
    print(result2)  # Missing {8, 9}, count=2 (even), return min(8,9)=8
    
    print("\nTest 3:")
    # No missing numbers
    test_values3 = [3, 2, 4, 1, -1, -1, 5]
    root3 = buildTree(test_values3)
    result3 = solve(root3, 1, 5)
    print(result3)  # Should print -1
    
    # Uncomment below for interactive testing
    # main()