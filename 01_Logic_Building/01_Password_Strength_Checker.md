# Password Strength Checker

## Problem Background

You are a cybersecurity engineer at ChaiCode, and you are building an API to evaluate password strength for users signing up on your platform. A strong password is essential to ensure users' accounts are safe from hackers. Your task is to write a function that checks if a given password meets specific strength criteria.

## Problem Statement

You need to implement a function that checks if a given password meets specific strength criteria.

### Requirements:

1. The password must be at least 8 characters long.
2. It must contain at least one uppercase letter (A-Z).
3. It must contain at least one lowercase letter (a-z).
4. It must contain at least one digit (0-9).
5. It must contain at least one special character (e.g., !@#$%^&\*).

Return **"Strong"** if the password meets all criteria, otherwise return **"Weak"**.

## Input Format

- A single string: `password`
- A string of length (1 ≤ length ≤ 1000), consisting of printable ASCII characters.

## Output Format

- A single string:
  - **"Strong"** if the password meets all the criteria.
  - **"Weak"** otherwise

## Example

**Input:** `"Password123!"`  
**Output:** `"Strong"`

## Explanation

- The password is at least 8 characters long.
- It contains at least one uppercase letter.
- It contains at least one lowercase letter.
- It contains at least one digit.
- It contains at least one special character.

## Constraints

1. (1 <= length of password <= 1000)
2. Password may contain any printable ASCII character.

## Approach

1. Check if the password length is at least 8 characters
2. Check for presence of uppercase letters (A-Z)
3. Check for presence of lowercase letters (a-z)
4. Check for presence of digits (0-9)
5. Check for presence of special characters
6. Return "Strong" only if all conditions are met, otherwise "Weak"
