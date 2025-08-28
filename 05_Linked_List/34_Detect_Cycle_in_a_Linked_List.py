class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def detectCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False

def create_linked_list_with_cycle(arr, cycle_pos):
    """Helper function to create linked list with potential cycle"""
    if not arr:
        return None
    
    # Create nodes
    nodes = []
    for val in arr:
        nodes.append(ListNode(val))
    
    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if specified
    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]
    
    return nodes[0]

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 1),   # Cycle: 5 -> 2
        ([1, 2, 3, 4, 5], -1),  # No cycle
        ([1], -1),              # Single node, no cycle
        ([1, 2], 0),            # Cycle: 2 -> 1
        ([], -1)                # Empty list
    ]
    
    for arr, cycle_pos in test_cases:
        head = create_linked_list_with_cycle(arr, cycle_pos)
        result = detectCycle(head)
        cycle_info = f"cycle at pos {cycle_pos}" if cycle_pos >= 0 else "no cycle"
        print(f"{arr} ({cycle_info}) -> {'true' if result else 'false'}")