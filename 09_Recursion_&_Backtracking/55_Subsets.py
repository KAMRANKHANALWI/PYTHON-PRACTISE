def subsets(nums):
    result = []
    
    def dfs(index, current):
        if index == len(nums):
            result.append(current[:])
            return
        
        # choice 1: include nums[index]
        current.append(nums[index])
        dfs(index+1, current)
        
        # backtrack (remove last element)
        current.pop()
        
        # choice 2: exclude nums[index]
        dfs(index+1, current)
        
    dfs(0, [])
    return result

print(subsets([1, 2, 3]))
        