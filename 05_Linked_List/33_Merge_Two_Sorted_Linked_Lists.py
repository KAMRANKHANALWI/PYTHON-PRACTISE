class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
    if list1:
        tail.next = list1
        
    if list2:
        tail.next = list2
        
    return dummy.next

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
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 4], [1, 3, 4]),
        ([], [0]),
        ([], []),
        ([1], [2])
    ]
    
    for arr1, arr2 in test_cases:
        list1 = create_linked_list(arr1)
        list2 = create_linked_list(arr2)
        merged_head = mergeTwoLists(list1, list2)
        result = linked_list_to_array(merged_head)
        print(f"{arr1} + {arr2} -> {result}")