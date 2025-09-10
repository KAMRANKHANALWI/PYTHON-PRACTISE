# Generate All Non-Empty Subsequences

## Problem Background
You're building a search suggestion system that needs to generate all possible non-empty subsequences of user queries to provide relevant autocomplete options. This problem is crucial in information retrieval systems, pattern matching algorithms, and natural language processing where empty results are not meaningful and should be filtered out.

## Problem Statement
Given a string, generate all possible non-empty subsequences using recursion.

A subsequence is a sequence that can be derived from the original string by deleting some or no characters without changing the order of the remaining characters. The empty subsequence should be excluded from the result.

## Input Format
* A string s containing lowercase English letters

## Output Format
* A list of strings containing all possible non-empty subsequences

## Example
**Input:**
```
"abc"
```

**Output:**
```
["a", "b", "c", "ab", "ac", "bc", "abc"]
```

**Explanation:**
For string "abc", we can form non-empty subsequences by including or excluding each character, but we exclude the empty subsequence:
- Include only 'a': "a"
- Include only 'b': "b"
- Include only 'c': "c"
- Include 'a' and 'b': "ab"
- Include 'a' and 'c': "ac"
- Include 'b' and 'c': "bc"
- Include all: "abc"
- Empty subsequence "" is excluded

## Constraints
* 1 ≤ length of s ≤ 10
* s contains only lowercase English letters
* Output should contain all unique non-empty subsequences
* Order of subsequences in output doesn't matter

## Approach
1. Use backtracking to explore all possibilities for each character
2. At each position, make two recursive calls:
   - Include the current character in the subsequence
   - Exclude the current character from the subsequence
3. Base case: when we've processed all characters, add the current subsequence to result only if it's non-empty
4. Alternative approach: Generate all subsequences and filter out the empty one
5. This generates all 2^n - 1 possible non-empty combinations through recursive exploration

## Algorithm Steps
```
1. Start with empty subsequence and index 0
2. Base case: if index equals string length
   a. If current subsequence is non-empty, add to result
   b. Return
3. For each character at current index:
   a. Include character: recursively call with updated subsequence
   b. Exclude character: recursively call with same subsequence
4. Return all collected non-empty subsequences
```

## Time and Space Complexity
- **Time Complexity**: O(2^n × n) where n is the length of string
  - 2^n subsequences to generate
  - Each subsequence takes O(n) time to build
- **Space Complexity**: O(2^n × n) for storing all non-empty subsequences
- **Recursion Depth**: O(n)