# Minimum Window Substring

## Problem Background
You are given two strings: a source string s and a target string t. Your task is to find the minimum window (substring) in s that contains all the characters from t, including duplicates.

If there is no such window, return an empty string.

If there are multiple windows with the minimum length, return any one of them.

## Problem Statement
You are given two strings: a source string s and a target string t. Your task is to find the minimum window (substring) in s that contains all the characters from t, including duplicates.

If there is no such window, return an empty string.

If there are multiple windows with the minimum length, return any one of them.

## Input Format
* The first line contains the source string s.
* The second line contains the target string t.
* Both strings consist of uppercase and lowercase English letters.

## Output Format
* Return the minimum window substring that contains all characters from t. If no such substring exists, return an empty string.

## Example
**Input:**
```
ADOBECODEBANC
ABC
```

**Output:**
```
BANC
```

**Explanation:**
"BANC" is the minimum window in s that contains all characters from t ('A', 'B', and 'C').

## Constraints
* 1 ≤ string lengths ≤ 10^5
* Strings contain uppercase and lowercase English letters
* Target string can have duplicate characters that must all be covered

## Approach
1. Use sliding window technique with two pointers (left and right)
2. Expand right pointer to include characters until all target chars are covered
3. Contract left pointer while maintaining all target characters in window
4. Track minimum window size and update answer when smaller window found
5. Use hash maps to count character frequencies efficiently
6. This achieves O(|s| + |t|) time complexity