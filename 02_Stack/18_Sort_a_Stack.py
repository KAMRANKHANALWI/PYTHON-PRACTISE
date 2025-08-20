def sort_stack(stack):
    # Please implement this function only
    helper = []
    while stack:
        curr = stack.pop()
        # while helper has elements bigger than curr
        while helper and helper[-1] > curr:
            stack.append(helper.pop())
        helper.append(curr)
        
    return helper[::-1]

if __name__ == "__main__":
    test_cases = [
        [5, 2, 9, 1, 5],
        [3, 1, 4, 2],
        [1],
        []
    ]
    
    for stack in test_cases:
        result = sort_stack(stack.copy())  # copy to preserve original
        print(f"{stack} -> {result}")