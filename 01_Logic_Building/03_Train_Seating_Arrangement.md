# Train Seating Arrangement

## Problem Background

Sherlock Holmes is once again faced with a perplexing mystery!

In a secret communication channel, a series of encrypted messages has been intercepted. Every message appears **exactly twice**, except for one unique message — the **Lone Survivor**.

This mysterious message holds the key to solving the case, but time is of the essence! Sherlock has tasked you, his trusted assistant, to decode the list and uncover the **unique message** that appears only once.

However, there's a challenge:

1. The solution must be **fast** (linear runtime complexity).
2. You can only use **constant extra space** (to ensure the secrecy of the operation).

Can you crack the case and find the **Lone Survivor** before it's too late?

## Problem Statement

Given a non-empty array of integers, `nums`, where every element appears **exactly twice** except for one unique element, find the **unique element**.

To crack the code, your solution must:

1. Run in **O(n)** time complexity.
2. Use only **O(1)** extra space.

## Input Format

- A single array of integers, `nums`, where every element appears **twice** except for one unique element.

## Output Format

- A single integer — the unique element in the array.

## Constraints

1. 1 <= nums.length <= 3 × 10^4
2. -3 × 10^4 <= nums[i] <= 3 × 10^4
3. Each element in the array appears **exactly twice** except for one element which appears only once.

## Approach1

1. Create a frequency map (dictionary) to count occurrences of each number
2. Iterate through the array and update the count for each element
3. Find the element with frequency 1 and return it
4. This achieves O(n) time complexity but uses O(n) space

## Approach2

1. Use XOR operation properties: a ⊕ a = 0, a ⊕ 0 = a
2. XOR all elements together - duplicate elements cancel out
3. The result will be the unique element
4. This achieves O(n) time and O(1) space complexity
