# Print Keypad Combinations

## Problem Background
You're developing a T9 predictive text system for mobile phones, similar to the old Nokia keypad where each number key corresponds to multiple letters. This problem is essential in telecommunications, mobile app development, and autocomplete systems where users input numbers and expect all possible letter combinations that could represent words.

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent on a mobile phone keypad using recursion.

**Keypad Mapping:**
```
2: "abc"    6: "mno"
3: "def"    7: "pqrs"  
4: "ghi"    8: "tuv"
5: "jkl"    9: "wxyz"
```

Note: 0 and 1 do not map to any letters.

## Input Format
* A string containing digits from 2-9

## Output Format
* A list of strings containing all possible letter combinations

## Example
**Input:**
```
"23"
```

**Output:**
```
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

**Explanation:**
- Digit '2' maps to "abc" 
- Digit '3' maps to "def"
- All combinations: a+d, a+e, a+f, b+d, b+e, b+f, c+d, c+e, c+f

## Visual Representation
```
Input: "23"

       ""
    /  |  \
   a   b   c     (digit '2': abc)
  /|\ /|\ /|\
 d e f d e f d e f  (digit '3': def)

Final combinations: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Constraints
* 0 ≤ length of digits ≤ 4
* digits[i] is a digit in the range ['2', '9']
* If input is empty, return empty list

## Approach
1. Create a mapping from digits to their corresponding letters
2. Use backtracking to explore all possible combinations
3. At each digit, try all possible letters for that digit
4. Build the combination character by character
5. Base case: when we've processed all digits, add combination to result
6. This generates all possible combinations through recursive exploration

## Algorithm Steps
```
1. Create digit-to-letters mapping dictionary
2. Start with empty combination and index 0
3. Base case: if index equals digits length, add current combination to result
4. Get letters for current digit
5. For each letter in the mapping:
   a. Add letter to current combination
   b. Recursively process next digit
   c. Backtrack (remove letter from combination)
6. Return all combinations
```

## Time and Space Complexity
- **Time Complexity**: O(3^n × 4^m) where n is digits with 3 letters, m is digits with 4 letters
  - Most digits map to 3 letters, '7' and '9' map to 4 letters
- **Space Complexity**: O(3^n × 4^m) for storing all combinations
- **Recursion Depth**: O(length of digits)

