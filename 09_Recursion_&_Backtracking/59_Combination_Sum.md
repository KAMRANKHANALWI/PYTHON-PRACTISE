# Combination Sum

## Problem Background
Combination sum algorithms are fundamental in financial optimization and resource allocation systems where you need to find different ways to achieve a target value using available resources. This problem simulates portfolio optimization, budget planning, and inventory management where you need to explore all possible combinations that sum to a specific target value.

## Problem Statement
Given an array of distinct positive integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may use the same number multiple times.

The same combination should not be returned more than once, and the combinations may be returned in any order.

## Input Format
* An array of distinct positive integers (candidates)
* A target integer (target sum to achieve)

## Output Format
* A list of lists containing all unique combinations that sum to target

## Example
**Input:**
```
candidates = [2, 3, 6, 7]
target = 7
```

**Output:**
```
[[2, 2, 3], [7]]
```

**Explanation:**
- 2 + 2 + 3 = 7
- 7 = 7
Both combinations sum to the target value 7.

## Constraints
* 1 ≤ candidates.length ≤ 30
* 2 ≤ candidates[i] ≤ 40
* All elements in candidates are distinct
* 1 ≤ target ≤ 40

## Approach
1. **Index-based Backtracking**: Use current index to decide between including current candidate or moving to next
2. **Reuse Current Element**: At each index, first try including the current element (stay at same index)
3. **Move to Next Element**: Then try excluding current element and move to next index
4. **Early Termination**: Stop recursion when target becomes negative or we've exhausted all candidates
5. **Base Case**: When target equals 0, we've found a valid combination
6. **Path Management**: Build combination incrementally and backtrack by removing last element
7. **Duplicate Prevention**: Using index progression ensures no duplicate combinations

## Algorithm Steps
```
1. Start with index=0, empty path, and original target
2. Base case: if target == 0, add current path to result
3. Termination: if target < 0 or index >= candidates.length, return
4. Include current candidate:
   a. Add candidates[index] to path
   b. Recursively call with same index and reduced target
   c. Remove last element from path (backtrack)
5. Exclude current candidate:
   a. Recursively call with next index and same target
6. Return all valid combinations
```

## Time and Space Complexity
- **Time Complexity**: O(N^(T/M)) where N is candidates length, T is target, M is minimal candidate value
- **Space Complexity**: O(T/M) for recursion depth and path storage
- **Recursion Depth**: O(target/min_candidate) in worst case