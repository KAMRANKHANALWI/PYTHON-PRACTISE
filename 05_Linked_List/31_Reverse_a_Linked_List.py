class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    # Your code here
    prev = None
    curr = head
    while curr:
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr
    return prev

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

def linked_list_to_array(head):
    """Helper function to convert linked list to array for display"""
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        []
    ]
    
    for arr in test_cases:
        head = create_linked_list(arr)
        new_head = reverse_linked_list(head)
        result = linked_list_to_array(new_head)
        print(f"{arr} -> {result}")