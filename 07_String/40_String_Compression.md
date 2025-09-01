# String Compression

## Problem Background
You are working on a file compression algorithm. As part of this process, you need to implement a basic string compression method that replaces consecutive repeated characters with the character followed by the count of repetitions.

For example, the string "aabcccccaaa" would become "a2b1c5a3".

If the compressed string is not smaller than the original string, your method should return the original string.

Your task is to implement this compression algorithm.

## Problem Statement
You are working on a file compression algorithm. As part of this process, you need to implement a basic string compression method that replaces consecutive repeated characters with the character followed by the count of repetitions.

For example, the string "aabcccccaaa" would become "a2b1c5a3".

If the compressed string is not smaller than the original string, your method should return the original string.

Your task is to implement this compression algorithm.

## Input Format
* The first line contains a string s consisting of uppercase and lowercase English letters.

## Output Format
* Return the compressed string if it is smaller than the original string, otherwise return the original string.

## Example
**Input:**
```
aabcccccaaa
```

**Output:**
```
a2b1c5a3
```

**Explanation:**
* 'aa' becomes 'a2'
* 'b' becomes 'b1'  
* 'ccccc' becomes 'c5'
* 'aaa' becomes 'a3'
* The compressed string 'a2b1c5a3' is shorter than the original 'aabcccccaaa', so it is returned.

## Constraints
* String length can be 0 to 10^4
* String contains only English letters (uppercase and lowercase)
* Return original string if compression doesn't reduce length

## Approach
1. Iterate through string counting consecutive identical characters
2. Build compressed string by appending character + count
3. Compare lengths and return shorter version
4. Handle edge cases like empty strings
5. This achieves O(n) time complexity with O(n) space for result