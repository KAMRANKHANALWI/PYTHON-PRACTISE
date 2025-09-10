# Generate Parentheses

## Problem Background
Parentheses generation is crucial in compiler design, expression parsing, and syntax validation systems where you need to enumerate all well-formed bracket sequences programmatically. This problem appears in code formatters, mathematical expression builders, and automated test case generation for parser validation.

## Problem Statement
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

A well-formed parentheses string is one where:
1. Every opening parenthesis has a corresponding closing parenthesis
2. Parentheses are properly nested (no crossing)
3. Every closing parenthesis has a matching opening parenthesis before it

## Input Format
* An integer n representing the number of pairs of parentheses

## Output Format
* A list of strings containing all valid combinations of parentheses

## Example
**Input:**
```
3
```

**Output:**
```
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

**Explanation:**
For n=3, we need to generate all valid combinations using 3 opening and 3 closing parentheses.

## Constraints
* 1 ≤ n ≤ 8
* Output should contain all unique valid combinations
* Order of combinations in output doesn't matter

## Approach
1. **Optimized Start**: Begin with "(" and counts (open_count=1, close_count=0) since valid combinations must start with opening parenthesis
2. **Smart Backtracking**: At each step, decide whether to add '(' or ')' based on constraints
3. **Opening Constraint**: Add '(' only if we haven't used all n opening parentheses
4. **Closing Constraint**: Add ')' only if it won't exceed the number of opening parentheses used so far
5. **Base Case**: When both open_count and close_count equal n, add valid combination to result
6. **Efficiency**: This approach skips invalid paths early, generating only valid combinations

## Algorithm Steps
```
1. Start with path="(" and counts (open_count=1, close_count=0)
2. Base case: if open_count == close_count == n, add path to result
3. Try adding opening parenthesis:
   a. If open_count < n, recurse with path+"(" and open_count+1
4. Try adding closing parenthesis:
   a. If close_count < open_count, recurse with path+")" and close_count+1
5. Return all valid combinations
```

## Time and Space Complexity
- **Time Complexity**: O(4^n / √n) - nth Catalan number complexity
- **Space Complexity**: O(4^n / √n) for storing all valid combinations
- **Recursion Depth**: O(2n) maximum depth for complete string