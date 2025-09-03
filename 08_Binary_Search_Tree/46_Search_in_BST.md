# Is Akash in Jail?

## Problem Background
Search operations in BSTs are fundamental to many real-world applications including prison management systems, employee databases, and inventory tracking. Law enforcement agencies use BST-like structures to quickly locate individuals in large databases, making search operations critical for public safety and administrative efficiency.

## Problem Statement
Hitesh and Anirudh are very worried because their best friend, Akash, was arrested for hitting a policeman. They don't know why he did it, but they believe Akash is innocent. So, they plan to break him out of jail.

Anirudh has some contacts in the police department and got information about the jail. The jail is organized like a tree with these features:
- Each cell has a unique ID
- Each cell (or node) has two details: a cell ID and a prisoner's name
- The left cell ID is always less than the current cell ID, and the right cell ID is always greater

Fortunately, Hitesh knows Akash's cell ID.

Quickly check if Akash is still in his cell. If he is, return "Help!!!" If he has already escaped, return "Hurrah!!" If the cell ID does not exist in the jail, return "Wrong Jail".

## Input Format
* First line contains N (number of cells in the jail)
* Next N lines contain cell ID and prisoner name
* Last line contains the cell ID where Akash might be

## Output Format
* Return "Help!!!" if Akash is found in the given cell ID
* Return "Hurrah!!" if the cell exists but Akash is not there
* Return "Wrong Jail" if the cell ID doesn't exist

## Example
**Input:**
```
3
1000 Priyo
300 Ayan
1010 Akash
1010
```

**Output:**
```
Help!!!
```

**Explanation:**
Cell ID 1010 exists in the jail and contains Akash, so we return "Help!!!"

## Constraints
* 0 <= Cell ID <= 10^9
* 1 <= length(prisoner's name) <= 20

## Approach
1. **BST Search**: Use binary search tree property to efficiently locate the cell
2. **Iterative Traversal**: Compare target cell ID with current node's ID
3. **Direction Decision**: Go left if target < current, go right if target > current
4. **Result Determination**: Check prisoner name once cell is found
5. **Time Complexity**: O(log N) average case, O(N) worst case
6. **Space Complexity**: O(1) - iterative approach uses constant space