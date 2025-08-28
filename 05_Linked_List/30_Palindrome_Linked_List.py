class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def isPalindrome(head):
    # Your code here
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle using slow/fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    second_half = reverse_list(slow)
    # Step 3: Compare first half and reversed second half
    first_half = head
    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

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
        [1, 2, 2, 1],
        [1, 2, 3],
        [1],
        [],
        [1, 2, 3, 2, 1]
    ]
    
    for arr in test_cases:
        head = create_linked_list(arr)
        result = isPalindrome(head)
        print(f"{arr} -> {'true' if result else 'false'}")