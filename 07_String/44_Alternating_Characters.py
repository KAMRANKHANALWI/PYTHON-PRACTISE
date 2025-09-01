def min_removal(s: str) -> int:
    # Your code here
    removals = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            removals += 1
    return removals

if __name__ == "__main__":
    test_cases = [
        "AAABBB",    # Expected: 4
        "ABABAB",    # Expected: 0
        "A",         # Expected: 0
        "AAAAAA",    # Expected: 5
        "ABABABA"    # Expected: 0
    ]
    
    for s in test_cases:
        result = min_removal(s)
        print(f"'{s}' -> {result}")