def combinationSum(candidates, target):
    ans = []

    def backtrack(idx, path, target):
        if target == 0:
            ans.append(path[:])
            return

        if target < 0 or idx == len(candidates):
            return

        path.append(candidates[idx])
        backtrack(idx, path, target - candidates[idx])
        path.pop()
        backtrack(idx + 1, path, target)

    backtrack(0, [], target)
    return ans


print(combinationSum([2, 3, 6, 7], 7))
