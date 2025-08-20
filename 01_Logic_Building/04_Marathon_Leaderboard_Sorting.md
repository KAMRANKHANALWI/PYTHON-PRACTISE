# Marathon Leaderboard Sorting

## Problem Background

You are managing the leaderboard for a spring marathon. Runners are ranked based on their completion time in ascending order. If two runners complete the marathon in the same time, their names are sorted alphabetically.

Your task is to implement a sorting function to display the leaderboard correctly.

## Problem Statement

Write a program to sort a list of marathon runners. Each runner is represented by:

- **name**: A string representing the runner's name.
- **time**: An integer representing the runner's completion time (in minutes).

Sort the runners by:

1. **Completion time (ascending)**.
2. **Name (alphabetically)** if two runners have the same time.

## Input Format

- An array of objects, where each object contains:
  - **name**: A string (1 ≤ length ≤ 100).
  - **time**: An integer (0 ≤ time ≤ 1000 seconds).

## Output Format

- A sorted array of objects based on the criteria above.

## Example

**Input:**

```json
[
  { "name": "John", "time": 150 },
  { "name": "Alice", "time": 120 },
  { "name": "Bob", "time": 150 }
]
```

**Output:**

```json
[
  { "name": "Alice", "time": 120 },
  { "name": "Bob", "time": 150 },
  { "name": "John", "time": 150 }
]
```

## Constraints

- The number of runners will not exceed 100.
- The time will be an integer between 0 and 1000 seconds.
- The names will be strings with lengths between 1 and 100 characters.

## Approach

1. Use a custom sorting key with tuple (time, name)
2. Sort by time first (ascending), then by name (alphabetical)
3. Return the sorted list of runner objects
