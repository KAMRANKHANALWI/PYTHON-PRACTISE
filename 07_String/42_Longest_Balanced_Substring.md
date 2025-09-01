# Longest Balanced Substring

## Problem Background
You are analyzing a string consisting only of the characters '(' and ')'. Your task is to find the length of the longest well-balanced substring.

A substring is considered well-balanced if:
1. It has an equal number of opening and closing parentheses.
2. Every closing parenthesis has a corresponding opening parenthesis that occurs before it.

For example, "()" and "(())" are balanced, while ")(" and "(()" are not balanced.

## Problem Statement
You are analyzing a string consisting only of the characters '(' and ')'. Your task is to find the length of the longest well-balanced substring.

A substring is considered well-balanced if:
1. It has an equal number of opening and closing parentheses.
2. Every closing parenthesis has a corresponding opening parenthesis that occurs before it.

For example, "()" and "(())" are balanced, while ")(" and "(()" are not balanced.

## Input Format
* The first line contains a single string s consisting only of the characters '(' and ')'.

## Output Format
* Return an integer - the length of the longest well-balanced substring.

## Example
**Input:**
```
(()
```

**Output:**
```
2
```

**Explanation:**
* The substring "()" is well-balanced and has a length of 2.
* The full string "(())" is not well-balanced because there's an extra open parenthesis.

## Constraints
* 1 ≤ string length ≤ 3 × 10^4
* String contains only '(' and ')' characters
* Empty balanced substring has length 0

## Approach
1. Use two-pass algorithm: left-to-right and right-to-left
2. First pass: count left and right parentheses, reset when right > left
3. Second pass: traverse right-to-left, reset when left > right
4. Track maximum balanced length when left == right in both passes
5. This handles cases where excess opening or closing parentheses appear
6. Achieves O(n) time complexity with O(1) space