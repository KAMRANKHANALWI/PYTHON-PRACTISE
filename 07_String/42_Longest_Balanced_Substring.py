def longest_balanced_substring(s: str) -> int:
    # Your code here
    l_count = r_count = max_len = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            l_count += 1
        else:
            r_count += 1
        
        if l_count == r_count:
            max_len = max(max_len, l_count + r_count)
        elif r_count > l_count:
            l_count = r_count = 0
        i+=1
    
    l_count = r_count = 0
    i = len(s) - 1
    while i >= 0:
        if s[i] == "(":
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            max_len = max(max_len, l_count + r_count)
        elif l_count > r_count:
            l_count = r_count = 0
        
        i-=1
    return max_len

if __name__ == "__main__":
    test_cases = [
        "(()",     # Expected: 2
        "())",     # Expected: 2
        "((()))",  # Expected: 6
        ")(",      # Expected: 0
        "()()"     # Expected: 4
    ]
    
    for s in test_cases:
        result = longest_balanced_substring(s)
        print(f"'{s}' -> {result}")