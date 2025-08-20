# Valid Parentheses

## Problem Background

You're working on a code editor feature that needs to validate if the brackets in a piece of code are properly balanced. In programming languages, brackets must open and close in the correct order. Implement a function that checks if a given string of brackets `{ [ ( ) ] }` is valid. A string is valid if:

This skill is crucial for code linters, IDEs, and compiler design!

## Problem Statement

You're working on a code editor feature that needs to validate if the brackets in a piece of code are properly balanced. In programming languages, brackets must open and close in the correct order. Implement a function that checks if a given string of brackets `{ [ ( ) ] }` is valid.

A string is valid if:

1. Open brackets must be closed by the same type of bracket
2. Open brackets must be closed in the correct order
3. Every closing bracket has a corresponding open bracket of the same type

## Input Format

- A string containing only parentheses characters: `(` and `)`

## Output Format

- Return `true` if the string is valid, `false` otherwise

## Example

**Input:**

```
"()"
```

**Output:**

```
true
```

**Input:**

```
"()[]{}"
```

**Output:**

```
true
```

**Input:**

```
"(]"
```

**Output:**

```
false
```

## Explanation

- `"()"` → `true` (properly opened and closed)
- `"()[]{}"` → `true` (multiple valid pairs)
- `"(]"` → `false` (mismatched brackets)

## Constraints

- String length can be 0 to 10^4
- String contains only parentheses characters
- Empty string is considered valid

## Approach

1. Use a stack data structure to track opening brackets
2. For each opening bracket, push it onto the stack
3. For each closing bracket, check if it matches the most recent opening bracket
4. Pop from stack when a valid pair is found
5. String is valid if stack is empty at the end
6. This achieves O(n) time complexity with O(n) space
