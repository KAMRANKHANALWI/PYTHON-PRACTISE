class Node:
    def __init__(self, id=-1, name="", left=None, right=None):
        self.ID = id  # Cell ID
        self.name = name  # Prisoner Name
        self.left = left
        self.right = right

def check(root, cellId):
    # Complete the function
    curr = root
    while curr:
        if cellId == curr.ID:
            # Found the cell
            if curr.name == "Akash":
                return "Help!!!"
            else:
                return "Hurrah!!!"
        elif cellId < curr.ID:
            curr = curr.left
        else:
            curr = curr.right
    
    # Cell ID not found
    return "Wrong Jail"

# Don't touch the below code
# Building the tree
def getBinaryTree(arr):
    if not arr:
        return None
    from collections import deque
    qu = deque()
    root = Node(arr[0][0], arr[0][1])
    qu.append(root)
    idx = 1
    while idx < len(arr):
        curr = qu.popleft()
        if arr[idx][0] == -1:
            curr.left = None
        else:
            curr.left = Node(arr[idx][0], arr[idx][1])
            qu.append(curr.left)
        idx += 1
        if idx < len(arr) and arr[idx][0] == -1:
            curr.right = None
        elif idx < len(arr):
            curr.right = Node(arr[idx][0], arr[idx][1])
            qu.append(curr.right)
        idx += 1
    return root

if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # Simulating the example: cells with (ID, Name)
    test_data = [(1000, "Priyo"), (300, "Ayan"), (1010, "Akash")]
    root = getBinaryTree(test_data)
    result = check(root, 1010)
    print(result)  # Should print "Help!!!"
    
    print("\nTest 2:")
    result2 = check(root, 300)
    print(result2)  # Should print "Hurrah!!"
    
    print("\nTest 3:")
    result3 = check(root, 9999)
    print(result3)  # Should print "Wrong Jail"
    
    # Uncomment below for interactive testing
    # import sys
    # input = sys.stdin.read
    # data = input().splitlines()
    # 
    # n = int(data[0])
    # nodeValues = []
    # for i in range(1, n + 1):
    #     id, name = data[i].split()
    #     nodeValues.append((int(id), name))
    # 
    # rootNode = getBinaryTree(nodeValues)
    # cellId = int(data[n + 1])
    # print(check(rootNode, cellId), end="")