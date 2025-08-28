# Generate Binary Numbers

## Problem Background

You're working on a computer science education platform that needs to demonstrate number system concepts. Students need to understand how binary representations work for numbers 1 to n. Rather than converting each number individually, you want to use a queue-based approach that generates these efficiently by building on previous results.

## Problem Statement

Generate binary numbers from 1 to n using a queue.

- You need to generate the binary representation of all numbers from 1 to n
- You must use a queue to generate these numbers efficiently
- For this problem, a queue is implemented as an array with these operations:
  - enqueue: Add an element at the end using push()
  - dequeue: Remove an element from the front using shift()
  - isEmpty: Check if the queue is empty by checking length
- For example, for n = 5, output should be ["1", "10", "11", "100", "101"]
- This demonstrates how queues can be used for sequence generation
- The algorithm is more efficient than converting each number individually

## Input Format

- An integer n representing the upper limit

## Output Format

- An array of strings where each string is the binary representation of numbers 1 to n

## Example

**Input:**

```
n = 3
```

**Output:**

```
["1", "10", "11"]
```

**Explanation:**

- 1 in binary is "1"
- 2 in binary is "10"
- 3 in binary is "11"

## Constraints

- 1 ≤ n ≤ 10^5
- Output should be array of strings

## Approach

1. Initialize queue with "1"
2. For each iteration, dequeue front element
3. Add it to result
4. Enqueue front + "0" and front + "1"
5. This builds binary numbers incrementally
6. Time complexity: O(n), Space complexity: O(n)
