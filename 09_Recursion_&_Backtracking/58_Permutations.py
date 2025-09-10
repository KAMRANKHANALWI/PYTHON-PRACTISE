def permute(nums):
    result = []

    def backtrack(idx):
        if idx == len(nums):
            result.append(nums[:])
            return

        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            backtrack(idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]

    backtrack(0)
    return result


print(permute([1, 2, 3]))
