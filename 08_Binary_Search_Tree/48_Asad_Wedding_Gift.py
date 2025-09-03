class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(preorder):
    # Complete the function
    idx = 0
    def helper(min, max):
        nonlocal idx
        if idx == len(preorder):
            return None
        
        val = preorder[idx]
        # check if this fits the range
        if val < min or val > max:
            return None
        
        # create node 
        root = Node(val)
        idx += 1
        # build left subtree (everything < root.val)
        root.left = helper(min, root.val)
        #build right subtree (everything > root.val)
        root.right = helper(root.val, max)
        return root
    return helper(float('-inf'), float('inf'))

# Don't touch the below code
INF = int(1e9)

def f(root, flag):
    if not root:
        return (INF, -INF)
    
    lt = f(root.left, flag)
    rt = f(root.right, flag)
    
    if root.val <= lt[1] or root.val >= rt[0]:
        flag[0] = False
    
    return (min(root.val, lt[0], rt[0]), max(root.val, lt[1], rt[1]))

def isBST(root):
    flag = [True]
    f(root, flag)
    return flag[0]

def getPreorderTraversal(root, arr):
    if not root:
        return
    arr.append(root.val)
    getPreorderTraversal(root.left, arr)
    getPreorderTraversal(root.right, arr)

def checkAnswer(root, preorder):
    arr = []
    getPreorderTraversal(root, arr)
    return arr == preorder and isBST(root)

def main():
    n = int(input())
    preorder = list(map(int, input().split()))
    
    root = constructBST(preorder)
    if checkAnswer(root, preorder):
        print("YES", end="")
    else:
        print("NO", end="")

if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # Valid BST preorder: [8, 5, 1, 7, 10]
    test_preorder = [8, 5, 1, 7, 10]
    root = constructBST(test_preorder)
    result = checkAnswer(root, test_preorder)
    print("YES" if result else "NO")
    
    print("\nTest 2:")
    # Another valid BST preorder: [10, 5, 1, 7, 40, 50]
    test_preorder2 = [10, 5, 1, 7, 40, 50]
    root2 = constructBST(test_preorder2)
    result2 = checkAnswer(root2, test_preorder2)
    print("YES" if result2 else "NO")
    
    # Uncomment below for interactive testing
    # main()