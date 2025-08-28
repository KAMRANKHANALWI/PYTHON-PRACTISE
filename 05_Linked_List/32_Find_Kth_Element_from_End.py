class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_kth_from_end(head, k):
    # Your code here
    first = head
    second = head
    # Step 1: Move 'first' k steps ahead
    for _ in range(k):
        if not first:
            return -1
        first = first.next
    
    # Step 2: Move both pointers until 'first' reaches the end
    while first:
        first = first.next
        second = second.next
    # Step 3: 'second' is at kth node from end
    return second.value if second else -1

def create_linked_list(arr):
    """Helper function to create linked list from array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),  # Expected: 4
        ([1, 2, 3, 4, 5], 1),  # Expected: 5
        ([1, 2, 3, 4, 5], 5),  # Expected: 1
        ([1], 1),              # Expected: 1
        ([1, 2], 3)            # Expected: -1
    ]
    
    for arr, k in test_cases:
        head = create_linked_list(arr)
        result = find_kth_from_end(head, k)
        print(f"{arr}, k={k} -> {result}")