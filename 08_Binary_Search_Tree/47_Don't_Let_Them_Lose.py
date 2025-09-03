from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBstToGst(root):
    # Complete the function
    total = 0
    def dfs(node):
        nonlocal total
        if node:
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)
    dfs(root)
    return root

# Don't touch the below code
def getBinaryTree(arr):
    if len(arr) == 0:
        return None, None
    qu = deque()
    root = Node(arr[0])
    qu.append(root)
    ans_first = root
    idx = 1
    while idx < len(arr):
        curr = qu.popleft()
        if arr[idx] == -1:
            curr.left = None
        else:
            curr.left = Node(arr[idx])
            qu.append(curr.left)
        idx += 1
        if idx < len(arr):
            if arr[idx] == -1:
                curr.right = None
            else:
                curr.right = Node(arr[idx])
                qu.append(curr.right)
            idx += 1
    while qu:
        qu.popleft()
    root = Node(arr[0])
    qu.append(root)
    idx = 1
    ans_second = root
    while idx < len(arr):
        curr = qu.popleft()
        if arr[idx] == -1:
            curr.left = None
        else:
            curr.left = Node(arr[idx])
            qu.append(curr.left)
        idx += 1
        if idx < len(arr):
            if arr[idx] == -1:
                curr.right = None
            else:
                curr.right = Node(arr[idx])
                qu.append(curr.right)
            idx += 1
    return ans_first, ans_second

def f(root, sum_ref):
    if root is None:
        return
    f(root.right, sum_ref)
    root.val += sum_ref[0]
    sum_ref[0] = root.val
    f(root.left, sum_ref)

def isSame(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)

def main():
    n = int(input())
    nodeValues = list(map(int, input().split()))
    temp_first, temp_second = getBinaryTree(nodeValues)
    convertBstToGst(temp_first)
    sum_ref = [0]
    f(temp_second, sum_ref)
    if isSame(temp_first, temp_second):
        print("YES", end="")
    else:
        print("NO", end="")

if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # Simple BST: [4, 1, 6, 0, 2, 5, 7]
    test_data = [4, 1, 6, 0, 2, 5, 7]
    tree1, tree2 = getBinaryTree(test_data)
    convertBstToGst(tree1)
    sum_ref = [0]
    f(tree2, sum_ref)
    result = isSame(tree1, tree2)
    print("YES" if result else "NO")
    
    # Uncomment below for interactive testing
    # main()