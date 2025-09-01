
import collections

def min_window(s: str, t: str) -> str:
    # Your code here
    if not s or not t or len(t) > len(s):
        return ""
        
    t_counts = collections.Counter(t)
    l = r = matches = 0
    required_matches = len(t_counts)
    window_counts = collections.defaultdict(int)
    ans = (float('inf'), 0, 0)
    
    while r < len(s):
        curr_char = s[r]
        window_counts[curr_char] += 1
        if curr_char in t_counts and t_counts[curr_char] == window_counts[curr_char]:
            matches += 1
        
        while l <= r and matches == required_matches:
            to_remove = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            
            window_counts[to_remove] -= 1
            if to_remove in t_counts and window_counts[to_remove] < t_counts[to_remove]:
                matches -= 1
            
            l += 1
        
        r += 1
    
    return s[ans[1]: ans[2] + 1] if ans[0] != float('inf') else ""

if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC"),  # Expected: "BANC"
        ("a", "a"),               # Expected: "a"
        ("a", "aa"),              # Expected: ""
        ("ab", "b")               # Expected: "b"
    ]
    
    for s, t in test_cases:
        result = min_window(s, t)
        print(f"Source: '{s}', Target: '{t}' -> '{result}'")