# Generate All Subsequences (Including Empty)

## Problem Background
Subsequence generation is fundamental in bioinformatics for DNA sequence analysis, text processing for finding all possible word combinations, and machine learning feature selection where you need to examine all possible subsets of features. This problem appears in data mining algorithms that analyze all possible patterns within datasets.

## Problem Statement
Given a string, generate all possible subsequences including the empty subsequence using recursion.

A subsequence is a sequence that can be derived from the original string by deleting some or no characters without changing the order of the remaining characters. The empty subsequence is also considered valid.

## Input Format
* A string s containing lowercase English letters

## Output Format
* A list of strings containing all possible subsequences including the empty string

## Example
**Input:**
```
"abc"
```

**Output:**
```
["abc", "ab", "ac", "a", "bc", "b", "c", ""]
```

**Explanation:**
For string "abc", we can form subsequences by including or excluding each character:
- Include all: "abc"
- Include 'a' and 'b': "ab"  
- Include 'a' and 'c': "ac"
- Include only 'a': "a"
- Include 'b' and 'c': "bc"
- Include only 'b': "b"
- Include only 'c': "c"
- Include none: ""

## Constraints
* 1 ≤ length of s ≤ 10
* s contains only lowercase English letters
* Output should contain all unique subsequences
* Order of subsequences in output doesn't matter

## Approach
1. **Recursive Choice Making**: At each character position, make two recursive calls
2. **Include Character**: Add current character to subsequence and recurse to next position
3. **Exclude Character**: Skip current character and recurse to next position  
4. **Base Case**: When index equals string length, add current subsequence to result
5. **Order**: Include choice is made first, then exclude choice (generates include-heavy combinations first)
6. **Complete Exploration**: This generates all 2^n possible combinations through systematic recursion

## Algorithm Steps
```
1. Start with empty subsequence and index 0
2. Base case: if index equals string length, add current subsequence to result
3. For each character at current index:
   a. Include character: recursively call with updated subsequence  
   b. Exclude character: recursively call with same subsequence
4. Return all collected subsequences
```

## Time and Space Complexity
- **Time Complexity**: O(2^n × n) where n is the length of string
  - 2^n subsequences to generate
  - Each subsequence takes O(n) time to build
- **Space Complexity**: O(2^n × n) for storing all subsequences
- **Recursion Depth**: O(n)