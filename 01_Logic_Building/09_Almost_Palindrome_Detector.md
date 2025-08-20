# Almost Palindrome Detector

## Problem Background

Developers often struggle naming variables. Companies like JetBrains and Microsoft use smart naming suggestions in their IDEs to improve code readability. You're building a smart code editor that helps developers choose variable names. The editor suggests palindromic variable names (like "level" or "radar") as they're easy to remember. Your feature should detect if a string can become a palindrome by removing just one character.

## Problem Statement

Developers often struggle naming variables. Companies like JetBrains and Microsoft use smart naming suggestions in their IDEs to improve code readability. You're building a smart code editor that helps developers choose variable names. The editor suggests palindromic variable names (like "level" or "radar") as they're easy to remember. Your feature should detect if a string can become a palindrome by removing just one character.

## Input Format

- A single string (s) (length: (|s| <= 10^5)).
- The string contains only lowercase letters ('a' to 'z').

## Output Format

- Return `true` if the string can become a palindrome by removing at most one character, otherwise return `false`.

## Example

**Input:**

```
racecar
```

**Output:**

```
true
```

## Example 2

**Input:**

```
abccba
```

**Output:**

```
true
```

## Constraints

1. (1 <= |s| length of s<= 10^5)
2. The input string (s) contains only lowercase alphabets.
3. Strings are guaranteed to have a minimum length of 1.

## Approach

1. Use two pointers from start and end of string
2. When characters don't match, try skipping either left or right character
3. Check if remaining substring is palindrome in both cases
4. Return true if either option results in palindrome
5. This achieves O(n) time complexity
