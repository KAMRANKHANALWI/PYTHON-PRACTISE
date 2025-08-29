# Minimum Time to Complete Tasks

## Problem Background
You have a task scheduler that needs to process n tasks. Each task has a processing time, but your scheduler has a special feature: it can run multiple instances of the same task simultaneously.

For a given task with processing time t, if you assign k instances to work on it simultaneously, the task will be completed in ceil(t/k) time. For example, a task with processing time 7 will take 4 time units with 2 instances (7/2 = 4) and 3 time units with 3 instances (7/3 = 3).

You have a maximum of maxInstances instances available. Your goal is to find the minimum time required to complete all tasks by optimally allocating these instances.

## Problem Statement
You have a task scheduler that needs to process n tasks. Each task has a processing time, but your scheduler has a special feature: it can run multiple instances of the same task simultaneously.

For a given task with processing time t, if you assign k instances to work on it simultaneously, the task will be completed in ceil(t/k) time. For example, a task with processing time 7 will take 4 time units with 2 instances (7/2 = 4) and 3 time units with 3 instances (7/3 = 3).

You have a maximum of maxInstances instances available. Your goal is to find the minimum time required to complete all tasks by optimally allocating these instances.

## Input Format
* The first line contains two integers n and maxInstances — the number of tasks and the maximum available instances.
* The second line contains n integers representing the processing time of each task.

## Output Format
* Return a single integer — the minimum time to complete all tasks.

## Example
**Input:**
```
3 5
2 4 8
```

**Output:**
```
4
```

**Explanation:**
We are given 3 tasks with processing times [2, 4, 8] and a total of 5 instances to allocate.

Our goal is to minimize the time required to complete all tasks by optimally allocating the available instances. For each task with processing time t, if we assign k instances, it will complete in ceil(t / k) time units.

Let's test if all tasks can be completed in 3 time units:
- Task 1 (2): ceil(2 / 3) = 1 → needs 1 instance
- Task 2 (4): ceil(4 / 3) = 2 → needs 2 instances  
- Task 3 (8): ceil(8 / 3) = 3 → needs 3 instances
- Total instances needed = 1 + 2 + 3 = 6 > 5
→ Not possible in 3 time units.

Try 4 time units:
- Task 1 (2): ceil(2 / 4) = 1 → needs 1 instance
- Task 2 (4): ceil(4 / 4) = 1 → needs 1 instance
- Task 3 (8): ceil(8 / 4) = 2 → needs 2 instances
- Total instances used = 1 + 1 + 2 = 4 ≤ 5 ✓
→ All tasks complete in 4 time units or less.

**Final Answer: 4**

## Constraints
* 1 ≤ n ≤ 10^5
* 1 ≤ maxInstances ≤ 10^9
* 1 ≤ processing time of each task ≤ 10^9

## Approach
1. Use binary search on the answer (time T)
2. For each candidate time T, check if all tasks can complete within maxInstances
3. For task with time t, it needs ceil(t/T) instances to complete in time T
4. If total required instances ≤ maxInstances, T is feasible
5. Binary search finds minimum feasible T
6. This achieves O(n log(max_task_time)) time complexity