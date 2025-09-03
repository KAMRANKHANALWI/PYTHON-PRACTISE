class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBst(root):
    # Complete the function
    def helper(node, min_val, max_val):
        # Empty node is valid
        if not node:
            return True

        # Current node must lie in (min_val, max_val)
        if not (min_val < node.val < max_val):
            return False

        # Recurse left and right with updated ranges
        return helper(node.left, min_val, node.val) and helper(
            node.right, node.val, max_val
        )

    # Start with the widest possible range
    return helper(root, float("-inf"), float("inf"))


def get_binary_tree(arr):
    if not arr:
        return None
    from collections import deque

    qu = deque()
    root = Node(arr[0])
    qu.append(root)
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
    return root


def main():
    n = int(input())
    node_values = list(map(int, input().split()))
    tree = get_binary_tree(node_values)
    if isBst(tree):
        print("YES", end="")
    else:
        print("NO", end="")


if __name__ == "__main__":
    # Test cases
    print("Test 1:")
    # Simulating input: 7\n8 3 10 1 6 14 4
    test_tree = get_binary_tree([8, 3, 10, 1, 6, 14, 4])
    result = isBst(test_tree)
    print("YES" if result else "NO")

    print("\nTest 2:")
    # Invalid BST test
    test_tree2 = get_binary_tree([5, 3, 8, 2, 7, 6, 9])
    result2 = isBst(test_tree2)
    print("YES" if result2 else "NO")

    # Uncomment below for interactive testing
    # main()
