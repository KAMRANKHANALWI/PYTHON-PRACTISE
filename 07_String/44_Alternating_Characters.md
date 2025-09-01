# Alternating Characters

## Problem Background
You are given a string consisting only of the characters 'A' and 'B'. Your task is to make the string beautiful by removing the minimum number of characters.

A beautiful string is one where no two adjacent characters are the same. For example, "ABA" and "BAB" are beautiful, but "AA" and "BB" are not.

Determine the minimum number of characters to remove to make the string beautiful.

## Problem Statement
You are given a string consisting only of the characters 'A' and 'B'. Your task is to make the string beautiful by removing the minimum number of characters.

A beautiful string is one where no two adjacent characters are the same. For example, "ABA" and "BAB" are beautiful, but "AA" and "BB" are not.

Determine the minimum number of characters to remove to make the string beautiful.

## Input Format
* The first line contains a string s consisting only of the characters 'A' and 'B'.

## Output Format
* Return an integer - the minimum number of characters that must be removed to make the string beautiful.

## Example
**Input:**
```
AAABBB
```

**Output:**
```
4
```

**Explanation:**
To make the string beautiful, we can remove "AAA" from the beginning and "BB" from the end, leaving "AB".
Alternatively, we could remove "AA" from the beginning and "BBB" from the end, leaving "AB".
In both cases, we remove 4 characters.

## Constraints
* 1 ≤ string length ≤ 10^5
* String contains only characters 'A' and 'B'
* Beautiful string has no adjacent identical characters

## Approach
1. Iterate through the string from left to right
2. Count consecutive identical characters
3. For each group of consecutive identical characters, keep only one
4. Total removals = total characters - number of groups
5. This achieves O(n) time complexity with O(1) space