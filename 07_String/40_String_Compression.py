def compress_string(s: str) -> str:
    # Your code here
    if not s:
        return s
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            # reset count = 1 for the new current char
            count = 1
    # Add the last group
    compressed.append(s[-1] + str(count))
    compress_str = "".join(compressed)
    # Return whichever is shorter
    return compress_str if len(compress_str) < len(s) else s

if __name__ == "__main__":
    test_cases = [
        "aabcccccaaa",  # Expected: a2b1c5a3
        "abc",          # Expected: abc (no compression)
        "aaa",          # Expected: a3
        "",             # Expected: ""
        "aaabbbccc"     # Expected: a3b3c3
    ]
    
    for s in test_cases:
        result = compress_string(s)
        print(f"'{s}' -> '{result}'")