# Valid Anagram Substrings

## Problem Background
You are given two strings: a pattern string p and a text string t. Your task is to find all starting indices of substrings in t that are anagrams of p.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once. For example, "listen" and "silent" are anagrams.

Can you efficiently find all positions where anagrams of the pattern appear in the text?

## Problem Statement
You are given two strings: a pattern string p and a text string t. Your task is to find all starting indices of substrings in t that are anagrams of p.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once. For example, "listen" and "silent" are anagrams.

Can you efficiently find all positions where anagrams of the pattern appear in the text?

## Input Format
* The first line contains the pattern string p.
* The second line contains the text string t.
* Both strings consist of lowercase English letters.

## Output Format
* Return a list of integers representing the starting indices (0-indexed) of all anagrams of p in t, in ascending order.

## Example
**Input:**
```
abc
cbaebabacd
```

**Output:**
```
0 6
```

**Explanation:**
* Substring [0:3] = "cba" is an anagram of "abc"
* Substring [6:9] = "bac" is an anagram of "abc"

## Constraints
* 1 ≤ length of p, t ≤ 3 × 10^4
* Both strings contain only lowercase English letters
* Pattern can have duplicate characters

## Approach
1. Use sliding window technique with character frequency counting
2. Maintain frequency count of pattern and current window
3. Slide window across text, updating frequencies efficiently
4. Compare frequency maps to detect anagrams
5. This achieves O(n) time complexity where n is length of text