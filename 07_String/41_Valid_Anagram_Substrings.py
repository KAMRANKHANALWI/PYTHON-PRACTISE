from typing import List
from collections import Counter

def find_anagrams(p: str, t: str) -> List[int]:
    # Your code here
    result = []
    m, n = len(p), len(t)
    if m > n:
        return result
    
    # Frequency count of pattern
    p_count = Counter(p)
    # Initial window frequency in text
    window_count = Counter(t[:m])
    # Slide the window across text
    for i in range(n - m + 1):
        if i > 0:
            # Remove the character going out of the window
            window_count[t[i - 1]] -= 1
            if window_count[t[i - 1]] == 0:
                del window_count[t[i - 1]]
            
            # Add the new character entering the window
            window_count[t[i + m - 1]] += 1
        # Compare current window with pattern
        if window_count == p_count:
            result.append(i)
    return result

if __name__ == "__main__":
    test_cases = [
        ("abc", "cbaebabacd"),  # Expected: [0, 6]
        ("ab", "abab"),         # Expected: [0, 1, 2]
        ("abc", "def"),         # Expected: []
        ("a", "aaa")           # Expected: [0, 1, 2]
    ]
    
    for p, t in test_cases:
        result = find_anagrams(p, t)
        print(f"Pattern: '{p}', Text: '{t}' -> {result}")